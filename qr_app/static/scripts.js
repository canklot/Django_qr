function checkNonAscii(text) {
  return [...text].some((char) => char.charCodeAt(0) > 127);
}

/*
This code uses jQuery and it intercepts submit request. 
If returns false request discarded. */

$("#qr_form_id").on("submit", function () {
  text = document.getElementById("qr_text_input_id").value;
  textList = text.split("\n"); //add var or let later on
  barcode_type = document.getElementById("qr_type_input_id").value;

  if (barcode_type == "qr_code") {
    return true;
  } else if (barcode_type == "Code128") {
    hasMoreThanAscii = checkNonAscii(text);
    if (hasMoreThanAscii) {
      alert("Code128 only supports ascii charecters");
      return false;
    }
  }
  myFetch(textList, barcode_type);
  return true;
});

function myFetch(textParam, typeParam) {
  fetch("http://localhost:8000/api", {
    method: "POST",
    headers: {
      Accept: "application/json, text/plain, */*",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text: textParam,
      barcode_type_selection: typeParam,
    }),
  })
    .then((response) => {
      return response.blob();
    })
    .then((blob) => {
      downloadFile(blob);
    });
}

//------------------
function downloadFile(blob, name = "file.pdf") {
  const href = URL.createObjectURL(blob);
  const a = Object.assign(document.createElement("a"), {
    href,
    style: "display:none",
    download: name,
  });
  document.body.appendChild(a);
  a.click();
  URL.revokeObjectURL(href);
  a.remove();
}

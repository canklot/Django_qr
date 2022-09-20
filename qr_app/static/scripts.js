function checkNonAscii(text) {
  return [...text].some((char) => char.charCodeAt(0) > 127);
}

/*
This code uses jQuery and it intercepts submit request. 
If returns false request discarded. */

$("#qr_form_id").on("submit", function () {
  text = document.getElementById("qr_text_input_id").value;

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
  myFetch();
  return true;
});

function myFetch() {
  fetch("http://localhost:8000/api", {
    method: "POST",
    headers: {
      Accept: "application/json, text/plain, */*",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text: ["asd1", "asd2"],
      barcode_type_selection: "qr_code",
    }),
  })
    .then((response) => {
      return response.blob();
    })
    .then((blob) => {
      var reader = new FileReader();
      reader.readAsArrayBuffer(blob);
      reader.onloadend = function () {
        var theBuffer = reader.result;
        downloadFile(theBuffer);
      };
    });
}

//------------------
function downloadFile(data, name = "file.pdf") {
  const blob = new Blob([data], { type: "octet-stream" });
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

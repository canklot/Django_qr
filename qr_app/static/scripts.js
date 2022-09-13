function checkNonAscii(text) {
  return [...text].some((char) => char.charCodeAt(0) > 127);
}

/*
This code uses jQuery and it intercepts submit request. 
If returns false request discarded. */

$("#qr_form_id").on("submit", function () {
  text = document.getElementById("qr_text_input_id").value;

  barcode_type = document.getElementById("qr_type_radio_input_id").value;

  if (barcode_type == "qr_code") {
    return true;
  }

  hasMoreThanAscii = checkNonAscii(text);
  if (hasMoreThanAscii) {
    alert("Code128 only supports ascii charecters");
    return false;
  }
  return true;
});

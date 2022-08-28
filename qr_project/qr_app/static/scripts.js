function checNotAscii(text) {
    let hasMoreThanAscii = [...text].some((char) => char.charCodeAt(0) > 127);
    return hasMoreThanAscii;
}

$("#qr_form_id").on("submit", function () {
    text = document.getElementById("qr_text_input_id").value;
    hasMoreThanAscii = checNotAscii(text);
    if (hasMoreThanAscii) {
        alert("The text has non ascii charecters. Code128 only supports ascii charecters");
        return false;
    } else {
        return true;
    }
});

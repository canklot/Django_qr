function checNotAscii(text) {
    let hasMoreThanAscii = [...text].some((char) => char.charCodeAt(0) > 127);
    return hasMoreThanAscii;
}

$("#qr_form_id").on("submit", function () {
    text = document.getElementById("qr_text_input_id").value;
    hasMoreThanAscii = checNotAscii(text);
    if (hasMoreThanAscii) {
        alert("non ascii detected");
        return false;
    } else {
        alert("text is good");
        return true;
    }
});

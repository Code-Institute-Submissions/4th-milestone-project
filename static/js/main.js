function viewContactDetails() {
    var x = document.getElementById("contact-details");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}

// publisch (multiple) checkboxes inline
$(document).ready(function () {
    $(".form-check").addClass("form-check-inline");
});

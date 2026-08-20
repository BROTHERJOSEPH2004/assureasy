// =========================
// ASSUREASY JAVASCRIPT
// =========================


// Insurance information
function showMessage(insuranceType) {
    alert(
        insuranceType +
        " gives you protection against unexpected costs. " +
        "Use AssurEasy to compare plans and choose the option that suits you."
    );
}


// Buy form
const buyForm = document.querySelector("form");

if (buyForm && window.location.pathname === "/buy") {
    buyForm.addEventListener("submit", function (event) {
        event.preventDefault();

        alert(
            "Thank you for choosing AssurEasy! " +
            "Your insurance request has been received."
        );
    });
}


// Reminder form
const reminderForm = document.querySelector("form");

if (
    reminderForm &&
    window.location.pathname === "/reminders"
) {
    reminderForm.addEventListener("submit", function (event) {
        event.preventDefault();

        alert(
            "Your insurance renewal reminder has been added successfully!"
        );
    });
}
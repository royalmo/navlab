const passwordInput = document.querySelector('input[name="password"]');
const passwordError = document.getElementById("passwordError");
const passwordConfirmation = document.querySelector('input[name="password_confirm"]');
const passwordErrorConf = document.getElementById("passwordErrorConf");
const passwordRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]{8,}$/;

passwordInput.addEventListener("input", () => {
    const password = passwordInput.value;
    let errorMessages = [];

    if (passwordRegex.test(password)) {
        passwordError.innerHTML = '<span class="text-green-600">Password meets all requirements</span>';
    } else {
        if (password.length < 8) {
            errorMessages.push("- Password must be at least 8 characters long");
        }
        if (!/(?=.*[A-Z])/.test(password)) {
            errorMessages.push("- Password must contain at least one uppercase letter");
        }
        if (!/(?=.*[a-z])/.test(password)) {
            errorMessages.push("- Password must contain at least one lowercase letter");
        }
        if (!/(?=.*\d)/.test(password)) {
            errorMessages.push("- Password must contain at least one number");
        }
        if (!/(?=.*[!@#$%^&*()_+])/.test(password)) {
            errorMessages.push("- Password must contain at least one special character (!@#$%^&*()_+)");
        }
        passwordError.innerHTML = errorMessages.map(message => `<span class="text-${password.length >= 8 && /(?=.*[A-Z])/.test(password) && /(?=.*\d)/.test(password) && /(?=.*[!@#$%^&*()_+])/.test(password) ? 'green' : 'red'}">${message}</span>`).join('<br>');
    }
});

passwordConfirmation.addEventListener("input", () => {
    const password = passwordInput.value;
    const passwordConf = passwordConfirmation.value;
    let errorMessages = [];

    if (password !== passwordConf) {
        errorMessages.push("Passwords do not match");
    }

    if (errorMessages.length > 0) {
        passwordErrorConf.innerHTML = errorMessages.map(message => `<span class="text-red-600">${message}</span>`).join('<br>');
    } else {
        passwordErrorConf.innerHTML = '<span class="text-green-600">Passwords match</span>';
    }
});

function validateForm() {
    var password = document.forms["register_form"]["password"].value;
    var confirm_password = document.forms["register_form"]["confirmation_password"].value;

    return password == confirm_password;
}

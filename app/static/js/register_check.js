const passwordInput = document.querySelector('input[name="password"]');
const passwordInputHint = document.getElementById("password_hints");
const passwordConfirmation = document.querySelector('input[name="password_confirm"]');
const passwordConfirmationHint = document.getElementById("password_confirm_hints");

const passwordRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]{8,}$/;

function set_element(e, failed) {
    if (failed) {
        e.classList.replace('text-green-700', 'text-red-700');
        e.children[0].classList.replace('fa-check', 'fa-times');
    }
    else {
        e.classList.replace('text-red-700', 'text-green-700');
        e.children[0].classList.replace('fa-times', 'fa-check');
    }
}

function register_check() {
    const password = passwordInput.value;
    const ch = passwordInputHint.children;

    set_element(ch[0], !/(?=.*[a-z])/.test(password));
    set_element(ch[1], !/(?=.*[A-Z])/.test(password));
    set_element(ch[2], !/(?=.*\d)/.test(password));
    set_element(ch[3], password.length < 8);
    set_element(ch[4], !/(?=.*[!@#$%^&*()_+])/.test(password));

    const passwordConf = passwordConfirmation.value;
    const firstChild = passwordConfirmationHint.children[0];
    const secondChild = passwordConfirmationHint.children[1];

    if (password !== passwordConf) {
        firstChild.style.display = "block";
        secondChild.style.display = "none";
    }
    else {
        firstChild.style.display = "none";
        secondChild.style.display = "block";
    }
}

passwordInput.addEventListener("input", register_check);
passwordConfirmation.addEventListener("input", register_check);

function validateForm() {
    var password = passwordInput.value;
    var confirm_password = passwordConfirmation.value;

    return password == confirm_password;
}

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("id-email").addEventListener("keyup", event => {
        let email = document.getElementById("id-email");

        if (email.value === "") {
            email.classList.remove("hasText", "error");
            document.querySelector(".input-error").hidden = true;
        } else {
            email.classList.add("hasText", "error");
            document.querySelector(".input-error").hidden = false;
        }

        is_email(email)
    });
});


function is_email_change() {
    let email_bool = false;
    let email = document.getElementById("id-email");
    let temp = is_email(email);

    if(temp) {
        email_bool = true;
    } else {
        email.classList.add("error")
        document.querySelector(".input-error").hidden = false;
        email.focus();
    }
    return email_bool
}

function is_email(obj) {
    let email_bool = true;

    if (obj.value.length < 5) {
        document.querySelector(".input-error").innerText = "이메일 주소를 입력해 주세요.";
        email_bool = false;
    } else {
        let regExp = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/i;
        if (obj.value.match(regExp) != null) {
            obj.classList.remove("error");
            document.querySelector(".input-error").hidden = true;
        } else {
            document.querySelector(".input-error").innerText = "정확한 이메일 주소를 입력하세요.";
            email_bool = false;
        }
    }

    return email_bool
}
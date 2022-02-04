document.addEventListener("DOMContentLoaded", () => {
   let parent = document.getElementById("our-story-logo");
   let logo_a = document.createElement('a');
   let email = document.getElementById("id-email");
   let password = document.getElementById("id-password");
   let username = document.getElementById("id-username");
   let phone_number = document.getElementById("id-phone-number");

   logo_a.setAttribute('href', '/kr');
   logo_a.setAttribute('class', 'logo-a');
   parent.parentNode.insertBefore(logo_a, parent);
   logo_a.appendChild(parent);

   if (!(email.value === "")) {
      email.classList.add("hasText");
   }

   if (!(phone_number.value === "")) {
      phone_number.classList.add("hasText");
   }

   keyUpEvent(email);
   keyUpEvent(password);
   keyUpEvent(username);
   keyUpEvent(phone_number)


});

function keyUpEvent(id) {
   id.addEventListener("keyup", event => {
      if (id.value === "") {
         id.classList.remove("hasText", "error");
         document.querySelector("."+ id.id +".input-error").hidden = true;
      } else {
         id.classList.add("hasText", "error");
         document.querySelector("."+ id.id +".input-error").hidden = false;
      }
      if (id.id === "id-email") {
         is_email(id);
      } else if (id.id === "id-password") {
         is_password(id);
      } else if (id.id === "id-phone-number") {
         is_phone_number(id);
      } else {
         is_username(id);
      }
   });
}


function is_email(obj) {
    let email_bool = true;

    if (obj.value.length < 5) {
       obj.classList.add("error");
       document.querySelector("."+ obj.id +".input-error").hidden = false;
       document.querySelector("." + obj.id + ".input-error").innerText = "이메일 주소 또는 핸드폰 번호 입력해 주세요.";
       email_bool = false;
    } else {
       let regExp = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/i;
       let regPhone = /^01([0|1|6|7|8|9])-?([0-9]{3,4})-?([0-9]{4})$/;

       if (obj.value.match(regExp) != null) {
          obj.classList.remove("error");
          document.querySelector("." + obj.id + ".input-error").hidden = true;
       } else {
          document.querySelector("."+ obj.id +".input-error").hidden = false;
          document.querySelector("." + obj.id + ".input-error").innerText = "이메일 주소를 정확하게 입력하세요.";
          email_bool = false;
       }
    }

    return email_bool
}

function is_password(obj) {
   let password_bool = true;

   if (obj.value.length < 6 || obj.value.length > 60) {
      obj.classList.add("error");
      document.querySelector("."+ obj.id +".input-error").hidden = false;
      document.querySelector("."+ obj.id +".input-error").innerText = "비밀번호는 6~60자 사이여야 합니다.";
      password_bool = false;
   } else {
      obj.classList.remove("error");
      document.querySelector("."+ obj.id +".input-error").hidden = true;
   }

   return password_bool;
}

function is_phone_number(obj) {
   let phone_number_bool = true;
   let regExp = /^01([0|1|6|7|8|9])-?([0-9]{3,4})-?([0-9]{4})$/;

   console.log('check')

   if (obj.value.match(regExp) != null) {
          obj.classList.remove("error");
          document.querySelector("." + obj.id + ".input-error").hidden = true;
       } else {
          document.querySelector("."+ obj.id +".input-error").hidden = false;
          document.querySelector("." + obj.id + ".input-error").innerText = "휴대폰 번호를 정확하게 입력하세요.";
          phone_number_bool = false;
       }

   return phone_number_bool;
}

function is_username(obj) {
   let is_username = true;
   if (obj.value.length < 2) {
      obj.classList.add("error");
      document.querySelector("."+ obj.id +".input-error").hidden = false;
      document.querySelector("."+ obj.id +".input-error").innerText = "이름을 입력해주세요.";
      is_username = false;
   } else {
      obj.classList.remove("error");
      document.querySelector("." + obj.id + ".input-error").hidden = true;
   }

   return is_username;
}
function signUp() {
   let email = document.getElementById("id-email");
   let password = document.getElementById("id-password");
   let username = document.getElementById("id-username");
   let phone_number = document.getElementById("id-phone-number");

   if (is_email(email) === false) {
      return false
   }
   if (is_password(password) === false) {
      return false
   }
   if (is_username(username) === false) {
      return false
   }
   if (is_phone_number(phone_number) === false) {
      return false
   }

   return true;
}
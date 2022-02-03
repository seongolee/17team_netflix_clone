function cinfirm_pw() {
    let pw1 = document.getElementById('id_newPassword').value;
    let pw2 = document.getElementById('id_confirmNewPassword').value;
    if (pw1!==pw2) {

    } else {

    }

}

function check_pw() {
    //최소 8 자, 하나 이상의 문자, 하나의 숫자 및 하나의 특수 문자 정규식
    let reg = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$";
    let pw1 = document.getElementById('id_newPassword').value;

    if( !reg.test(pw1) ) {
    alert("비밀번호 정규식 규칙 위반!!");
    return false;
}
}
function cinfirm_pw() {
    let pw1 = document.getElementById('id_newPassword').value;
    let pw2 = document.getElementById('id_confirmNewPassword').value;
    if (pw1!==pw2) {
        document.getElementById('pw_check').innerHTML = '비밀번호가 일치하지 않습니다.';
        document.getElementById('pw_check').style.color = 'red';
        document.getElementById('pw_check').style.fontSize = "8px";
        document.getElementById('id_confirmNewPassword').style.borderColor = 'red';
        document.getElementById('btn-save').disabled = true;
    } else {
        document.getElementById('pw_check').innerHTML = '';
        document.getElementById('id_confirmNewPassword').style.borderColor = 'green';
        document.getElementById('btn-save').disabled = false;
    }

}

function check_pw() {
    //최소 8 자, 하나 이상의 문자, 하나의 숫자 및 하나의 특수 문자 정규식
    let reg = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$";
    let pw1 = document.getElementById('id_newPassword').value;
    if (!pw1) {
        document.getElementById('pw_form').innerHTML = '';
        document.getElementById('id_newPassword').style.borderColor = 'gray';
        document.getElementById('btn-save').disabled = true;
    } else {
        if (reg.test(pw1) == false) {
            document.getElementById('pw_form').innerHTML = '최소 8 자, 하나 이상의 문자, 하나의 숫자 및 하나의 특수 문자를 입력하세요.';
            document.getElementById('pw_form').style.color = '#b00500';
            document.getElementById('pw_form').style.fontSize = '8px';
            document.getElementById('id_newPassword').style.borderColor = 'red';
            document.getElementById('id_newPassword').style.borderWidth='1px';
            document.getElementById('btn-save').disabled = true;
        } else {
            document.getElementById('pw_form').innerHTML = '';
            document.getElementById('id_newPassword').style.borderColor = 'gray';
            document.getElementById('btn-save').disabled = false;
        }

    }
}
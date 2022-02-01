// 라디오버튼 클릭후 보여지는부분 알려주는 함수

function which_show() {
    let checked = document.querySelector("input[name='choice']:checked")
    if (checked.value == 'email'){
        document.getElementById('email_result').style.display = "flex";
        document.getElementById('msg_result').style.display = "none";
        document.getElementById('send-btn').innerText = '이메일로 받기';
        document.getElementById('send-msg').disabled = true;
        document.getElementById('send-email').disabled = false;

    }
    else {
        document.getElementById('email_result').style.display = "none";
        document.getElementById('msg_result').style.display = "flex";
        document.getElementById('send-btn').innerText = '문자로 받기';
        document.getElementById('send-email').disabled = true;
        document.getElementById('send-msg').disabled = false;

    }

}

//이용약관 보여주는 함수
function show_detail() {
    document.getElementById('detail').style.display='none'
    document.getElementById('google-sec').style.display='block'

}

//이메일 입력시 유효한 형식인지 판단하는 함수
function checkIt() {
    var input_email = document.getElementById('send-email')
    var email = input_email.value;
    var exptext = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/i;

    if (!email) {
        document.getElementById('error_email').innerHTML = ''
        document.getElementById('send-email').style.borderColor = 'gray'
        document.getElementById('send-btn').disabled = false;
        input_email.focus();


   } else {
        if (exptext.test(email) == false) {
            document.getElementById('error_email').innerHTML = '정확한 이메일 주소를 입력하세요.'
            document.getElementById('error_email').style.color = '#b00500'
            document.getElementById('error_email').style.fontSize = '8px'
            document.getElementById('send-email').style.borderColor = 'red'
            document.getElementById('send-email').style.borderWidth='1px'
            document.getElementById('send-btn').disabled = true;
            //이메일 형식이 알파벳+숫자@알파벳+숫자.알파벳+숫자 형식이 아닐경우

        }
        else {
            document.getElementById('error_email').innerHTML = ''
            document.getElementById('send-email').style.borderColor = 'gray'
            document.getElementById('send-btn').disabled = false;
        }
    }

}


//전화번호 형식이 유효한지 확인하는 함수
function checkPhone() {
    var input_num = document.getElementById('send-msg')
    var num = input_num.value;
    var exptext = /^[0-9]+$/;

    if (!num) {
        document.getElementById('error_phone').innerHTML = ''
        document.getElementById('send-msg').style.borderColor = 'gray'
        document.getElementById('send-btn').disabled = false;
      input_num.focus();


   } else {
        if (exptext.test(num) == false) {
            document.getElementById('error_phone').innerHTML = '정확한 전화번호를 입력하세요.'
            document.getElementById('error_phone').style.color = '#b00500'
            document.getElementById('error_phone').style.fontSize = '8px'
            document.getElementById('send-msg').style.borderColor = 'red'
            document.getElementById('send-msg').style.borderWidth='1px'
            document.getElementById('send-btn').disabled = true;
            //이메일 형식이 알파벳+숫자@알파벳+숫자.알파벳+숫자 형식이 아닐경우

        }
        else {
            document.getElementById('error_phone').innerHTML = ''
            document.getElementById('send-msg').style.borderColor = 'gray'
            document.getElementById('send-btn').disabled = false;
        }
    }

}

function to_url(){

}
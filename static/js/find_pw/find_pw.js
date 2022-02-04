// 라디오버튼 클릭후 보여지는부분 알려주는 함수
function which_show() {
    let checked = document.querySelector("input[name='type_choice']:checked")
    if (checked.value == 'EMAIL'){
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
        document.getElementById('send-btn').disabled = true;
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
        document.getElementById('send-btn').disabled = true;


   } else {
        if (exptext.test(num) == false ) {
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

function radio_check(){
    let radio_value = document.querySelector("input[name='type_choice']:checked").value;
    return radio_value;
}

function auth_user_check(){
    let radio_value = radio_check()
    let input_value = '';
    let temp = false;

    if (radio_value === 'EMAIL') {
        input_value = document.getElementById('send-email').value;
    } else {
        input_value = document.getElementById('send-msg').value;
    }

    $.ajax({
        url: 'auth-user/',
        type: 'GET',
        data: {
            'input_type':radio_value,
            'input_val':input_value
        },
        async: false,
        datatype: 'json', // 서버에서 반환되는 데이터 json 형식
        success: function(data){ // AJAX 통신이 성공하면 해당 과일의 영어 단어가 출려되도록
            if (data.result === false) {
                if (radio_value === 'EMAIL') {
                    document.querySelector('.none-email').hidden = false;

                } else {
                    document.querySelector('.none-phone').hidden = false;
                }
                temp = false;
            } else {
                temp = true;
            }
        }
    });
    return temp;
}
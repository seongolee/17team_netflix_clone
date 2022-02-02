function check_auth() {
    let auth_number = document.getElementById('certi_num').value;
    let error_auth = document.getElementById('error_auth');
    let temp = false;

    $.ajax({
        // url: 'auth-num/',
        url: '/find-user/auth-num',
        type: 'GET',
        data: {
            'auth_number': auth_number
        },
        async: false,
        datatype: 'json', // 서버에서 반환되는 데이터 json 형식
        success: function(data){ // AJAX 통신이 성공하면 해당 과일의 영어 단어가 출려되도록
            // console.log(data.temp)
            // temp = data.temp;
            //
            // if (temp === false) {
            //     document.getElementById('certi_num').style.borderColor = 'red';
            //     error_auth.innerText = '인증 코드를 잘못 입력하셨습니다.';
            //     error_auth.style.fontSize = '8px';
            //     error_auth.style.color = '#b00500';
            // } else {
            //     temp = true
            // }

            if (data.temp === false) {
                document.getElementById('certi_num').style.borderColor = 'red';
                error_auth.innerText = '인증 코드를 잘못 입력하셨습니다.';
                error_auth.style.fontSize = '8px';
                error_auth.style.color = '#b00500';
                temp = false;
            } else {
                temp = true;
            }
        }
    });
    return temp;
}
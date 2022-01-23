function which_show() {
    let checked = document.querySelector("input[name='choice']:checked")
    if (checked.value == 'email'){
        document.getElementById('email_result').style.display = "flex";
        document.getElementById('msg_result').style.display = "none";
        document.getElementById('send-btn').innerText = '이메일로 받기'

    }
    else {
        document.getElementById('email_result').style.display = "none";
        document.getElementById('msg_result').style.display = "flex";
        document.getElementById('send-btn').innerText = '문자로 받기'
    }

}

function show_detail() {
    document.getElementById('detail').style.display='none'
    document.getElementById('google-sec').style.display='block'

}
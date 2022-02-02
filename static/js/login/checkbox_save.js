// id_userLoginId
// id_password
// bxid_rememberMe_true
//
//
// 인터넷에서 범용적으로 돌고 있는 예제이다. 쿠키를 7일 동안 심거나 쿠키를 가져오거나 삭제한다.

$(document).ready(function(){

    // 저장된 쿠키값을 가져와서 ID 칸에 넣어준다. 없으면 공백으로 들어감.
    let idkey = getCookie("idkey");
    $("#id_userLoginId").val(idkey);
    let passwordkey = getCookie("passwordkey");
    $("#id_password").val(passwordkey);

    if($("#id_userLoginId").val() != ""){ // 그 전에 ID를 저장해서 처음 페이지 로딩 시, 입력 칸에 저장된 ID가 표시된 상태라면,
        $("#bxid_rememberMe_true").attr("checked", true); // ID 저장하기를 체크 상태로 두기.
    }

    $("#bxid_rememberMe_true").change(function(){ // 체크박스에 변화가 있다면,
        if($("#bxid_rememberMe_true").is(":checked")){ // 체크박스 체크했을 때,
            setCookie("idkey", $("#id_userLoginId").val(), 7); // 7일 동안 쿠키 보관
            setCookie("passwordkey", $("#id_password").val(), 7); // 7일 동안 쿠키 보관
        }else{ // ID 저장하기 체크 해제 시,
            deleteCookie("idkey","passwordkey");
        }
    });
    // ID 저장하기를 체크한 상태에서 ID를 입력하는 경우, 이럴 때도 쿠키 저장.
    $("#id_userLoginId").keyup(function(){ // ID 입력 칸에 ID를 입력할 때,
        if($("#bxid_rememberMe_true").is(":checked")){ // 체크박스를 체크한 상태라면,
            setCookie("idkey", $("#id_userLoginId").val(), 7); // 7일 동안 쿠키 보관
            setCookie("passwordkey", $("#id_password").val(), 7); // 7일 동안 쿠키 보관
        }
    });
});

function setCookie(cookieName, value, exdays){
    let exdate = new Date();
    exdate.setDate(exdate.getDate() + exdays);
    let cookieValue = escape(value) + ((exdays==null) ? "" : "; expires=" + exdate.toGMTString());
    document.cookie = cookieName + "=" + cookieValue;
}
function deleteCookie(cookieName){
    let expireDate = new Date();
    expireDate.setDate(expireDate.getDate() - 1);
    document.cookie = cookieName + "= " + "; expires=" + expireDate.toGMTString();
}
function getCookie(cookieName) {
    cookieName = cookieName + '=';
    let cookieData = document.cookie;
    let start = cookieData.indexOf(cookieName);
    let cookieValue = '';
    if(start != -1){
        start += cookieName.length;
        let end = cookieData.indexOf(';', start);
        if(end == -1)end = cookieData.length;
        cookieValue = cookieData.substring(start, end);
    }
    return unescape(cookieValue);
}






// 연습예제
// $(function () {
//
// // 쿠키값을 가져온다.
//     let cookie_user_id = getLogin();
//
//     /**
//
//      * 쿠키값이 존재하면 id에 쿠키에서 가져온 id를 할당한 뒤
//
//      * 체크박스를 체크상태로 변경
//      */
//     if (cookie_user_id != "") {
//         $("#id_userLoginId").val(cookie_user_id);
//         $("#bxid_rememberMe_true").attr("checked", true);
//     }
//
// // 아이디 저장 체크시
//     $("#bxid_rememberMe_true").on("click", function () {
//         let _this = this;
//         let isRemember;
//         if ($(_this).is(":checked")) {
//             isRemember = confirm("이 PC에 로그인 정보를 저장하시겠습니까? PC방등의 공공장소에서는 개인정보가 유출될 수 있으니 주의해주십시오.");
//             if (!isRemember)
//                 $(_this).attr("checked", false);
//         }
//     });
//
// // 로그인 버튼 클릭시
//
//     $("#btn_login").on("click", function () {
//         if ($("#bxid_rememberMe_true").is(":checked")) { // 저장 체크시
//             saveLogin($("#user_id").val());
//         } else { // 체크 해제시는 공백
//             saveLogin("");
//         }
//     });
// });
//
//
// /**
//  * saveLogin
//  * 로그인 정보 저장
//  * @param id
//  */
//
// function saveLogin(id) {
//     if (id != "") {
// // userid 쿠키에 id 값을 7일간 저장
//         setSave("userid", id, 7);
//     } else {
// // userid 쿠키 삭제
//         setSave("userid", id, -1);
//     }
// }
//
//
// /**
//  * setSave
//  * Cookie에 user_id를 저장
//  * @param name
//  * @param value
//  * @param expiredays
//  */
//
// function setSave(name, value, expiredays) {
//     let today = new Date();
//     today.setDate(today.getDate() + expiredays);
//     document.cookie = name + "=" + escape(value) + "; path=/; expires=" + today.toGMTString() + ";"
// }
// /**
//  * getLogin
//  * 쿠키값을 가져온다.
//  * @returns {String}
//  */
//
// function getLogin() {
// // userid 쿠키에서 id 값을 가져온다.
//     let cook = document.cookie + ";";
//     let idx = cook.indexOf("userid", 0);
//     let val = "";
//
//     if (idx != -1) {
//         cook = cook.substring(idx, cook.length);
//         begin = cook.indexOf("=", 0) + 1;
//         end = cook.indexOf(";", begin);val = unescape(cook.substring(begin, end));
//     }
//
//     return val;
// }
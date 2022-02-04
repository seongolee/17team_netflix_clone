const loremIpsum = document.getElementById("lorem-ipsum")

fetch("https://baconipsum.com/api/?type=all-meat&paras=200&format=html")
    .then(response => response.text())
    .then(result => loremIpsum.innerHTML = result)


// 버튼 클릭시 display: flex 값 / 닫기 버튼 클릭시 modal display none 값

// const modal = document.getElementById("modal")



function modalOn() {
    const modal = document.getElementById("modal")
    modal.style.display = "flex"
}

function isModalOn() {
    return modal.style.display === "flex"
}

function modalOff() {
    modal.style.display = "none"
}

const btnModal = document.getElementById("btn-modal")

btnModal.addEventListener("click", e => {
    modalOn()
})

const closeBtn = modal.querySelector(".close-area")

closeBtn.addEventListener("click", e => {
    modalOff()
})


// 모달창 바깥 영역을 클릭하면 모달창이 꺼지게 하기
// 모달 창 외의 영역을 클릭하면 이벤트 타깃 요소에 modal-overlay 클래스가 있으므로 종료하고,
//     모달 창을 클릭하면 이벤트 타깃 요소에 modal-overlay가 없기 때문에 종료
modal.addEventListener("click", e => {
    const evTarget = e.target
    if(evTarget.classList.contains("modal-overlay")) {
        modalOff()
    }
})


// 모달창이 켜진 상태에서 ESC 버튼을 누르면 모달창이 꺼지게 하기
window.addEventListener("keyup", e => {
    if(isModalOn() && e.key === "Escape") {
        modalOff()
    }
})


// 우측 상단 2nd 네비 열고 닫기


// $('#account-dropdown-button').on('change', function() {
  //  alert( this.value ); // or $(this).val()
// $(document).ready(function(){
//     $('#sub-menu').hide();
// });
//
// Toggle = true;
//
//
// let dropdownlist = `<div role="menu" tabindex="0" class="account-drop-down sub-menu theme-lakira"
//                                          style="opacity: 1; transition-duration: 150ms;">
//                                         <div class="ptrack-content"
//                                              data-ui-tracking-context="%7B%22appView%22:%22accountDropdownPanel%22%7D"
//                                              data-tracking-uuid="8ae535ba-cbb2-4db9-a60e-247eb5dfdec7">
//                                             <div class="topbar"></div>
//                                             <ul class="sub-menu-list profiles" role="list" aria-label="프로필">
//                                                 <li class="sub-menu-item profile" role="listitem">
//                                                     <div><a class="profile-link" tabindex="0"
//                                                             href="/SwitchProfile?tkn=XYQMPBXLEBAWTCAR6ZGHFI6GXA"
//                                                             data-uia="action-select-profile+primary">
//                                                         <div class="avatar-wrapper"><img class="profile-icon"
//                                                                                          src="https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/K6hjPJd6cR6FpVELC5Pd6ovHRSk/AAAABW6CcyxMhswxsXLwQIU0aOSE3fbpOWawb9JenXFNMJgF5uXHTW2eG_gqqoTnw6CYl6XPW60UvrQnjsE8hPKwQMU.png?r=552"
//                                                                                          alt=""></div>
//                                                         <span class="profile-name">김지용</span></a>
//                                                         <div class="profile-children"></div>
//                                                     </div>
//                                                 </li>
//                                                 <li class="sub-menu-item profile" role="listitem">
//                                                     <div><a class="profile-link" tabindex="0"
//                                                             href="/SwitchProfile?tkn=SLXQHUKPMVE2PMISJS5QGZ4RXU"
//                                                             data-uia="action-select-profile+secondary">
//                                                         <div class="avatar-wrapper"><img class="profile-icon"
//                                                                                          src="https://occ-0-3077-993.1.nflxso.net/dnm/api/v6/K6hjPJd6cR6FpVELC5Pd6ovHRSk/AAAABXywvdPHBhL7h0TOuNr2uURK28yBKhjImyfjzYLWmUOB3qbQLUsIIYd9maV-kCAB2CqWulEzCApnRtm09vQoD6M.png?r=6f4"
//                                                                                          alt=""></div>
//                                                         <span class="profile-name">김지연</span></a>
//                                                         <div class="profile-children"></div>
//                                                     </div>
//                                                 </li>
//                                                 <li class="sub-menu-item profile-link" role="listitem"><a
//                                                         aria-label="프로필 관리" class="sub-menu-link"
//                                                         href="/profiles/manage">프로필 관리</a></li>
//                                             </ul>
//                                             <ul class="sub-menu-list responsive-links"></ul>
//                                             <ul class="account-links sub-menu-list" aria-label="계정">
//                                                 <li class="sub-menu-item"><a class="sub-menu-link" href="/YourAccount">계정</a>
//                                                 </li>
//                                                 <li class="sub-menu-item"><a class="sub-menu-link"
//                                                                              href="https://help.netflix.com/">고객 센터</a>
//                                                 </li>
//                                                 <li class="sub-menu-item"><a class="sub-menu-link"
//                                                                              href="/logout">넷플릭스에서 로그아웃</a>
//                                                 </li>
//                                             </ul>
//                                         </div>
//                                     </div>
// `
// function creat_function(){
//     if(aria-expanded=false){
//         $('#account-dropdown-button').append(dropdownlist);
//         aria-expanded=true
//     }
//     else{
//         $('#account-dropdown-button').remove(dropdownlist)
//         aria-expanded=false
//     }
// }
// function delete_function()
// {
//         if Toggle == True:
//         Toggle = false;
//         return Toggle
//     $('#account-dropdown-button').remove(dropdownlist)
// }
//
//
//
// drop = document.getElementsByClassName("sub-menu");
 function dropdownshow(){
     let drop =  document.getElementById("dropdown");
     if(drop.style.display=='none'){
		drop.style.display = 'block';
        console.log('나는빡빡이다!')
	}else{
		drop.style.display = 'none';
        console.log('나의 모발은 빽빽이다!')
	}
}

// var bDisplay = true;
// function doDisplay(){
// 	var con = document.getElementById("myDIV");
// 	if(con.style.display=='none'){
// 		con.style.display = 'block';
// 	}else{
// 		con.style.display = 'none';
// 	}
// }
// jQuery로 dropdown



// let temp_html = `<div class="col">
//                                             <div class="card">
//                                                 <img src="${img_url}"
//                                                      class="card-img-top" alt="...">
//                                                 <div class="card-body" onclick="window.open('${url}')">
//                                                     <h5 class="card-title">${title}</h5>
//                                                 </div>
//                                             </div>
//                                         </div>`
//                         $('#foot3').append(temp_html)
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

// base_main.html 헤더 우측상단 2번째 네비 리스트 열고 닫기 기능
function dropdownshow(){
     let drop =  document.getElementById("dropdown");
     if(drop.style.display=='block'){
		drop.style.display = 'none';
        console.log('나는빡빡이다!')
	}else{
		drop.style.display = 'block';
        console.log('나의 모발은 빽빽이다!')
	}
}

function showColumn() {
    $.ajax({
        type: 'GET',
        url: '/show-col',
        data: {},
        async: false,
        datatype: 'json',
        success: function (data) {
            let video_title = data.video_title
            let video_image = data.video_image
            let detail = data.explain
            for (let i = 0; i < video_title.length; i++) {
                let title = video_title[i]
                let img = video_image[i]
                let explain = detail[i]
                let temp_html = `<figure class="snip1273">
                                    <img src=${img} style="background-size: cover;"
                                         alt="sample72"/>
                                    <figcaption>
                                        <h3>${title}</h3>
                                        <p>${explain}</p>
                                        <img src="../../img/mainpage_img/play-3-64.png"
                                             style="width: 30px; height: 30px; margin-right: 10px; z-index: 2" onclick=""
                                             alt="play_icon">
                                        <img src="{% static 'img/mainpage_img/plus-5-64.png' %}"
                                             style="width: 30px; height: 30px; margin-right: 10px; z-index: 2" onclick=""
                                             alt="plus_icon">
                                        <img src="{% static 'img/mainpage_img/thumb-up-64.png' %}"
                                             style=" width: 30px; height: 30px; margin-right: 10px; z-index: 2" onclick=""
                                             alt="thumbup_icon">
                                        <img src="{% static 'img/mainpage_img/thumb-down-64.png' %}"
                                             style="width: 30px; height: 30px; margin-right: 10px; z-index: 2" onclick=""
                                             alt="thumbdown_icon">
                                        <img src="{% static 'img/mainpage_img/arrow-206-64.png' %}"
                                             style="width: 30px; height: 30px; z-index: 2;"
                                             onclick="modalOn()" alt="arrow_icon">
                                        <a href="#"></a>
                                    </figcaption>
                                </figure>`
                $('.movie-container').append(temp_html)
            }
        }
    });
}


// function moveScrollLeft(){
//     let _scrollX = $('.movie-list').scrollLeft();
//     $('.movie-list').scrollLeft(_scrollX + 20);
// }

// // Get the video
// let video = document.getElementById("myVideo");
//
// // Get the button
// let btn = document.getElementById("myBtn");
//
// // Pause and play the video, and change the button text
// function myFunction() {
//   if (video.paused) {
//     video.play();
//     btn.innerHTML = "Pause";
//   } else {
//     video.pause();
//     btn.innerHTML = "Play";
//   }
// }


// /* Get the documentElement (<html>) to display the page in fullscreen */
// let elem = document.documentElement;
//
// /* View in fullscreen */
// function openFullscreen() {
//   if (elem.requestFullscreen) {
//     elem.requestFullscreen();
//   } else if (elem.webkitRequestFullscreen) { /* Safari */
//     elem.webkitRequestFullscreen();
//   } else if (elem.msRequestFullscreen) { /* IE11 */
//     elem.msRequestFullscreen();
//   }
// }
//
// /* Close fullscreen */
// function closeFullscreen() {
//   if (document.exitFullscreen) {
//     document.exitFullscreen();
//   } else if (document.webkitExitFullscreen) { /* Safari */
//     document.webkitExitFullscreen();
//   } else if (document.msExitFullscreen) { /* IE11 */
//     document.msExitFullscreen();
//   }
// }
window.onload = function() {
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
                                    <figcaption onclick="modalOn()">
                                        <h3>${title}</h3>
                                        <p>${explain}</p>
                                        <a href="#"></a>
                                    </figcaption>
                                </figure>`
                $('.popular').append(temp_html)
                //별점 높은순
            let star_title = data.star_title
            let star_image = data.star_image
            let star_explain = data.star_explain

            for (let i = 0; i < star_title.length; i++) {
                let title = star_title[i]
                let img = star_image[i]
                let explain = star_explain[i]
                let temp_html = `<figure class="snip1273">
                                <img src=${img} style="background-size: cover;"
                                     alt="sample72"/>
                                <figcaption onclick="modalOn()">
                                    <h3>${title}</h3>
                                    <p>${explain}</p>
                                    <a href="#"></a>
                                </figcaption>
                            </figure>`
                $('.star_rank').append(temp_html)
            }

            // 장르 로맨스
            let romance_title = data.romance_title
            let romance_image = data.romance_image
            let romance_explain = data.romance_explain

            for (let i = 0; i < romance_title.length; i++) {
                let title = romance_title[i]
                let img = romance_image[i]
                let explain = romance_explain[i]
                let temp_html = `<figure class="snip1273">
                                <img src=${img} style="background-size: cover;"
                                     alt="sample72"/>
                                <figcaption onclick="modalOn()">
                                    <h3>${title}</h3>
                                    <p>${explain}</p>
                                    <a href="#"></a>
                                </figcaption>
                            </figure>`
                $('.Romance').append(temp_html)
            }

            //장르 액션
            let action_title = data.action_title
            let action_image = data.action_image
            let action_explain = data.action_explain

            for (let i = 0; i < action_title.length; i++) {
                let title = action_title[i]
                let img = action_image[i]
                let explain = action_explain[i]
                let temp_html = `<figure class="snip1273">
                                <img src=${img} style="background-size: cover;"
                                     alt="sample72"/>
                                <figcaption onclick="modalOn()">
                                    <h3>${title}</h3>
                                    <p>${explain}</p>
                                    <a href="#"></a>
                                </figcaption>
                            </figure>`
                $('.Action').append(temp_html)
            }
            // 장르 공포
            let horror_title = data.horror_title
            let horror_image = data.horror_image
            let horror_explain = data.horror_explain

            for (let i = 0; i < horror_title.length; i++) {
                let title = horror_title[i]
                let img = horror_image[i]
                let explain = horror_explain[i]
                let temp_html = `<figure class="snip1273">
                                <img src=${img} style="background-size: cover;"
                                     alt="sample72"/>
                                <figcaption onclick="modalOn()">
                                    <h3>${title}</h3>
                                    <p>${explain}</p>
                                    <a href="#"></a>
                                </figcaption>
                            </figure>`
                $('.Horror').append(temp_html)
            }
            // 장르 코미디
            let comedy_title = data.comedy_title
            let comedy_image = data.comedy_image
            let comedy_explain = data.comedy_explain

            for (let i = 0; i < comedy_title.length; i++) {
                let title = comedy_title[i]
                let img = comedy_image[i]
                let explain = comedy_explain[i]
                let temp_html = `<figure class="snip1273">
                                <img src=${img} style="background-size: cover;"
                                     alt="sample72"/>
                                <figcaption onclick="modalOn()">
                                    <h3>${title}</h3>
                                    <p>${explain}</p>
                                    <a href="#"></a>
                                </figcaption>
                            </figure>`
                $('.Comedy').append(temp_html)
            }
            // 장르 판타지
            let fantasy_title = data.fantasy_title
            let fantasy_image = data.fantasy_image
            let fantasy_explain = data.fantasy_explain

            for (let i = 0; i < fantasy_title.length; i++) {
                let title = fantasy_title[i]
                let img = fantasy_image[i]
                let explain = fantasy_explain[i]
                let temp_html = `<figure class="snip1273">
                                <img src=${img} style="background-size: cover;"
                                     alt="sample72"/>
                                <figcaption onclick="modalOn()">
                                    <h3>${title}</h3>
                                    <p>${explain}</p>
                                    <a href="#"></a>
                                </figcaption>
                            </figure>`
                $('.Fantasy').append(temp_html)
            }
            }
        }
    });
}




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
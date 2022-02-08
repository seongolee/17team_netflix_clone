window.onload = function () {
    $.ajax({
        type: 'GET', url: '/show-col', data: {}, async: false, datatype: 'json', success: function (data) {
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
                                    <figcaption id=${title} onclick="modalOn(this.id)">
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
                                <figcaption id=${title} onclick="modalOn(this.id)">
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
                                <figcaption id=${title} onclick="modalOn(this.id)">
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
                                <figcaption id=${title} onclick="modalOn(this.id)">
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
                                <figcaption id=${title} onclick="modalOn(this.id)">
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
                    let temp_html = `<figure  class="snip1273">
                                <img src=${img} style="background-size: cover;"
                                     alt="sample72"/>
                                <figcaption id=${title} onclick="modalOn(this.id)">
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
                                <figcaption id = ${title} onclick="modalOn()">
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


function modalOn(clicked_id) {
    const modal = document.getElementById("modal")
    $('.modal-overlay').empty()
    modal.style.display = "flex"
    let title = clicked_id
    $.ajax({
        type: 'GET', url: '/modal', data: {
            'title': title
        }, async: false, datatype: 'json', success: function (data) {
            let title = data.video_title;
            let clip = data.video_clip;
            let description = data.description;
            let genre = data.genre;
            let actors = data.actor;
            let rating = data.rating;

            let temp_html = `<div class="modal-window">
                    <iframe width="500" height="300"
                            src=${clip}&mute=1&controls=0
                            title="YouTube video player" frameborder="0"></iframe>
                    <!--                    <div class="tmp_box">-->
                    <!--                    </div>-->
                    <div class="close-area" onclick="modalOff()">X</div>
                    <div class="title" style="display:inline-block;">
                        <h2 style="margin-right: 30px; display:inline-block;">${title}</h2>
                        
                        <div class="buttonControls--container mini-modal has-smaller-buttons"
     data-uia="mini-modal-controls"><a tabindex="0" toolkitsize="small"
                                       data-uia="play-button"
                                       role="link" aria-label="재생"
                                       style="margin-left: 30rem; display:inline-block;"
                                       class="primary-button playLink isToolkit isRound"
                                       href="${clip}&controls=0"
    <button class="color-primary hasIcon round ltr-1knzl35" tabindex="-1" type="button">
        <div class="ltr-1ksxkn9">
            <div class="small ltr-18dhnor" role="presentation">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none"
                     xmlns="http://www.w3.org/2000/svg"
                     class="Hawkins-Icon Hawkins-Icon-Standard">
                    <path d="M3 2.69127C3 1.93067 3.81547 1.44851 4.48192 1.81506L21.4069 11.1238C22.0977 11.5037 22.0977 12.4963 21.4069 12.8762L4.48192 22.1849C3.81546 22.5515 3 22.0693 3 21.3087V2.69127Z"
                          fill="currentColor"></path>
                </svg>
            </div>
        </div>
    </button>
</a>
    <div class="ltr-79elbk">
        <div class="ptrack-content">
            <button aria-label="내가 찜한 콘텐츠에 추가"
                    class="color-supplementary hasIcon round ltr-1knzl35"
                    data-uia="add-to-my-list" type="button">
                <div class="ltr-1ksxkn9">
                    <div class="small ltr-18dhnor" role="presentation">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none"
                             xmlns="http://www.w3.org/2000/svg"
                             class="Hawkins-Icon Hawkins-Icon-Standard">
                            <path fill-rule="evenodd" clip-rule="evenodd"
                                  d="M11 2V11H2V13H11V22H13V13H22V11H13V2H11Z"
                                  fill="currentColor"></path>
                        </svg>
                    </div>
                </div>
            </button>
        </div>
    </div>
    <div class="ltr-79elbk">
        <button aria-label="'좋아요'로 평가하기"
                class="color-supplementary hasIcon round ltr-1knzl35"
                data-uia="thumbsUp-button" type="button">
            <div class="ltr-1ksxkn9">
                <div class="small ltr-18dhnor" role="presentation">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none"
                         xmlns="http://www.w3.org/2000/svg"
                         class="Hawkins-Icon Hawkins-Icon-Standard">
                        <path fill-rule="evenodd" clip-rule="evenodd"
                              d="M9.97014 1C8.88206 1 8 1.88206 8 2.97014V5.76393L5.8023 10.1593L2.72528 11.0385C2.29598 11.1611 2 11.5535 2 12V19C2 19.4465 2.29598 19.8389 2.72528 19.9615L6.17609 20.9475L6.84053 21.2132C8.13985 21.733 9.52641 22 10.9258 22H16.7086C18.5124 22 20.0931 20.7927 20.5677 19.0525L21.9313 14.0525C22.6253 11.5079 20.7097 9 18.0722 9H14.2808L14.7276 7.21268C14.9267 6.41648 14.9267 5.58352 14.7276 4.78732L14.705 4.69686C14.1618 2.52419 12.2097 1 9.97014 1ZM9.78885 6.65836C9.92771 6.38065 10 6.07442 10 5.76393V3.00015C11.3093 3.01358 12.4465 3.90926 12.7647 5.18193L12.7873 5.27239C12.9068 5.75011 12.9068 6.24989 12.7873 6.72761L12.0299 9.75746L11.7192 11H13H18.0722C19.391 11 20.3488 12.254 20.0018 13.5262L18.6381 18.5262C18.4008 19.3964 17.6105 20 16.7086 20H10.9258C9.78085 20 8.64639 19.7815 7.58331 19.3563L6.87139 19.0715C6.83975 19.0589 6.80749 19.0478 6.77472 19.0385L4 18.2457V12.7543L6.35174 12.0824C6.89079 11.9284 7.34044 11.5552 7.59116 11.0538L9.78885 6.65836Z"
                              fill="currentColor"></path>
                    </svg>
                </div>
            </div>
        </button>
    </div>
    <div class="ltr-79elbk">
        <button aria-label="'맘에 안 들어요'로 평가하기"
                class="color-supplementary hasIcon round ltr-1knzl35"
                data-uia="thumbsDown-button" type="button">
            <div class="ltr-1ksxkn9">
                <div class="small ltr-18dhnor" role="presentation">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none"
                         xmlns="http://www.w3.org/2000/svg"
                         class="Hawkins-Icon Hawkins-Icon-Standard">
                        <path fill-rule="evenodd" clip-rule="evenodd"
                              d="M14.0302 23C15.1182 23 16.0003 22.1179 16.0003 21.0299V18.2361L18.198 13.8407L21.275 12.9615C21.7043 12.8389 22.0003 12.4465 22.0003 12V5C22.0003 4.55352 21.7043 4.16113 21.275 4.03848L17.8242 3.05253L17.1598 2.78676C15.8604 2.26703 14.4739 2 13.0745 2H7.29168C5.48788 2 3.90724 3.20728 3.43263 4.94753L2.06899 9.94753C1.37502 12.4921 3.29055 15 5.92805 15H9.71952L9.27269 16.7873C9.07364 17.5835 9.07364 18.4165 9.27269 19.2127L9.2953 19.3031C9.83847 21.4758 11.7906 23 14.0302 23ZM14.2114 17.3416C14.0726 17.6194 14.0003 17.9256 14.0003 18.2361V20.9998C12.691 20.9864 11.5538 20.0907 11.2356 18.8181L11.213 18.7276C11.0935 18.2499 11.0935 17.7501 11.213 17.2724L11.9704 14.2425L12.2811 13H11.0003H5.92805C4.6093 13 3.65153 11.746 3.99852 10.4738L5.36215 5.47376C5.59946 4.60364 6.38978 4 7.29168 4H13.0745C14.2194 4 15.3539 4.21848 16.417 4.64371L17.1289 4.92848C17.1605 4.94113 17.1928 4.95216 17.2256 4.96152L20.0003 5.7543V11.2457L17.6485 11.9176C17.1095 12.0716 16.6599 12.4448 16.4091 12.9462L14.2114 17.3416Z"
                              fill="currentColor"></path>
                    </svg>
                </div>
            </div>
        </button>
    </div>
</div>
                        
                    </div>
                    <div class="content">
                        <p class="genres">장르 : ${genre}  / 연령제한 : ${rating}</p>
                        <p class="des" style="">${description}</p>
                        <p class="starring"><span>Starring: ${actors}
                        </span></p>
                    </div>
                </div>`

            $('.modal-overlay').append(temp_html)

        }


    });

}

function modalOff(clicked_id) {
    modal.style.display = "none"
}

const btnModal = document.getElementById("btn-modal")

btnModal.addEventListener("click", e => {
    modalOn(clicked_id)
})

const closeBtn = modal.querySelector(".close-area")

closeBtn.addEventListener("click", e => {
    modalOff(clicked_id)
})


// 모달창 바깥 영역을 클릭하면 모달창이 꺼지게 하기
// 모달 창 외의 영역을 클릭하면 이벤트 타깃 요소에 modal-overlay 클래스가 있으므로 종료하고,
//     모달 창을 클릭하면 이벤트 타깃 요소에 modal-overlay가 없기 때문에 종료
modal.addEventListener("click", e => {
    const evTarget = e.target
    if (evTarget.classList.contains("modal-overlay")) {
        modalOff()
    }
})


// 모달창이 켜진 상태에서 ESC 버튼을 누르면 모달창이 꺼지게 하기
window.addEventListener("keyup", e => {
    if (isModalOn() && e.key === "Escape") {
        modalOff()
    }
})

// base_main.html 헤더 우측상단 2번째 네비 리스트 열고 닫기 기능
// function dropdownshow(){
//      let drop =  document.getElementById("dropdown");
//      if(drop.style.display=='block'){
// 		drop.style.display = 'none';
//         console.log('나는빡빡이다!')
// 	}else{
// 		drop.style.display = 'block';
//         console.log('나의 모발은 빽빽이다!')
// 	}
// }


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



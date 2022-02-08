// $(document).ready(function () {
//             showvideo();
//         });
//
window.onload = function showvideo() {
    let query = document.getElementById('query').value;
    $.ajax({

        type: "GET",
        url: "/search",
        data: {'query':query},
        async: false,
        datatype: 'json',
        success: function (data) {
            let video_title = data.video_title
            let video_image = data.video_image
            // let detail = data.explain
            let video_clip = data.video_clip
            for (let i = 0; i < video_title.length; i++) {
                let title = video_title[i]
                let img = video_image[i]
                // let explain = detail[i]
                let video_url = video_clip[i]
                let temp_html = `<div class="slider-item slider-item-0" aria-label="${title}">
                                    <div class="title-card-container ltr-0">
                                        <div id="title-card-0-0" class="title-card">
                                            <div class="ptrack-content">
                                                <a href="${video_url}"
                                                   role="link" aria-label="${title}" tabindex="0"
                                                   aria-hidden="false" class="slider-refocus">
                                                    <div class="boxart-size-16x9 boxart-container boxart-rounded">
                                                        <img class="boxart-image boxart-image-in-padded-container"
                                                             src="${img}"
                                                             alt="">
                                                        <div class="fallback-text-container"
                                                             aria-hidden="true"><p
                                                                class="fallback-text">${title}</p>
                                                        </div>
                                                    </div>
                                                    <div class="click-to-change-JAW-indicator">
                                                        <div class="bob-jawbone-chevron">
                                                            <svg width="24" height="24"
                                                                 viewBox="0 0 24 24" fill="none"
                                                                 xmlns="http://www.w3.org/2000/svg"
                                                                 class="svg-icon svg-icon-chevron-down">
                                                                <path fill-rule="evenodd"
                                                                      clip-rule="evenodd"
                                                                      d="M19.293 7.29297L12.0001 14.5859L4.70718 7.29297L3.29297 8.70718L11.293 16.7072C11.4805 16.8947 11.7349 17.0001 12.0001 17.0001C12.2653 17.0001 12.5196 16.8947 12.7072 16.7072L20.7072 8.70718L19.293 7.29297Z"
                                                                      fill="currentColor"></path>
                                                            </svg>
                                                        </div>
                                                    </div>
                                                </a>
                                            </div>
                                            <div class="bob-container"></div>
                                        </div>
                                    </div>
                                </div>`
                $('#fullPage').append(temp_html)
            }
        }
    })

}
    // 중간 메인


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

    // $("#search-input").keyup(function () {
    //     //keyup 이벤트 발생 시 해당 input의 value 가져오기.
    //     var searchText = $(this).val();
    //     //실시간 검색이 필요한 table의 모든 행(tr) 숨김 처리
    //     $("#fullPage > div").hide();
    //     console.log('모든 행 가리기 성공!')
    //     //해당 table에서 input에 입력한 데이터가 있는 td Element 찾기.
    //     var temp = $("#fullPage div").filter(function () {
    //         $(this).toggle($(this).text().toLowerCase().indexOf(searchText) > -1)
    //     });
    //     //입력한 데이터가 있는 Elemnet의 부모 Elemnet(td)만 표시.
    //     $(temp).parent().show();
    //     console.log('타이핑에 맞춰서 보여주기 성공')
    // });




// 검색 기능
// $(document).ready
// window.onload = (function () {
//     $("#search-input").keyup(function () {
//         //keyup 이벤트 발생 시 해당 input의 value 가져오기.
//         var searchText = $(this).val();
//         //실시간 검색이 필요한 table의 모든 행(tr) 숨김 처리
//         // $("#fullPage > div > div").hide();
//         console.log('모든 행 가리기 성공!')
//         //해당 table에서 input에 입력한 데이터가 있는 td Element 찾기.
//         var temp = $("#fullPage > div > div").filter(function () {
//             $(this).toggle($(this).text().toLowerCase().indexOf(searchText) > -1)
//         });
//         //입력한 데이터가 있는 Elemnet의 부모 Elemnet(td)만 표시.
//         $(temp).parent().show();
//         console.log('타이핑에 맞춰서 보여주기 성공')
//     });
// });

// 검색 기능 2
// $(document).ready(function(){
//   $("#search-input").on("keyup", function() {
//     var value = $(this).val().toLowerCase();
//     $("#fullPage div").filter(function() {
//       $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
//     });
//   });
// });
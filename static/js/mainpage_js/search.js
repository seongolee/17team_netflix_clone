$(document).ready(function () {
            showvideo();
        });





function showvideo() {
            // 중간 메인
            $.ajax({
                type: "GET",
                url: "/video/re",
                data: {},
                success: function (response) {
                    let video = response['videos']
                    for (let i = 0; i < prodct.length; i++) {
                        let title = prodct[i]['title']
                        let img_url = prodct[i]['img']
                        let price = prodct[i]['price']
                        let url = prodct[i]['url']

                        let temp_html = `<div class="col" id="search_result">
                                            <div class="card h-100" >
                                                <img class="card-img-top"
                                                     src="${img_url}"
                                                     alt="Card image cap">
                                                <div class="heart">
                                                    <svg onclick="likeheart('${title}')" class="like" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24">
                                                        <path d="M0 0h24v24H0z" fill="none"/>
                                                        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                                                    </svg>
                                                </div>
                                                <div class="card-body" onclick="window.open('${url}')">
                                                    <h5 class="card-text">${title}</h5>
                                                    <p class="price">${price}</p>
                                                </div>
                                            </div>
                                        </div>`
                        $('#fullPage').append(temp_html)
                    }
                }

            })

        }



               //검색 기능
        $(document).ready(function () {
            $("#searchQueryInput").keyup(function () {
                var searchText = $(this).val();
                // $("#fullPage > div > div").hide();
                var temp = $("#fullPage > div").filter(function () {
                    $(this).toggle($(this).text().toLowerCase().indexOf(searchText) > -1)
                });
                $(temp).parent().show();
            });
        });

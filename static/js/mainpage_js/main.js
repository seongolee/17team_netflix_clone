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
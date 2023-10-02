let navbar_layout = document.querySelector("#navbar-container")
let navbar_toggle = document.querySelector("#navbar-toggle")

let navbar_status = 0

navbar_toggle.addEventListener('click', () => {
    if(navbar_status === 0) {
        navbar_layout.style.maxHeight = '800px'

        navbar_status = 1
    } 
    else if(navbar_status === 1) {
        navbar_layout.style.maxHeight = '64px'
        
        navbar_status = 0
    }
})
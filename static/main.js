let jupyterBtn = document.querySelector('.jupyter');

if(jupyterBtn) {
    jupyterBtn.addEventListener('click', () => {
        window.open("http://127.0.0.1:8888/lab?", '_blank');
        console.log("Hello");
    })
}
import Toastify from 'toastify-js'
import "toastify-js/src/toastify.css"

export default function showMessage(message, state='error', callback_fun) {
    let background_color;
    if (state == 'error') {
        background_color = "linear-gradient(to right, #ff5f6d, #ffc371)"
    }else {
        background_color = "linear-gradient(to right, #00b09b, #96c93d)"
    }
    Toastify({
        text: message,
        duration: 3000,
        close: true,
        gravity: "top", // `top` or `bottom`
        position: "left", // `left`, `center` or `right`
        stopOnFocus: true, // Prevents dismissing of toast on hover
        style: {
            background: background_color,
        },
        callback: function () {
            if (!callback_fun) return;
            if (callback_fun) {
                callback_fun()
            }
        },
        onClick: function(){
            alert('debug onclick')
        } // Callback after click
        }).showToast();
}
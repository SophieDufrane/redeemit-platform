document.addEventListener("DOMContentLoaded", function () {
    // Select all Django messages
    const messages = document.querySelectorAll(".custom-message");

    //Loop through messages and set a timer to remove them
    messages.forEach((message) => {
        setTimeout(() => {
            message.style.transition = "opacity 0.5s ease-out";
            message.style.opacity = "0";
            setTimeout(() => {
                message.remove();
            }, 500);
        }, 3000); // Messages disappear after 3 seconds
    });
});
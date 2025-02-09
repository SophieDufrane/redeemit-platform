document.addEventListener("DOMContentLoaded", function () {
    // Select all Django messages
    const messages = document.querySelectorAll(".custom-message");

    //Loop through messages and set a timer to remove them
    messages.forEach((message) => {
        // Add fade-in class after a slight delay
        setTimeout(() => {
            message.classList.add("fade-in");
        }, 100);

        // Remove message after 3 seconds
        setTimeout(() => {
            message.classList.remove("fade-in");
            message.classList.add("fade-out");

            setTimeout(() => {
                message.remove();
            }, 500);
        }, 3000);
    });
});
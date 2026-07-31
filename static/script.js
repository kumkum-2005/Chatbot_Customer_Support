// Chat Box
const chatBox = document.getElementById("chat-box");

// Input Box
const messageInput = document.getElementById("message");


// ----------------------------
// Send Message
// ----------------------------
function sendMessage() {

    const message = messageInput.value.trim();

    if (message === "") {
        return;
    }

    // Show User Message
    chatBox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

    // Scroll Down
    chatBox.scrollTop = chatBox.scrollHeight;

    // Clear Input
    messageInput.value = "";

    // Send Message to Flask
    fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })

    })

    .then(response => response.json())

    .then(data => {

        chatBox.innerHTML += `
            <div class="bot-message">
                ${data.response}
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    })

    .catch(error => {

        chatBox.innerHTML += `
            <div class="bot-message">
                Error: Unable to connect to chatbot.
            </div>
        `;

        console.error(error);

    });

}


// ----------------------------
// Enter Key Support
// ----------------------------
messageInput.addEventListener("keypress", function(event){

    if(event.key === "Enter"){

        sendMessage();

    }

});


// ----------------------------
// Clear Chat
// ----------------------------
function clearChat(){

    chatBox.innerHTML = `
        <div class="bot-message">
            Hello! 👋 Welcome. How can I help you today?
        </div>
    `;

    messageInput.focus();

}
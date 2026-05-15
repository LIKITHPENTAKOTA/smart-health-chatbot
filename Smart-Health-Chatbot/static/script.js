function sendMessage() {
  const inputField = document.getElementById("user-input");
  const message = inputField.value.trim();
  if (message === "") return;

  const chatBox = document.getElementById("chat-box");

  // Add user message
  const userDiv = document.createElement("div");
  userDiv.className = "user-message";
  userDiv.innerText = message;
  chatBox.appendChild(userDiv);

  inputField.value = "";

  // Scroll to bottom
  chatBox.scrollTop = chatBox.scrollHeight;

  // Show typing indicator
  const typingDiv = document.createElement("div");
  typingDiv.className = "bot-message";
  typingDiv.innerText = "🤖 Typing...";
  chatBox.appendChild(typingDiv);
  chatBox.scrollTop = chatBox.scrollHeight;

  // Send to backend
  fetch("/get", {
    method: "POST",
    body: JSON.stringify({ message: message }),
    headers: { "Content-Type": "application/json" }
  })
  .then(response => response.json())
  .then(data => {
    // Remove typing indicator
    chatBox.removeChild(typingDiv);

    // Show bot reply
    const botDiv = document.createElement("div");
    botDiv.className = "bot-message";
    botDiv.innerText = data.reply;
    chatBox.appendChild(botDiv);

    // Scroll again
    chatBox.scrollTop = chatBox.scrollHeight;
  });
}

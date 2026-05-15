// Typing animation for chatbot header
document.addEventListener("DOMContentLoaded", () => {
  const heading = document.querySelector("h1");
  if (heading) {
    let text = heading.innerText;
    heading.innerText = "";
    let i = 0;

    function typeEffect() {
      if (i < text.length) {
        heading.innerText += text.charAt(i);
        i++;
        setTimeout(typeEffect, 80);
      }
    }
    typeEffect();
  }
});

// Form validation
const form = document.querySelector("form");
if (form) {
  form.addEventListener("submit", function (event) {
    const symptoms = document.querySelector("textarea").value.trim();
    if (symptoms === "") {
      alert("⚠️ Please enter at least one symptom.");
      event.preventDefault();
    }
  });
}

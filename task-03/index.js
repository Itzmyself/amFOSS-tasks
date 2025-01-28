document.querySelectorAll(".drum").forEach(function (button) {
  button.addEventListener("click", function () {
    playsound(this.classList[0]); // Use button's class to identify the key
  });
});

// Add event listener for keyboard presses
document.addEventListener("keydown", function (event) {
  playsound(event.key.toLowerCase()); // Use the key pressed
});


function playsound(key) {
  switch (key) {
    case "w":
      new Audio("sounds/crash.mp3").play();
      break;
    case "a":
      new Audio("sounds/kick-bass.mp3").play();
      break;
    case "s":
      new Audio("sounds/snare.mp3").play();
      break;
    case "d":
      new Audio("sounds/tom-1.mp3").play();
      break;
    case "j":
      new Audio("sounds/tom-2.mp3").play();
      break;
    case "k":
      new Audio("sounds/tom-3.mp3").play();
      break;
    case "l":
      new Audio("sounds/tom-4.mp3").play();
      break;
  }
}
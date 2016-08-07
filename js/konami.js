// Number of keypresses in konami code
var konamiCodeLenth = 11;

// The keys used in the konami code
var upKeyCode = 38;
var downKeyCode = 40;
var leftKeyCode = 37;
var rightKeyCode = 39;
var bKeyCode = 66;
var aKeyCode = 65;
var startKeyCode = 32; // space

// The order of the konami code
var konamiCode = [upKeyCode, upKeyCode, downKeyCode, downKeyCode,
                  leftKeyCode, rightKeyCode, leftKeyCode, 
                  rightKeyCode, bKeyCode, aKeyCode, startKeyCode];

// Array to hold the last 11 key presses
var keyPresses = new Array(konamiCodeLenth);

// Update the array of last key presses and check if it holds the konami code
function updateAndCheckKonamiCode(keyCodePressed)
{
  // Shuffle previous keypresses backwards
  for (i = 1; i < konamiCodeLenth; i++)
  {
    keyPresses[i - 1] = keyPresses[i];
  }

  // Add the new keypress
  keyPresses[konamiCodeLenth - 1] = keyCodePressed;

  // Return whether or not we hold the konami code now
  var haveKonamiCode = true;
  for (i = 0; i < konamiCodeLenth; i++)
  {
    if (keyPresses[i] != konamiCode[i])
    {
      haveKonamiCode = false;
    }
  }

  return haveKonamiCode;
}
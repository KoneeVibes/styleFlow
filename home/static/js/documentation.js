const userInput = document.querySelectorAll('input'),
      moveUpScreen = document.querySelector('.move-up'),
      moveDownScreen = document.querySelector('.move-down')
      

function displayScreen(){
    textBoxName = this.name
    textBoxValue = this.value
    
    if (textBoxName === 'move-up'){
        if (textBoxValue === 'class = "move-up"'){
            moveUpScreen.innerHTML = "it works"
        }
    }
    else if(textBoxName === 'move-down'){
        if (textBoxValue === 'class = "move-down"'){
            moveDownScreen.innerHTML = "it works"
        }
    }
}

userInput.forEach(element => {
    element.addEventListener('change', displayScreen)
});



//optimization -- use switch statements and listen for something better than a change.
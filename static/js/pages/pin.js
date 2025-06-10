const buttonGroups = document.querySelectorAll(".button-group")
const inputField = document.getElementById("pinField")

buttonGroups.forEach(function(group){
    group.addEventListener('click', () => {

        // execute some function when click is registered in the parent
        inputField.value += "*";

        if (inputField.value.length >= 4){
            console.log("Mock PIN entered, navigating to success screen");
            window.location.href = "/pin";
        }
    })
})
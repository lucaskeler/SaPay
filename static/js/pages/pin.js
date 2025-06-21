// PIN entry page functionality
const buttonGroups = document.querySelectorAll(".button-group")
const inputField = document.getElementById("pinField")

// Add click listeners to all pin button groups
buttonGroups.forEach(function(group){
    group.addEventListener('click', () => {

        // execute some function when click is registered in the parent
        inputField.value += "*";

        // check if PIN is complete (4 digits)
        if (inputField.value.length >= 4){
            console.log("Mock PIN entered, navigating to loading screen");
            window.location.href = "/loading";
        }
    })
})
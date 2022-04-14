// Bunch of variable selectors
const submit = document.getElementById('submit');
const first = document.getElementsByName("Question1");
const second = document.getElementsByName("Question2");
const third = document.getElementsByName("Question3");
const fourth = document.getElementsByName("Question4");
const fifth = document.getElementsByName("Question5");

// What happens when the submit buttons is clicked on
submit.addEventListener('click', () => {
    // First check that the questions are all filled out
    if (completed(first) && completed(second) && completed(third) && completed(fourth) && completed(fifth)) {
        // Create temp answer sheet
        const answers = {
            Question1: getChoice(first),
            Question2: getChoice(second),
            Question3: getChoice(third),
            Question4: getChoice(fourth),
            Question5: getChoice(fifth)
        };

        // Handing things over to python side for now
        fetch("http://localhost:8080/", {
            method: "POST",
            body: JSON.stringify(answers)
        })
            .catch(errorError);
    }
});

// Function for checking all the values are completed
function completed(choices) {
    for (i = 0; i < choices.length; i++) {
        if (choices[i].checked) {
            return true;
        }
    }
    alert("Make sure to fill all the questions!")
    return false;
}

// Function for retrieving which option was selected
function getChoice(choices) {
    var choice = -1;
    for (i = 0; i < choices.length; i++) {
        if (choices[i].checked) {
            choice = choices[i].value;
        }
    }
    return choice;
}

// Worst case scenario, error message
function errorError(error) {
    console.error(error);
}
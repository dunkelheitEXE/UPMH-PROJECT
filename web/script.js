document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#input_message").addEventListener("keydown", function(e) {
      if (e.code === "Enter") {
          console.log("Presionaste boton")
      }
    });
});


const inputField = document.getElementById("input")
    inputField.addEventListener("keydown", function(e) {
        if (e.code === "Enter") {
            let input = inputField.value;
            inputField.value = "";
            output(input);
    }
});
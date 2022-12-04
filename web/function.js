let consult;
let box = document.getElementById('text');

let userWords = ['hola', 'disculpa'];
let botWords = ['Hola usuario', 'Dime ¿En que puedo ayudarte?'];

let message_confirm = 1;

function sendResponse() {
    consult = document.getElementById('input_message').value;
    word = consult.toLowerCase();
    box.innerHTML += '<h4 style="text-align: right;">' + consult + '</h4>';
    document.getElementById('input_message').value = '';

    // BOT RESPONSE ----
    for (let i = 0; i < userWords.length; i++) {
        if (word == userWords[i]) {
            box.innerHTML += '<h4>Bot: ' + botWords[i] + '</h4>';
            break;
        } else {
            continue;
        }
    }

    //return consult;
}

//let word = sendResponse();


/*
function getResponse() {
    for (let i = 0; i < userWords.length; i++) {
        if (word == userWords[i]) {
            box.innerHTML += '<h4>Bot: ' + botWords[i] + '</h4>';
        } else {
            box.innerHTML += '<h4>Bot: Sorry, but i couldn´t help you</h4>';
        }
    }
}
*/

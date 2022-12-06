let consult;
let box = document.getElementById('text');

let userWords = ['hola',
                'donde esta la enfermeria?',
                'consulta de becas',
                'con quien puedo acudir para becas?',
                ];
let botWords = ['Hola usuario',
                'Usted puede encontrar la enfermeria en el edificio LT1',
                'Con la lic. Elisa Acuña',
                'En el edificio UD1'];

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

let text = document.getElementById('text');

let preguntas = ['¿Donde puedo consultar sobre becas?',
                '¿Donde esta la enfermeria?'];

let responses = ['Dirigete al edificio UD1 con la Lic. Elisa Acuña',
                'Puedes encontrarla en el edificio LT1'];

               
function sendMessage() {
    let q = document.getElementById('selector').value;
    text.innerHTML += '<h4 style="text-align: right;">' + q + '</h4>';

    for (let index = 0; index < preguntas.length; index++) {
        if (q == preguntas[index]) {
            text.innerHTML += '<h4>Bot:' + responses[index] +'</h4>';
            break;
        } else {
            continue;
        }
    }
}



let text = document.getElementById('text');

let preguntas = ['¿Donde puedo consultar sobre becas?',
                '¿Donde esta la enfermeria?',
                '¿Tenemos biblioteca virtual?',
                "¿Es de libre acceso?",
                "¿Puedo tener una consulta en servicio medico?",
                "¿Donde se encuentra serivicio medico?"
            ];

let responses = ['Dirigete al edificio UD1 con la Lic. Elisa Acuña',
                'Puedes encontrarla en el edificio LT1',
                "No por el momento no se cuante con biblioteca virtual pero la escuela cuenta con convenios con paginas que te pueden ser utiles las cuale puedes encontrar en el siguiente link: https://www.upmetropolitana.edu.mx/centro-informacion/bibliotecas-digitales",
                "Si, el acceso es libre, solo ocupas tu credencial de estudiante de la UPMH",
                "NR",
                "NR"
            ];

               
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



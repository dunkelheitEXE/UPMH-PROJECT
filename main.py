from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('UPMH-friend')
# lista = ['Pregunta', 'respuesta del bot', ...]
words = ['Me siento mal', 'Contamos con una enfermeria en el edificio LT1',
        'Necesito ayuda emocional', 'Puedes acudir con tus orientadores en su respectivo edificio',
        #Becas
        '¿Como puedo saber sobre becas', 'Puedes acudir al edificio UD1 con la Lic. Elisa Acuña',
        "¿Que becas de movilidad hay?","Solo hay una beca de movilidad esta dirigida a estudiantes de escasos recursos, que no cuenten con ningún otro apoyo en efectivo o en especie y que colaboren en un servicio administrativo u operativo dentro de la Universidad.",
        "¿Por que no hay respuesta de jovenes escribiendo el futuro?","El encargados de la beca ""Jovenes Escribiendo El futuro"" es gobierno del estado, no la universidad ",
        "¿Cuando son las fechas para las proximas becas?","Para la beca benito juarez podrar realizar el registro hasta el  de Diciembre del 2022,ingresa al sistema de citas. para mas informacion visita: ",
        "¿Cual es el proceso de tramite para becas?","El proseso para cada beca es diferente, el la sigiente lista puedes leer el proseso para cada beca o puedes acercarte a el departamento de becas ",
        "¿Cuales son las becas con las que cuenta la escuela?","¨Lista de becas¨",
        "¿Puedo tener mas de una beca?","No, Solo puedes tener una beca a la vez",
        "¿Como saber si soy beneficiario a una beca?","NR",
        "¿Cuales son las fechas de los resultados de la beca?","NR",
        "¿Que pasa si mi beca fue rechazada?","Lo sentimos mucho,Puedes intentarlo la proxima vez en las proximas fechas",
        #Biblioteca
        "¿Tenemos biblioteca virtual?","No por el momento no se cuante con biblioteca virtual pero la escuela cuenta con convenios con paginas que te pueden ser utiles las cuale puedes encontrar en el siguiente link: https://www.upmetropolitana.edu.mx/centro-informacion/bibliotecas-digitales",
        "¿Es de libre acceso?","Si, el acceso es libre, solo ocupas tu credencial de estudiante de la UPMH ",
        "¿Cual es el proceso de registro para la biblioteca?","NR",
        #Servicios medicos
        "¿Puedo tener una consulta en servicio medico?","NR",
        "¿Donde se encuentra serivicio medico?","NR",
        "¿Que proporciona el servicio medico de la escuela?","NR",
        "¿Como se si ya estoy dado de alta en el serviocio medico?","NR",
        "¿Como hacer el tramite del servicio medico?","NR",
        "¿Cual es la fecha para terminar el proceso de inscripcion al servicio medico?","NR",
        "¿En caso de un posible caso de Covid 19?,¿cual es el protocolo de ermergencia?","NR",
        #Talleres
        "¿Que talleres hay?","NR",
        "¿Para que cuatrimestres estas disponibles los talleres?","NR",
        "¿Cuales son las fechas de inscripción?","NR",
        "¿Cual es el proseso de inscripcion a los talleres?","NR",
        "¿Los talleres son obligatorios?","NR",
        "¿Solo puedo tomar un taller por cuatrimentres?","NR",
        "¿Puedo iniciar mi propio taller?","NR",
        "¿Como puedo cambiar de taller?","NR",
        "¿Se agregran mas talleres?","NR",
        "¿Como puedo abandonar mi taller?","NR",
        "¿Puedo escoger un horario para los talleres?","NR",
        "¿Que pasaria si se cruzan los talleres con mis clases?","NR",
        #Cordinacion de Idiomas
        "¿Habra nuevos idiomas en un futuro?","NR",
        "¿Cuales son los idiomas disponibles?","NR",
        "¿Que es la cordinacion de idiomas?","NR",
        "¿Cuales son las funciones de la coordinacion de idiomas?","NR",
        "¿La coordnacion de idiomas hace los examenes parciales de ingles?","NR",
        #Control Escolar
        "¿Que funciones tiene el departamento de Control Escolar?","NR",
        "¿Que tramites puedo hacer en Control Escolar?","NR",
        #Otros
        "¿El examen iTEP funciona para titulacion?","NR",
        "¿Cuando estara dispnible el gym?","NR",
        "","",
        "","",
        "","",
        "","",
        "","",
         ]

trainer = ListTrainer(bot)
trainer.train(words)

while True:
    consulta = input("User: ")
    respuesta = bot.get_response(consulta)
    # Comando de conexion a JavaScript.c(respuesta)
    print("Bot: ", respuesta)
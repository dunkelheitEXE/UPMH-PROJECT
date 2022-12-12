from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
Leo = ChatBot('Leo')
# lista = ['Pregunta', 'respuesta del bot', ...]
words = ['Me siento mal', 'Contamos con una enfermeria en el edificio LT1',
        'Necesito ayuda emocional', 'Puedes acudir con tus orientadores en su respectivo edificio',
        #Conversacion
        "","",
        "","",
        "","",
        "","",
        "","",
        "Hola","Hola, ¿Como estas? ¿Como puedo ayudarte?",
        "¿Que puedes hacer?","Estoy programado para poder repoder algunas de tus dudas sobre temas referentes a la UPMH",
        "¿sobre que temas me puedes ayudar?","Bueno, puedo ayudarte con los temas siguientes: Becas, Bliblioteca, Servivcion medicos, Talleres, Cordinacion de idiomas, Control escolar y algunas otras dudas puntuales. Pregunta y te dire si tengo uan respouesta para eso",
        "","",
        "","",
        #Alumnos
        "","",
        "","",
        "","",
        "","",
        "","",
        #Becas
        '¿Cómo puedo saber sobre becas?','Puedes acudir al edificio UD1 con la Lic. Elisa Acuña',
        "¿Qué becas de movilidad hay?","Solo hay una beca de movilidad está dirigida a estudiantes de escasos recursos, que no cuenten con ningún otro apoyo en efectivo o en especie y que colaboren en un servicio administrativo u operativo dentro de la Universidad.",
        "¿Por que no hay respuesta de jóvenes escribiendo el futuro?","El encargados de la beca ""Jóvenes Escribiendo El futuro"" es gobierno del estado, no la universidad ",
        "¿Cuándo son las fechas para las próximas becas?","Para la beca benito juarez podrá realizar el registro hasta el  de Diciembre del 2022,ingresa al sistema de citas. para mas información visita: ",
        "¿Cuál es el proceso de trámite para becas?","El proceso para cada beca es diferente, el la siguiente lista puedes leer el proceso para cada beca o puedes acercarte a el departamento de becas ",
        "¿Cuales son las becas con las que cuenta la escuela?","¨Lista de becas¨",
        "¿Puedo tener mas de una beca?","No, Sólo puedes tener una beca a la vez",
        "¿Como saber si soy beneficiario a una beca?","NR",
        "¿Cuales son las fechas de los resultados de la beca?","NR",
        "¿Que pasa si mi beca fue rechazada?","Lo sentimos mucho,Puedes intentarlo la próxima vez en las próximas fechas",
        #Biblioteca
        "¿Tenemos biblioteca virtual?","No por el momento no se cuante con biblioteca virtual pero la escuela cuenta con convenios con paginas que te pueden ser utiles las cuale puedes encontrar en el siguiente link: https://www.upmetropolitana.edu.mx/centro-informacion/bibliotecas-digitales",
        "¿Es de libre acceso?","Si, el acceso es libre, solo ocupas tu credencial de estudiante de la UPMH ",
        "¿Cual es el proceso de registro para la biblioteca?","NR",
        #Servicios médicos
        "¿Puedo tener una consulta en el servicio médico?","NR",
        "¿Dónde se encuentra el servicio médico?","NR",
        "¿Que proporciona el servicio médico de la escuela?","NR",
        "¿Cómo sé si ya estoy dado de alta en el servicio médico?","NR",
        "¿Cómo hacer el trámite del servicio médico?","NR",
        "¿Cuál es la fecha para terminar el proceso de inscripción al servicio médico?","NR",
        "¿En caso de un posible caso de Covid 19?,¿cuál es el protocolo de emergencia?","NR",
        #Talleres
        "¿Qué talleres hay?","NR",
        "¿Para que cuatrimestres estas disponibles los talleres?","NR",
        "¿Cuales son las fechas de inscripción?","NR",
        "¿Cuál es el proceso de inscripción a los talleres?","NR",
        "¿Los talleres son obligatorios?","NR",
        "¿Solo puedo tomar un taller por cuatrimestres?","NR",
        "¿Puedo iniciar mi propio taller?","NR",
        "¿Como puedo cambiar de taller?","NR",
        "¿Se agregan más talleres?","NR",
        "¿Cómo puedo abandonar mi taller?","NR",
        "¿Puedo escoger un horario para los talleres?","NR",
        "¿Que pasaria si se cruzan los talleres con mis clases?","NR",
        #Coordinación de Idiomas
        "¿Habrá nuevos idiomas en un futuro?","NR",
        "¿Cuales son los idiomas disponibles?","NR",
        "¿Qué es la coordinación de idiomas?","NR",
        "¿Cuáles son las funciones de la coordinación de idiomas?","NR",
        "¿La coordinación de idiomas hace los exámenes parciales de ingles?","NR",
        #Control Escolar
        "¿Que funciones tiene el departamento de Control Escolar?","NR",
        "¿Que tramites puedo hacer en Control Escolar?","NR",
        #Otros
        "¿El examen ITEP funciona para titulación?","NR",
        "¿Cuándo estará disponible el gym?","NR",
        "","",
        "","",
        "","",
        "","",
        "","",]

trainer = ListTrainer(Leo)
trainer.train(words)
print("Hola, Soy Leo. ¿En que puedo ayudarte?")
while True:
    consulta = input("Tú: ")
    respuesta = Leo.get_response(consulta)
    # Comando de conexion a JavaScript.c(respuesta)
    print("Leo: ", respuesta)
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('UPMH-friend')
# Hola
# linesahdbhja
# kjsdajkhasd

# lista = ['Pregunta', 'respuesta del bot', ...]
words = ['Me siento mal', 'Contamos con una enfermeria en el edificio LT1',
        'Necesito ayuda emocional', 'Puedes acudir con tus orientadores en su respectivo edificio',
        '¿Como puedo saber sobre becas', 'Puedes acudir al edificio UD1 con la Lic. Elisa Acuña']

trainer = ListTrainer(bot)
trainer.train(words)
#holapapito
#Hola bb
while True:
    consulta = input("User: ")
    respuesta = bot.get_response(consulta)
    print("Bot: ", respuesta)
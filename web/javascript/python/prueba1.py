from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

pruva1 = ChatBot('pruva')

words = ['Hola', 'Hola usuario',
        'Becas', 'Puede acudir con la Lic. elisa acuña']

trainer = ListTrainer(words)
trainer.train(pruva1)


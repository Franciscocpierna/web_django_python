from django.db import models
from django.contrib.auth import get_user_model
 

class Post(models.Model):
    autor = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Título', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo


'''usado no python console
   from textblob import TextBlob
   from deep_translator import GoogleTranslator
   #texto = TextBlob('evolua seu lado geek')
   #texto.translate(to='es')
   texto_original = 'Evolua seu lado geek'
   print(f"Original (PT): {texto_original}")
   traducao_bruta = GoogleTranslator(source='pt', target='en').translate(texto_original)
   texto_espanhol = TextBlob(traducao_bruta)
   print(f"Traduzido (ES): {texto_espanhol}")


   usando pip install translate
   from translate import Translator  
   translator = Translator(to_lang="en")  
   translation = translator.translate("Estou estudando Django na Geek University")  
   print(translation)
Estou estudando Django na Geek University
'''



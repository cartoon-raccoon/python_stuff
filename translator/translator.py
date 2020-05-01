from translate import Translator

with open('translator/translate.txt', mode = 'r') as file:
    to_translate = file.readline()
    
print('to translate: ' + to_translate)
translator = Translator(to_lang='ja')
translated = translator.translate(to_translate)
print('translated: ' + translated)
translated.encode('utf-8')

with open('translator/translate.txt', mode = 'a', encoding='utf-8') as file:
    file.write('\n'+translated)
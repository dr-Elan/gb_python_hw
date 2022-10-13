from cgi import test
import re

text = "Вот мы в автобусе сидим, и сидим, и сидим И из окошечка глядим – все глядим! Глядим назад, глядим вперед – вот так вот, вот так вот Ну что ж автобус не везет – не везет?"

lst_ow_word = re.findall('\w+', text)

[ lst_ow_word.remove(word) for word in lst_ow_word if 'а' in word and 'б' in word and 'с' in word]
    
print(lst_ow_word)
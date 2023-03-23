text = "Esta linea será grabada en un archivo plano " 

with open('chatHistory.txt', 'a') as file:
    file.write(text + '\n'+ '-'*15)
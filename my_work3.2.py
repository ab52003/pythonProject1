def send_email(message, recipient, *, sender = "university.help@gmail.com"): # объявление функции
    if "@" not in recipient or "@" not in sender: # проверка наличия символа @ в эл. адресах получателя и отправителя
        print("Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient) # сообщение об ошибке
    elif recipient.endswith(".com") == False and recipient.endswith(".ru") == False and recipient.endswith(".net") == False: # проверка наличия окончаний .com, .ru, .net в эл. адресе получателя
        print("Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient) # сообщение об ошибке
    elif sender.endswith(".com") == False and sender.endswith(".ru") == False and sender.endswith(".net") == False: # проверка наличия окончаний .com, .ru, .net в эл. адресе отправителя
        print("Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient) # сообщение об ошибке
    elif recipient == sender: # проверка совпадения эл. адресов получателя и отправителя
        print("Нельзя отправить письмо самому себе!") # сообщение об ошибке
    elif sender == "university.help@gmail.com": # проверка эл. адреса отправителя
        print("Письмо успешно отправлено с адреса " + sender + " на адрес " + recipient) # сообщение об успешной отправке
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес " + recipient) # сообщение об отправке с другого адреса

message = input("Введите сообщение: ").split() # ввод данных
recipient = input("Введите адрес эл. почты получателя: ") # ввод данных

send_email(message, recipient) # вызов функции
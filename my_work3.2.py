def send_email(message, recipient, *, sender = "university.help@gmail.com"): # объявление функции
    while 1 > 0: # цикл проверки пустого поля ввода эл. адреса отправителя
        if sender == '' or sender.isspace() == True: # проверка поля ввода эл. адреса отправителя
            sender = 'university.help@gmail.com' # эл. адрес отправителя по умолчанию
        break # выход из цикла
    while 1 > 0: # цикл проверки пустого поля ввода эл. адреса получателя
        if recipient == '' or recipient.isspace() == True: # проверка поля ввода эл. адреса получателя
            recipient = 'не указан' # сообщение в случае пустого поля ввода эл. адреса получателя
        break # выход из цикла
    if "@" not in recipient or "@" not in sender: # проверка наличия символа @ в эл. адресах получателя и отправителя
        print("Невозможно отправить письмо с адреса " + "(" + sender + ")" + " на адрес " + "(" + recipient + ")") # сообщение об ошибке
    elif not recipient.endswith((".com", ".ru", ".net")) or not sender.endswith((".com", ".ru", ".net")): # проверка наличия окончаний .com, .ru, .net в эл. адресе получателя и отправителя
        print("Невозможно отправить письмо с адреса " + "(" + sender + ")" + " на адрес " + "(" + recipient + ")") # сообщение об ошибке
    elif recipient == sender: # проверка совпадения эл. адресов получателя и отправителя
        print("Нельзя отправить письмо самому себе!") # сообщение об ошибке
    elif sender == "university.help@gmail.com": # проверка эл. адреса отправителя
        print("Письмо успешно отправлено с адреса " + "(" + sender + ")" + " на адрес " + "(" + recipient + ")") # сообщение об успешной отправке
    else: # иначе
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + "(" + sender + ")" + " на адрес " + "(" + recipient + ")") # сообщение об отправке с другого адреса


message = input("Введите сообщение: ").split() # ввод сообщения
recipient = input("Введите адрес эл. почты получателя: ") # ввод эл. адреса получателя
sender1 = input("Введите адрес эл. почты отправителя, если он отличается от university.help@gmail.com: ") # ввод эл. адреса отправителя


send_email(message, recipient, sender=sender1) # вызов функции
def send_emails(message, addressee,*, sender = "university.help@gmail.com"):
    if addressee == sender:
            print("Нельзя отправить письмо самому себе!")

    elif sender == "university.help@gmail.com":
            print("Письмо успешно отправлено с адреса", sender, "на адрес", addressee)

    elif "@" and (".com" or ".ru" or ".net") not in (sender or addressee):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", addressee)

    elif sender != "university.help@gmail.com":
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", addressee,".")


send_emails('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_emails('Вы видите это сообщение как лучший студент курса!',
            'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_emails('Пожалуйста, исправьте задание', 'urban.student@mail.ru',
            sender='urban.teacher@mail.uk')
send_emails('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
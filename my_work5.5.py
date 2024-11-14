class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль, возраст.
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    """
    Класс видео, содержащий атрибуты: заголовок, продолжительность, секунда остановки, ограничение по возрасту.
    """

    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False


class UrTube:
    """
    Класс платформа, содержащий атрибуты: список объектов User, список объектов Video, текущий пользователь, User.
    """

    def __init__(self):
        self.users = []
        self.videos = []
        #self.videos_title = []
        self.current_user = None


    def register(self, nickname, password, age):
        if len(self.users) == 0:
            password = hash(password)
            self.current_user = User(nickname, password, age)
            self.users.extend([self.current_user])
        else:
            for i in range(len(self.users)):
                if nickname == self.users[i].nickname:
                    print(f'Пользователь {nickname} уже существует')
            password = hash(password)
            self.current_user = User(nickname, password, age)
            self.users.extend([self.current_user])


    def log_in(self, nickname, password):
        a = 0
        if len(self.users) == 0:
            print(f'Зарегистрируйтесь, пожалуйста')
        else:
            for i in range(len(self.users)):
                if nickname == self.users[i].nickname:
                    password = hash(password)
                    if password == self.users[i].password:
                        self.current_user = nickname
                        self.current_user_age = self.users[i].age
                        a = 1
                    else:
                        a = 1
                        print(f'Неверный пароль')
        if a == 0:
            print(f'Пользователь не найден')


    def log_out(self):
        self.current_user = None


    def add(self, title, duration, time_now, adult_mode):
        if len(self.videos) == 0:
            self.video = Video(title, duration, time_now, adult_mode)
            self.videos.extend([self.video])
        else:
            for i in range(len(self.videos)):
                if title == self.videos[i].title:
                    return f'Такое видео уже есть'
            self.video = Video(title, duration, time_now, adult_mode)
            self.videos.extend([self.video])
            self.videos_duration = self.videos[i].duration


    def get_videos(self, word):
        word = word.lower()
        if len(self.videos) == 0:
            return f'Такого видео нет'
        else:
            i = 0
            list = []
            for i in range(len(self.videos)):
                if word not in self.videos[i].title.lower() or self.videos[i].title.lower() not in word:  # проверка нахождения слова в словах из списка
                    return f'Такого видео нет'
                else:
                    list.append(self.videos[i].title)  # добавление слова в список
                    return list  # возврат списка


    def watch_video(self, word):
        if word not in self.videos_title:
            pass
        else:
            if self.current_user is None:
                return f'Войдите в аккаунт, чтобы смотреть видео'
            else:
                if self.adult_mode and self.age < 18:
                    return f'Вам нет 18 лет, пожалуйста, покиньте страницу'
                else:
                    list_1 = []
                    time_now = 0
                    while time_now < self.duration:
                        time_now +=1
                        list_1.append(time_now)
                    self.time_now = 0
                    return list_1, 'Конец видео', self.time_now



current_user = UrTube()

current_user.register('Den', 123, 15)

current_user.register('Den', 123, 15)

current_user.register('Bob', 123, 22)

current_user.register('Max', 123, 18)

current_user.register('Max', 123, 18)

#current_user.register('Den', 123, 15)

#print(current_user.register('', '', ''))

#print(current_user.log_in('Den', 123))

current_user.log_in('Den',123)

#print(current_user.log_out())

print(current_user.add('Bodyguard', 20, 0, False))

print(current_user.add('Tutsy', 10, 0, True))

print(current_user.add('Tutsy', 10, 0, True))

#print(current_user.add(video_1))

print(current_user.get_videos('tut'))

#print(current_user.watch_video('Tutsy'))

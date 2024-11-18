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

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    """
    Класс платформа, содержащий атрибуты: список объектов User, список объектов Video, текущий пользователь, User.
    """

    def __init__(self):
        self.users = []
        self.videos = []
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
                        self.current_user = None
        if a == 0:
            print(f'Пользователь не найден')
            self.current_user = None


    def log_out(self):
        self.current_user = None


    def add(self, title, duration, time_now, adult_mode):
        a = 0
        if len(self.videos) == 0:
            self.video = Video(title, duration, time_now, adult_mode)
            self.videos.extend([self.video])
        else:
            for i in range(len(self.videos)):
                if title == self.videos[i].title:
                    print(f'Такое видео уже есть')
                    a = 1
            if a == 0:
                self.video = Video(title, duration, time_now, adult_mode)
                self.videos.extend([self.video])


    def get_videos(self, word):
        word = word.lower()
        list = []
        if len(self.videos) == 0:
            print(f'Такого видео нет')
        else:
            for i in range(len(self.videos)):
                if word in self.videos[i].title.lower() or self.videos[i].title.lower() in word:
                    list.append(self.videos[i].title)
                    print(list)
        if len(list) == 0:
            print(f'Такого видео нет')


    def watch_video(self, word):
        list = []
        for i in range(len(self.videos)):
            if word in self.videos[i].title:
                list.append(self.videos[i])
                self.video_adult_mode = self.videos[i].adult_mode
                self.video_duration = self.videos[i].duration
        if len(list) == 0:
            print(f'Такого видео нет')
        else:
            if self.current_user is None:
                print(f'Войдите в аккаунт, чтобы смотреть видео')
            else:
                if self.video_adult_mode and self.current_user_age < 18:
                    print(f'Вам нет 18 лет, пожалуйста, покиньте страницу')
                else:
                    list_1 = []
                    time_now = 0
                    while time_now < self.video_duration:
                        time_now +=1
                        list_1.append(time_now)
                    self.time_now = 0
                    print(' '.join(map(str, list_1)), f'Конец видео')



current_user = UrTube()

current_user.register('Den', 123, 15)

current_user.register('Den', 123, 15)

current_user.register('Bob', 123, 22)

current_user.register('Max', 123, 18)

current_user.register('Max', 123, 18)

current_user.log_in('Den',123)

#current_user.log_out()

current_user.add('Bodyguard', 20, 0, False)

current_user.add('Tutsy', 10, 0, True)

current_user.add('Tutsy', 10, 0, True)

current_user.get_videos('tut')

current_user.watch_video('Tutsy')

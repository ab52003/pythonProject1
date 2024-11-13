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

    def __init__(self, users, videos, videos_title, current_user):
        self.users = []
        self.videos = []
        self.videos_title = []
        self.current_user = current_user


    def register(self, nickname, password, age):
        if nickname in self.users:
           return f'Пользователь {nickname} уже существует'
        else:
            self.users.extend([nickname, password, age])
            self.age = age
            return self.users, self.age


    def log_in(self, nickname, password,):
        if nickname in self.users:
            password_1 = self.users[self.users.index(nickname) + 1]
            if password == password_1:
                self.current_user = nickname
                return self.current_user
            else:
                return f'Неверный пароль'
        else:
            return f'Пользователь не найден'


    def log_out(self):
        self.current_user = None
        return self.current_user


    def add(self, video):
        if video.title in self.videos:
           return f'Такое видео уже есть'
        else:
            self.videos.extend([video.title, video.duration, video.adult_mode])
            self.videos_title.extend([video.title])
            self.adult_mode = video.adult_mode
            self.duration = video.duration
            return self.videos, self.videos_title, self.adult_mode, self.duration


    def get_videos(self, word):
        word = word.lower()
        vid = [x.lower() for x in self.videos_title]
        list = []
        for i in vid:  # цикл
            if word in i or i in word:  # проверка нахождения слова в словах из списка
                list.append(i)  # добавление слова в список
        return list  # возврат списка


    def watch_video(self, word):
        if word not in self.videos_title:
            pass
        else:
            if self.current_user is None:
                return f'Войдите в аккаунт, чтобы смотреть видео'
            else:
                if self.adult_mode and self.age < 18:
                    return f'Вам нет 18 лет, пожалуйста покиньте страницу'
                else:
                    list_1 = []
                    time_now = 0
                    while time_now < self.duration:
                        time_now +=1
                        list_1.append(time_now)
                    self.time_now = 0
                    return list_1, 'Конец видео', self.time_now



user_1 = User('Den', 123, 15)
user_2 = User('Max', 222, 22)
video_1 = Video('Bodyguard', 20, 0, False)
video_2 = Video('Tutsy', 10, 0, True)


current_user = UrTube([], [], [], current_user = None)

print(current_user.register('Den', 123, 15))

#print(current_user.register('', '', ''))

print(current_user.log_in('Den', 123))

#print(current_user.log_in('',''))

#print(current_user.log_out())

print(current_user.add(video_1))

print(current_user.add(video_2))

#print(current_user.add(video_1))

#print(current_user.get_videos(word))

print(current_user.watch_video('Tutsy'))

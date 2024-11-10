from operator import index
from webbrowser import register


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
        self.adult_mode = adult_mode


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
        nickname = input('Введите логин: ')
        password = hash(input('Введите пароль: '))
        age = int(input('Введите возраст: '))
        if nickname in self.users:
           return f'Пользователь {nickname} уже существует'
        else:
            self.users.extend([nickname, password, age])
            return self.users


    def log_in(self, nickname, password):
        nickname = input('Введите логин: ')
        if nickname in self.users:
            password = hash(input('Введите пароль: '))
            password_1 = self.users[self.users.index(nickname) + 1]
            if password == password_1:
                current_user = nickname
                return current_user
            else:
                return f'Неверный пароль'
        else:
            return f'Пользователь не найден'


    def log_out(self):
        return None


    def add(self, video):
        title = video.title
        duration = video.duration
        adult_mode = video.adult_mode
        if title in self.videos:
           return f'Такое видео уже есть'
        else:
            self.videos.extend([title, duration, adult_mode])
            self.videos_title.extend([title])
            return self.videos, self.videos_title


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
            for i in self.users:
                if current_user not in i:
                    return f'Войдите в аккаунт, чтобы смотреть видео'



person = User(nickname = '', password = '', age = '')
video_1 = Video('Bodyguard', 20, 0, False)
video_2 = Video('Tutsy', 10, 0, True)
word = input('Введите слово: ')

current_user = UrTube([], [], [], current_user = ('', ''))

print(current_user.register('', '', ''))

#print(current_user.register('', '', ''))

print(current_user.log_in('', ''))

#print(current_user.log_in('',''))

#print(current_user.log_out())

print(current_user.add(video_1))

print(current_user.add(video_2))

#print(current_user.add(video_1))

#print(current_user.get_videos(word))

print(current_user.watch_video(word))

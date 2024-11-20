team1_num = 5
team2_num = 6

score_1 = 40
score_2 = 42

team1_time = 1552.512
team2_time = 2153.31451

tasks_total = 82

time_avg = (score_1 + score_2)/(team1_time + team2_time)
time_avg_1 = score_1/team1_time
time_avg_2 = score_2/team2_time

challenge_result = 'Победа команды Волшебники данных!'

#Использование %:

print("В команде Мастера кода участников: %s!" % str(team1_num))
print("В команде Волшебники данных участников: %s!" % str(team2_num))

print("Итого сегодня в командах участников: %s и %s!" % (str(team1_num), str(team2_num)))


#Использование format():

print("Команда Волшебники данных решила задач: {}!".format(str(score_2)))
print("Волшебники данных решили задачи за {} с!".format(str(round(team2_time, 2))))
print("Среднее время решения задачи командой Волшебники данных составило {} с!".format(str(round(time_avg_2, 2))))

print("Команда Мастера кода решила задач: {}!".format(str(score_1)))
print("Мастера кода решили задачи за {} с!".format(str(round(team1_time, 2))))
print("Среднее время решения задачи командой Мастера кода составило {} с!".format(str(round(time_avg_1, 2))))


#Использование f-строк:

print(f"Команды решили {str(score_1)} и {str(score_2)} задач.")

print(f"Результат битвы: {challenge_result}")

print(f"Сегодня было решено {str(tasks_total)} задач, в среднем по {str(round(time_avg, 2))} секунды на задачу!")
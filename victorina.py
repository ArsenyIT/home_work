from random import choice

student = input('Представтесь, пожалуйста:')
try:
    level = int(input('Выберите уровень сложности 1 - 3:'))
except:
    level = 1
    print('Установлен 1 уровень сложности.')
if level < 1 or level > 3:
    level = 1
    print('Установлен 1 уровень сложности.')

print(f'Хорошо, {student}. Тебе задачка:')

questions = {
    1: [('Столица России?', 'Москва'), ('Столица Франции?', 'Париж'), ('Столица Италии?', 'Рим'),],
    2: [('Какая самая большая страна по площади?', 'Россия'), ('На каком материке находится Австралия?', 'Австралия'),
        ('Кака самая длинная река в мире?', 'Амазонка'),],
    3: [('Какое самое солёное море?', 'Мёртвое море'), ('Какая самая густонаселённая страна?', 'Индия'),
        ('Какая пустыня самая большая?', 'Сахара')]}

points = 0
for i in range(3):
    question, correct_answer = choice(questions[level])
    print(f'{student}, {question}', end='')
    student_answer = input().strip().lower()
    if student_answer == correct_answer.lower():
        points += 1
        print(f'Правильно!')
    else:
        print(f'Не правельно. Правильный ответ {correct_answer}.')

if points == 3:
    print(f'Ты настоящий знаток географии, {student}!')
elif points == 2:
    print(f'Хорошо, {student}, но можно лучше.')
else:
    print(f'Нужно подтянуть географию, {student}.')
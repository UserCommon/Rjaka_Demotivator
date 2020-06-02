from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

import random
import os

import uuid


font1 = ImageFont.truetype('times.ttf', size=28) #Шрифт
font2 = ImageFont.truetype('times.ttf', size=24) #Шрифт
message = ['Умные мысли часто приследуют его <но он быстрее', 'Кольцо всевластия ', 'Ошибка молодости', 'Машина времени', 'Министр культуры РФ',
'Ленивая Шарлотка', 'Гигант Мысли <Отец Русской Демократии', 'Аниме<ставшее легендой', 'Мыслант Гыгсли< рустец отсосской картодемии',
'Окурок блять<есть 2 рубля', 'Именно он', 'А нахуя?', 'Твой потолок<это чей то пол', 'Вирус XXI Века', 'Его идеи<будут актуальны всегда',
'Его идеи<полная хуйня', 'Пидорасы, что с них взять...<ну просто долбоёбы', 'Подрочил бы ему?', 'Может хватит?', 'Индус-триальные решения',
'А сейчас молодой джедай<ты умрешь.', 'Заголовок<текст', 'Шах и Мат', 'Шах и Мат аутисты<ой то есть аметисты', 'Центр Туризма', 'Теперь понятно стало',
'Игра <изменившая жизнь', 'Алё <ну чё там с деньгами',
] # цитаты !!!Важно!!! если вы ставите < то появляется саб строка


def concatinate(b):
    unique_filename = str(uuid.uuid1())
    color = (255, 255, 255) # цвет
    im1 = Image.open('demotivator.png') # Демотиватор
    im2 = Image.open(image_path) # Наша картинка
    height = 454 #Высота
    width = 454 #Ширина
    demotivator_width = 500 # ширина демотиватора
    demotivator_height = 600 # высота демотиватора
    im2 = im2.resize((width, height)) #Меняем размеры
    im1.paste(im2, (23, 23)) #Вставляем картинку
    draw = ImageDraw.Draw(im1) # Пишем
    msg = random.choice(message) # Рандомное сообщение


    tag_open = msg.find('<') # ищем скобку

    if tag_open > 0: # Если < есть, то создаем текст для суб строки
        msg_main, msg_sub = msg.split('<') # Превращаем в 2 массива Главного и Вторичного текста
        w, h = font1.getsize(msg_main)
        sub_w, sub_h = font2.getsize(msg_sub)
        draw.text((((demotivator_width-w)/2), 490), msg_main, fill=color, font=font1) #Пишем на центре Главный текст (width-w)/2, (490)/1
        draw.text(((demotivator_width-sub_w)/2, 525), msg_sub, fill=color, font=font2) #Пишем на центре Вторичный текст (width-w)/2, (490)/1
    else:
        msg_main = msg
        w, h = font1.getsize(msg_main)
        draw.text((((demotivator_width-w)/2), 490), msg_main, fill=color, font=font1) #Пишем на центре Главный текст (width-w)/2, (490)/1
    im1.save('demotivators/dem' + unique_filename +'.png')
    

def concatinate_plus(b, im1, im2):
    unique_filename = str(uuid.uuid1())
    color = (255, 255, 255) # цвет
    height = 454 #Высота
    width = 454 #Ширина
    demotivator_width = 500 # ширина демотиватора
    demotivator_height = 600 # высота демотиватора
    im2 = im2.resize((width, height)) #Меняем размеры
    im1.paste(im2, (23, 23)) #Вставляем картинку
    draw = ImageDraw.Draw(im1) # Пишем
    msg = random.choice(message) # Рандомное сообщение
    tag_open = msg.find('<') # ищем скобку

    if tag_open > 0: # Если < есть, то создаем текст для суб строки
        msg_main, msg_sub = msg.split('<') # Превращаем в 2 массива Главного и Вторичного текста
        w, h = font1.getsize(msg_main)
        sub_w, sub_h = font2.getsize(msg_sub)
        draw.text((((demotivator_width-w)/2), 490), msg_main, fill=color, font=font1) #Пишем на центре Главный текст (width-w)/2, (490)/1
        draw.text(((demotivator_width-sub_w)/2, 525), msg_sub, fill=color, font=font2) #Пишем на центре Вторичный текст (width-w)/2, (490)/1
    else:
        msg_main = msg
        w, h = font1.getsize(msg_main)
        draw.text((((demotivator_width-w)/2), 490), msg_main, fill=color, font=font1) #Пишем на центре Главный текст (width-w)/2, (490)/1
    im1.save('demotivators/dem' + str(b) +'.png')    
    


b = 0
print('Выберите:\n1)Разные демотиваторы для одной картинки\n2)Много демотиваторов для одной картинки')
choose = int(input()) # Выбор
print('Сколько вариаций/итераций вам нужно?')
count = int(input()) # Число демотиваторов

print('Вставьте путь картинки и ее название(Если картинка в папке проекта, то просто ее название) c разрешением')
image_path = input()

if choose == 1: # Если выбрал 1
    while count > b:
        concatinate(b) # вызов функции
        b += 1
else: #Если выбрал 2
    im2 = Image.open(image_path) # Наша картинка
    while count > b:
        im1 = Image.open('demotivator.png') # Демотиватор
        concatinate_plus(b, im1, im2)
        im2 = im1
        b += 1
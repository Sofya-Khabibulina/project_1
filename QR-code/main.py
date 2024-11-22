import segno
from NewYear import new_year
from Halloween import halloween
from Womenday import women_day

def color_new_year():
    """Функция предлагает выбрать цвет для QR-кода под тематику Новый год"""
    qrcode = segno.make_qr("https://gov.cap.ru/Content2019/news/201912/26/snovim_godm_anime.gif")
    while True:
        your_color = input('Выберите цвет QR-кода (синий, голубой, красный, чёрный): ')  # Выбор пользователем цвета QR-кода
        if your_color == 'синий':
            qrcode.save("basic_qrcode.png", scale=15, border=2, dark="blue", )
            return qrcode
        if your_color == 'красный':
            qrcode.save("basic_qrcode.png", scale=15, border=2, dark="red", )
            return qrcode
        if your_color == 'голубой':
            qrcode.save("basic_qrcode.png", scale=15, border=2, dark="lightblue", )
            return qrcode
        if your_color == 'чёрный':
            qrcode.save("basic_qrcode.png", scale=15, border=2, dark="black", )
            return qrcode
        else:
            print('Выберите цвет из предоженных')

def color_halloween():
    """Функция предлагает выбрать цвет для QR-кода под тематику Хэллоуин"""
    qrcode = segno.make_qr("https://i.gifer.com/T60Y.gif")
    while True:
        your_color = input('Выберите цвет QR-кода (чёрно-оранжевый, чёрно-жёлтый, оранжевый, чёрный): ')  # Выбор пользователем цвета QR-кода
        if your_color == 'чёрно-оранжевый':
            qrcode.save("basic_qrcode.png", scale=38, border=2, dark="orange", light="lightyellow", data_dark="black")
            return qrcode
        if your_color == 'чёрно-жёлтый':
            qrcode.save("basic_qrcode.png", scale=38, border=2, dark="yellow", light="lightyellow", data_dark="black")
            return qrcode
        if your_color == 'оранжевый':
            qrcode.save("basic_qrcode.png", scale=38, border=2, dark="orange", )
            return qrcode
        if your_color == 'чёрный':
            qrcode.save("basic_qrcode.png", scale=38, border=2, dark="black", )
            return qrcode
        else:
            print('Выберите цвет из предоженных')

def color_march():
    """Функция предлагает выбрать цвет для QR-кода под тематику 8 марта"""
    qrcode = segno.make_qr("https://www.izhsm.ru/images/2020_3_7_fioletovye-tyulpany.gif")
    while True:
        your_color = input('Выберите цвет QR-кода (фиолетово-розовый, розовый, фиолетовый, светло-зелёный, чёрный): ')  # Выбор пользователем цвета QR-кода
        if your_color == 'фиолетово-розовый':
            qrcode.save("basic_qrcode.png", scale=12, border=2, dark="pink", light="lightyellow", data_dark="purple")
            return qrcode
        if your_color == 'светло-зелёный':
            qrcode.save("basic_qrcode.png", scale=12, border=2, dark="lightgreen", )
            return qrcode
        if your_color == 'розовый':
            qrcode.save("basic_qrcode.png", scale=12, border=2, dark="pink", )
            return qrcode
        if your_color == 'фиолетовый':
            qrcode.save("basic_qrcode.png", scale=12, border=2, dark="purple", )
            return qrcode
        if your_color == 'чёрный':
            qrcode.save("basic_qrcode.png", scale=12, border=2, dark="black", )
            return qrcode

def favorite_holiday():
    """Выводит тот праздник, который больше всего нравится пользователю"""
    holidays = ['Новый год', 'Хэллоуин', '8 марта']
    while True:
        holiday = input("Какой праздник вам больше нравится/необходим для создания QR-кода (Новый год, Хэллоуин, 8 марта)? ").strip()

        if holiday in holidays:
            print(f"Вы выбрали: {holiday}")
            return holiday
        else:
            print("Выберите один из предложенных праздников: Новый год, Хэллоуин или 8 марта.")

favorite_holiday()
user_input = input('Вы хотите создать тематический QR-код для вашего любимого праздника? (Если хотите стандартный, напишите "нет") (да/нет): ').strip().upper()
# Генерация стандартного QR-кода
# Алгоритм создания самого QR-кода взят из https://realpython.com/python-generate-qr-code/
# Некоторые модули, созданные мной, прогонялись через нейросети, чтобы проверить наличие ошибок в моём коде
if user_input=='НЕТ':
    qrcode = segno.make_qr("This is your QR-code")
    qrcode.save("basic_qrcode.png", scale=12, border= 7,)
    print('Ваш QR-код сохранен в basic_qrcode.png')
elif user_input=='ДА':
    new_input = input('Выберите тематику ещё раз (Новый год, Хэллоуин, 8 марта): ').strip().upper()
    # Генерация новогоднего QR-кода с изменением цвета
    if new_input=='НОВЫЙ ГОД':
        color_new_year()
        new_year("basic_qrcode.png",
                               "https://printfelt.ru/wa-data/public/shop/products/89/43/4389/images/10965/Fon_novogodniy-8.750x0.jpg",
                               "your_qrcode.png")
    # Генерация QR-кода с изменением цвета на Хэллоуин
    elif new_input=='ХЭЛЛОУИН':
        color_halloween()
        halloween("basic_qrcode.png",
                 "https://i.pinimg.com/originals/b6/83/b8/b683b85e579e1150bb573877b96bcd4f.jpg",
                 "your_qrcode.png")
    # Генерация QR-кода с изменением цвета на 8 марта
    elif new_input=='8 МАРТА':
        color_march()
        women_day("basic_qrcode.png",
                 "https://img.goodfon.com/original/1280x720/2/6f/tsvety-konvert-tiulpany-rozovye.jpg",
                 "your_qrcode.png")
    else:
        print ('Такой тематики нет')
else:
    print('Неверный ответ')

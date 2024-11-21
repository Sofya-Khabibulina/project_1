import segno
from NewYear import new_year
from Halloween import halloween
from Womenday import women_day
def favorite_holiday():
    """Выводит тот праздник, который больше всего нравится пользователю"""
    holidays = ['Новый год', 'Хэллоуин', '8 марта']
    while True:
        holiday = input("Какой праздник вам больше нравится (Новый год, Хэллоуин, 8 марта)? ").strip()

        if holiday in holidays:
            print(f"Ваш любимый праздник: {holiday}")
            return holiday
        else:
            print("Выберите один из предложенных праздников: Новый год, Хэллоуин или 8 марта.")

favorite_holiday()
user_input = input('Вы хотите создать тематический QR-код для вашего любимого праздника? (да/нет): ').strip().upper()
# Генерация стандартного QR-кода
# Алгоритм создания самого QR-кода взят из https://realpython.com/python-generate-qr-code/
if user_input=='НЕТ':
    qrcode = segno.make_qr("This is your QR-code")
    qrcode.save("basic_qrcode.png", scale=12, border= 7,)
    print('Ваш QR-код сохранен в basic_qrcode.png')
elif user_input=='ДА':
    new_input = input('Выберите тематику ещё раз (Новый год, Хэллоуин, 8 марта): ').strip().upper()
    # Генерация новогоднего QR-кода с изменением цвета
    if new_input=='НОВЫЙ ГОД':
        qrcode = segno.make_qr("https://gov.cap.ru/Content2019/news/201912/26/snovim_godm_anime.gif")
        qrcode.save(
            "basic_qrcode.png",
            scale=15,
            border= 2,
            dark="red",
            light="white"
)
        new_year("basic_qrcode.png",
                               "https://printfelt.ru/wa-data/public/shop/products/89/43/4389/images/10965/Fon_novogodniy-8.750x0.jpg",
                               "your_qrcode.png")
    # Генерация QR-кода с изменением цвета на Хэллоуин
    elif new_input=='ХЭЛЛОУИН':
        qrcode = segno.make_qr("https://i.gifer.com/T60Y.gif")
        qrcode.save(
            "basic_qrcode.png",
            scale=38,
            border=2,
            dark="orange",
            light="lightyellow",
            data_dark="black"
)
        halloween("basic_qrcode.png",
                 "https://i.pinimg.com/originals/b6/83/b8/b683b85e579e1150bb573877b96bcd4f.jpg",
                 "your_qrcode.png")
    # Генерация QR-кода с изменением цвета на 8 марта
    elif new_input=='8 МАРТА':
        qrcode = segno.make_qr("https://www.izhsm.ru/images/2020_3_7_fioletovye-tyulpany.gif")
        qrcode.save(
            "basic_qrcode.png",
            scale=12,
            border=2,
            dark="lightgreen",
)
        women_day("basic_qrcode.png",
                 "https://img.goodfon.com/original/1280x720/2/6f/tsvety-konvert-tiulpany-rozovye.jpg",
                 "your_qrcode.png")
    else:
        print ('Такой тематики нет')
else:
    print('Неверный ответ')
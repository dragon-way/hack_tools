import serial

ser = serial.Serial('com11', 9600, timeout=0.050)
in_m = []


message = False


# Открываем Serial порт ('COMX' замените на имя вашего порта)

    # # Отправляем строку "Hello, Arduino!" на Arduino, предварительно преобразовав ее в байты
    # i = f"{input("send")} \n"
    # ser.write(i.encode())
    # Читаем ответ от Arduino через Serial порт
while ser.in_waiting != 0 and message == True:
    response = ser.read()

    #print(response.decode("utf-8"))

    # Декодируем ответ из байтов в строку с использованием UTF-8
    for r in response:
        in_m.append(chr(r))

    print(in_m[2:-11])
    message = True
# Закрываем порт

#ser.write(open("target.txt","rb").read())

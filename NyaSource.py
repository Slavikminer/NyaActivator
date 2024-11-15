import time, subprocess
print("NyaActivator")
print("by SlavikMiner")
print("Ver 1.1, RU")
time.sleep(3)
keydel = "slmgr.vbs /upk"
win1 = "slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX"
win2 = "slmgr.vbs /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
win3 = "slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX"
win4 = "slmgr.vbs /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
winold1 = "slmgr.vbs /ipk FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4"
winold2 = "slmgr.vbs /ipk 33PXH-7Y6KF-2VJC9-XBBR8-HVTHH"
winold3 = "slmgr.vbs /ipk 73KQT-CD9G6-K7TQG-66MRP-CQ22C"
win2old1 = "slmgr.vbs /ipk YFKBB-PQJJV-G996G-VWGXY-2V3X8"
win2old2 = "slmgr.vbs /ipk VKK3X-68KWM-X2YGT-QR4M6-4BWMV"
kms1 = "slmgr /skms kms.digiboy.ir"
ato1 = "slmgr /ato"
def win7thinpc():
    print("Удаление текущего ключа...")
    process = subprocess.Popen(['cmd', '/C', keydel], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    print("Текущий ключ активатора удален.")
    time.sleep(2)
    print("Начинаю активацию...")
    print("Ввод ключа системы...")
    process = subprocess.Popen(['cmd', '/C', winold3], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Ввод сервера активации...")
    process = subprocess.Popen(['cmd', '/C', kms1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Отправка запроса на активацию системы...")
    process = subprocess.Popen(['cmd', '/C', ato1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(2)
    print("Запрос на активацию Windows 7 ThisPc отправлен!")
    print("Результаты активации вы получите в другом окне")
    print("в течение 30 секунд.")
    print("Спасибо что выбрали NyaActivator :3")
def win7edu():
    print("Удаление текущего ключа...")
    process = subprocess.Popen(['cmd', '/C', keydel], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    print("Текущий ключ активатора удален.")
    time.sleep(2)
    print("Начинаю активацию...")
    print("Ввод ключа системы...")
    process = subprocess.Popen(['cmd', '/C', winold2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Ввод сервера активации...")
    process = subprocess.Popen(['cmd', '/C', kms1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Отправка запроса на активацию системы...")
    process = subprocess.Popen(['cmd', '/C', ato1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(2)
    print("Запрос на активацию Windows 7 Образовательная отправлен!")
    print("Результаты активации вы получите в другом окне")
    print("в течение 30 секунд.")
    print("Спасибо что выбрали NyaActivator :3")
def win7pro():
    print("Удаление текущего ключа...")
    process = subprocess.Popen(['cmd', '/C', keydel], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    print("Текущий ключ активатора удален.")
    time.sleep(2)
    print("Начинаю активацию...")
    print("Ввод ключа системы...")
    process = subprocess.Popen(['cmd', '/C', winold1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Ввод сервера активации...")
    process = subprocess.Popen(['cmd', '/C', kms1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Отправка запроса на активацию системы...")
    process = subprocess.Popen(['cmd', '/C', ato1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(2)
    print("Запрос на активацию Windows 7 Профессиональная отправлен!")
    print("Результаты активации вы получите в другом окне")
    print("в течение 30 секунд.")
    print("Спасибо что выбрали NyaActivator :3")
def win11home():
    print("Удаление текущего ключа...")
    process = subprocess.Popen(['cmd', '/C', keydel], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    print("Текущий ключ активатора удален.")
    time.sleep(2)
    print("Начинаю активацию...")
    print("Ввод ключа системы...")
    process = subprocess.Popen(['cmd', '/C', win4], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Ввод сервера активации...")
    process = subprocess.Popen(['cmd', '/C', kms1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Отправка запроса на активацию системы...")
    process = subprocess.Popen(['cmd', '/C', ato1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(2)
    print("Запрос на активацию Windows 11 Home отправлен!")
    print("Результаты активации вы получите в другом окне")
    print("в течение 30 секунд.")
    print("Спасибо что выбрали NyaActivator :3")
    time.sleep(90)
def win11pro():
    print("Удаление текущего ключа...")
    process = subprocess.Popen(['cmd', '/C', keydel], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    print("Текущий ключ активатора удален.")
    time.sleep(2)
    print("Начинаю активацию...")
    print("Ввод ключа системы...")
    process = subprocess.Popen(['cmd', '/C', win3], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(2)
    print("Ввод сервера активации...")
    process = subprocess.Popen(['cmd', '/C', kms1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Отправка запроса на активацию системы...")
    process = subprocess.Popen(['cmd', '/C', ato1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(2)
    print("Запрос на активацию Windows 11 Pro отправлен!")
    print("Результаты активации вы получите в другом окне")
    print("в течение 30 секунд.")
    print("Спасибо что выбрали NyaActivator :3")
    time.sleep(90)
def win10home():
    print("Удаление текущего ключа...")
    process = subprocess.Popen(['cmd', '/C', keydel], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    print("Текущий ключ активатора удален.")
    time.sleep(2)
    print("Начинаю активацию...")
    print("Ввод ключа системы...")
    process = subprocess.Popen(['cmd', '/C', win2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Ввод сервера активации...")
    process = subprocess.Popen(['cmd', '/C', kms1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Отправка запроса на активацию системы...")
    process = subprocess.Popen(['cmd', '/C', ato1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(2)
    print("Запрос на активацию Windows 10 Home отправлен!")
    print("Результаты активации вы получите в другом окне")
    print("в течение 30 секунд.")
    print("Спасибо что выбрали NyaActivator :3")
    time.sleep(90)
def win10pro():
    print("Удаление текущего ключа...")
    process = subprocess.Popen(['cmd', '/C', keydel], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    print("Текущий ключ активатора удален.")
    time.sleep(2)
    print("Начинаю активацию...")
    print("Ввод ключа системы...")
    process = subprocess.Popen(['cmd', '/C', win1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Ввод сервера активации...")
    process = subprocess.Popen(['cmd', '/C', kms1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Отправка запроса на активацию системы...")
    process = subprocess.Popen(['cmd', '/C', ato1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(2)
    print("Запрос на активацию Windows 10 Pro отправлен!")
    print("Результаты активации вы получите в другом окне")
    print("в течение 30 секунд.")
    print("Спасибо что выбрали NyaActivator :3")
    time.sleep(90)
def winvistabus():
    print("Удаление текущего ключа...")
    process = subprocess.Popen(['cmd', '/C', keydel], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    print("Текущий ключ активатора удален.")
    time.sleep(2)
    print("Начинаю активацию...")
    print("Ввод ключа системы...")
    process = subprocess.Popen(['cmd', '/C', win2old1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Ввод сервера активации...")
    process = subprocess.Popen(['cmd', '/C', kms1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Отправка запроса на активацию системы...")
    process = subprocess.Popen(['cmd', '/C', ato1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(2)
    print("Запрос на активацию Windows Vista Business отправлен!")
    print("Результаты активации вы получите в другом окне")
    print("в течение 30 секунд.")
    print("Спасибо что выбрали NyaActivator :3")
    time.sleep(90)
def winvistaent():
    print("Удаление текущего ключа...")
    process = subprocess.Popen(['cmd', '/C', keydel], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    print("Текущий ключ активатора удален.")
    time.sleep(2)
    print("Начинаю активацию...")
    print("Ввод ключа системы...")
    process = subprocess.Popen(['cmd', '/C', win2old2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Ввод сервера активации...")
    process = subprocess.Popen(['cmd', '/C', kms1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(4)
    print("Отправка запроса на активацию системы...")
    process = subprocess.Popen(['cmd', '/C', ato1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if out:
        result += out.decode('cp866').encode('utf-8')
    if err:
        result += err.decode('cp866').encode('utf-8')
    time.sleep(2)
    print("Запрос на активацию Windows Vista Enterprise отправлен!")
    print("Результаты активации вы получите в другом окне")
    print("в течение 30 секунд.")
    print("Спасибо что выбрали NyaActivator :3")
    time.sleep(90)
def win7menu():
    print("Выберите вашу операционную систему")
    print("1. Windows 7 Профессиональная")
    print("2. Windows 7 Образовательная")
    print("3. Windows 7 ThinPC (не проверено)")
    print("Домашняя версия не доступна.")
    print("Введите цифру.")
    winwin = int(input())
    if winwin == 1:
        win7pro()
    elif winwin == 2:
        win7edu()
    elif winwin == 3:
        win7thinpc()
    else:
        print("Вы ввели неверное число")
        print("Для продолжения работы придётся перезапустить активатор.")
        input()
def winvistamenu():
    print("Выберите вашу операционную систему")
    print("1. Windows Vista Business")
    print("2. Windows Vista Enterprise")
    print("Остальные версии не доступны.")
    print("Введите цифру.")
    winwinwin = int(input())
    if winwinwin == 1:
        winvistabus()
    elif winwinwin == 2:
        winvistaent()
    else:
        print("Вы ввели неверное число")
        print("Для продолжения работы придётся перезапустить активатор.")
        input()
print("Можем приступать к активации")
time.sleep(1)
print("Выберите вашу операционную систему")
print("1. Windows 10 Pro")
print("2. Windows 10 Home")
print("3. Windows 11 Pro")
print("4. Windows 11 Home")
print("5. Windows 8")
print("6. Windows 7")
print("7. Windows Vista")
print("Введите цифру.")
win = int(input())
if win == 1:
    win10pro()
elif win == 2:
    win10home()
elif win == 3:
    win11pro()
elif win == 4:
    win11home()
elif win == 5:
    print("Windows 8 пока нет.")
    print("Ждите новых обновлений :3")
    input()
elif win == 6:
    win7menu()
elif win == 7:
    winvistamenu()
else:
    print("Вы ввели неверное число")
    print("Для продолжения работы придётся перезапустить активатор.")
    input()
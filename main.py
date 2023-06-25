import os
import json
import ctypes
from art import tprint
from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.RED)
tprint("VXRGXS", "rand", space=1)

ctypes.windll.kernel32.SetConsoleTitleA(b"MMR")

print(Style.BRIGHT)

work = True
name = os.environ["UserName"]
while work:
    content = os.listdir("C:\\Users\\" + name + "\\AppData\\LocalLow\\1CGS\\Caliber\\Replays")
    content.sort(
        key=lambda x: os.path.getmtime("C:\\Users\\" + name + "\\AppData\\LocalLow\\1CGS\\Caliber\\Replays\\" + x),
        reverse=True)
    for i, file in enumerate(content):
        print(Fore.BLUE + str(i) + " " + Fore.GREEN + content[i])
    number = input(Fore.BLUE + "Введите номер реплея\n")
    os.system('CLS')
    if number.isdigit() and int(number) < len(content):
        number = int(number)
        with open("C:\\Users\\" + name + "\\AppData\\LocalLow\\1CGS\\Caliber\\Replays\\" + content[number], "rb") as f:
            text = f.readline()
            text = str(text)  # приведение к str с byte
            text = text[text.find("{"):text.rfind("}") + 2]  # обрезка с первого { по последний }
            sub_text = text[:text.find("\"Log\"")]  # обрезка первой части "Log"
            sub_text1 = sub_text[:sub_text.rfind("]}") + 2]  # удаление "Log" в первой части
            if len(sub_text1) < 2:
                print(Fore.RED, "Не удается открыть реплей")
                continue
            block1 = json.loads(sub_text1)  # 1 блок логов
            players = block1["7"]  # Список игроков в 1 блоке
            regime = block1["4"]
            pveregime = {
                "polygon": 1, "pvehard": 4, "pve": 4, "onslaughtnormal": 4, "onslaughthard": 4, "pvpdestruction": 8,
                "pvpve": 8, "pvp": 8, "hacking": 8
            }
            # Вывод инфы
            print(Fore.MAGENTA + "ID реплея: ", Fore.RED, block1["0"], Fore.MAGENTA, "\tКарта: ", Fore.RED, block1["2"],
                  Fore.MAGENTA, "\tРежим: ", Fore.RED, block1["4"], Fore.MAGENTA, "\tРегион: ", Fore.RED,
                  block1["6"])
            for i in range(int(pveregime.get(regime))):
                if i == 0:
                    print(Fore.BLUE + "\nКоманда #1")
                if i == 4:
                    print(Fore.BLUE + "\nКоманда #2")
                player = players[i]
                playerOper = player["8"]
                print(
                    f"""{Fore.RED}{("{0:<18}").format(player["2"])}{Fore.MAGENTA}ID группы: {Fore.RED}{("{0:<10}").format(player["1"])}{Fore.MAGENTA}ID игрока: {Fore.RED}{("{0:<10}").format(player["0"])}{Fore.MAGENTA}Опер: {Fore.RED}{("{0:<14}").format(playerOper["1"])}{Fore.MAGENTA}Уровень: {Fore.RED}{("{0:<4}").format(player["3"])}{Fore.MAGENTA}""")


            # Вывод доп инфы
            while True:
                word = input(
                    f"""{Fore.BLUE}\ninfo{Fore.GREEN} - Доп информация об игроках\n{Fore.BLUE}rep{Fore.GREEN} - к списку реплеев\n{Fore.BLUE}exit{Fore.GREEN} - выход\n""")
                if word == "info":
                    for i in range(int(pveregime.get(regime))):
                        player = players[i]
                        playerOper = player["8"]
                        print(Fore.BLUE, i, Fore.GREEN, player["2"], Fore.BLUE)
                        if i == 3:
                            print("")
                    numberPlayer = input(
                        "\n*********************\nВведите номер игрока, чтобы посмотреть дополнительную информацию:\n")
                    if numberPlayer.isdigit() and int(numberPlayer) < int(pveregime.get(regime)):
                        player = players[int(numberPlayer)]
                        playerOper = player["8"]
                        print(
                            f"""
{Fore.RED}{player["2"]}\n
{Fore.MAGENTA}Оперативник:            {Fore.RED}{playerOper["1"]}
{Fore.MAGENTA}Резервы:                {Fore.RED}{playerOper["14"]}
{Fore.MAGENTA}Установленные навыки:   {Fore.RED}{playerOper["15"]}
{Fore.MAGENTA}Уровень оперативника:   {Fore.RED}{playerOper["18"]}
{Fore.MAGENTA}Престижа оперативника:  {Fore.RED}{playerOper["19"]}
{Fore.MAGENTA}Опыт оперативника:      {Fore.RED}{playerOper["4"]}

{Fore.MAGENTA}Навыки аккаунта:
{Fore.RED}{player["20"]}
""")

                    else:
                        print(Fore.RED, "\n***Введен неверный номер***")
                        break
                elif word == "exit":
                    work = False
                    break
                elif word == "rep":
                    os.system('CLS')
                    break
                else:
                    print(Fore.RED, "\nОшибка")
                    continue

    else:
        os.system('CLS')
        print(Fore.RED, "\n***Введен неверный номер***")

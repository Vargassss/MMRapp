import os
import json
import ctypes
from art import tprint
from colorama import init
from colorama import Fore, Back, Style

init()

allOp = {  # Словарь ид оперативника : название
    "recruita": "", "recruitg": "Р-Поддержка", "recruitm": "Р-Медик", "recruits": "Р-Снайпер",
    "fsb2004a": "Волк", "fsb2004g": "Алмаз", "fsb2004m": "Дед", "fsb2004s": "Стрелок",
    "fsb2016a": "Перун", "fsb2016g": "Сварог", "fsb2016m": "Травник", "fsb2016s": "Сокол",
    "sso2013a": "Ворон", "sso2013g": "Спутник", "sso2013m": "Бард", "sso2013s": "Комар",
    "22spn2016a": "Плут", "22spn2016g": "Кит", "22spn2016m": "Каравай", "22spn2016s": "Тень",
    "grom2014a": "Кошмар", "grom2014g": "Пророк", "grom2014m": "Микола", "grom2014s": "Стилет",
    "ksk2011a": "Рейн", "ksk2011g": "Штерн", "ksk2011m": "Шатц", "ksk2011s": "Курт",
    "seal2014a": "Корсар", "seal2014g": "Бурбон", "seal2014m": "Монк", "seal2014s": "Скаут",
    "tfb2008a": "Стрелинг", "tfb2008g": "Бишоп", "tfb2008m": "Ватсон", "tfb2008s": "Арчер",
    "raid2017a": "Авангард", "raid2017g": "Бастион", "raid2017m": "Велюр", "raid2017s": "Вагабонд",
    "nesher2015a": "Афела", "nesher2015g": "Хагана", "nesher2015m": "Шаршерет", "nesher2015s": "Эйма",
    "ezapaca": "Фаро", "ezapacg": "Матадор", "ezapacm": "Мигель", "ezapacs": "Диабло",
    "arystana": "Мустанг", "arystang": "Тибет", "arystanm": "Багги", "arystans": "Султан",
    "belssoa": "Лазутчик", "belssog": "Зубр", "belssom": "Каваль", "belssos": "Бусел",
    "amfa": "Старкад", "amfg": "Один", "amfm": "Фрейр", "amfs": "Видар",
    "jiaolonga": "Шаовэй", "jiaolongg": "Инчжоу", "jiaolongm": "Яован", "jiaolongs": "Цанлун",
    "csta": "Слай", "cstg": "Фортресс", "cstm": "Боунс", "csts": "Аваланш"
}

groups = {  # Создаем номер группы и с уникальным цветом(максимум возможно 4 группы)
    0: Back.GREEN, 1: Back.CYAN, 2: Back.WHITE, 3: Back.YELLOW
}
allRegimes = {  # Список режимов и количество игроков в нем
    "polygon": 1, "pvehard": 4, "pve": 4, "onslaughtnormal": 4, "onslaughthard": 4, "pvpdestruction": 8,
    "pvpve": 8, "pvp": 8, "hacking": 8
}

print(Fore.RED)
tprint("VXRGXS", "rand")

ctypes.windll.kernel32.SetConsoleTitleA(b"MMR")

print(Style.BRIGHT)

work = True
name = os.environ["UserName"]
while work:
    content = os.listdir("C:\\Users\\" + name + "\\AppData\\LocalLow\\1CGS\\Caliber\\Replays")
    content.sort(  # сортируем по времени
        key=lambda x: os.path.getmtime("C:\\Users\\" + name + "\\AppData\\LocalLow\\1CGS\\Caliber\\Replays\\" + x),
        reverse=True)
    for i, file in enumerate(content):  # вывод реплеев
        print(Fore.BLUE + str(i) + " " + Fore.GREEN + content[i])
    number = input(Fore.BLUE + "Введите номер реплея\n")
    os.system('CLS')
    if number.isdigit() and int(number) < len(content):  # проверка введенного на число, количество
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

            print(Fore.MAGENTA + "ID реплея: ", Fore.RED, block1["0"], Fore.MAGENTA, "\tКарта: ", Fore.RED, block1["2"],
                  Fore.MAGENTA, "\tРежим: ", Fore.RED, block1["4"], Fore.MAGENTA, "\tРегион: ", Fore.RED,
                  block1["6"])

            gr = [players[i]["1"] for i in range(int(allRegimes.get(regime)))]  # Заполняем список всеми ИД групп
            gr2 = {}
            grCount = 0
            for i in range(len(gr)):    # словарь с ид группы и ид цвета
                if gr.count(players[i]["1"]) > 1 and players[i]["1"] not in gr2:
                    gr2[players[i]["1"]] = grCount
                    grCount += 1
            for i in range(int(allRegimes.get(regime))):
                color = " "
                if i == 0:
                    print(Fore.BLUE + "\nКоманда #1")
                elif i == 4:
                    print(Fore.BLUE + "\nКоманда #2")
                if players[i]["1"] in gr2:  # проверка, состоит ли игрок в группе
                    color = groups[gr2.get(players[i]["1"])] + " "
                    if players[i]["1"] == players[i]["0"]:  # проверка на лидера группы
                        color = groups[gr2.get(players[i]["1"])] + Fore.BLACK + Style.NORMAL + "!"
                print(
                    f"""{color}{Back.RESET + Style.BRIGHT + Fore.RED}{("{0:<20}").format(players[i]["2"])}{Fore.MAGENTA}ID игрока: {Fore.RED}{("{0:<10}").format(players[i]["0"])}{Fore.MAGENTA}Опер: {Fore.RED}{("{0:<14}").format(allOp[players[i]["8"]["1"]] if allOp.get(players[i]["8"]["1"]) != None else players[i]["8"]["1"])}{Fore.MAGENTA}Уровень: {Fore.RED}{("{0:<4}").format(players[i]["3"])}{Fore.MAGENTA}""")

            # Вывод доп инфы
            while True:
                word = input(
                    f"""{Fore.BLUE}\ni (info){Fore.GREEN} - Дополнительная информация об игроках\n{Fore.BLUE}r (replays){Fore.GREEN} - к списку реплеев\n{Fore.BLUE}e (exit){Fore.GREEN} - выход\n""").lower()
                if word == "info" or word == "i":
                    for i in range(int(allRegimes.get(regime))):
                        print(Fore.BLUE, i, Fore.GREEN, players[i]["2"], Fore.BLUE)
                        if i == 3:
                            print("")
                    numberPlayer = input(
                        "\n*********************\nВведите номер игрока, чтобы посмотреть дополнительную информацию:\n")
                    if numberPlayer.isdigit() and int(numberPlayer) < int(allRegimes.get(regime)):
                        player = players[int(numberPlayer)]
                        print(f"""{Fore.RED}{player["2"]}\n
{Fore.MAGENTA}Оперативник:            {Fore.RED}{allOp[player["8"]["1"]] if allOp.get(player["8"]["1"]) != None else player["8"]["1"]}
{Fore.MAGENTA}Резервы:                {Fore.RED}{player["8"]["14"]}
{Fore.MAGENTA}Установленные навыки:   {Fore.RED}{player["8"]["15"]}
{Fore.MAGENTA}Уровень оперативника:   {Fore.RED}{player["8"]["18"]}
{Fore.MAGENTA}Престижа оперативника:  {Fore.RED}{player["8"]["19"]}
{Fore.MAGENTA}Опыт оперативника:      {Fore.RED}{player["8"]["4"]}

{Fore.MAGENTA}Навыки аккаунта:
{Fore.RED}{player["20"]}
""")

                    else:
                        print(Fore.RED, "\n***Введен неверный номер***")
                        break
                elif word == "exit" or word == "e":
                    work = False
                    break
                elif word == "replays" or word == "r":
                    os.system('CLS')
                    break
                else:
                    print(Fore.RED, "\nОшибка")
                    continue

    else:
        os.system('CLS')
        print(Fore.RED, "\n***Введен неверный номер***")

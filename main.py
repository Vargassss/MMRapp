import os
import json
import ctypes
import time
from art import tprint
from colorama import init
from colorama import Fore, Back, Style
from datetime import datetime, timezone

init()

allOp = {
    "recruita": "Р-Штурмовик", "recruitg": "Р-Поддержка", "recruitm": "Р-Медик", "recruits": "Р-Снайпер",
    "fsb2004a": "Волк", "fsb2004g": "Алмаз", "fsb2004m": "Дед", "fsb2004s": "Стрелок",
    "fsb2016a": "Перун", "fsb2016g": "Сварог", "fsb2016m": "Травник", "fsb2016s": "Сокол",
    "sso2013a": "Ворон", "sso2013g": "Спутник", "sso2013m": "Бард", "sso2013s": "Комар",
    "22spn2016a": "Плут", "22spn2016g": "Кит", "22spn2016m": "Каравай", "22spn2016s": "Тень",
    "grom2014a": "Кошмар", "grom2014g": "Пророк", "grom2014m": "Микола", "grom2014s": "Стилет",
    "ksk2011a": "Рейн", "ksk2011g": "Штерн", "ksk2011m": "Шатц", "ksk2011s": "Курт",
    "seal2014a": "Корсар", "seal2014g": "Бурбон", "seal2014m": "Монк", "seal2014s": "Скаут",
    "tfb2008a": "Стерлинг", "tfb2008g": "Бишоп", "tfb2008m": "Ватсон", "tfb2008s": "Арчер",
    "raid2017a": "Авангард", "raid2017g": "Бастион", "raid2017m": "Велюр", "raid2017s": "Вагабонд",
    "nesher2015a": "Афела", "nesher2015g": "Хагана", "nesher2015m": "Шаршерет", "nesher2015s": "Эйма",
    "ezapaca": "Фаро", "ezapacg": "Матадор", "ezapacm": "Мигель", "ezapacs": "Диабло",
    "arystana": "Мустанг", "arystang": "Тибет", "arystanm": "Багги", "arystans": "Султан",
    "belssoa": "Лазутчик", "belssog": "Зубр", "belssom": "Каваль", "belssos": "Бусел",
    "amfa": "Старкад", "amfg": "Один", "amfm": "Фрейр", "amfs": "Видар",
    "jiaolonga": "Шаовэй", "jiaolongg": "Инчжоу", "jiaolongm": "Яован", "jiaolongs": "Цанлун",
    "csta": "Слай", "cstg": "Фортресс", "cstm": "Боунс", "csts": "Аваланш", "bopea": "Мартелу", "bopeg": "Баррейра",
    "bopem": "Асаи", "bopes": "Касадор",
}
operID = {
    0: "Р-Штурмовик", 1: "Р-Снайпер", 2: "Р-Поддержка", 3: "Р-Медик", 4: "4", 5: "5", 6: "6", 7: "7", 8: "Волк",
    9: "Стрелок", 10: "Алмаз",
    11: "Дед", 12: "Кошмар", 13: "Стилет", 14: "Пророк", 15: "Микола", 16: "Перун", 17: "Сокол", 18: "Сварог",
    19: "Травник", 20: "Рейн", 21: "Курт", 22: "Штерн", 23: "Шатц", 24: "Ворон", 25: "Комар", 26: "Спутник", 27: "Бард",
    28: "Корсар", 29: "Скаут", 30: "Бурбон", 31: "Монк", 32: "Плут", 33: "Тень", 34: "Кит", 35: "Каравай", 36: "Ватсон",
    37: "Арчер", 38: "Стерлинг", 39: "Бишоп", 40: "Бастион", 41: "Велюр", 42: "Авангард", 43: "Вагабонд", 44: "Афелла",
    45: "Эйма", 46: "Хагана", 47: "Шаршарет", 48: "Диабло", 49: "Мигель", 50: "Матадор", 51: "Фаро", 52: "Мустанг",
    53: "Султан", 54: "Багги", 55: "Тибет", 56: "Лазутчик", 57: "Бусел", 58: "Зубр", 59: "Каваль", 60: "Стардкад",
    61: "Один", 62: "Фрейр", 63: "Видар", 64: "Шаовей", 65: "Инчжоу", 66: "Цанлун", 67: "Яован", 68: "Слай",
    69: "Аваланш", 70: "Фортресс", 71: "Боунс", 72: "Мартелу", 73: "Баррейра", 74: "Асаи", 75: "Касадор", 76: "76",
    77: "77", 78: "78", 79: "79", 80: "80", 81: "81", 82: "82", 83: "83"
}

abilityID = {
    0: "Ловкость рук", 1: "Трен. дыхания", 2: "Угл. тренировка", 3: "Вооруж. забег", 4: "Б. закалка",
    5: "Крепкие нервы", 6: "Сыв.гемоглабина", 7: "Вт. дыхание", 8: "Стрелк. позиция", 9: "Хороший отдых",
    10: "Герм. материалы", 11: "Суб. мельдоний", 12: "Противооскол. слой", 13: "Суб. морфин", 14: "Реген. материалы",
    15: "Адапт. броня", 16: "Пл. прилегание", 17: "Комб. броня", 18: "Защ. головы", 19: "Обр. цевья",
    20: "Пр.нарез. ствола", 21: "Быстр. магазины", 22: "Мод. зат. мех.", 23: "Чувств. спуск. к.", 24: "Бб. патроны",
    25: "Тяж. боеприпасы", 26: "Тепловизор", 27: "Настильность", 28: "Вольфрам. покрытие", 29: "Зап. шприц",
    30: "Ул. формула", 31: "Холодный расчет", 32: "Выс. подготовка", 33: "Скрытый воин", 34: "Засада",
    35: "Кровавая ярость", 36: "Контратака", 37: "Охота за г.", 38: "Возмездие", 39: "Облегченная защита",
    40: "Самолечение", 41: "Одинокий волк", 42: "Доп. подсумки", 43: "Расчетливость", 44: "Скорая помощь",
    45: "Тяга к жизни", 46: "Беспощадность", 47: "Крепкий орешек", 48: "Фактор лечения", 49: "Усил. стим.",
    50: "Готовность", 51: "Калибровка техники", 52: "Готовность", 53: "Тяж. ствол", 54: "Хладнокровие",
    55: "Обл. разгрузка", 56: "Стим. медикаменты", 57: "Прилив адреналина", 58: "Скрыт перемещение",
    59: "Экспанс. пули", 60: "Под прицелом", 61: "Внутр. резерв", 62: "Свои приоритеты", 63: "Плечом к плечу",
    64: "Приоритетная цель", 65: "Ус. защита", 66: "Общий мед пакет", 67: "Свежие силы", 68: "68", 69: "69", 70: "70",
    71: "71"
}

groups = {  # Создаем номер группы и с уникальным цветом(максимум возможно 4 группы)
    0: Back.GREEN, 1: Back.CYAN, 2: Back.WHITE, 3: Back.YELLOW
}
allRegimes = {  # Список режимов и количество игроков в нем
    "polygon": 1, "pvehard": 4, "pve": 4, "onslaughtnormal": 4, "onslaughthard": 4, "pvpdestruction": 8,
    "pvpve": 8, "pvp": 8, "hacking": 8
}
consumablesID = {
    0: "Стимулятор", 1: "Мед. пакет", 2: "Пластина", 3: "Патроны", 4: "Ящик", 5: "Ящик", 6: "-"
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
    number = input(
        Fore.GREEN + "Введите" + Fore.BLUE + " НОМЕР " + Fore.GREEN + "реплея или" + Fore.BLUE + " b (battle) " + Fore.GREEN + "чтобы посмотреть игроков в текущем поиске\n" + Fore.BLUE)
    os.system('CLS')
    if number.lower() == "b" or number == "battle":
        bufTime = 0.0
        workBattle = True
        while workBattle:
            with open("C:\\Users\\" + name + "\\AppData\\LocalLow\\1CGS\\Caliber\\Player.log", "r") as f:
                textBattle = f.readlines()
                for i in range(len(textBattle)):
                    textLine = str(textBattle[len(textBattle) - i - 1])
                    if textLine[100:160].find("battlepreparation/me") != -1:
                        battleLine = textBattle[len(textBattle) - i]
                        if len(battleLine) < 100:  # проверка, пустая ли строка с реплеем
                            continue
                        timeLine = textLine[1:textLine.find("]")]
                        timeLine = datetime.fromisoformat(timeLine)
                        currentTime = datetime.now(timezone.utc)
                        if bufTime == timeLine.timestamp():  # проверка, выведена ли эта информация
                            if (currentTime.timestamp() - timeLine.timestamp()) > 21:
                                print(
                                    Fore.RED + "Выведена информация о последнем поиске боя."
                                               " Подготовка к раунду закончилась больше 20 сек. назад.")
                                input("Нажмите" + Fore.GREEN + " ENTER " + Fore.RED + "чтобы продолжить")
                                workBattle = False
                                break
                            print("\r", end="")
                            print(Fore.MAGENTA + "Последняя информация получена " + Fore.RED +
                                  str(int(
                                      currentTime.timestamp() - timeLine.timestamp())) + Fore.MAGENTA + " сек. назад.",
                                  end="")
                            time.sleep(0.5)
                            break
                        bufTime = timeLine.timestamp()
                        print()
                        os.system('CLS')

                        battleJson = json.loads(battleLine)

                        print(Fore.MAGENTA, battleJson["b"]["Mission"]["SelectedMission"]["MissionId"], "\n")
                        print(Fore.MAGENTA,
                              battleJson["b"]["Stages"][battleJson["b"]["CurrentStage"]["Index"]]["stage_type"])
                        for plCount in range(len(battleJson["b"]["Teams"])):
                            if plCount == 0:
                                print(Fore.BLUE + "\nКоманда #1")
                            elif plCount == 1:
                                print(Fore.BLUE + "\nКоманда #2")

                            battlePlayersGr = [battleJson["b"]["Teams"][plCount]["Users"][p] for p in range(
                                len(battleJson["b"]["Teams"][plCount]["Users"]))]  # берем список игроков
                            battlePlayersGr.sort(key=lambda x: x["Role"])  # Сортируем
                            for plTeams in range(len(battlePlayersGr)):  # Вывод
                                abil = "| "
                                consumables = "| "
                                if battlePlayersGr[plTeams]["PickedCard"] is not None:
                                    for t in range(2):  # расходники
                                        consumables += "{0:^12}".format(consumablesID.get(
                                            battlePlayersGr[plTeams]["PickedCard"]["Card"]["14"][t])) + "|"
                                    for l in range(4):  # навыки
                                        abil += "{0:^18}".format(abilityID.get(
                                            battlePlayersGr[plTeams]["PickedCard"]["Card"][
                                                "15"][l]) if battlePlayersGr[plTeams]["PickedCard"]["Card"]["15"][
                                                                 l] is not None else "-") + "|"
                                print(
                                    f"""{Fore.MAGENTA}{"+" if battlePlayersGr[plTeams]["IsReady"] else "-"} {Fore.RED}{"{0:<22}".format(battlePlayersGr[plTeams]["Nickname"])}{Fore.MAGENTA}Роль: {Fore.RED}{"{0:<8}".format(battlePlayersGr[plTeams]["Role"])}{Fore.MAGENTA}Опер: {Fore.RED}{"{0:<10}".format(operID.get(battlePlayersGr[plTeams]["PickedCard"]["Card"]["1"]) if battlePlayersGr[plTeams]["PickedCard"] is not None else "Не выбран")}{Fore.MAGENTA} Ур оп:{Fore.RED}{"{0:^4}".format(battlePlayersGr[plTeams]["PickedCard"]["Card"]["18"] if battlePlayersGr[plTeams]["PickedCard"] is not None else "None")}{Fore.MAGENTA}Расходники:{Fore.RED}{consumables}""")
                                print(f"""{Fore.GREEN}{abil}""")
                        break
                    elif i == len(textBattle) - 1:
                        print(Fore.RED, "Игра не найдена. Введите b во время старта боя")
                        workBattle = False
                        break


    elif number.isdigit() and int(number) < len(content):  # проверка введенного на число, количество
        number = int(number)
        if not content[number].endswith(".bytes"):
            print(Fore.RED + "Нельзя открыть этот файл")
            continue
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
            for i in range(len(gr)):  # словарь с ид группы и ид цвета
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
                    f"""{color}{Back.RESET + Style.BRIGHT + Fore.RED}{("{0:<22}").format(players[i]["2"])}{Fore.MAGENTA}ID игрока: {Fore.RED}{("{0:<10}").format(players[i]["0"])}{Fore.MAGENTA}Опер: {Fore.RED}{("{0:<14}").format(allOp[players[i]["8"]["1"]] if allOp.get(players[i]["8"]["1"]) is not None else players[i]["8"]["1"])}{Fore.MAGENTA}Уровень: {Fore.RED}{("{0:<4}").format(players[i]["3"])}{Fore.MAGENTA}""")

            # Вывод доп инфы
            while True:
                word = input(
                    f"""{Fore.BLUE}\ni (info){Fore.GREEN} - Дополнительная информация об игроках\n{Fore.BLUE}r (replays){Fore.GREEN} - к списку реплеев\n{Fore.BLUE}e (exit){Fore.GREEN} - выход\n{Fore.BLUE}""").lower()
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

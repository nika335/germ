import csv
from tabulate import tabulate

def main():
    while True:
        print("1 - სიტყვები 1დან 100მდე")
        print("2 - rewers სიტყვები 1დან 100მდე")
        print("3 - 100იანი სიტყვები ")
        print("4 - rewers 100იანი სიტყვები ")
        print("5 - ნებისმიერი")
        print("6 - revers ნებისმიერი")
        x = input("Enter a number: ")
        if x == "1":
            words_1__100()
            break
        elif x == "2":
            rewers_words_1__100()
            break
        elif x == "3":
            words_in_100()
            break
        elif x == "4":
            rewers_words_in_100()
            break
        elif x == "5":
            any_woerds()
            break
        elif x == "6":
            rwvwers_any_woerds()
            break
        else:
            print("invalid input entered")

def words_1__100():
    words = []
    with open("words_1__100.txt", encoding="utf-8") as file:
        reader = csv.reader(file)
        for raw in reader:
            words.append(raw)
    t = []
    for j in words:
        print(j[2])
        mode = input()
        if mode == "k":
            print(f"{j[0]} - {j[1]}")
            print("|")
        g_mode = input()
        if g_mode == "l":
            print("|")
            t.append([j[2], j[0], j[1]])
        else:
            continue
    print(tabulate(t, tablefmt="simple"))

def rewers_words_1__100():
    words = []
    with open("words_1__100.txt", encoding="utf-8") as file:
        reader = csv.reader(file)
        for raw in reader:
            words.append(raw)
    t = []
    for j in words:
        print(j[0])
        mode = input()
        if mode == "k":
            print(f"{j[1]} - {j[2]}")
            print("|")
        g_mode = input()
        if g_mode == "l":
            print("|")
            t.append([j[0], j[1], j[2]])
        else:
            continue
    print(tabulate(t, tablefmt="simple"))

def words_in_100():
    num = input("choose a number: ")
    words = []
    with open(f"{num}_words_in_100s.txt", encoding="utf-8") as file:
        reader = csv.reader(file)
        for raw in reader:
            words.append(raw)
    t = []
    for j in words:
        print(j[2])
        mode = input()
        if mode == "k":
            print(f"{j[0]} - {j[1]}")
            print("|")
        g_mode = input()
        if g_mode == "l":
            print("|")
            t.append([j[2], j[0], j[1]])
        else:
            continue
    print(tabulate(t, tablefmt="simple"))

def rewers_words_in_100():
    num = input("choose a number: ")
    words = []
    with open(f"{num}_words_in_100s.txt", encoding="utf-8") as file:
        reader = csv.reader(file)
        for raw in reader:
            words.append(raw)
    t = []
    for j in words:
        print(j[0])
        mode = input()
        if mode == "k":
            print(f"{j[1]} - {j[2]}")
            print("|")
        g_mode = input()
        if g_mode == "l":
            print("|")
            t.append([j[0], j[1], j[2]])
        else:
            continue
    print(tabulate(t, tablefmt="simple"))

def any_woerds():
    words = []
    with open("any_words.txt", encoding="utf-8") as file:
        reader = csv.reader(file)
        for raw in reader:
            words.append(raw)
    t = []
    for j in words:
        print(j[2])
        mode = input()
        if mode == "k":
            print(f"{j[0]} - {j[1]}")
            print("|")
        g_mode = input()
        if g_mode == "l":
            print("|")
            t.append([j[2], j[0], j[1]])
        else:
            continue
    print(tabulate(t, tablefmt="simple"))

def rwvwers_any_woerds():
    words = []
    with open("any_words.txt", encoding="utf-8") as file:
        reader = csv.reader(file)
        for raw in reader:
            words.append(raw)
    t = []
    for j in words:
        print(j[0])
        mode = input()
        if mode == "k":
            print(f"{j[1]} - {j[2]}")
            print("|")
        g_mode = input()
        if g_mode == "l":
            print("|")
            t.append([j[0], j[1], j[2]])
        else:
            continue
    print(tabulate(t, tablefmt="simple"))

if __name__ == "__main__":
    main()
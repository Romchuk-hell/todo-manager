FILE_NAME = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                flag, title = line.split("|", 1)
                tasks.append([int(flag), title])
    except FileNotFoundError:
        # якщо файл ще не створений — повертаємо пустий список
        pass
    return tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for stan, title in tasks:
            f.write(f"{int(stan)}|{title}\n")

def show_menu():
    print("\n========================= To-Do Manager =========================")
    print("  [1] Додати задачу")
    print("  [2] Показати задачі")
    print("  [3] Позначити/зняти")
    print("  [4] Видалити задачу")
    print("  [5] Редагувати задачу")
    print("  [0] Вийти з програми")

def add_task(tasks):
    nazva=input("Введіть назву задачі: ").strip()
    if nazva=="":
        print("Назва не може бути порожня")
    else:
        tasks.append([0,nazva])

def list_tasks(tasks):
    if not tasks:
        print("(порожньо)")
    else:
        i=1
        for task in tasks:
            stan= task[0] #статус(0 чи 1)
            nazva= task[1] #назва
            if stan==1:
                mark = "✅"
            else:
                mark = "❌"
            print(f"{i}. {mark} {nazva}")
            i+=1

def toggle_task(tasks):
    if  not tasks:
        print("Список порожній")
        return
    list_tasks(tasks)
    try:
        n=int(input("Введіть номер задачі: "))
    except ValueError:
            print("Треба ввести число!")
            return
    if n<1 or n>len(tasks):
         print("Неправильний номер")
         return
    if  tasks[n-1][0]==0:
        tasks[n-1][0]=1
    else:
        tasks[n-1][0]=0

def edit_task(tasks):
    if not tasks:
        print("Список порожній")
        return
    list_tasks(tasks)
    try:
        n = int(input("Введіть номер задачі для редагування: "))
    except ValueError:
          print("Треба ввести число!")
          return
    if n < 1 or n > len(tasks):
        print("Неправильний номер")
        return
    new_text=input("Введіть новий текст задачі: ").strip()
    if new_text=="":
        print("Назва не може бути порожня")
        return
    else:
        tasks[n-1][1]=new_text
    print("Зміни були внесені")

def delete_task(tasks):
    if not tasks:
        print("Список порожній")
        return
    list_tasks(tasks)
    try:
        n=int(input("Введіть номер задачі для видалення: "))
    except ValueError:
        print("Треба ввести число!")
        return
    if n<1 or n>len(tasks):
        print("Неправильний номер")
        return
    del tasks[n-1]
    print("Задачу видалено")

tasks = load_tasks()
while True:
    show_menu()
    choice=input("Виберіть дію зі списку: ")
    if choice == "1":
        add_task(tasks)
        save_tasks(tasks)
    elif choice == "2":
        list_tasks(tasks)
    elif choice == "3":
        toggle_task(tasks)
        save_tasks(tasks)
    elif choice == "4":
        delete_task(tasks)
        save_tasks(tasks)
    elif choice == "5":
        edit_task(tasks)
        save_tasks(tasks)
    elif choice == "0":
        print("Програму завершено. Дякую за користування!")
        exit()
    else:
        print("Виберіть вірну цифру зі списку: ")











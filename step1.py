a_list = []
print("Трекер задач")

while True:
    task = input("Введите задачу(или 'выход')")
    if task.lower() == 'выход':
        break
    if task:
        a_list.append(task)
        print(f"Задача '{task}' добавлена!")

print("/n Список ваших задач: ")
for item in a_list:
    print(f"{item}")

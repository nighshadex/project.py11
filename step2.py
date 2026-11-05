a_list = []
print("Трекер задач 2 ")

while True:
    task = input("Введите задачу(или 'выход')").strip()
    
    if task.lower() == 'выход':
        break
    
    if task:
        new_task = {'text': task, 'two': False}
        a_list.append(new_task)
        print("задача сделана")
    
print("/n Текущие задачи: ")
for item in a_list:
    status = "Сделано" if item['two'] else "Не сделано"
    print(f"{item[text] [{status}]}")
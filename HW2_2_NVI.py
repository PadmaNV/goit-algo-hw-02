from collections import deque

def is_palindrome(string):
    # Перетворення рядка в нижній регістр і видалення пробілів
    string = string.lower().replace(" ", "")
    # Створення двосторонньої черги
    queue = deque()
    
    # Додавання символів рядка до черги
    for char in string:
        queue.append(char)
    
    # Порівняння символів з обох кінців черги
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

while True:
    phrase = input("Введіть фразу для перевірки або 'exit', щоб вийти: ")
    if phrase.lower() == "exit":
        break
    if is_palindrome(phrase):
        print("Паліндромом!!! 🙂")
    else:
        print("Ця фраза не є паліндромом. 😒")


import queue
import time
import threading
import random

# Створення черги заявок
request_queue = queue.Queue()

# Функція для генерації нової заявки та її додавання до черги
def generate_request():
    while True:
        # Генеруємо унікальний ідентифікатор для заявки (тут просто використовуємо випадкове число)
        request_id = int(time.time() * 10)
        request_queue.put(request_id)
        print(f"Заявка {request_id} була додана до черги")
        time.sleep(random.uniform(0.5, 2))  # Затримка між створенням заявок

# Функція для обробки заявки з черги
def process_request():
    while True:
        if not request_queue.empty():
            # Видаляємо заявку з черги
            request_id = request_queue.get()
            print(f"Заявка {request_id} була оброблена")
            # Тут можна додати додаткові дії з обробки заявки
        else:
            print("Черга пуста")
        time.sleep(random.uniform(1, 3))  # Затримка між обробкою заявок

# Запускаємо функції в окремих потоках
generator_thread = threading.Thread(target=generate_request)
processor_thread = threading.Thread(target=process_request)

generator_thread.start()
processor_thread.start()

# Чекаємо, доки обидва потоки не завершаться (тут можна задати умову виходу з програми)
generator_thread.join()
processor_thread.join()

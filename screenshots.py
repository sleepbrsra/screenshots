import subprocess
import time
import os

def take_screenshot(filename):
    try:
        # Делаем скриншот с помощью scrot
        subprocess.run(['scrot', filename], check=True)
        print(f"Скриншот сохранен как {filename}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при создании скриншота: {e}")

def main():
    # Запрашиваем время в секундах у пользователя
    while True:
        try:
            second_time = float(input("Время в секундах: "))
            if second_time <= 0:
                raise ValueError("Время должно быть положительным числом.")
            break
        except ValueError as ve:
            print(f"Ошибка ввода: {ve}. Попробуйте еще раз.")

    # Директория для хранения скриншотов
    screenshot_dir = 'screenshots'
    
    # Создаем директорию, если она не существует
    os.makedirs(screenshot_dir, exist_ok=True)
    
    # Генерируем уникальное имя для файла
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    filename = os.path.join(screenshot_dir, f'screenshot_{timestamp}.png')
    
    # Делаем паузу перед созданием скриншота
    print(f"Переходите к нужному окну или области. Скриншот будет сделан через {second_time} секунд...")
    time.sleep(second_time)  # Используем числовое значение для задержки
    
    take_screenshot(filename)

if __name__ == "__main__":
    main()

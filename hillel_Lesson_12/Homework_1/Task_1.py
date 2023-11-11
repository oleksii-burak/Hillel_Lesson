# Відкриваємо файл для запису
with open("user_data.txt", "w") as file:
    while True:
        line = input("Введіть рядок (або залиште порожнім для завершення): ")
        if not line:  # Перевіряємо, чи рядок порожній
            break
        file.write(line + "\n")  # Записуємо рядок у файл

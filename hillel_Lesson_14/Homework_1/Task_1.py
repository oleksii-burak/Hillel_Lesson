import argparse


def count_words(file_path):
    """
    Відкриваємо файл за заданим шляхом та читаємо його вміст
    :param file_path:
    :return:
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Розділяємо вміст файлу на слова та рахуємо їх кількість
        words = content.split()
        return len(words)


def main():
    """
    Створення парсера аргументів командного рядка;
    Додавання аргументу --file, який є обов'язковим і визначає шлях до файлу
    для читання;
    Розбір аргументів командного рядка;
    Виконання функції підрахунку слів для заданого файлу;
    Виведення результату;
    :return:
    """
    parser = argparse.ArgumentParser(description="Підрахунок слів у файлі")
    parser.add_argument("--file", type=str, required=True,
                        help="Шлях до файлу для читання")
    args = parser.parse_args()
    word_count = count_words(args.file)
    print(f"Кількість слів у файлі: {word_count}")


# Перевірка, чи скрипт запущено напряму, і не є імпортованим
if __name__ == "__main__":
    main()

"""
Для запуску програми використовуйте команду в терміналі, 
замінивши file_to_read.txt на шлях до бажаного файлу:
python Task_1.py --file file_to_read.txt
"""

text0 = """Любіть Україну, як сонце, любіть,

як вітер, і трави, і води…

В годину щасливу і в радості мить,

любіть у годину негоди.

Любіть Україну у сні й наяву,

вишневу свою Україну,

красу її, вічно живу і нову,

і мову її солов’їну.

Між братніх народів, мов садом рясним,

сіяє вона над віками…

Любіть Україну всім серцем своїм

і всіми своїми ділами.

Для нас вона в світі єдина, одна

в просторів солодкому чарі…

Вона у зірках, і у вербах вона,

і в кожному серця ударі,

у квітці, в пташині, в електровогнях,

у пісні у кожній, у думі,

в дитячий усмішці, в дівочих очах

і в стягів багряному шумі…"""

# Видаляємо розділові знаки з тексту.
textwor = (
    text0.replace(",", "").replace("…", "")
    .replace(".", "").replace("\n", " ").split()
)

# Створюємо словник.
word_count = {}

# Створюємо списки.
most_common_words = []
least_common_words = []

# Присвоюємо значення клькості слів яка вміщається в рядок.
words_per_line = 12

# Створення словника зі словами як ключами та кількістю
# їх входжень як значеннями.
for text in textwor:
    word_count[text] = word_count.get(text, 0) + 1

# Знаходження всіх слів, які зустрічаються найчастіше та найрідше
max_count = max(word_count.values())
min_count = min(word_count.values())

# Додаємо слова які зустрічаються найбільшу кількість та
# найменьшу кілткісить разів до списків.
for word, count in word_count.items():
    if count == max_count:
        most_common_words.append(word)

for word1, count1 in word_count.items():
    if count1 == min_count:
        least_common_words.append(word1)

# Присвоюємо змінні для подальшого їх застосування в циклах.
words1 = most_common_words
words2 = least_common_words

# Створюємо списки в яких будуть зберігатися рядки.
lines1 = []
lines2 = []

# Робимо так щоб після кожного слова в результаті була кома та розділяємо
# слова на рядки по заданійі кількості слів після чого додаємо їх до списків.
for i in range(0, len(words1), words_per_line):
    line = ', '.join(words1[i:i+words_per_line])
    lines1.append(line)

for i in range(0, len(words2), words_per_line):
    line = ', '.join(words2[i:i+words_per_line])
    lines2.append(line)

# Робимо так щоб кожен заданний рядок був з нового рядка та останнє слово
# містило в кінці кому.
formatted_text1 = ',\n'.join(lines1)
formatted_text2 = ',\n'.join(lines2)

# Виводимо результат.
print(
    f"Слова, які зустрічаються найчастіше: ",
    f"'{formatted_text1}' - {max_count} разів."
)
print(
    f"Слова, які зустрічаються найрідше: ",
    f"'{formatted_text2}' - {min_count} раз."
)

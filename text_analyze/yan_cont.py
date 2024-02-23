import Levenshtein

# Чтение словаря из файла dictionary.txt
with open('dictionary.txt', 'r', encoding='utf-8') as f:
    dictionary = [word.strip() for word in f.readlines()]

# Чтение списка слов запросов из файла queries.txt
with open('queries.txt', 'r', encoding='utf-8') as f:
    queries = [word.strip() for word in f.readlines()]


# Функция для поиска наименьшего расстояния Levenshtein и исправления
def find_correction(word, dictionary):
    min_distance = float('inf')
    corrected_word = None

    for dict_word in dictionary:
        distance = Levenshtein.distance(word, dict_word)

        if distance < min_distance:
            min_distance = distance
            corrected_word = dict_word

    return corrected_word, min_distance


# Генерация выходной строки для каждого слова запроса
output_lines = []
for word in queries:
    # Проверка, если слово присутствует в словаре
    if word in dictionary:
        output_lines.append(f"{word} 0")
    else:
        # Поиск наименьшего расстояния Levenshtein и исправления
        corrected_word, distance = find_correction(word, dictionary)

        if distance == 1:
            output_lines.append(f"{word} 1 {corrected_word}")
        elif distance == 2:
            second_correction, distance2 = find_correction(corrected_word, dictionary)

            if distance2 == 1:
                output_lines.append(f"{word} 2 {corrected_word} {second_correction}")
            else:
                output_lines.append(f"{word} 3+")
        else:
            output_lines.append(f"{word} 3+")

# Запись результатов в файл answer.txt
with open('answer.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

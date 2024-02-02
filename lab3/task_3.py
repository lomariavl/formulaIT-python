def count_letters(text: str) -> dict:
    dict_letters = {}
    for letter in text.lower():
        if not letter.isalpha():
            continue
        dict_letters[letter] = dict_letters.setdefault(letter, 0) + 1
    return dict_letters


def calculate_frequency(dict_letters: dict):
    new_dict_letters = {}
    count_letters = sum(dict_letters.values())
    for letter, count in dict_letters.items():
        frequency = count / count_letters
        new_dict_letters[letter] = frequency
    return new_dict_letters


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

main_dict = count_letters(main_str)
main_dict = calculate_frequency(main_dict)
for k, v in main_dict.items():
    print(f'{k}: {v:.2f}')

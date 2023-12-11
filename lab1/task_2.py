volume = 1.44 * 1024 * 1024  # Информационный объем диска в Мб, переводим в байты для удобства рассчета
pages_book = 100
lines_page = 50
simbols_line = 25
code_symbol = 4

count_books = int(volume // (pages_book * lines_page * simbols_line * code_symbol))
print("Количество книг, помещающихся на дискету:", count_books)

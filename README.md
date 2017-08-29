# Поиск дубликатов

Скрипт позволяет найти всех дублирующие файлы в указанной папке и всех подпапках внутри и выдает список найденных файлов.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash
# Программа принимает 1 параметр
# python3 duplicates.py -f [путь к папке]
# -f [указываете путь к папке]

$ python3 duplicates.py -f ./test_folders
# пример ответа скрипта

Дубликаты найдены:
Эти файлы одинаковые. Названия файлов могут быть разными, но содержание одинаковое:

--- одинаковые файлы ---
./test_folders/wallpaper/nextfolder/Image_from_Skype.jpg
./test_folders/Teambuilding_21_07_2017/Image_from_Skype.jpg


--- одинаковые файлы ---
./test_folders/whats.jpg
./test_folders/Teambuilding_21_07_2017/4.jpg


--- одинаковые файлы ---
./test_folders/wallpaper/5.jpg
./test_folders/wallpaper/nextfolder/new5.jpg
./test_folders/Teambuilding_21_07_2017/5.jpg

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)

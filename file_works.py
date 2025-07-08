"""
Переведите содержимое файла purchase_log.txt* в словарь purchases вида:
{‘1840e0b9d4’: ‘Продукты’, …}

Для каждого user_id в файле visit_log.csv определите третий столбец с категорией покупки, 
если покупка была.
Cам файл visit_log.csv* изменять не надо. 
В файл funnel.csv запишите визиты из файла visit_log.csv*, 
в которых были покупки с указанием категории.

Учтите условия на данные:
содержимое purchase_log.txt* помещается в оперативную память компьютера;
содержимое visit_log.csv* — нет; используйте только построчную обработку этого файла.

*Все файлы, необходимые для выполнения домашнего задания, находятся в разделе 
“Дополнительные материалы к домашнему заданию” (нужно скачать архив).

Примечание
Домашнее задание сдаётся ссылкой Google Colab или на репозиторий GitHub, 
но только если вы знакомы с Git и устанавливали ПО.
"""

import json
from pathlib import Path

print('Hello files!')
path_1 = Path("Files/purchase_log.txt")

with open(path_1, encoding='utf-8') as f_purchase:
    data_dict = {}

    for line in f_purchase:
        line_dict = json.loads(line)
        if line_dict.get("user_id") != "user_id" and line_dict.get("category") != "category":
            data_dict.setdefault(line_dict.get("user_id"), line_dict.get("category"))

path_2 = Path("Files/visit_log.csv")
path_3 = Path("Files/funnel.csv")

with open(path_2, encoding='utf-8') as f_visit:
    with open(path_3, 'w', encoding='utf-8') as f_funnel:
        for line in f_visit:
            line_list = line.strip().split(',')
            if line_list[0] in data_dict.keys():
                new_line_list = line_list.copy()
                new_line_list.append(data_dict.get(line_list[0]))
                line_for_write = ','.join(new_line_list) + "\n"
                print(line_for_write)
                f_funnel.write(line_for_write)

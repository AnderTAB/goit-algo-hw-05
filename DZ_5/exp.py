# path = 'C:\Users\tutov\OneDrive\Documents\GitHub\goit-algo-hw-05\DZ_5\article_1.txt'
# with open(r'C:\Users\tutov\OneDrive\Documents\GitHub\goit-algo-hw-05\DZ_5\article_1.txt', 'r', encoding='cp1251') as f:
#     print(f.read())
    
    
# with open("article_1.txt", 'r', encoding='cp1251') as f:
#     print(f.read())

import os

file_path = r"..\goit-algo-hw-05\DZ_5\article_1.txt"

# if os.path.exists(file_path):
#     with open(file_path, 'r', encoding='cp1251') as f:
#         print(f.read())
# else:
#     print(f"File not found: {file_path}")


# directory_path = r"C:\Users\tutov\OneDrive\Documents\GitHub\goit-algo-hw-05\DZ_5"
# directory_path = r"..\goit-algo-hw-05\DZ_5"
# # Получить список файлов в указанной директории
# file_list = os.listdir(directory_path)

# # Вывести список файлов
# print(f"Список файлов в {directory_path}:")
# for file_name in file_list:
#     print(file_name)
with open(file_path, 'r', encoding='cp1251') as f:
    print(f.read())
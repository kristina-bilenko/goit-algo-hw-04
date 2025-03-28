from pathlib import Path

def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            final_list = []
            try:
                for line in file:
                    id, name, age = line.strip().split(",")
                    info_dict = {"id": id, "name": name, "age": age}
                    final_list.append(info_dict)
            except Exception as exception_read:
                print(f"Сталася помилка {exception_read} при зчитуванні файлу.")
            return final_list
    except FileNotFoundError:
        print("Файл не знайдено")
    except Exception as exception_open:
        print(f"Сталася помилка {exception_open} при відкритті файлу.")

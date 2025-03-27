from pathlib import Path

def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                total_sum = 0
                workers_number = 0
                while True:
                    line = file.readline()
                    if line:
                        name, salary_str = line.strip().split(",")
                        salary = int(salary_str)
                        total_sum += salary
                        workers_number += 1
                    else:
                        break
            except Exception as exception_read:
                print(f"Сталася помилка {exception_read} при зчитуванні файлу.")
            average_salary = total_sum/workers_number
            final_values = (total_sum, average_salary)
            return final_values
    except FileNotFoundError:
        print("Файл не знайдено")
    except Exception as exception_open:
        print(f"Сталася помилка {exception_open} при відкритті файлу.")
from collections import namedtuple, defaultdict, Counter
import sys
from pathlib import Path
from typing import Callable

def parse_log_line(line: str):
    data = []
    data=[i.split(' ') for i in line.readlines()]  #читаємо файл по рядку і розділяємо "пробілом"
    for i in data:
        yield {'date':i[0],'time':i[1],'level':i[2], 'message':" ".join(i[3:]).strip()} #створюємо словник для кожного логу

def load_logs(file_path:str) -> list: 
    if Path(file_path).exists() and Path(file_path).is_file():  #перевірка існування шляху та чи це є файл
        try:
            with open(file_path,'r',encoding='UTF-8') as file:  #відкриваємо файл
                log_list=[i for i in parse_log_line(file)]      #викликаємо ф-ію парсингу і створюємо список логів
        except:
            print("wrong data")    # помилка з даними у файлі
    else:
        print("wrong path")   # файл не існує або це не файл 
    return log_list # повертаємо список словників - логів

def filter_logs_by_level(logs: list, level: str) -> list:
    filter_log_list=[i['date']+' '+i['time']+' - '+i['message'] for i in logs if i['level']==level.upper()]
    print(f"Деталі логів для рівня '{level.upper()}':")
    for i in filter_log_list:
        print(i)
    return filter_log_list

def count_logs_by_level(logs: list) -> dict:
    counts = {} 
    for i in logs:
        if i["level"] not in counts:
            counts [i["level"]] = 0
        counts[i["level"]] +=1
    return counts

def display_log_counts(counts: dict):
    print(f"Рівень логування  |  Кількість")
    print(f"__________________|____________")
    print(f"INFO              |  {counts["INFO"]}")
    print(f"DEBUG             |  {counts["DEBUG"]}")
    print(f"ERROR             |  {counts["ERROR"]}")
    print(f"WARNING           |  {counts["WARNING"]}\n")
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до директорії як аргумент.")
    else:
        path = sys.argv[1]
    try:
        if sys.argv[2]:
                display_log_counts(count_logs_by_level(load_logs(path)))
                filter_logs_by_level(load_logs(path),sys.argv[2])
    except:
        display_log_counts(count_logs_by_level(load_logs(path)))
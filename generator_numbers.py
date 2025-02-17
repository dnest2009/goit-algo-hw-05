import re
from typing import Callable

def generator_numbers(text:str): 
    numbers = text.split()                                     
    numbers= re.findall(r'\s\d+.\d+\s', text)    #[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?'  використовуємо регулярний вираз для знаходження чисел у тексті
    for number in numbers:  
        yield number            #вертаємо число зі списку у форматі string
        
def sum_profit(text: str, func: Callable):
    total_income = sum([float(i) for i in func(text)])     #створюємо список з чисел у форматі float. Використовуємо ф-ію sum для підсумовування чисел
    print(f"Загальний дохід: {total_income}")

text ="Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
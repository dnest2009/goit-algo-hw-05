def caching_fibonacci():
    cache = {}                    # Створити порожній словник
    def fibonacci(n):
        if n not in cache:       # перевіряємо чи є число у словникуза ключем n
            if n <= 0:
                result = 0
            elif n == 1:
                result = 1
            else:
                result = fibonacci(n-1) + fibonacci(n-2) 
            cache[n]=result              #   додаємо значення у словник
        else:
            result = cache[n]            #   витягуємо значення зі словника
        return result                    #   повертаємо результат - число Фібоначчі
    return fibonacci
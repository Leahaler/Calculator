symbols = {'ноль' : 0, 'один' : 1, 'два' : 2, 'три' : 3, 'четыре' : 4,
           'пять' : 5, 'шесть' : 6, 'семь' : 7, 'восемь' : 8,
           'девять' : 9, 'десять' : 10, 'одиннадцать' : 11, 'двенадцать' : 12,
           'тринадцать' : 13, 'четырнадцать' : 14,'пятнадцать' : 15,
           'шестнадцать' : 16, 'семнадцать' : 17, 'восемнадцать' : 18,
           'девятнадцать' : 19, 'двадцать' : 20,'тридцать' : 30,
           'сорок' : 40, 'пятьдесят' : 50, 'шестьдесят' : 60,
           'семьдесят' : 70, 'восемьдесят' : 80, 'девяносто' : 90,
           'сто' : 100,'двести': 200, 'триста': 300, 'четыреста': 400,
           'пятьсот': 500, 'шестьсот': 600, 'семьсот': 700, 'восемьсот': 800,
           'девятьсот': 900, 'одна тысяча': 1000, 'две тысячи': 2000,
           'три тысячи': 3000,'четыре тысячи': 4000, 'пять тысяч': 5000,
           'шесть тысяч': 6000, 'семь тысяч': 7000,'восемь тысяч': 8000,
           'девять тысяч': 9000,'плюс' : '+', 'минус' : '-', 'умножить' : '*',
           'открывается': '(', 'закрывается': ')'}

def key_value(symbol):
    '''
    функция принимает число и возвращает его строковую запись

    Args:
           symbol(int) - число
    Returns:
           key(str) - строковая запись числа
    '''
    for key, value in symbols.items():
        if symbol == value:
            return key
def calc(string):
    '''
    функция принимает строку(пример)преобразовывает ее в числовую запись,
    после чего выполняет вычисления и выводит результат
    Args:
           string(list) - пример в строковой записи
    '''
    result_0 = []
    result_1 = ''
    digit = []

    while 'на' in string:
        string.remove('на')
    while 'скобка' in string:
        string.remove('скобка')
        
    for symbol in string:
        try:
            int(symbols[symbol])
            try:
                int(result_0[-1])
                result_0[-1] += symbols[symbol]
            except:
                result_0.append(symbols[symbol])
        except:
            result_0.append(symbols[symbol])
            
    for elem in result_0:
        result_1 += str(elem)
        
    result = eval(result_1)

    for ten in range(1, len(str(result))+1):
        if result%100 > 10 and result%100 < 20 and ten == 1:
            continue
        else:
            if result % (10**ten) != 0:
                digit.insert(0, result % (10**ten))
                result -= result % (10**ten)
    print('Ваш результат: ', end ='')            
    for symbol in digit:
        print(key_value(symbol), end =' ')
string = list(input('Введите пример: ').split())
calc(string)


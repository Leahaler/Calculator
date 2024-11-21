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
           'девять тысяч': 9000,'плюс' : '+', 'минус' : '-', 'умножить' : '*' }

def key_value(symbol):
    for key, value in symbols.items():
        if symbol == value:
            return key
def calc():
    
    example = []
    string = list(input('Введите пример: ').split())
    numbers = ['_']
    op = []
    while 'на' in string:
        string.remove('на')
        
    for symbol in string:
        try:
            int(symbols[symbol])
            try:
                int(numbers[-1])
                numbers[-1] += symbols[symbol]
            except:
                numbers.append(symbols[symbol])
                op.append(None)
        except:
            op.append(symbols[symbol])
            numbers.append(None)
    numbers.remove('_')
    
    print(numbers)
    print(op)
    while '*' in op:
        numbers[op.index('*')-1] = numbers[op.index('*') - 1] * numbers[op.index('*') +1]
        del numbers[op.index('*')+1]
        del numbers[op.index('*')]
        del op[op.index('*') + 1]
        del op[op.index('*')]
    result = numbers[0]
    for indx in range(1, len(numbers)):
        try:
            int(numbers[indx])
            if op[indx - 1] == '+':
                result += numbers[indx]
            else:
                result -= numbers[indx]
        except:
            continue
    digit = []
    for ten in range(1, len(str(result))+1):
        if result%100 > 10 and result%100 < 20 and ten == 1:
            continue
        else:
            if result % (10**ten) != 0:
                digit.insert(0, result % (10**ten))
                result -= result % (10**ten)
    print(digit)
    print(result)

    for symbol in digit:
        print(key_value(symbol), end =' ')
calc()

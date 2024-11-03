calls = 0
def count_calls():
        global calls
        calls += 1

def string_info(string):
    count_calls()
    tuple_info = (len(string), string.upper(), string.lower())
    return tuple_info

def is_contain(string, list_to_search):
    count_calls()
    return string.lower() in [i.lower() for i in list_to_search]



print(string_info('АПОЛЛОН'))
print(string_info('дИоНиС'))
print(is_contain('Анна', ['Анюта', 'АННА', 'АнЕчКа',]))
print(is_contain('Володя', ['ВОВА', 'владимир', 'Вовка', 'ВоЛоДьКа']))
print(calls)







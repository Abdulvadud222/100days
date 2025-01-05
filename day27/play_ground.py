def add(*args): ### because of the symbol *, this can take unlimited inputs. the inputs are stored in a tuple.
    result = 0
    for arg in args:
        result += arg
    print(result)

add(1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)


def calculate(**kwargs):
    print(kwargs) ###this is a dictionary
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["subtract"])

calculate(subtract=12, divide=23)





def func(x):
    def func2(y):
        print(f'{y},  hello there by {x}')
    return func2
result_func = func(10)
result_func(-5)


def speak(text, loud):
    def yell():
        print(text.upper())
    def whisper():
        print(text.lower())
    if loud > 1 :
        return yell()
    else:
        return whisper()
speak('something', 10)
speak('something', -10)

def null_decorator(func):
    def func3():
        return f'Decorator {func()}'
    print('Here was decorator')
    return func
@null_decorator
def func1():
    print('Hello world!')

func1()


def test_function():
    print()
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()
    return

test_function()
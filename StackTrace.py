def function_c():
    result = 1 / 0  # This will raise a ZeroDivisionError
    return result

def function_b():
    value = function_c()
    return value

def function_a():
    data = function_b()
    print(data)

if __name__ == "__main__":
    function_a()
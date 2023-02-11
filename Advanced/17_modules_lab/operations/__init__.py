def calculate(*args):
    num1, operator, num2 = args

    operations = {"/": lambda a, b: a / b,
                  "*": lambda a, b: a * b,
                  "-": lambda a, b: a - b,
                  "+": lambda a, b: a + b,
                  "^": lambda a, b: a ** b,
                  }
    result = operations[operator](float(num1), int(num2))

    return f"{result:.2f}"

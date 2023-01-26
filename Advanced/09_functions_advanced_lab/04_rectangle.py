def rectangle(length, width):
    if isinstance(length, int) and isinstance(width, int):
        def area():
            return length * width

        def perimeter():
            return (length + width) * 2
    else:
        return "Enter valid values!"

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle(2, 10))
print(rectangle('2', 10))

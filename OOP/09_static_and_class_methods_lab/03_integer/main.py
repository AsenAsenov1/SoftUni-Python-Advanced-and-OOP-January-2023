class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0

        for char in value[::-1]:
            current_value = roman_values[char]
            if current_value >= prev_value:
                result += current_value
            else:
                result -= current_value
            prev_value = current_value

        return cls(result)

    @classmethod
    def from_string(cls, value):
        try:
            if not isinstance(value, str):
                raise ValueError
            return cls(int(value))
        except ValueError:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)
print(second_num.from_string("2"))

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))

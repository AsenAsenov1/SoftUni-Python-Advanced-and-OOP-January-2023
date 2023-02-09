def create_triangle(number):
    def upper_stage():
        for row in range(1, number + 1):
            for col in range(1, row + 1):
                print(col, end=" ")
            print()

    def lower_stage():
        for r in range(number - 1, 0, -1):
            for c in range(1, r + 1):
                print(c, end=" ")
            print()

    upper_stage(), lower_stage()

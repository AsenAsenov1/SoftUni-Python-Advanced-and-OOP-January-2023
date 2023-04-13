def cache(func):
    def wrapper(number):
        key = number
        if key not in wrapper.log:
            wrapper.log[key] = func(number)
        return wrapper.log[key]

    wrapper.log = {}
    return wrapper

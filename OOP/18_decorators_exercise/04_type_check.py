def type_check(data_type):  # gets the decorator parameter
    def decorator(function_ref):  # receives first_letter function
        def wrapper(argument):  # receives the argument of first_letter function
            if not isinstance(argument, data_type):
                return "Bad Type"
            else:
                return function_ref(argument)

        return wrapper

    return decorator

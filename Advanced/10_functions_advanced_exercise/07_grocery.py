def grocery_store(**kwargs):
    sorted_products = {k: v for k, v in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))}
    products_list = [f"{key}: {value}" for key, value in sorted_products.items()]

    return "\n".join(products_list)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print()
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

def bigger_price(limit, data):
    """
        TOP most expensive goods -- limit: int, data: list  -> результат должен быть list
    """
    my_list = sorted(data, key=lambda x: x['price'], reverse=True)
    return my_list[0:2]


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    print(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))
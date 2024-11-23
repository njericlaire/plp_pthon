


def calculate_discout():
    price=int(input("What is the original price? "))
    discount_percent=int(input("What is your discount? "))
    if discount_percent>=20:
        return price-(price*discount_percent/100)
    else:
        return price
print(calculate_discout())

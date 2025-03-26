
originalPrice= int(input("Please enter Price: "))
discount_percent= int(input("Please enter Discount: "))


def calculate_discount( originalPrice, discount_percent ):
    if discount_percent >= 20:
        a= (discount_percent/100) * originalPrice
        print(f"Result {a}")
    else:
        print(f"Result {originalPrice}")
    
calculate_discount( originalPrice, discount_percent )
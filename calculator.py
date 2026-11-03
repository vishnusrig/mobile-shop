def calculate_total(phone_price, delivery):
    return phone_price + delivery
    
def calculate_discounted_total(phone_price, delivery):
    discount = phone_price * 0.10
    return phone_price - discount + delivery

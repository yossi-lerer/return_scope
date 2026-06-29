# part 1
# Q 1
# will print 8 and 10

# part 2
# step 1 - Mission Distance Converter
def meter_to_cm(meters) -> int:
    return meters * 100

def msg_distance(msg) -> str:
    return f"Robot moved {msg} centimeters"

def meter_and_msg_distance(meters):
    cm = meter_to_cm(meters)
    msg = msg_distance(cm)
    print(msg)

meter_and_msg_distance(5)
# step 2 - Simple Price Calculator

def price_with_delivery(price):
    return price + 10

def multiple_price_by_two(price):
    return price * 2

def final_price(orginal_price):
    add_price_delivery = price_with_delivery(orginal_price)
    Doubling_the_price = multiple_price_by_two(add_price_delivery)
    print(Doubling_the_price)

final_price(5)
# step 3 - Name Formatter
def connecting_two_strings(str1, str2):
    return str1 + " " + str2

def str_to_uppercase(string):
    return string.upper()

def prepares_user_name(first_name, last_name):
    connecting_first_and_last_name = connecting_two_strings(first_name, last_name)
    user_to_upper = str_to_uppercase(connecting_first_and_last_name)
    print(user_to_upper)

prepares_user_name("yossi", "lerer")
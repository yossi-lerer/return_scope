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
# step 4 - Temperature Report 
def celsius_to_fahrenheit(Celsius):
    return Celsius * 9 / 5 + 32

def msg_with_fahrenheit(fahrenheit):
    return f"The temperture in fahrenheit is {fahrenheit}" 

def Temperature_Report(Celsius):
    convert_c_to_f = celsius_to_fahrenheit(Celsius)
    report_with_c = msg_with_fahrenheit(convert_c_to_f)
    print(report_with_c)
Temperature_Report(32)
# step 5 - Game Health Calculator
def health_damage(health, damage):
    return health - damage
def health_healing(health, healing):
    return health + healing
def final_health():
    new_health = health_damage(100, 30)
    final_health = health_healing(new_health, 25)
    print(f"new health is: {final_health}")
final_health()
# step 6 - Shopping Bag Total
def total_price(product1, product2, product3):
    return product1 + product2 + product3
def discount_20_percent(total):
    return total / 100 * 80
def msg_final_price(discount, price):
    return f"The final price after a {discount} percent discount is {price}."
def shopping_Bag_Total():
    calculate = total_price(50, 80, 150)
    discount = discount_20_percent(calculate)
    msg = msg_final_price(20, discount)
    print(msg)
shopping_Bag_Total()
# step 7 - Password Cleaner
def password_with_out_space(password):
    return password.strip()
def password_length(password):
    return len(password)
def check_len(password):
    if password >= 8:
        return True
    else:
        return False
def password_cleaner_and_check():
    password_from_user = password_with_out_space(" ndjjjjj ")
    len = password_length(password_from_user)
    print(check_len(len))
password_cleaner_and_check()
# step 8 - Student Grade Bonus
def bonus_5_grade(grade):
    return grade + 5
def multiply_grade(grade):
    return grade * 1.1
def returning_a_score_up_to_100(grade):
    if grade >= 100:
        return 100
    else:
        return grade
def final_returned_grade():
    bonus = bonus_5_grade(85)
    multi = multiply_grade(bonus)
    check_grade = returning_a_score_up_to_100(multi)
    print(f"The score after weighting: {check_grade}") 
final_returned_grade()
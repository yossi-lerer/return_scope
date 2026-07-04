# part 1
# Q 1
# will print 8 and 10
# Q 2 
# will print Spy, 40, Agent, 2
# Q 3 
# will print 30, 20
# Q 4
# will print 30, 75, 100
# Q5
# will print ['map', 'key', 'torch', 'coin'], ['map', 'key', 'torch', 'coin']
# Q 6
# will print ['potion', 'shield'], ['map', 'key']
# Q 7
# will print 20, 20
# Q8
# will print running, ready, waiting
# Q9
# will print 16 and 16 and the last print print error because he doesn't have access to the code inside the function
# q10
# will print 25, ['key', 'map', 'coin'], 25, ['key', 'map', 'coin'], 1, ['key', 'map', 'coin']

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
# step 9 Text Analyzer 
def sentence_in_lowercase(sentence):
    return sentence.lower()
def how_many_times_the_letter_a(sentence):
    a_in_sentence = 0
    for i in sentence:
        if i == "a":
            a_in_sentence += 1
    return a_in_sentence
def msg_in_sentence(a_in_sentence):
    return f"The letter a appears {a_in_sentence} times"
def func_manage():
    sentence = sentence_in_lowercase("hu ahcsho abcahdb")
    couning_a = how_many_times_the_letter_a(sentence)
    msg = msg_in_sentence(couning_a)
    print(msg)
func_manage()
# step 10 - Inventory Value
def item_price_and_amount(price, amout):
    return price + amout
def value_after_subtracting_15_shekels(price):
    return price - 15
def greater_than_100(price):
    if price > 100:
        return True
    else:
        return False
def main_inventory():
    calculate = item_price_and_amount(100, 50)
    subtracting = value_after_subtracting_15_shekels(calculate)
    greater = greater_than_100(subtracting)
    print(greater)
main_inventory()
# step 11 - Username Generator
def firstname_the_first_3_characters(first_name):
    return first_name[:3]
def lastname_the_first_3_characters(last_name):
    return last_name[:3]
def one_username_joined_with_(first_name, last_name):
    return f"{first_name}_{last_name}"
def username_in_lowercase(username):
    return username.lower()
def main_Username_Generator():
    first_name = firstname_the_first_3_characters("yossi")
    last_name = lastname_the_first_3_characters("Lerer")
    join = one_username_joined_with_(first_name, last_name)
    lowercase = username_in_lowercase(join)
    print(lowercase)
main_Username_Generator()
# step 12 - Trip Fuel Calculator
def total_fuel_needed(distance, fuel_usage_km):
    return distance / fuel_usage_km
def total_fuel_cost(total_fuel, fuel_price):
    return total_fuel * fuel_price
def cost_per_passengers(cost, passengers ):
    return cost / passengers
def main_trip_fuel_calculator():
    calc_fuel = total_fuel_needed(300, 10)
    cost = total_fuel_cost(calc_fuel, 8)
    cost_per_passenger = cost_per_passengers(cost, 5)
    print(f"cost per passengers: {cost_per_passenger}")
main_trip_fuel_calculator()
# step 13 - List Score Processor
def sum_of_the_scores(list_score):
    total_score = 0
    number_of_score = 0
    for i in list_score:
        total_score += i
        number_of_score += 1
    return total_score, number_of_score
def average_score(total_score, number_of_score):
    return total_score / number_of_score
def pass_if_it_is_at_least_60(average):
    if average >= 60:
        return "pass"
    else:
        "fail"
def main_score_processor():
    total_score = sum_of_the_scores([80, 60, 90, 50])
    average = average_score(total_score[0], total_score[1])
    pass_or_fail = pass_if_it_is_at_least_60(average)
    print(f"game scores: {pass_or_fail}")
main_score_processor()
# step 14 - Order Summary
def returns_a_sentence(product_name, amount):
    return f"{product_name} {amount}"
def sentence_with_the_total(sentence, total):
    return f"{sentence} {total}"
def sentence_order_ready(sentence):
    return f"{sentence} - order ready"
def main_Order_Summary():
    order = returns_a_sentence("pc", 5)
    price = sentence_with_the_total(order, 2500)
    order_ready = sentence_order_ready(price)
    print(order_ready)
main_Order_Summary() 
# step 15 - Basic Bank Action
def balance_after_deposit(balance, deposit ):
    return balance + deposit
def balance_after_withdrawal(balance, withdrawal):
    return balance - withdrawal
def check_balance(balance):
    if balance < 0:
        return "Warning"
    else:
        return "OK"
def main_bank():
    deposit = balance_after_deposit(500, 300)
    withdrawal = balance_after_withdrawal(deposit, 900)
    check = check_balance(withdrawal)
    print(check)
main_bank()
# step 16 - Tax Calculator With Global Tax Rate
tax_rate = 0.17
def subtotal(product_price, amount):
    return product_price * amount
def subtotal_after_tax(subtotal):
    return subtotal + (subtotal * tax_rate)
def receipt_sentence(subtotal):
    return f"the price after tax is {subtotal}"
def main_tax_calculator():
    total_before_tax = subtotal(6, 5)
    subtotal_after = subtotal_after_tax(total_before_tax)
    receipt = receipt_sentence(subtotal_after)
    print(receipt)
main_tax_calculator()
# step 17 - Game Score With Global Bonus
bonus_points = 5
def returns_the_base_score(wins):
    return wins * 10
def adding_the_global_bonus(base_score):
    return base_score + bonus_points
def advanced_or_training(score):
    if score >= 50:
        return "advanced"
    else:
        return "training"
def main_game_score():
    base_score = returns_the_base_score(5)
    bonus = adding_the_global_bonus(base_score)
    check = advanced_or_training(bonus)
    print(check)
main_game_score()
# step 18 - Nested Mission Code
def agent_mission(agent_nam):
    mission_number = 4452
    def agent_name(agent_name):
        return f"{agent_name[:2]}{mission_number}"
    return agent_name(agent_nam)
def msg_agent():
    agent = agent_mission("moshe")
    print(f"Mission code: {agent}")
msg_agent()
# step 19 - Counter With Local Scope
counter = 100
def receives_a_number(number):
    counter = number
    return (counter + 10) * 2
def difference_between_it_and_the_global_counter(number):
    return f"{number} {counter}"
def main_counter():
    rec = receives_a_number(130)
    print(difference_between_it_and_the_global_counter(rec))
main_counter()
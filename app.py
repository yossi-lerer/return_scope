# part 1
# Q 1
# will print 8 and 10

# part 2
# step 1
def meter_to_cm(meters):
    return meters * 100

def msg_distance(msg):
    return f"Robot moved {msg} centimeters"

def meter_and_msg_distance(meters):
    cm = meter_to_cm(meters)
    msg = msg_distance(cm)
    print(msg)

meter_and_msg_distance(5)
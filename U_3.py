import random


def randomgerade(): 
    global m1_value,b1_value,m2_value,b2_value
    m1_value = random.randint(-100,100)
    b1_value = random.randint(-100,100)
    print(f"y = {m1_value}x +{b1_value}")
    m2_value = random.randint(-100,100)
    b2_value = random.randint(-100,100)
    print(f"y = {m2_value}x +{b2_value}")

def schnittpunkte():
    schnittpunkt_x_value = (b2_value-b1_value)//(m1_value-m2_value)
    schnittpunkt_y_value = m1_value*schnittpunkt_x_value + b1_value
    print(f"Der Schnittpunkt ist ({schnittpunkt_x_value} , {schnittpunkt_y_value})")

randomgerade()
schnittpunkte()
# Question 3

def BMI_calc():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))

    height /= 100
    user_bmi = weight / (height ** 2)
    print("Your body mass index (BMI) is " + str(user_bmi))

    if age > 35:
        if user_bmi < 19:
            print(name + ", you are underweight")
        if 19 <= user_bmi <= 26:
            print(name + ", you are normal")
        if user_bmi > 26:
            print(name + ", you are overweight")
    if 17 <= age <= 35:
        if user_bmi < 18:
            print(name + ", you are underweight")
        if 18 <= user_bmi <= 24:
            print(name + ", you are normal")
        if user_bmi > 24:
            print(name + ", you are overweight")
    if age < 17:
        if user_bmi < 15:
            print(name + ", you are underweight")
        if 15 <= user_bmi <= 20:
            print(name + ", you are normal")
        if user_bmi > 20:
            print(name + ", you are overweight")

BMI_calc()




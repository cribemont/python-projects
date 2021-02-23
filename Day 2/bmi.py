#BMI calculator
weight = input("current weight : ")
height = input("current height : ")


result = int(weight) / (float(height) ** 2)

print("Your BMI is " + str(result) )
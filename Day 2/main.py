# Variables and stuff

# String "Meow meow" - like other lang. strings can be subscriptd  "String"[0] => S
# Ints 12345  12-345 => 12,345 for US marking
# Float 2.5
# Bool ? True : False

# type() => show type

# convert int to str =>  my_int_str = str( int )
# also other way =>   my_str_int = int(str)   or   float()

# + - * / **(expo)

#BMI calculator

weight = input("current weight : ")
height = input("current height : ")


result = int(weight) / (float(height) ** 2)

print("Your BMI is " + str(result) )
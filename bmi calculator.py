# def full_name = (first_name, last_name):
#   print(f"Hi there {first_name} {last_name}")
#   print("Let's check your bmi")


height_m = 164 / 100
weight_kg = 89

bmi = weight_kg / (height_m ** 2)

print(weight_kg)
print(height_m)
print(bmi)
if bmi < 18.5:
    print("You are underweight")
elif bmi <= 24.9:
    print("You have neither underweight nor overweight")
elif bmi <= 29.9:
    print("You are overweight")
else:
    print("You are obese")


height_m = 164 / 100
weight_kg = 60

bmi = weight_kg / (height_m ** 2)

print(f"Your weight is{weight_kg}")
print(f"Your height is{height_m}")
print("Now let's calculate your BMI")
print(f"Your BMI is {bmi}")
if bmi < 18.5:
    print("You are underweight")
elif bmi <= 24.9:
    print("You have neither underweight nor overweight")
elif bmi <= 29.9:
    print("You are overweight")
else:
    print("You are obese")

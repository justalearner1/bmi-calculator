full_name('John', 'Doe')

# bmi input data
height_m = (170/100)
weight_kg = 70

# calculate bmi
bmi = weight_kg / (height_m ** 2)

# print calculated bmi value
print(f'bmi: ' "{0:.2f}".format(bmi))

# bmi logic code
if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print(" You are neither underweight nor overweight")
elif bmi >= 25 and bmi <= 29.9:
    print("You are overweight")
else:
    print("You are obese")

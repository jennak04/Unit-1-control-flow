height = int(input("Input your height in inches: "))
weight = int(input("Input your weight in pounds: "))

BMI = (weight/height**2) * 703


print(f"BMI: {BMI:.2f}")

calculated_BMI = ("Underweight" if BMI < 18.5 else
                  "Normal" if 18.5 <= BMI < 25 else
                  "Overweight" if 25 <= BMI < 30 else
                  "Obese")

print(f"Your BMI of {BMI:.2f} is: {calculated_BMI}") 
# i used .2f to format the BMI into 2 decimal points to make it look neater
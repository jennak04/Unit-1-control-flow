print("\n== BMI CALCULATOR ==")

height = int(input("Input your height in inches: "))
weight = int(input("Input your weight in pounds: "))


print("\n=====================")
print("BMI Health Report")
print("=====================\n")


BMI = (weight/height**2) * 703



category = ("Underweight" if BMI < 18.5 else
                  "Normal" if 18.5 <= BMI < 25 else
                  "Overweight" if 25 <= BMI < 30 else
                  "Obese" if BMI >= 30 else
                  "Input a valid number")

recomendation = ("Gain weight" if category == "Underweight" else
                 "Maintain weight" if category == "Normal" else
                 "Lose weight" if category == "Overweight" else
                 "Lose a lot of weight" if category == "Obese" else
                 "Error!")

health_risk = ("Moderate" if category == "Underweight" or "Overweight" else
               "Low" if category == "Normal" else
               "High" if category == "Obese" else
               "Error")

print(f"Height:  {height}\"")
print(f"Weight:  {weight} lbs")
print(f"BMI: {BMI:.2f}")
print(f"Category: {category}")
print(f"Recomendation: {recomendation}")
print(f"Health Risk: {health_risk}")

print("\n=====================")


# i used .2f to format the BMI into 2 decimal points to make it look neater
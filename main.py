# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def calculateBMI(data):
    OverWeight_Count = 0
    for i in data:
        HeightM = i["HeightCm"]/100
        BMI = round(i["WeightKg"]/HeightM**2,2)
        i["BMIKg/m2"] = BMI
        if BMI <= 18.4:
            BMI_Category = "Underweight"
            Health_Risk = "Malnutrition risk"
            i["BMI_Category"] = BMI_Category
            i["Health_Risk"] = Health_Risk
        elif 18.5 <= BMI <= 24.9:
            BMI_Category = "Normal weight"
            Health_Risk = "Low risk"
            i["BMI_Category"] = BMI_Category
            i["Health_Risk"] = Health_Risk
        elif 25 <= BMI <= 29.9:
            OverWeight_Count+=1
            BMI_Category = "Overweight"
            Health_Risk = "Enhanced risk"
            i["BMI_Category"] = BMI_Category
            i["Health_Risk"] = Health_Risk
        elif 30 <= BMI <= 34.9:
            BMI_Category = "Moderately obese"
            Health_Risk = "Medium risk"
            i["BMI_Category"] = BMI_Category
            i["Health_Risk"] = Health_Risk
        elif 35 <= BMI <= 39.9:
            BMI_Category = "Severely obese"
            Health_Risk = "High risk"
            i["BMI_Category"] = BMI_Category
            i["Health_Risk"] = Health_Risk
        elif 40 <= BMI:
            BMI_Category = "Very severely obese"
            Health_Risk = "Very high risk"
            i["BMI_Category"] = BMI_Category
            i["Health_Risk"] = Health_Risk
    return "Number of Overweight People : "+str(OverWeight_Count) ,data



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
    85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
    "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
    "HeightCm": 167, "WeightKg": 82}]
    print(calculateBMI(data))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

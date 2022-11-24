#programmed by Sarah Donohue
#11/12/22
#Donohue-HealthCalculator.py
#this application will calculate BMI and series of heart rate values using the Karvonen formula


def bmi_calc():
    print('Please enter the following values for the user . . . \n')
    try: 
        height_in = float(input('Height in inches: '))
        height_m2 = (height_in * 0.0254)**2
        weight_lb = float(input('Weight in pounds: '))
        weight_kg = weight_lb * 0.454
        age = int(input('Current age: '))
        rest_hr = int(input('Resting heart rate: '))
    except (ValueError):
        print('Invalid input!\n' )
    print('Results . . . \n')
    bmi = weight_kg / height_m2
    intensity = .50
    if bmi <= 18.5:
        print('Your BMI is, ', (round(bmi, 2)), ' -- Underweight' )
    elif bmi >= 18.5 and bmi <= 24.9:
        print('Your BMI is, ', (round(bmi, 2)), ' -- Normal Weight' )
    elif bmi >= 25 and bmi <= 29.9:
        print('Your BMI is ', (round(bmi, 2)), ' -- Overweight')
    else:
        print('Your BMI is ', (round(bmi, 2)), ' -- Obese')
    karvonen_calc(age, rest_hr, intensity)
        
def karvonen_calc(age, rest_hr, intensity):
   print('Exercise Intensity Heart Rates:')
   print('Intensity\t Max Heart Rate\n')
   intensity = .50
   for i in range(10):
       karvonen = (((220 - age) - rest_hr) * intensity) + rest_hr
       print(round(intensity, 3), '\t', int(karvonen))
       intensity += 0.05

bmi_calc()

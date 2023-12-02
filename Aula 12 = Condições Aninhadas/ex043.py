weight = float(input('What is your weight? '))
height = float(input('What is your height? '))
BMI = weight / (height ** 2)
if BMI < 18.5:
    print('Your BMI is {:.1f} and you are underweight.'.format(BMI))
elif BMI <= 25:
    print('Your BMI is {:.1f} and you are at your ideal weight.'.format(BMI))
elif BMI <= 30:
    print('Your BMI is {:.1f} and you are overweight.'.format(BMI))
elif BMI <= 40:
    print('Your BMI is {:.1f} and you are obese.'.format(BMI))
else:
    print('Your BMI is {:.1f} and you are morbidly obese.'.format(BMI))

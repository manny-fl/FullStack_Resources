#Reference : Zybooks 10.2 Multiple exception handlers
#10.2.1: BMI example with multiple exception types.
user_input = ''
while user_input != 'q':
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
    except ValueError:
        print('Could not calculate health info.\n')
    except ZeroDivisionError:
        print('Invalid height entered. Must be different from 0.')

    user_input = input("Enter any key ('q' to quit): ")
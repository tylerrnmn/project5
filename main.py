# Tyler Main
# Project 5 Due 07/24/22

# this is the function definition it has two parameters, an expression doing calculations and a return
def f_calc_gear_ratio(p_drive_gear, p_driven_gear):
    gear_ratio = p_driven_gear/p_drive_gear
    # this is just a simple expression we learned in Chapter 2.
    return gear_ratio

# lets give the user input variables a default value before we enter a loop


user_drive_gear = 0
user_driven_gear = 0

# maybe we'd like a counter
counter = 0

# getting input from the user is always better with a while loop because we don't know how many passes we will make
while user_drive_gear >= 0:
    counter = counter + 1
    user_drive_gear = int(input('Please enter the drive gear tooth count (-1 to exit):\n'))
    if user_drive_gear < 0:
        break
    elif user_drive_gear > 0:
        user_driven_gear = int(input('Please enter the driven gear tooth count:\n'))
    print(f'Drive Gear has {user_drive_gear} teeth Driven gear has {user_driven_gear} teeth for an effective gear ratio'
          f'of {f_calc_gear_ratio:.2f}')

print(f'Thank you for using the gear ratio calculator, you have completed {counter} calculations')

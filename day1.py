# password retry system python challenge

# Hardcoded correct pasword
correct_password = 'python1234'

# Number of allowed attempts
max_attempts = 3
attempts = 0

#loop until the user has used up all attempts
while attempts < max_attempts:
    entered_password = input('Enter your password: ')

    if entered_password == correct_password:
        print('access granted')
        break
    else:
        attempts += 1
        print(f'incorrect password. attempt {attempts} of {max_attempts}. ')

# if user used all attempts without success

if attempts == max_attempts:
    print('too many attempts. you are locked out. ')

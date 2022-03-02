import random
number = random.ranint(1,10 )

player_name = input("hello, whats your name ?")
number_of_guesses = 0
print('okay!'+ player_name + 'i am guessing a numberbetween i1 and 10')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('your guess is too low')
        if guess >  number:
            print('your guess is too high')
            if guess == number:
                break
if guess == number:
    print('you gussed the number in'+ str(number_of_guesses) + 'tries!')
else:
    print('you did not guess the number, the number was' + str(number))             

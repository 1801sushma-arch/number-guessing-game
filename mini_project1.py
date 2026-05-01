#built a number guessing game where the user guesses a random number from 1 to 100 
#with higher/lower hints and attempt counting
import random   
secret_number = random.randint(1,100)  

attempts = 0         
guess = 0 

while guess != secret_number:        
    guess=int(input("enter your guess(1-100):"))
    attempts += 1 
    if attempts >= 7:
        print(f"game is over.\nthe number was {secret_number}")
        break          
    if guess > secret_number:
        print("your guess is high")  
    elif guess < secret_number:
        print("your guess is low")    
    else:                 
        print(f"your guess is correct 😍 its {guess} ")
        print(f"amazing!, you took {attempts} attempts")
        break  


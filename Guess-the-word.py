""" Guess the number made by Jonathan D """
import random

number = random.randint(1, 100) # Get a number from 1 to 100
""" Keep number outside from while loop to stop it from changing its value """

while True: # Loop if answer is wrong
  answer = int(input("Guess the number from 1 to 100 # ")) # If input doesn't work try raw_input
  """ Keep answer inside the loop to change your answer if you're wrong """
  if (answer < number): # If answer is lower than number
    print("Guess higher") # Tell them to guess higher
  elif (answer > number): # If answer is greather than number
    print("Guess lower")
  elif (answer == number): # If answer is equal to number
    print("Nice your guess was correct, ({})".format(number))
    """ .format(number) replaces {} with number """
    break # Break the loop to stop it from going
    
  

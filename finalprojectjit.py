#Created by: Dillen Koranteng
#Created date: 03/13/22
#Version = '1.0'
#-----------------------------------------
'''''This is a text based adventure through the life of a discord mod'''
"""Password within the start part is "Start" spelled with an uppercase S"""
#-----------------------------------------
import random
from datetime import datetime
#-----------------------------------------
import fpmodule



current_time = datetime.today()
formatted_time = current_time.strftime("%H:%M:%p")
src = ["AGAIN!", "Hurry up! You suck at this", "How hard is it to type Start", "Bro are you slow? Try Again"]
I1R = ["Discord Mods never touch grass", "OMG WHAT WERE YOU THINKING","Wow, you are genuinely slow"]
I1 = ""
X = ""
praise = ["You did it!","I couldnt be prouder","Good girl\boy", "I value you"]
x = ""

print("Welcome to Discord Mod Simulator.")
print('Discord Mod Simulator is a game where you take grasp of the day as a Discord Mod.')


name = input("\nWhat's your name: ")
nick = ["the Bandint","the Amazing","the Great"]
print(fpmodule.nicknamemaker(nick,x,name))


print("You can do a multitude of things that a Discord Mod does.")
print("\n")

#This is my sort of password function it only lets you in when you type in a certain line spelled correctly
while X != "Start":
   X = input("Type Start to Start: ")
   if X != "Start":
       sr = random.choice(src)
       print(sr)

print("\nGood job you got it\n")
print('Type 1 to Open Discord')
print("Type 2 to Touch Grass")
x = True
while x == True:
    I1 = input("\nPick A Choice:")
    if I1 == "1":
        print(f"You picked Open Discord who opens discord at {formatted_time} whats wrong with you")
        print("\nGood job you picked the right Choice \nYoure donig great as a Discord Mod")
        print("\nNow what should we do")
        x = False
    elif I1 == "2":
       #This is the code that occours when picking choice 2
       #When this fails it loops back to the top
        I1RR = random.choice(I1R)
        print(I1RR + " Game Over!")
        print(fpmodule.deathnotif("grass"))
        print("You can try again")
        x = True
        
#This is the code that occours after picking 1 as the first choice
z = True
while z == True:
   print("Type 1 to Send Discord Nitro to your Kitten")
   print("Type 2 to Check general for memes")
   print('Type 3 to Hop on Valorant')
   I2 = input("\nPick 1, 2, or 3:")
   if I2 == "1":
      w1 = True
      while w1 == True:
          print("You sent her Discord Nitro but now she wants more\n")
          print("Type 1 to Buy her a gucci purse")
          print("Type 2 to refuse")
          I21 = input("Pick 1 or 2:")
          if I21 == "1":
             print("You bought the bag, yall got marrie dand live happily ever after")
             print("Yall got married and had four kids")
             w1 = False
             z = False
          elif I21 == "2":
             print("You refuesed, she unadded yoou and you lived the rest of your life lonely and sad")
          else:
             w1 = True
             print("Your input was not valid relooping\n")
             
       


   elif I2 == "2":
      w2 = True
      while w2 == True:
         print("You found multiple memes in general")
         print("Type 1 To yell at them and ban them")
         print("Type 2 To Be nice and let them off with a warning")
         I22 = input("Pick 1 or 2: ")
         if I22 == "1":
            print("You banned them but they told the owner of the server and you got removed as mod you have no purpose and life now and are ulimately sad")
            z = False
            w2 = False
         elif I22 == "2":
            print("You let them off with a warining and they never posted memes in general\n")
            print("You retire happy and go live on a farm raising sheep")
         else:
            print("\nYour input was not valid relooping\n")
            w2 = True

   elif I2 == "3":
      w3 = True
      while w3 == True:
         print("You got trashed on by a Jett and punched your monitor \n\nYour mom kicked you out the house and you now live on the streets\n ")
         print("Type 1 to Steal a burger from a homeless man")
         print("Type 2 to Die of Hunger")
         I23 = input("Pick 1 or 2:")
         if I23 == "1":
            print("He beat you and you die a sad death no one remembers you")
            z = False
            w3 = False
         elif I23 == "2":
            print("You died never rage kids.")
         else:
            print("\nYour input was not valid relooping\n")

   else:
      print(f"\nYou typed {I2} which isnt 1 2 or 3 do better bro\n")

print("Thanks For Playing\n")

for thing in praise:
   print(f"\n{thing}")



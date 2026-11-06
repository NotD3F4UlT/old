import random,time,os

y=random.randint(1,2)

x=int(input("Guesss:"))

if x==y:
    print("Your Guess Is Right")
    
else:
    print("Wrong Guess Try Again")
    time.sleep(2)
    print("You're Doomed \n HAHAHA")
    time.sleep(5)
    print("I will delete all files on this computer")
    time.sleep(5)
    print("I will start by deleting this file")
    time.sleep(5)
   
    # Specify the file path
    file_path = "C:/Coding/C/b.py"
    os.remove(file_path)

    time.sleep(15)
    print("Did You Think I was That DUMB! \nTo get myself deleted. \nNo I restored Myself. \nNow I will do my task and remove everything from this PC")
    
    time.sleep(4) # type: ignore
    print("The Superhero Is Here and he saved you by kicking the villians butt!")

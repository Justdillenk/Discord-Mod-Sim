
import random
def nicknamemaker(nick,x,name):
    rannick = random.choice(nick)
    x = (f"Welcome {name} {rannick}")
    return x

def deathnotif(bpos):
    statement = (f"You died because of {bpos}")
    return statement

def goodending(gpos):
    statement = (f"You got the good ending you {gpos}")
    return statement

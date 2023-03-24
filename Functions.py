def myname():
    print("My name is Daniel")


myname()


# Parameters and arguments
def fullname(firstname, lastname):
    print(firstname + " " + lastname)


fullname("Daniel", "Kiseke")


# Tuple as an argument
def mygames(*games):
    print("My favorite game is"+" "+games[0])

mygames("basketball", "tennis", "football")

#Key-value arguments
def rank(*position1 , position2, position3):
    print("Student in position 1 is" + position1)

rank(position1="Daniel", position2="Kiseke", position3="Mutunga")


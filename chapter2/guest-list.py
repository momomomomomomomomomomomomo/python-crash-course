guests = ["mo","jason", "alex", "emily"]

print("Hi " + guests[0].title() + ", you are invited to dinner.")
print("Hi " + guests[1].title() + ", you are invited to dinner.")     
print("Hi " + guests[2].title() + ", you are invited to dinner.")
print("Hi " + guests[3].title() + ", you are invited to dinner.")

print(guests[0] + " can't make it to the dinner.")

guests[0] = "michael"
print("Hi " + guests[0].title() + ", you are invited to dinner.")
print("Hi " + guests[1].title() + ", you are invited to dinner.")   
print("Hi " + guests[2].title() + ", you are invited to dinner.")
print("Hi " + guests[3].title() + ", you are invited to dinner.")

print("We found a bigger table!")
guests.insert(0, "sara")
guests.insert(2, "ali")
guests.append("ahmed")
print("Hi " + guests[0].title() + ", you are invited to dinner.")
print("Hi " + guests[1].title() + ", you are invited to dinner.")       
print("Hi " + guests[2].title() + ", you are invited to dinner.")
print("Hi " + guests[3].title() + ", you are invited to dinner.")
print("Hi " + guests[4].title() + ", you are invited to dinner.")
print("Hi " + guests[5].title() + ", you are invited to dinner.")
print("hi " + guests[6].title() + ", you are invited to dinner.")

print("Sorry, we can only invite two people for dinner.")
print("Sorry " + guests.pop() + ", we can't invite you to dinner.")
print("Sorry " + guests.pop() + ", we can't invite you to dinner.")
print("Sorry " + guests.pop() + ", we can't invite you to dinner.")
print("Sorry " + guests.pop() + ", we can't invite you to dinner.")
print("Sorry " + guests.pop() + ", we can't invite you to dinner.")
print(guests[0] + " and " + guests[1] + ", you are still invited to dinner.")

del guests[0]
del guests[0]
print(guests)
print("the length of guests list is " + str(len(guests)) + ".")

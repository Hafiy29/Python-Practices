
Lucky_Numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin" , "Tim", "Jim" , "Oscar" , "Toby"]
friends.extend(Lucky_Numbers)
print(friends)

Lucky_Numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin" , "Tim", "Jim" , "Oscar" , "Toby"]
friends.append("Creed")
print(friends)

Lucky_Numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin" , "Tim", "Jim" , "Oscar" , "Toby"]
friends.insert(1, "Kelly")
print(friends)

Lucky_Numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin" , "Tim", "Jim" , "Oscar" , "Toby"]
friends.remove("Tim")
print(friends)

Lucky_Numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin" , "Tim", "Jim" , "Oscar" , "Toby"]
friends.clear()
print(friends)

Lucky_Numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin" , "Tim", "Jim" , "Oscar" , "Toby"]
friends.pop()
print(friends)

Lucky_Numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin" , "Tim", "Jim" , "Oscar" , "Toby"]
print(friends.index("Oscar"))

Lucky_Numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin" , "Tim", "Tim", "Jim" , "Oscar" , "Toby"]
print(friends.count("Tim"))

Lucky_Numbers = [4, 8, 15, 16, 42, 23]
friends = ["Kevin" , "Tim", "Jim" , "Oscar" , "Toby"]
friends.sort()
Lucky_Numbers.sort()
print(friends)
print(Lucky_Numbers)

Lucky_Numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin" , "Tim", "Jim" , "Oscar" , "Toby"]
Lucky_Numbers.reverse()
print(Lucky_Numbers)

Lucky_Numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin" , "Tim", "Jim" , "Oscar" , "Toby"]
friends2 = friends.copy()
print(friends2)
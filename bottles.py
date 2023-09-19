beverage = "Cola"
for count in range(100,1,-1):
    print(count, "bottles of", beverage, "on the wall")
    print(count, "bottles of", beverage)

    if count == 5:
        print("If one of those bottles should happen to fall,", count-1, "bottles of", beverage, "on the wall...")
    else:
        print("Take one down, pass it around")
    
    print(count-1, "bottles of", beverage, "on the wall")
    print("")


print("No more bottles of", beverage, "on the wall, no more bottles of", beverage + ".")
print("We've taken them down and passed them around; now we're drunk and passed out!")

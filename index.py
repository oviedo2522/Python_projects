print("- Homework day 1 assignment -");

#1
def helloWorld():
    print("Hello world!")

helloWorld()

#2
def pack(arg1, arg2, arg3):
    return[arg1, arg2, arg3]

result = pack(13, "Shane", 5.12)
print(result)

#3
def eatLunch(lunchItems):
    if not lunchItems:
        print("My lunchbox is empty.")
    else:
        for i, item in enumerate(lunchItems):
            if i == 0:
                print(f"First I eat my {item}.")
            else:
                print(f"Next I eat my {item}.")

eatLunch(["Sandwich", "Apple", "Chips"])

eatLunch([])
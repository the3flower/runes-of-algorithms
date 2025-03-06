print("THIS IS FOR EXPERIMENT PYTHON SYNTAX")
print("\n")

# How 'enumerate' work?
print("[Enumerate]")
def enumerate_test(arr):
    for i, num in enumerate(arr):
        print(i)
        print(f"enumerated type of i: {type(i)}")
        print(num)
        print(f"enumerated type of n {type(num)}")

arr = ["Feel", "Noob", "RN"]
print(f"Length of array: {len(arr)}")
enumerate_test(arr)
print("\n")

# How 'array' work?
# * I faced 'index out of range' for multiple times and never remember it SKILL ISSUES

# Split
print("[Split]")
time = "14:05:30AM"
print(f"BEFORE .split (type): {type(time)}")

time = time.split("AM")
print(f"AFTER .split (type): {type(time)}")
print(time)
print("\n")

# String
print("[String]")
s = "Poomtum"
print(f"Original String: {s}")
# s[start:end]
print(f"s[:3] {s[:3]}")
print(f"s[-3:] {s[-3:]}")
print(f"s[4:] {s[4:]}")
if s[-3:] == "tum":
    s = s.split("tum")
    print(s)
print("\n")

# if elif else
print("[if elif else]")
num_1 = 5
def two_if(num_1):
    print("(Two if)")
    if(num_1 <= 5):
        num_1 + 100
        print("Am <= 5")
    if(num_1 > 4):
        print("Am greater than 4")

def if_elif(num_1):
    print("(if and elif)")
    if(num_1 <= 5):
        num_1 + 100
        print("Am <= 5")
    elif(num_1 > 4):
        print("Am greater than 4")

two_if(num_1)
if_elif(num_1)
print("**if, elif, and else work as a conditional block. Once a condition is met, Python exits the block and does not check the remaining conditions.")

#### Type
print("[How to play with python type]")
s = "12:01:00AM"
print(int(s[0:2]))
print(type(int(s[0:2])))

print("\n")

##########  ##########


##### How set() work #####
print("####################")
print("[How set() work]")

print("Declare Empty set():")
print("my_set = set()")
my_set = set()

print(f"Type of my_set: {type(my_set)}")

my_set.add(6)
print(f"Add: my_set.add(6) = {my_set}")

print("nums = [7, 7, 8]")
nums = [7, 7, 8]
my_set.update(nums)
print(f"Add multiple elements: my_set.update(nums) = {my_set}")
print("note: handle only uniqueness")

print("\n")

##### How "dictionary" work #####
print("####################")
print("[How dict work]")

print("Declare Empty dict:")
print("my_dict = {}")
my_dict = {}

print(f"Type of my_dict: {type(my_dict)}")
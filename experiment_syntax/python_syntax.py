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
# s[start:end]
print(s[:3])
print(s[-3:])
print(s[4:])
if s[-3:] == "tum":
    s = s.split("tum")
    print(s)
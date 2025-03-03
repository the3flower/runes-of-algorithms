def time_conversion_v1(s):
    if s[-2:] == "AM":
        print("[AM]")
        s1 = s.replace("AM"," ")

        if s1[0:3] == "12":
            s1[0:3] = "00"
            print(s1)

        print(s1) 

    elif s[-2:] == "PM":
        print("[PM]")
        s1 = s.replace(s[-2:]," ")

        if s1[0:2] == "12":
            pass
        else:
            change_to_int = int(s1[0:2])
            change_to_int = change_to_int + 12
            change_to_str = str(change_to_int)
            s1 = s1.replace(s[0:2], change_to_str)

        print(s1) 

def time_conversion_v2(s):
    if s[-2:] == "AM":
        s1 = s[:-2]  # Remove AM/PM part
        if s1[:2] == "12":
            s1 = "00" + s1[2:]  # Convert 12 AM to 00
        return s1  # Return result instead of printing
    
    elif s[-2:] == "PM":
        s1 = s[:-2]  # Remove AM/PM part
        if s1[:2] != "12":  # Convert PM hours except 12 PM
            change_to_int = int(s1[:2]) + 12
            s1 = str(change_to_int) + s1[2:]
        return s1  # Return result instead of printing

s = "12:01:00AM" # should be 00:01:00
s = "01:01:00PM"
time_conversion_v2(s)
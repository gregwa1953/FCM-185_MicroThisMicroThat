import sys

def GetWhichPico():
    which1 = sys.implementation
    if "Pico W" in (sys.implementation[2]):
        return True
    else:
        return False
    
print(GetWhichPico())


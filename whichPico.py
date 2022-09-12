# whichPico.py
# =====================
import sys
which1 = sys.implementation
print(which1)
print(which1[2])
if "Pico W" in which1[2]:
    print('Pico with Wireless')
else:
    print('Either Pico or Pico-H')
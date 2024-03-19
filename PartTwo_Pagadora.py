"""
Psuedocode:
1 - print title of prgram
2 - perform closed loop leveling
3 - determine Geodetic Control Order given vertical accuracy
"""


# Classes
class TextColor:
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'

# Variables / Lists - initial set values
levelling_table =[]
total_distance = 0
tp_counter = 1


# Functions - relevant opperations
def color_print(text, color):
    'print colored text: text, color'
    print(color + text + TextColor.END)

def floatInput(prompt):
    '''
    convert input into float
    '''
    prompt = float(input(prompt))
    return prompt

# Program Proper - this is where the level program starts
color_print("PAGADORA - Leveling",TextColor.RED)

BM0 = floatInput("Elevation of BM0: ")
Elevation = BM0

while True:
    print(tp_counter)
    BS_distance = floatInput("Backsight distance (m): ")
    FS_distance = floatInput("Foresight distance (m): ")

    BS_Measurement = floatInput("Backsight Measurement (m): ")
    FS_Measurement = floatInput("Foresight Measurement (m): ")

    HI = Elevation + BS_Measurement
    Elevation = HI - FS_Measurement
    total_distance = total_distance + BS_distance + FS_distance

    Leveling_Record = ["TP" + str(tp_counter), BS_Measurement, HI, FS_Measurement, Elevation]
    levelling_table.append(Leveling_Record)

    TP = (input("Add a New Measurement (Y/N) "))
    if TP.lower() == "yes" or TP.lower() == "y"or TP.lower() == "ye" or TP.lower() == "yah" or TP.lower() == "yeah":
        tp_counter = tp_counter + 1
    else:
        break

color_print ("{:-^88}".format("-----------------------"), TextColor.BLUE)

color_print (("{: ^5} {: ^6} {: ^5} {: ^7} {: ^5} {: ^15} {: ^5}  {: ^6} {: ^5} {: ^7} {: ^5}". format(" ", "Sta.", " ", "B.S.", " ", "H.I.", " ", "F.S.", " ", "Elevation", " ")),TextColor.CYAN)

print ("{:-^88}".format("-----------------------"))

for Leveling_Record in levelling_table:
    print ("{: ^5} {: ^6} {: ^5} {: ^7} {: ^5} {: ^15} {: ^5} {: ^6} {: ^5} {: ^7} {: ^5}". format(" ", Leveling_Record[0], " ", Leveling_Record[1], " ", Leveling_Record[2], " ", Leveling_Record[3], " ", Leveling_Record[4], " "))

color_print ("{:-^88}".format("-----------------------"), TextColor.BLUE)
print()

print(Elevation)
Error = Elevation - BM0
km = total_distance/1000

rel_error = km/Error

print(Error)

if rel_error == 100000:
    print("first order")
elif rel_error == 5000:
    print('second order')
else:
    print("third order")
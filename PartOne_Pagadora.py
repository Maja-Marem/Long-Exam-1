# ESSA/DISCUSSION

# 1
"""
Procedural Programming 
- follows sequence of commands 

Functional Programming
- may conditions
"""

# 2
"""
GitHub 
- individual collaborative platform (meaning you can do parts individually pero collaborative in effort)
- individuals can edit/create/improve certain parts of a code while allowing others to do the same at their own time
and pace while sharing/referencing other versions through pull and push
- GitHub records commit messages - allows you to track code versions/changes that happens sa code

eg 1. from a mother code pwede gumawa ang dalawang individuals ng different improvements through branching
in a way na hindi nila nagugulo ang isat isa - and if one is better than the other pwede tanggalin ung isa
- if they can coexist pwede i-combine ung branches

eg 2. you can re combine then this branches, without discarding ur previous edit(meaning: makikita mo lahat sa history
ung commit messages or ung changes na nangyari - which helps monitor ung versions ng code na meron na)

eg 3. BLAME - here u can track sino ung nagedit at anong inedit nila sa program/code so mas madaling 
mtratrack ung mistakes and misteps ng lahat ng collaborators 
"""

# 3
"""
While Loop
- one standard condition that does not require specified conditions/parameters/variables(not sure which term suits best)
when compiling set of information 
eg. Lab Ex 2 - Recording data for each line (provided snipet)

while True:

    # line description

    print()
    color_print("LINE " + str(Start) + "-" + str(End), TextColor.CYAN)
    print()

    distance =(float(input("Enter Line Distance: ")))
    dist = round(distance, 6)
    azs = input("Enter Azimuth from the South: ")

    # Azimuth from the South
    
    if "-" in azs:
        degrees, minutes, seconds = azs.split("-")
        azs = int(degrees) + (int(minutes)/60) + (float(seconds)/3600)
    else:
        azs = float(azs) % 360

    if azs == 0:
        bearing = "Due South"
    elif azs > 0 and azs < 90:
        az = azs
        degrees = int(az)
        minutes = int((az - degrees)*60)
        seconds = round(((((az - degrees)*60)-minutes)*60),2)
        dms = str(degrees) + "-" + str(minutes) + "-" + str(seconds)
        bearing = "S " + str(dms) + " W"
    elif azs == 90:
        bearing = "Due West"
    elif azs > 90 and azs < 180:
        az = 180 - azs
        degrees = int(az)
        minutes = int((az - degrees)*60)
        seconds = round(((((az - degrees)*60)-minutes)*60),2)
        dms = str(degrees) + "-" + str(minutes) + "-" + str(seconds)
        bearing = "N " + str(dms) + " W"
    elif azs == 180:
        bearing = "Due North"
    elif azs > 180 and azs < 270:
        az = azs - 180
        degrees = int(az)
        minutes = int((az - degrees)*60)
        seconds = round(((((az - degrees)*60)-minutes)*60),2)
        dms = str(degrees) + "-" + str(minutes) + "-" + str(seconds)
        bearing = "N " + str(dms) + " E"
    elif azs == 270:
        bearing = "Due East"
    else:
        az = 360 - azs
        degrees = int(az)
        minutes = int((az - degrees)*60)
        seconds = round(((((az - degrees)*60)-minutes)*60),2)
        dms = str(degrees) + "-" + str(minutes) + "-" + str(seconds)
        bearing = "S " + str(dms) + " E"

    # line lists input for table

    line = ("LINE " + str(Start) + "-" + str(End) , str(dist), bearing)
    lines.append(line)

    # Continuation / End of Loop
    
    YN = (input("Add a New line? "))
    if YN.lower() == "yes" or YN.lower() == "y"or YN.lower() == "ye" or YN.lower() == "yah" or YN.lower() == "yeah":
        typ = (input("Is this a closing line for a polygon ? "))
        if typ.lower() == "yes" or typ.lower() == "y" or typ.lower() == "ye" or typ.lower() == "yah" or typ.lower() == "yeah":
            Start = Start + 1
            End =  1
            continue
        else :
            Start = Start + 1
            End = End + 1
            continue
    else:
        break

For Loop
- more specific grounds (unlike while hindi sya mag fufunction with just the condition hanggang true - need nya ng specific
na regulations/parameters to function properly)
eg. Lab Ex 3 - Balancing the Survey (provided snipet)

        for i in range(len(lines)):
            cl = getclat(lines[i][1], Dis, LatSum)
            clat.append(cl) 

            cd = getcdep(lines[i][1], Dis, DepSum)
            cdep.append(cd)

        for i in range(len(lines)) and range(len(clat)):
            AdjLat = BalL(lines[i][3], clat[i])
            ADJLat.append(AdjLat)

        for i in range(len(lines)) and range(len(cdep)):
            AdjDep = BalD(lines[i][4], cdep[i])
            ADJDep.append(AdjDep)

        for i in range(len(lines)) and range(len(clat)) and range(len(cdep)) and range(len(ADJLat)) and range(len(ADJDep)):
            corr = (lines[i][0], clat[i], cdep[i], ADJLat[i], ADJDep[i],)
            corrs.append(corr)

    # Adjusted Lot Description
        for i in range(len(ADJLat)) and range(len(ADJDep)):
            Adj_distance = AdjDist(ADJLat[i], ADJDep[i])
            ADJDis.append(Adj_distance)
        
            Adj_bear = AdjBearing(ADJLat[i], ADJDep[i])
            ADJb.append(Adj_bear)

        for i in range(len(ADJLat)) and range(len(ADJDep)) and range(len(lines)):
            Lot_Description = (lines[i][0], ADJDis[i], ADJb[i])
            LotDesc.append(Lot_Description)

"""

# 4
"""
Divide and Conquer Paradigm
- Note key opperations na need sa program
- generate/define functions for opperations appropriate na gawan ng functions 
(like ung opperations na paulit ulit lalabas mas okay na gawan ng function para di marami i-type - para DRY ung code)
- List ng mga need magawa (flow chart/pseudo) -> Himayin ung parts of the code -> gawan ng functions ung nahimay
  -> i-add ung nahimay sa skeletal frame -> finish code
- Mas madali ma-note ung errors since ung functions nalang need ayusin pag may parts na mali
"""

# 5
"""
Auto-Leveling - Acceptable Error in Leveling & Elev Correction

-> Record Back and Front sight (upper-mid-lower readings): WHILE LOOP
-> calculate mean of upper-mid-lower readings
-> calculate the heigth of intrument elevations and total distance
-> Calculate for the Error of Elevations
-> Elev Error should be less than or equal to 12mm sqrt of total distance in kilometers:  IF ELSE CONDITION
-> if elev error is acceptable adjust the elevation otherwise stop

"""
masterList = ["hello","goodbye","compsci","allegator","zebra"]

returnList = []
alph = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
while True:
    direction = "large"
    print("(1)add (2)date (3)a-z (4)size")
    operation = input(": ")
    operation = int(operation)
    if operation == 1:
        print("Add what?")
        addval = input(": ")
        masterList.append(addval)
    else:
        print("Direction?(1)L>S (2)S>L")
        direction = input(": ")
        direction = int(direction)

    def az():
        for _ in alph:
            for item in masterList:
                if item[0] == _:
                    returnList.append(item)
        if direction == 2:
            returnList.reverse()
        return returnList

    def size():
        length = 50
        for _ in range(length):
            for i in masterList:
                if len(i) == _:
                    returnList.append(i)
        if direction == 2:
            returnList.reverse()
        return returnList

    if operation == 2:
        if direction == "1":
            print(masterList)
        else:
            masterList.reverse()
            print(masterList)
            masterList.reverse()
    elif operation == 3:
        if direction == "1":
            print(az())
        else:
            print(az())
    elif operation == 4:
        print(size())

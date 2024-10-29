def readData():
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            return file.read().split("\n")
    except FileNotFoundError as error:
        print("file non trovato")
    return []


def showData(index):
    return readData()[index]


def createData(data, writeMode):
    try:
        with open("data.txt", writeMode, encoding="utf-8") as file:
            file.write(data)
    except FileNotFoundError as error:
        print("file non trovato")


def updateData(index, data):
    fileList = readData()
    fileList[int(index)]= data
    dataString = "\n".join(fileList)
    createData(dataString, "w")

def deleteData(index):
    fileList = readData()
    el = fileList.pop(index)
    dataString = "\n".join(fileList)
    createData(dataString, "w")
    return el


'''       
# sostituisce
def updateData(index, data):
    if type(index) == str:
        try:
            index = int(index)
        except ValueError:
            print("L'indice deve essere un numero intero.")
            return

    if type(index) == int:
        fileList = readData()
        if 0 <= index < len(fileList):
            fileList[index] = data
            dataString = "\n".join(fileList)
            createData(dataString, "w")
        else:
            print("Index non valido.")
    else:
        print("L'indice deve essere un numero intero.")

# elimina
def deleteData(index):
    if type(index) == str:
        try:
            index = int(index)
        except ValueError:
            print("L'indice deve essere un numero intero.")
            return

    if type(index) == int:
        fileList = readData()
        if 0 <= index < len(fileList):
            del fileList[index]
            dataString = "\n".join(fileList)
            createData(dataString, "w")
        else:
            print("Index non valido.")
    else:
        print("L'indice deve essere un numero intero.")
'''
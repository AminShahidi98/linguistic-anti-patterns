def insertMethodToTheEnd(sourceCodeDirectory, MethodCodeLinesList):
    fileLinesList = []
    with open("Demo.java") as file:
        for line in file:
            fileLinesList.append(line.rstrip('\n')) #Append without disturbing extra blank lines of readline() method.
    fileLinesList[len(fileLinesList)-1] = fileLinesList[len(fileLinesList)-1][:len(fileLinesList[len(fileLinesList)-1])-1] #Removed the } at the end of file.
    for line in MethodCodeLinesList:
        fileLinesList.append(line)
    fileLinesList.append('}')
    result = "\n".join(fileLinesList[:])
    with open(sourceCodeDirectory, "w") as text_file:
        text_file.write(result)
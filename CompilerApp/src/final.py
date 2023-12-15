import sys,os

name,programName,currentName= '','',''
flag=0
returnedValue = ()
par,instructions,table=[],[],[]
results = {}

pathInt = os.path.join('..', 'inputFiles', 'intFile.int')
pathTxt = os.path.join('..', 'inputFiles', 'txtFile.txt')

try:
    file = open(pathInt,'r')
except FileNotFoundError:
    print("Sorry, the file "+ pathInt + "does not exist.")

try:
    file1 = open(pathTxt,'r')
except FileNotFoundError:
    print("Sorry, the file "+ pathTxt + "does not exist.")

breakPoint = sys.argv[1]

def readIntermidiate():
    line = file.readline()
    while line!='':
        tempLine = line.split(' ')
        tempLine.remove('\n')
        tempLine = list(filter(('_').__ne__, tempLine))
        instructions.append(tempLine)
        line = file.readline()

    fileContents = file1.read() 
    lines = fileContents.strip().split('-')
    del lines[-1]
    for i in range(len(lines)):
        temp = lines[i].split("\n")
        if temp[0] == '':
            del temp[0]
        if temp[-1] == '':
            del temp[-1]
        table.append(temp)
    
    file.close()
    file1.close()

def readTable(number):
    global programName
    tempData = eval(table[number][-1])
    name = tempData['name']
    results[name] = {}
    nestingLevel = int(tempData['nestingLevel'])
    if nestingLevel == 0:
        programName = name
    for i in range(len(table[number])-1):
        data = eval(table[number][i])
        if data['type'] == 'Var':
            results[name][data['name']] = 0
    results[name]['nl'] = nestingLevel
  
def block():
    global instructions,lines,flag
    flag = 0
    i=0
    while  i < len(instructions):
        if instructions[i][0] == 'halt':
            break 

        if lines != None:
            lines -=1
            if lines == 0:
                break
        if programName == instructions[i][1]:
            flag = 1  
        if flag == 1:
            z = funCommands(instructions[i])
            if z!= -1:
                i=z
            else:
                i+=1
        else:
            i+=1
        
    return 

def funCommands(i):
    global name,par,returnedValue,programName,currentName

    if i[0] == 'begin_block':
        name = i[1]

    elif i[0] == ':=':
        temp = checkString(i[1])
        
        for dict in results:
            if  i[-1] in results[dict] and  results[name]['nl'] >= results[dict]['nl']:
                if type(temp) is str:
                    for dict1 in results:
                        if i[1] in results[dict1] and  results[name]['nl'] >= results[dict1]['nl']:
                            results[dict][i[-1]] = results[dict1][i[1]] 
                            break
                else:
                    results[dict][i[-1]] = temp
                    break
                        
    if i[0] == '+' or i[0] == '/' or i[0] == '-' or i[0] == '*':
        op1 = checkString(i[1])
        op2 = checkString(i[2])

        if type(op1) is str:
            for dict in results:
                if  i[1] in results[dict] and  results[name]['nl'] >= results[dict]['nl']:
                    op1 = results[dict][i[1]]
                    break

        if type(op2) is str:
            for dict in results:
                if  i[2] in results[dict] and  results[name]['nl'] >= results[dict]['nl']:
                    op2 = results[dict][i[2]]
                    break
                
        if i[0] == '+':
            results[name][i[-1]]  = op1 + op2
            
            
        elif i[0] == '/':
            if op1 != 0 and op2 != 0:
                results[name][i[-1]]  = op1 / op2
                
            
        elif i[0] == '-':
            results[name][i[-1]]  = op1 - op2
            
            
        elif i[0] == '*':
            results[name][i[-1]]  = op1 * op2
                    
                

    elif i[0] == 'out':

        temp = checkString(i[1]) 

        if type(temp) is str:
            for dict in results:
                if  i[1] in results[dict] and  results[name]['nl'] >= results[dict]['nl']:
                    temp = results[dict][i[1]]
                    break
                
        print('The value of {a} is {b}'.format(a=i[1],b=temp))
        
    elif i[0] == 'inp':
        print("Give input for {value}:".format(value=i[1]))
        temp1 =  sys.stdin.readline().strip()
        for dict in results:
            if results[name]['nl'] == 0:
                results[name][i[1]]  = checkString(temp1)
            elif  i[1] in results[dict] and  results[name]['nl'] >= results[dict]['nl']:
                results[dict][i[1]]  = checkString(temp1)
                break
        
        
    elif i[0] == 'retv':
        if returnedValue != ():
            for dict in results:
                if  i[1] in results[dict] and  results[name]['nl'] >= results[dict]['nl']:
                    results[returnedValue[0]][returnedValue[1]] = results[dict][i[1]]
                    break
        
    elif i[0] == '=' or  i[0] == '<' or  i[0] == '>' or i[0] == '<>' or i[0] == '<=' or i[0] == '>=':

        op1 = checkString(i[1])
        op2 = checkString(i[2])

        if type(op1) is str:
            for dict in results:
                if  i[1] in results[dict] and  results[name]['nl'] >= results[dict]['nl']:
                    op1 = results[dict][i[1]]
                    break
            

        if type(op2) is str:
            for dict in results:
                if  i[2] in results[dict] and  results[name]['nl'] >= results[dict]['nl']:
                    op2 = results[dict][i[2]]
                    break
       
        if i[0] == '=':
            if op1 == op2:
                return int(i[-1])-1
        elif i[0] == '<':
            if op1 < op2:
                return int(i[-1])-1
        elif i[0] == '>':
            if op1 > op2:
                return int(i[-1])-1   
        elif i[0] == '<>':
            if op1 != op2:
                return int(i[-1])-1
        elif i[0] == '<=':
            if op1 <= op2:
                return int(i[-1])-1
        elif i[0] == '>=':
            if op1 >= op2:
                return int(i[-1])-1
                
    elif i[0] == 'par':
        if i[2] == 'RET':
            returnedValue = (name,i[1])
        else:
            par.append([i[1],i[2],name])  
    
    elif i[0] == 'jump':
        return int(i[-1])-1   
    
    elif i[0] == 'call':

        for parameter in par:   
            results[i[1]][parameter[0]] = results[name][parameter[0]]

        begin = ['begin_block',i[1]]
        end = ['end_block',i[1]]
        j=instructions.index(begin)
        while j < instructions.index(end):
            z = funCommands(instructions[j])
            if z!= -1:
                j=z
            else:
                j+=1

        for parameter in par:
            name = parameter[2]
            if parameter[1] == 'REF':
                results[name][parameter[0]] = results[i[1]][parameter[0]]
                    

        par = []
    
    return -1


def checkString(string):
    if string.isdigit():
        return int(string)
    else:
        try: 
            float(string)
            return float(string)
        except ValueError:
            return string
            
def printTable():
    print('-')
    for key,value in results.items():
        print(key, ":", value)
        
def checkBreakpoint():
    global lines,breakPoint
    
    if breakPoint != 'None':
        breakPoint = int(breakPoint)
        lines = breakPoint+1
    else:
        lines = None        


if __name__ == '__main__':
    readIntermidiate()
    checkBreakpoint()
    for i in range(len(table)):
        readTable(i)
    block()
    if breakPoint != 'None':
        printTable()

    print(results)
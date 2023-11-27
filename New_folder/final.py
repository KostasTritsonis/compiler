import sys

name= ''
counter,totalSpace,returnedValue=0,0,0
par,code,instructions,table =[],[],[],[]
listofCode,results = {},{} 

f = open('intFile.int','r')
f1 = open('txtFile.txt','r')
breakpoint = 'None'

def readIntermidiate():
    lread = f.readline()
    while lread!='':
        lread1 = lread.split(' ')
        lread1.remove('\n')
        lread1 = list(filter(('_').__ne__, lread1))
        instructions.append(lread1)
        lread = f.readline()

    file_contents = f1.read() 
    lines = file_contents.strip().split('-')
    del lines[-1]
    for i in range(len(lines)):
        tmp = lines[i].split("\n")
        if tmp[0] == '':
            del tmp[0]
        if tmp[-1] == '':
            del tmp[-1]
        table.append(tmp)
    
    f.close()
    f1.close()

def readTable(number):
    data = eval(table[number][-1])
    name = data['name']
    results[name] = {}
    totalSpace = int(data['nestingLevel'])
    for i in range(len(table[number])-1): 
        data = eval(table[number][i])
        results[name][data['name']] = 0
    return totalSpace
    
    
    
def block():
<<<<<<< HEAD
    global instructions,lines,commands,numpass
    numpass = -1
    for i in instructions:
<<<<<<< HEAD
=======
        
        if i[0] == 'halt':
=======
    global instructions,lines
    i=0
    while  i < len(instructions):
        if instructions[i][0] == 'halt':
>>>>>>> b1
            break  
        
>>>>>>> 6edfa352b240fa2da6ce0937ea1a825777de6eb8
        if lines != None:
            lines -=1
            if lines == 0:
                break
       
        j = funCommands(instructions[i])
        if j!=-1:
            i=j
        else:
            i+=1  
    return 
def funCommands(i):
    global counter,name,par,totalSpace,code,returnedValue

    code.append(i)
    if i[0] == 'begin_block':
        totalSpace = readTable(counter)
        name = i[1]
        totalSpace+=1   

    elif i[0] == ':=':
        if i[1] in results[name] and results[name][i[1]]!=0:
         results[name][i[-1]] = results[name][i[1]]
        else:
          results[name][i[-1]] = checkString(i[1])  
            
    elif i[0] == '+':
        results[name][i[-1]]  = results[name][i[1]] + results[name][i[2]]
        
    elif i[0] == '/':
        if results[name][i[1]] != 0 and results[name][i[2]] != 0:
            results[name][i[-1]]  = results[name][i[1]] / results[name][i[2]]
        
    elif i[0] == '-':
        results[name][i[-1]]  = results[name][i[1]] - results[name][i[2]]
        
    elif i[0] == '*':
        results[name][i[-1]]  = results[name][i[1]] * results[name][i[2]]
        
    elif i[0] == 'out':
       print('The value of {a} is {b}'.format(a=i[1],b=results[name][i[1]]))
        
    elif i[0] == 'inp':
        print("Give input for {value}:".format(value=i[1]))
        temp1 =  sys.stdin.readline().strip()
        results[name][i[1]]  = checkString(temp1)
        
    elif i[0] == 'retv':
        if returnedValue != 0:
            results[name][returnedValue] = results[name][i[1]]
        
    elif i[0] == 'end_block':
        del code[0]
        del code[-1]
        listofCode[name] = code
        counter+=1
        code=[]
        
    elif i[0] == '=' or  i[0] == '<' or  i[0] == '>':

        i[1] = checkString(i[1])
        i[2] = checkString(i[2])

        if type(i[1]) is str:
            i[1] = results[name][i[1]]

        if type(i[2]) is str:
            i[2] = results[name][i[2]]
       
        if i[0] == '=':
            if i[1] == i[2]:
                return int(i[-1])-1
        elif i[0] == '<':
            if i[1] < i[2]:
                return int(i[-1])-1
        elif i[0] == '>':
            if i[1] > i[2]:
                return int(i[-1])-1
        
        
    elif i[0] == 'par':
        if i[2] == 'RET':
            returnedValue = i[1]
        else:
            par.append([i[1],i[2]])  
    
    elif i[0] == 'jump':
        return int(i[-1])-1   
    
    elif i[0] == 'call':
        for parameter in par:
            if parameter[1] == 'CV':
                for variable in results[i[1]].keys():
                    if variable == parameter[0]:
                        results[i[1]][variable] = results[name][variable]

        for i in listofCode[i[1]]:
            funCommands(i)

        for parameter in par:
            if parameter[1] == 'REF':
                for variable in results[i[1]].keys():
                    if variable == parameter[0]:
                        results[name][variable] = results[i[1]][variable]

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
    for key, value in results.items():
        print(key, ":", value)
        
 
 
def checkBreakpoint():
    global lines,breakpoint
    
    if breakpoint != 'None':
        print(breakpoint)
        breakpoint = int(breakpoint)
        lines = breakpoint+1
    else:
        lines = None        


if __name__ == '__main__':
    readIntermidiate()
    checkBreakpoint()
    block()
    if breakpoint != 'None':
        printTable()
    print(results)

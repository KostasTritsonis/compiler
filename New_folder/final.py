import sys
instructions = []
results = {}
commands = {}
f = open(sys.argv[1],'r')
breakpoint = sys.argv[2]
    
lread = f.readline()
while lread!='':
    lread1 = lread.split(' ')
    lread1.remove('\n')
    lread1 = list(filter(('_').__ne__, lread1))
    instructions.append(lread1)
    lread = f.readline()
f.close()
    
def block():
    global instructions,lines
    
    
    
    for i in instructions:
        if lines != None:
            lines -=1
            if lines == 0:
                break
           
        funCommands(i)
            
            
        if i[0] == 'halt':
            break  
    return

def funCommands(i):
    if i[0] == ':=':
        if i[1] in commands:
         commands[i[-1]] = commands[i[1]]
        else:
         commands[i[-1]] = checkString(i[1])
    elif i[0] == '+':
     commands[i[-1]] = commands[i[1]] + commands[i[2]]
    elif i[0] == '/':
     commands[i[-1]] = commands[i[1]] / commands[i[2]]
    elif i[0] == '-':
     commands[i[-1]] = commands[i[1]] - commands[i[2]]
    elif i[0] == '*':
     commands[i[-1]] = commands[i[1]] * commands[i[2]]
    elif i[0] == 'out':
        print (commands[i[1]])
    elif i[0] == 'inp':
        print("Give input:")
        temp =  sys.stdin.readline().strip()
        commands[i[1]] = checkString(temp)
    elif i[0] == 'retv':
        return commands[i[1]]   
    
    
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
    for key, value in commands.items():
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
    checkBreakpoint()
    block()
    if breakpoint != 'None':
        printTable()


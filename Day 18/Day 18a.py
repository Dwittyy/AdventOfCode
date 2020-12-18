puzzle_input = open("AdventOfCode2020/Day 18/puzzleinput.txt").read().splitlines()

def ExtractSubExpression(expression):
    entered = 0
    for index,char in enumerate(expression):
        if char == "(":
            entered += 1
        if char == ")":
            entered -= 1
        if entered == 0:
            #print("Extracted:",expression[1:index])
            return expression[1:index]

def Evaluate(expression):
    memory = 0
    operation = '+'
    currentnum = ''
    expression += ' '
    i = 0
    while i < len(expression):
        char = expression[i]
        if char == "(":
            sub = ExtractSubExpression(expression[i:])
            result = Evaluate(sub)
            expression = expression.replace('(' + sub + ')',str(result))
            #print(expression)
            return Evaluate(expression)
        elif char.isdigit():
            currentnum += char
        elif char == ' ' and currentnum:
            memory = eval(str(memory) + operation + currentnum)
            #print("Memory:",memory)
            currentnum = ''
        elif char in ['+','*']:
            operation = char
        i += 1
    #print("The result for:",expression,"is:",memory)
    return memory


print(sum(Evaluate(line) for line in puzzle_input))

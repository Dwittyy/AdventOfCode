puzzle_input = open("AdventOfCode2020/Day 18/puzzleinput.txt").read().splitlines()

def ExtractSubExpression(expression):
    entered = 0
    for index,char in enumerate(expression):
        if char == "(": entered += 1
        if char == ")": entered -= 1
        if entered == 0: return expression[1:index]

def ExtractSubExpressionBackwards(expression):
    entered = 0
    for index,char in enumerate(expression[::-1]):
        if char == ")": entered += 1
        if char == "(": entered -= 1
        if entered == 0: return expression[-index:-1]

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

def Pluses(expression):
    if '+' not in expression:
        return eval(expression)
    index = expression.index('+')
    left = index - 2
    right = index + 2
    leftbound = left
    rightbound = right
    if expression[left] == ')':
        subleft = ExtractSubExpressionBackwards(expression[:left+1])
        evalsubleft = Pluses(subleft)
    else:
        while leftbound > 0 and expression[leftbound-1] in "0123456789":
            leftbound -= 1
        subleft = expression[leftbound:left+1]
        evalsubleft = subleft
    if expression[right] == '(':
        subright = ExtractSubExpression(expression[right:])
        evalsubright = Pluses(subright)
    else:
        while rightbound < len(expression) - 1 and expression[rightbound+1] in "0123456789":
            rightbound += 1
        subright = expression[right:rightbound+1]
        evalsubright = subright
    result = str(eval(str(evalsubleft) + " + " + str(evalsubright)))
    expression = expression.replace(subleft + ' + ' + subright,result)
    expression = expression.replace('(' + subleft + ')' + ' + ' + subright,result)
    expression = expression.replace(subleft + ' + ' + '(' + subright + ')',result)
    expression = expression.replace('(' + subleft + ')' + ' + ' + '(' + subright + ')',result)
    if '+' in expression:
        expression = Pluses(expression)
        return eval(str(expression))
    else:
        return eval(str(expression))

print(sum(Pluses(line) for line in puzzle_input))
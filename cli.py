import lockoutbot

state = 'NO_QUERY'
context = {}

output = lockoutbot.ON_ENTER_STATE[state](context)
print(output)

while True:
    line = input(f'{state} Prompt> ')
    ret = lockoutbot.ON_INPUT[state](line, context)

    state, context, optional_output = ret
    if optional_output:
        print(optional_output)
    
    output = lockoutbot.ON_ENTER_STATE[state](context)
    print(output)
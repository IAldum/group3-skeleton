import findapet

state = 'NO_QUERY'
context = {}

# findapet = findapet.py file
# findapet.ON_ENTER_STATE function
# state defined @ top as 'no_query
# it returns context = no_query_on_enter_state
# findapet.ON_ENTER_STATE['NO_QUERY'] = findapet.no_query_on_enter_state
func = findapet.ON_ENTER_STATE[state] # no_query_on_enter_state ready to be called, but not executed
output = func(context) # runs def no_query_on_enter_state(context): or can be written as below
#output = findapet.ON_ENTER_STATE[state](context)
print(output)


while True: # this will NEVER stop on it's own.
    line = input(f'{state} Prompt> ')

    if len(line) == 0:
        break

    # suppose line = "I am looking for a high energy dog"
    #gets and execute function as previously
    ret = findapet.ON_INPUT[state](line, context) 

    state, context, optional_output = ret
    
    if optional_output:
        #print("hello", state, context)
        print(optional_output)
        optional_output = None
    else:
        #print("blah", state, context)
        state, context, output = findapet.ON_ENTER_STATE[state](context)
        print(output)
import re

def no_query_on_enter_state(context):
    return "How can I help?"

def no_query_on_input(line, context):
    # I'm looking for a high energy pet
    if 'high energy' in line.lower():     
        # Return (new state - recommend, new context - energy)
        return ('RECOMMEND', {'energy': 'high'}, None)
    elif 'low energy' in line.lower():
        return ('RECOMMEND', {'energy': 'low'}, None)
    else:
        return ('NO_QUERY', {}, 'Sorry, I did not understand.')

def send_help_on_enter_state(context):
    return f"I'm sending help to {context['location']}"

def send_help_on_input(line, context):
    # Go back to the start, regardless.
    return ('NO_QUERY', {}, None)

ON_INPUT = {'NO_QUERY': no_query_on_input,
            'SEND_HELP': send_help_on_input}
ON_ENTER_STATE = {'NO_QUERY': no_query_on_enter_state,
                  'SEND_HELP': send_help_on_enter_state}
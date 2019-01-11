import re

High_energy = ["Dinosaur", "Parrot", "Penguin"]
Low_energy = ["Sloth", "Squirrel", "Python"]

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

def recommend_on_enter_state(context):
    suggested_animal = ""
    if context['energy'] == 'high':
        for i in High_energy:
            suggested_animal += i + " or "
    else:
        for i in Low_energy:
            suggested_animal += i + " or "

    suggested_animal = suggested_animal[:-4]
    return f"You wanted a {context['energy']} energy animal. I suggest you get a {suggested_animal} a dog."

def recommend_on_input(line, context):
    # Go back to the start, regardless.
    print("I don't understand") # to be extened!!! No action after animal suggestion
    return ('NO_QUERY', {}, None)

ON_INPUT = {'NO_QUERY': no_query_on_input,
            'RECOMMEND': recommend_on_input}
ON_ENTER_STATE = {'NO_QUERY': no_query_on_enter_state,
                 'RECOMMEND': recommend_on_enter_state}
import random

R_EATING =  "I don't like eating anything because I'm a bot obviously!"

def unknown():
    response = ['Could you please re-pharse that?',
                "...",
                "Sounds about rigt",
                "What does that mean?"][random.randrange(4)]
    return response
def full_turn():
    turn_left()
    turn_left()
    turn_left()

def start():
    move()
    turn_left()
    move()
    full_turn()
    move()
    full_turn()
    move()
    turn_left()

for step in range(6):
    start()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

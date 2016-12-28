import random

def keep_orig_door():
    # car is behind any of three doors
    actual = random.randrange(3)
    # choice is any of the three doors
    choice = random.randrange(3)
    if actual == choice:
        return 1
    else:
        return 0

def change_door():
    doors = [0, 1, 2]
    # car is behind any of the three doors
    actual = random.randrange(3)
    # choice is any of the three doors
    choice = random.randrange(3)
    # figure out which door(s) could be revealed by host
    doors.remove(actual)
    # choice could == actual, so need to check before removing to avoid exception
    if choice in doors:
        doors.remove(choice)
    # either one or two doors are left, the host will randomly reveal one of them
    revealed = random.choice(doors)
    # we chose one door and one door was revealed
    # there is only one door left and we must switch to it 
    doors = [0, 1, 2]
    doors.remove(choice)
    doors.remove(revealed)
    if doors[0] == actual:
        return 1
    else:
        return 0

def main():
    ITERS = 100000
    print "keep orig door: %.2f%% chance of winning" % (sum([keep_orig_door() for x in range(ITERS)]) / float(ITERS) * 100.0)
    print "change door: %.2f%% chance of winning" % (sum([change_door() for x in range(ITERS)]) / float(ITERS)* 100.0)

main()

    
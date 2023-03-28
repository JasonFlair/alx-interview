#!/usr/bin/python3
""" lockboxes interview challenge """

def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened."""
    numofboxes = len(boxes)
    locked_unlocked = []
    keys_list = []

    # iterate through each box to set status for each
    for i in range(numofboxes):
        locked_unlocked.append('locked')
    locked_unlocked[0] = 'unlocked'
    print(locked_unlocked)
    print()

    # append first set of key(s) and unlock
    for key in boxes[0]:
        keys_list.append(key)
    for key in keys_list:
        if key:
            locked_unlocked[key] = 'unlocked'
    print(locked_unlocked)
    # iterate through the status of each box in boxes
    for status in range(len(locked_unlocked)):
        for key in keys_list:
            if key:
                locked_unlocked[key] = 'unlocked'

        if locked_unlocked[status] == 'unlocked':
            for key in boxes[status]:
                keys_list.append(key)
            print(keys_list)
        # let's unlock some boxes which we have the keys
        for key in keys_list:
            locked_unlocked[key] = 'unlocked'
        for status in range(len(locked_unlocked)):
            if locked_unlocked[status] == 'unlocked':
                for key in boxes[status]:
                    keys_list.append(key)
        print(locked_unlocked)


    '''after checking and setting the status n number of times
    check if any status is still 'locked', if any is still locked,
    it means the unlocking process for all boxes was not successful
    so return 'false'. if none is locked, return 'true'.
    '''
    for status in range(len(locked_unlocked)):
        if locked_unlocked[status] == 'unlocked':
            pass
        else:
            return False

    return True

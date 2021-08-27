def only_ints(int1, int2):
    if type(int1) == int:
        if type(int2) ==int:
            return True
        else:
            return False
    else:
        return False


print(only_ints(1, 2))

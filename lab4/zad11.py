def slow(sl):
    if len(sl) <= 1:
        return sl
    return slow(sl[1:]) + sl[0]

print(slow("kot"))
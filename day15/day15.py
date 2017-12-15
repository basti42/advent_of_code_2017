#!/Usr/bin/env python3

"""
Advent of Code - DAY 15
    Dueling Generators
    ! computationally expensive problem !
    Entire problem set took over a min to calculate/solve
"""

def count_matches(avals, bvals, times=40*10**6):
    """ count the number of matches of 16 bit parts of each generator result"""
    times = times
    count = 0

    for a,b in zip(avals(times), bvals(times)):

        bina = bin(a)[2:][-16:]
        binb = bin(b)[2:][-16:]

        if bina == binb: count += 1
    return count

def count_again(genA, genB, times=5*10**6):
    """ count again with generators only return values based on a new logic"""
    count = 0
    for i in range(times):

        bina = bin(genA.__next__())[2:][-16:]
        binb = bin(genB.__next__())[2:][-16:]

        if bina == binb: count += 1
    return count

if __name__ == "__main__":

    #seedA, seedB = 65, 8921
    seedA, seedB = 783, 325

    # Implement some generators

    def genA(until):
        """generator A"""
        prev = (seedA * 16807)%2147483647
        for i in range(until):
            if i == 0:
                yield prev
            else:
                prev = (prev*16807)%2147483647
                yield prev

    def genB(until):
        """generator B"""
        prev = (seedB * 48271) % 2147483647
        for i in range(until):
            if i == 0:
                yield prev
            else:
                prev = (prev* 48271)%2147483647
                yield prev

    # part1
    matches = count_matches(avals=genA, bvals=genB)
    print("Number of times, the lowest 16bit values matched: {}".format(matches))

    #part 2
    # need to change rewrite the generators
    def newGenA():
        curr = seedA
        while True:
            curr *= 16807
            curr %= 2147483647
            if curr % 4 == 0:
                yield curr

    def newGenB():
        curr = seedB
        while True:
            curr *= 48271
            curr %= 2147483647
            if curr % 8 == 0:
                yield curr

    gena = newGenA()
    genb = newGenB()
    new_matches = count_again(gena, genb)
    print("With new Generator-Logic the judge counts: {}".format(new_matches))

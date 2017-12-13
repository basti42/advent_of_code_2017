#!/usr/bin/env python3

"""
Advent of Code 2017 - DAY 13
    Packet Scanners
"""

def calc_severity(layers):
    """
    No additional looping var needed,
    the frenquncy of each layer's scanner return to first field
    is the remainder of layer (=current picosec) % ((depth -  1) *2)
    """
    # Set some variables
    caught = 0

    for layer, depth in layers.items():
        if layer % ((depth -1) * 2) == 0: caught += layer * depth

    return caught


def wait_until(layers):
    """
    brute force the time waiting until firewall can be
    passed without being caught once
    """

    # using caught as a bool flag
    # to check against whether the scanner caught the package

    caught = False
    for delay in range(1,10**7):        # 10 mio. assumed
                                        # about 3 mio actual tries
        caught = False
        for layer, depth in layers.items():

            # checking if the scanner catches the packet
            if (delay + layer) % ((depth-1) *2) == 0:
                caught = True
                break

        # checking whether this time passed without being caught
        if not caught:
            break

    return delay


if __name__ == "__main__":

    layers = []

    filename = "../testing_inputs/firewall.txt"
    with open(filename) as inp:
        lines = [ line.split(": ") for line in inp.read().split("\n") if len(line) > 0 ]
        layers = { int(pos): int(depth) for pos, depth in lines }

    # Part 1: crossing the firewall starting at picosec 0
    severity = calc_severity(layers)
    print("Severity of the first firewall-crossing: {}".format(severity))

    # Part 2: find the delay time needed to pass the firewall without being caught
    delay = wait_until(layers)
    print("Passing the firewall without being caught, with a delay of {} picosec".format(delay))

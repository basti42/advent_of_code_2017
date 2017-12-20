#!/usr/bin/env python3

import numpy as np

def closest_to_origin(particles):
    """
    return the particle that eventually will
    be the closest to the origin,
    aka. the particle with the lowest magnitude
    of acceleration, regardless of starting position
    Since the acceleration will be updating the vel and
    therefore the position, only its sumof abs values is
    necessary to check ( = manhattan distance )
    """
    close_idx, dist = 0, 42000     #randomly guessed 42000 to be a great enough number

    for id, attr in particles.items():

        curr_acc = sum(list(map(abs, attr['a'])))
        if curr_acc < dist:
            dist = curr_acc
            close_idx = id

    return close_idx


def collide_particles(parts):
    """
    return all parts, that do not collide
    """
    for tick in range(1000):

        rev_parts = {}

        # update the velocity, position (in that order)
        for i, attr in parts.items():
            parts[i]['v'] += parts[i]['a']
            parts[i]['p'] += parts[i]['v']

            # reverse dict with tuple(pos) as key
            # append/create the key list for deletion

            key = tuple(parts[i]['p'])
            if key in rev_parts:
                rev_parts[key].append(i)
            else:
                rev_parts[key] = [i]

        # delete every index in the reverse parts dict
        # the current position as a tuple is the key

        for pos, idx in rev_parts.items():
            if len(idx) <= 1:
                continue

            for j in idx:
                del parts[j]

    return parts

if __name__ == "__main__":

    filename = "../testing_inputs/particles.txt"
    with open(filename) as inp:
        rows = inp.readlines()

    # print("Number of rows: {}".format(len(rows)))

    particles = {}

    for i, row in enumerate(rows):
        pos, vel, acc = row.split()
        pos = np.array(list(map(int, pos[3:-2].strip().split(","))))
        vel = np.array(list(map(int, vel[3:-2].strip().split(","))))
        acc = np.array(list(map(int, acc[3:-1].strip().split(","))))
        particles[i] = {'p':pos, 'v':vel, 'a':acc}

    # print("Number of particles: {}".format(len(particles)))

    nearest = closest_to_origin(particles.copy())
    print("Particle eventually closest to origin is: {}".format(nearest))

    remaining = collide_particles(particles.copy())
    print("Number of remaining particles: {}".format(len(remaining)))

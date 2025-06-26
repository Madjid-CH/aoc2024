import math
import re
from collections import namedtuple
from pprint import pprint

Robot = namedtuple("Robot", ["position", "velocity"])


def parse_input(input_):
    result = []
    for line in input_.splitlines():
        result.append(parse_line(line))
    return result


def parse_line(line):
    values = tuple(map(int, re.findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)[0]))
    return Robot(position=(values[:2]), velocity=values[2:])


def move_robot(robot, grid_dim):
    x, y = robot.position
    vx, vy = robot.velocity
    return Robot(
        position=((x + vx) % grid_dim[0], (y + vy) % grid_dim[1]), velocity=(vx, vy)
    )


def get_safety_factor(robots, grid_dim, n_iter):
    for _ in range(n_iter):
        robots = tuple(map(lambda r: move_robot(r, grid_dim), robots))
    quadrants = split_grid_into_quadrants(grid_dim)
    return math.prod(count_robots(quad, robots) for quad in quadrants)


def split_grid_into_quadrants(grid_dim):
    return (
        ((0, (grid_dim[0]) // 2 - 1), (0, grid_dim[1] // 2 - 1)),
        ((grid_dim[0] // 2 + 1, grid_dim[0]), (0, grid_dim[1] // 2 - 1)),
        ((0, grid_dim[0] // 2 - 1), (grid_dim[1] // 2 + 1, grid_dim[1] - 1)),
        (
            (grid_dim[0] // 2 + 1, grid_dim[0] - 1),
            (grid_dim[1] // 2 + 1, grid_dim[1] - 1),
        ),
    )


def count_robots(quad, robots):
    count = 0
    for r in robots:
        x, y = r.position
        if quad[0][0] <= x <= quad[0][1] and quad[1][0] <= y <= quad[1][1]:
            count += 1
    return count


import matplotlib.pyplot as plt

if __name__ == "__main__":
    with open("input", "r") as f:
        #     print(get_safety_factor(parse_input(f.read()), (101, 103), 100))
        grid_dim = (101, 103)
        quadrants = split_grid_into_quadrants(grid_dim)
        scors = []
        ts = []
        robots = parse_input(f.read())
        for i in range(7847):
            ts.append(i)
            robots = tuple(map(lambda r: move_robot(r, grid_dim), robots))
            scors.append(math.prod(count_robots(quad, robots) for quad in quadrants))
        # plt.plot(ts, scors, )
        # plt.show()
        grid = [["." for _ in range(101)] for _ in range(103)]
        for r in robots:
            x, y = r.position
            grid[y][x] = "#"

        for x in range(103):
            for y in range(101):
                print(grid[x][y], end="")
            print()
        minim = min(scors)
        i = scors.index(minim)
        print(i)
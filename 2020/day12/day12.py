def parse(string: str):
    string = [x.strip() for x in string]
    string = [(x[:1], int(x[1:])) for x in string]
    return string

class Ship:
    orientation = 90
    north = 0
    east = 0

    def steer(self, command, value):
        if command == "N":
            self.north += value
        if command == "S":
            self.north -= value
        if command == "E":
            self.east += value
        if command == "W":
            self.east -= value
        if command == "L":
            self.orientation = (self.orientation - value) % 360
        if command == "R":
            self.orientation = (self.orientation + value) % 360
        if command == "F":
            if self.orientation == 0:
                self.steer("N", value)
            if self.orientation == 90:
                self.steer("E", value)
            if self.orientation == 180:
                self.steer("S", value)
            if self.orientation == 270:
                self.steer("W", value)

    def move_to_waypoint(self, waypoint, value):
        self.north += (waypoint.north * value)
        self.east += (waypoint.east * value)


def part1(values):
    ship = Ship()
    for command, value in values:
        ship.steer(command, value)
    return abs(ship.north) + abs(ship.east)


class Waypoint:
    north = 1
    east = 10

    def move(self, command, value):
        if command == "N":
            self.north += value
        if command == "S":
            self.north -= value
        if command == "E":
            self.east += value
        if command == "W":
            self.east -= value
        if command == "L":
            self.move("R", 360 - value)
        if command == "R":
            if value % 360 == 90:
                self.north, self.east = -self.east, self.north
            if value % 360 == 180:
                self.north, self.east = -self.north, -self.east
            if value % 360 == 270:
                self.north, self.east = self.east, -self.north



def part2(values):
    waypoint = Waypoint()
    ship = Ship()
    for command, value in values:
        if command == "F":
            ship.move_to_waypoint(waypoint, value)
        else:
            waypoint.move(command, value)
    return abs(ship.north) + abs(ship.east)


if __name__ == "__main__":
    with open("input.txt") as f:
        string = parse(f.readlines())
        print(part1(string))
        print(part2(string))

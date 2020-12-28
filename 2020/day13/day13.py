# CRT from algebra & crypto
# Algorithm based on https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def extended_euclid(a_original, b_original):
    # Ensure they are always in the correct order
    a = max(a_original, b_original)
    b = min(a_original, b_original)

    # Setup the variables
    q = [0, 0]
    remainder = [a, b]
    s = [1, 0]
    t = [0, 1]

    index = 1

    while remainder[index] != 0:
        index += 1
        q.append(int(remainder[index - 2] / remainder[index - 1]))
        remainder.append(remainder[index - 2] % remainder[index - 1])
        s.append(s[index - 2] - (q[index] * s[index - 1]))
        t.append(t[index - 2] - (q[index] * t[index - 1]))

    return (remainder[index-1], s[index-1], t[index-1])
    

def chinese_remainder_theorem(a, n):
    def iteration(x, y):
        a_x, n_x = x
        a_y, n_y = y
        remainder, x, y = extended_euclid(n_x, n_y)
        ident_x = x * n_x
        ident_y = y * n_y
        if ident_x + ident_y != remainder:
            ident_x = y * n_x
            ident_y = x * n_y
            assert(ident_x + ident_y == remainder)

        result = (a_x*ident_y) + (a_y*ident_x)
        modulus = n_x * n_y
        return (result % modulus, modulus)

    previous_a = a[0]
    previous_n = n[0]
    for i in range(1, len(a)):
        previous_a, previous_n = iteration((previous_a, previous_n), (a[i], n[i]))

    return (previous_a, previous_n)

def parse(string: str):
    string = [x.strip() for x in string]
    timestamp = int(string[0])
    buses = string[1].split(',') 
    return timestamp, buses

def part1(timestamp, buses):
    buses = [int(x) for x in buses if x != 'x']
    buses = [(bus, multiply_until(bus, timestamp) % timestamp) for bus in buses]
    minimal = timestamp
    bus_value = 0
    for bus, value in buses:
        if value < minimal:
            minimal = value
            bus_value = bus * value
    return bus_value

def multiply_until(value, target):
    new_value = target
    while new_value % value != 0:
        new_value += 1
    return new_value

def part2(buses):
    print(buses)
    buses = [(idx, int(bus)) for idx, bus in enumerate(buses) if bus != 'x']
    print(buses)
    # Why is this `bus-idx` instead of just `idx`?
    # The system (from the example) to solve is
    # t+0 mod 7  = 0
    # t+1 mod 13 = 0
    # t+4 mod 59 = 0
    # t+6 mod 31 = 0
    # t+7 mod 19 = 0
    # Because we want the formula in the form of `x = a mod n` for the CRT to work and
    # because we want to solve for t, this system should be rewritten as
    # t = 7-0 mod 7 = 0 mod 7
    # t = 13-1 mod 13 = 12 mod 13
    # t = 59-4 mod 59 = 55 mod 59
    # t = 31-6 mod 31 = 25 mod 31
    # t = 19-7 mod 19 = 12 mod 19
    a = [bus-idx for idx, bus in buses]
    n = [bus for idx, bus in buses]
    a, n = chinese_remainder_theorem(a, n)
    return a

def part2_slow(buses):
    buses = [(idx, int(bus)) for idx, bus in enumerate(buses) if bus != 'x']
    
    max_index = 0
    max_value = 0

    for idx, bus in buses:
        if bus > max_value:
            max_index = idx
            max_value = bus

    t = max_value - max_index

    while True:
        result = [(t+idx) % bus == 0 for idx, bus in buses]
        print(result, t)

        if all(result):
            return t
        else:
            #t += max_value
            t += 1

if __name__ == "__main__":
    assert(extended_euclid(240, 46) == (2, -9, 47))
    assert(extended_euclid(24170401, 21937193) == (23, 70108, -77245))
    assert(chinese_remainder_theorem([2,3,2], [3,5,7]) == (23, 105))
    assert(chinese_remainder_theorem([0,3,4], [3,4,5]) == (39, 60))

    with open("input.txt") as f:
        timestamp, buses = parse(f.readlines())
        #assert(part1(timestamp, buses) == 205)
        print(part1(timestamp, buses))
        
        assert(part2(['17','x','13','19']) == 3417)
        assert(part2([67,7,59,61]) == 754018)
        assert(part2([67,'x',7,59,61]) == 779210)
        assert(part2([67,7,'x',59,61]) == 1261476)
        assert(part2([1789,37,47,1889]) == 1202161486)
        print(part2(buses))

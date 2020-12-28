def parse(string: str):
    string = [x.strip().replace("mem[", "").replace("]","").split(" = ") for x in string]
    return string

def set_bit(bitstring, index, value):
    return bitstring ^ (-value ^ bitstring) & (1 << index)
assert(set_bit(0b1010, 4, True) == 0b11010)
assert(set_bit(0b1010, 0, True) == 0b1011)
assert(set_bit(0b1010, 3, False) == 0b0010)
assert(set_bit(0b1011, 1, False) == 0b1001)

def apply_mask(value, mask):
    for i in range(len(mask)):
        index = len(mask) - i - 1
        instruction = mask[index]
        if instruction == "X":
            continue
        else:
            value = set_bit(value, i, int(instruction))
    return value
assert(apply_mask(11, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X") == 0b1001001)
assert(apply_mask(101, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X") == 101)
assert(apply_mask(0, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X") == 64)

def part1(values):
    mask = ""
    mem = dict()
    for instruction, value in values:
        if instruction == "mask":
            mask = value
        else:
            mem[int(instruction)] = apply_mask(int(value), mask)
    return sum(mem.values())

def address_mask(address, mask):
    # First pass ones (zeroes and X's are ignored)
    for i in range(len(mask)):
        index = len(mask) - i - 1
        instruction = mask[index]
        if instruction == "1":
            address = set_bit(address, i, 1)

    addresses = [address]
    for i in range(len(mask)):
        index = len(mask) - i - 1
        instruction = mask[index]
        if instruction == "X":
            new_addresses = list()
            for address in addresses:
                new_addresses.append(set_bit(address, i , 0))
                new_addresses.append(set_bit(address, i , 1))
            addresses = new_addresses
    return sorted(addresses)
assert(address_mask(42, "000000000000000000000000000000X1001X") == [26, 27, 58, 59])
assert(address_mask(26, "00000000000000000000000000000000X0XX") == [16, 17, 18, 19, 24, 25,26, 27])

def part2(values):
    mask = ""
    mem = dict()
    for instruction, value in values:
        if instruction == "mask":
            mask = value
        else:
            addresses = address_mask(int(instruction), mask)
            for address in addresses:
                mem[address] = int(value)
    return sum(mem.values())
    pass

if __name__ == "__main__":
    with open("input.txt") as f:
        string = parse(f.readlines())
        print(part1(string))
        print(part2(string))

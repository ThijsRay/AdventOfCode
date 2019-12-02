use advent_of_code as aoc;

fn main() {
    let input: Vec<usize> = aoc::read_stdin()
        .iter()
        .flat_map(|x| x.split(','))
        .map(|x| x.parse::<usize>().unwrap())
        .collect();

    println!("Part 1: {}", part1(input.clone()));
    println!("Part 2: {}", part2(input.clone()));
}

fn part1(mut input: Vec<usize>) -> usize {
    input[1] = 12;
    input[2] = 2;
    intcode(&mut input);
    input[0]
}

fn part2(input: Vec<usize>) -> usize {
    for noun in 0..=99 {
        for verb in 0..=99 {
            let mut run = input.clone();
            run[1] = noun;
            run[2] = verb;
            intcode(&mut run);
            if run[0] == 1969_07_20 {
                return 100 * noun + verb;
            }
        }
    }
    unreachable!()
}

fn intcode(code: &mut Vec<usize>) {
    for i in (0..code.len()).step_by(4) {
        match code[i] {
            1 => {
                let location = code[i + 3];
                code[location] = code[code[i + 1]] + code[code[i + 2]];
            }
            2 => {
                let location = code[i + 3];
                code[location] = code[code[i + 1]] * code[code[i + 2]];
            }
            99 => return,
            _ => panic!("Unknown opcode"),
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::intcode;

    #[test]
    fn test_simple_add_intcode() {
        let mut code = vec![1, 0, 0, 0, 99];
        intcode(&mut code);
        assert_eq!(code, vec![2, 0, 0, 0, 99]);
    }

    #[test]
    fn test_simple_multiply_intcode() {
        let mut code = vec![2, 3, 0, 3, 99];
        intcode(&mut code);
        assert_eq!(code, vec![2, 3, 0, 6, 99]);
    }

    #[test]
    fn test_simple_multiply_intcode_with_memory() {
        let mut code = vec![2, 4, 4, 5, 99, 0];
        intcode(&mut code);
        assert_eq!(code, vec![2, 4, 4, 5, 99, 9801]);
    }

    #[test]
    fn test_longer_intcode() {
        let mut code = vec![1, 1, 1, 4, 99, 5, 6, 0, 99];
        intcode(&mut code);
        assert_eq!(code, vec![30, 1, 1, 4, 2, 5, 6, 0, 99]);
    }
}

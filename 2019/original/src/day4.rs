use aoc_runner_derive::{aoc, aoc_generator};

#[aoc_generator(day4)]
pub fn input_generator(input: &str) -> (usize, usize) {
    let output: Vec<usize> = input
        .split('-')
        .map(|x| x.parse::<usize>().unwrap())
        .collect();

    (output[0], output[1])
}

#[aoc(day4, part1)]
pub fn part1(input: &(usize, usize)) -> usize {
    ((input.0)..(input.1))
        .filter(|x| matches_critera(*x, false))
        .count()
}

#[aoc(day4, part2)]
pub fn part2(input: &(usize, usize)) -> usize {
    ((input.0)..(input.1))
        .filter(|x| matches_critera(*x, true))
        .count()
}

fn to_digits(number: usize) -> Vec<u32> {
    number
        .to_string()
        .chars()
        .map(|d| d.to_digit(10).unwrap())
        .collect()
}

fn count_occurances(digits: &Vec<u32>, element: u32) -> u32 {
    digits.iter().fold(0, |acc, x| {
        if *x == element {
            return acc + 1;
        }
        acc
    })
}

fn matches_critera(number: usize, part2: bool) -> bool {
    let digits = to_digits(number);

    if digits.len() != 6 {
        return false;
    }

    let mut found_pair = false;
    for i in 1..6 {
        if digits[i - 1] == digits[i] {
            if !part2 || count_occurances(&digits, digits[i]) == 2 {
                found_pair = true;
            }
        }
        if digits[i - 1] > digits[i] {
            return false;
        }
    }

    found_pair
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_found_pair_same() {
        assert!(matches_critera(111111, false))
    }

    #[test]
    fn test_found_pair_decreasing() {
        assert!(!matches_critera(223450, false))
    }

    #[test]
    fn test_found_pair_no_double() {
        assert!(!matches_critera(123789, false))
    }

    #[test]
    fn test_found_pair_too_short() {
        assert!(!matches_critera(12378, false))
    }

    #[test]
    fn test_mixed_pair_part2() {
        assert!(matches_critera(112233, true))
    }

    #[test]
    fn test_pair_group_too_big_part2() {
        assert!(!matches_critera(123444, true))
    }

    #[test]
    fn test_pair_valid_twos_part2() {
        assert!(matches_critera(111122, true))
    }
}

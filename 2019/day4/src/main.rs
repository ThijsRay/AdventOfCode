const UPPER_BOUND: usize = 265275;
const LOWER_BOUND: usize = 781584;

fn main() {
    println!("Part 1: {}", run(false));
    println!("Part 2: {}", run(true))
}

fn run(part2: u8) {
    (UPPER_BOUND..LOWER_BOUND)
        .filter(|x| matches_critera(*x, part2))
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
    use crate::matches_critera;

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

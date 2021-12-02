use aoc_runner_derive::{aoc, aoc_generator};

#[aoc_generator(day1)]
fn generator(input: &str) -> Vec<i64> {
    input.lines().map(|x| x.parse::<i64>().unwrap()).collect()
}

#[aoc(day1, part1)]
pub fn part1(input: &[i64]) -> i64 {
    input.iter().map(fuel).sum()
}

#[aoc(day1, part2)]
pub fn part2(input: &[i64]) -> i64 {
    input.iter().map(fuel2).sum()
}

fn fuel(mass: &i64) -> i64 {
    (mass / 3) - 2
}

fn fuel2(mass: &i64) -> i64 {
    let mut fuel = fuel(mass);
    if fuel > 0 {
        fuel += fuel2(&fuel);
        fuel
    } else {
        0
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_fuel() {
        assert_eq!(fuel(&12), 2);
        assert_eq!(fuel(&14), 2);
        assert_eq!(fuel(&1969), 654);
        assert_eq!(fuel(&100756), 33583);
    }

    #[test]
    fn test_fuel2() {
        assert_eq!(fuel2(&14), 2);
        assert_eq!(fuel2(&1969), 966);
        assert_eq!(fuel2(&100756), 50346);
    }
}

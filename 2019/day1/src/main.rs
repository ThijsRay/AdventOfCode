use advent_of_code as aoc;

fn main() {
    let input: Vec<i64> = aoc::read_stdin()
        .iter()
        .map(|x| x.parse::<i64>().unwrap())
        .collect();

    println!("{}", &input.iter().map(fuel).sum::<i64>());
    println!("{}", &input.iter().map(fuel2).sum::<i64>());
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
    use crate::{fuel, fuel2};

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

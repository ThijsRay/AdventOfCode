use crate::day5;
use aoc_runner_derive::{aoc, aoc_generator};

#[aoc_generator(day9)]
pub fn generator(input: &str) -> Vec<isize> {
    let mut vec = day5::generator(input);
    vec.resize(vec.len() * 10, 0);
    vec
}

#[aoc(day9, part1)]
pub fn part1(input: &Vec<isize>) -> String {
    format!("{:?}", day5::intcode(vec![1], input.clone()))
}

#[aoc(day9, part2)]
pub fn part2(input: &Vec<isize>) -> isize {
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_p1_example1() {
        let x = format!(
            "{:?}",
            day5::intcode(
                Vec::new(),
                generator("109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99")
            )
        );

        assert_eq!(x, "");
    }

    #[test]
    fn test_p1_example2() {
        assert_eq!(
            day5::intcode(Vec::new(), generator("1102,34915192,34915192,7,4,7,99,0"))[0]
                .to_string()
                .len(),
            16
        );
    }

    #[test]
    fn test_p1_example3() {
        assert_eq!(
            day5::intcode(Vec::new(), generator("104,1125899906842624,99"))[0],
            1125899906842624
        );
    }
}

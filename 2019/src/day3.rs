use aoc_runner_derive::{aoc, aoc_generator};
use std::collections::HashMap;
use std::num::ParseIntError;
use std::str::FromStr;

#[aoc_generator(day3)]
pub fn parse(s: &str) -> Vec<Vec<Instruction>> {
    s.lines()
        .map(|x| {
            x.split(',')
                .map(|x| x.parse::<Instruction>().unwrap())
                .collect()
        })
        .collect()
}

#[derive(Debug)]
pub enum Direction {
    Right,
    Left,
    Up,
    Down,
}

#[derive(Debug)]
pub struct Instruction {
    direction: Direction,
    amount: usize,
}

impl FromStr for Instruction {
    type Err = ParseIntError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (direction, amount) = s.split_at(1);
        let direction = match direction {
            "R" => Direction::Right,
            "L" => Direction::Left,
            "U" => Direction::Up,
            "D" => Direction::Down,
            _ => panic!("Incorrect direction"),
        };

        let amount = amount.parse()?;

        Ok(Instruction { direction, amount })
    }
}

#[derive(Clone, Debug, PartialEq, Eq, Hash)]
struct Position {
    x: isize,
    y: isize,
}

impl Position {
    fn new() -> Self {
        Position { x: 0, y: 0 }
    }

    fn move_to(&mut self, direction: &Direction) {
        match direction {
            Direction::Right => self.x += 1,
            Direction::Left => self.x -= 1,
            Direction::Up => self.y += 1,
            Direction::Down => self.y -= 1,
        }
    }

    fn distance(&self) -> isize {
        self.x.abs() + self.y.abs()
    }
}

#[aoc(day3, part1)]
pub fn part1(instructions: &Vec<Vec<Instruction>>) -> isize {
    if instructions.len() != 2 {
        return 0;
    }

    let mut positions = HashMap::new();

    for instruction_set in instructions {
        let mut position = Position::new();
        for instruction in instruction_set {
            for _ in 0..(instruction.amount) {
                position.move_to(&instruction.direction);
                if let Some(x) = positions.insert(position.clone(), 1) {
                    positions.insert(position.clone(), x + 1);
                }
            }
        }
    }

    positions
        .into_iter()
        .filter_map(|(k, v)| if v > 1 { Some(k.distance()) } else { None })
        .min()
        .unwrap()
}

#[aoc(day3, part2)]
pub fn part2(instructions: &Vec<Vec<Instruction>>) -> isize {
    if instructions.len() != 2 {
        return 0;
    }

    let mut positions = HashMap::new();

    for instruction_set in instructions {
        let mut position = Position::new();
        let mut steps_so_far = 0;
        for instruction in instruction_set {
            for _ in 0..(instruction.amount) {
                position.move_to(&instruction.direction);
                steps_so_far += 1;
                if let Some((intersections, steps)) =
                    positions.insert(position.clone(), (1, steps_so_far))
                {
                    positions.insert(position.clone(), (intersections + 1, steps + steps_so_far));
                }
            }
        }
    }

    positions
        .into_iter()
        .filter_map(
            |(_, (intersections, steps))| if intersections > 1 { Some(steps) } else { None },
        )
        .min()
        .unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    //    #[test]
    //    fn test_part1_example1() {
    //        let instructions =
    //            parse("R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83");
    //        assert_eq!(part1(&instructions), 159)
    //    }

    #[test]
    fn test_part1_example2() {
        let instructions = parse(
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
        );
        assert_eq!(part1(&instructions), 135)
    }

    //    #[test]
    //    fn test_part2_example1() {
    //        let instructions =
    //            parse("R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83");
    //        assert_eq!(part2(&instructions), 610)
    //    }

    #[test]
    fn test_part2_example2() {
        let instructions = parse(
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
        );
        assert_eq!(part2(&instructions), 410)
    }
}

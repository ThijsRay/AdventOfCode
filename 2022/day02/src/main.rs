use std::fs::File;
use std::io::BufRead;
use std::{cmp::Ordering, io::BufReader};

#[derive(PartialEq)]
enum Shape {
    Rock,
    Paper,
    Scissors,
}

impl Shape {
    fn value(&self) -> usize {
        match self {
            Shape::Rock => 1,
            Shape::Paper => 2,
            Shape::Scissors => 3,
        }
    }

    fn score(&self, other: &Self) -> usize {
        self.value()
            + match self.partial_cmp(other).unwrap() {
                Ordering::Less => 0,
                Ordering::Equal => 3,
                Ordering::Greater => 6,
            }
    }

    fn from_char(char: Option<&str>) -> Option<Self> {
        match char? {
            "A" | "X" => Some(Self::Rock),
            "B" | "Y" => Some(Self::Paper),
            "C" | "Z" => Some(Self::Scissors),
            _ => None,
        }
    }

    fn from_opponent_and_goal(opponent: &Shape, strategy: Option<&str>) -> Option<Shape> {
        let strategy = match strategy? {
            "X" => Some(Ordering::Less),
            "Y" => Some(Ordering::Equal),
            "Z" => Some(Ordering::Greater),
            _ => None,
        }?;

        let shapes = [Shape::Rock, Shape::Paper, Shape::Scissors];
        for shape in shapes {
            if shape.partial_cmp(&opponent)? == strategy {
                return Some(shape);
            }
        }
        None
    }
}

impl PartialOrd for Shape {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        match self {
            Shape::Rock => match other {
                Shape::Rock => Some(Ordering::Equal),
                Shape::Paper => Some(Ordering::Less),
                Shape::Scissors => Some(Ordering::Greater),
            },
            Shape::Paper => match other {
                Shape::Rock => Some(Ordering::Greater),
                Shape::Paper => Some(Ordering::Equal),
                Shape::Scissors => Some(Ordering::Less),
            },
            Shape::Scissors => match other {
                Shape::Rock => Some(Ordering::Less),
                Shape::Paper => Some(Ordering::Greater),
                Shape::Scissors => Some(Ordering::Equal),
            },
        }
    }
}

fn main() {
    let filename = "input.txt";
    let f = File::open(filename).unwrap();
    let f = BufReader::new(f);
    let lines: Vec<(Shape, Shape)> = f
        .lines()
        .filter_map(|line| {
            let line = line.ok()?;
            let mut split = line.split_whitespace();
            let opponent = Shape::from_char(split.next());
            let you = Shape::from_char(split.next());
            Some((you?, opponent?))
        })
        .collect();
    println!("Part 1: {}", score(&lines));

    let f = File::open(filename).unwrap();
    let f = BufReader::new(f);
    let lines: Vec<(Shape, Shape)> = f
        .lines()
        .filter_map(|line| {
            let line = line.ok()?;
            let mut split = line.split_whitespace();
            let opponent = Shape::from_char(split.next())?;
            let you = Shape::from_opponent_and_goal(&opponent, split.next());
            Some((you?, opponent))
        })
        .collect();
    println!("Part 2: {}", score(&lines));
}

fn score(vec: &Vec<(Shape, Shape)>) -> usize {
    vec.iter().map(|(you, opponent)| you.score(opponent)).sum()
}

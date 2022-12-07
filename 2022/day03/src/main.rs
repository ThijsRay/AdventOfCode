use std::io::BufRead;
use std::{fs::File, io::BufReader};

#[derive(Debug)]
struct Rucksack(String);

impl Rucksack {
    fn split(&self) -> (&str, &str) {
        let (x, y) = self.0.split_at(self.0.len() / 2);
        assert!(x.len() == y.len());
        (x, y)
    }
}

fn main() {
    let f = File::open("input.txt").unwrap();
    let f = BufReader::new(f);

    let mut rucksacks = Vec::new();
    for line in f.lines() {
        let line = line.unwrap();

        let rucksack = Rucksack(line.to_owned());
        rucksacks.push(rucksack);
    }

    println!("Part 1: {}", part1(&rucksacks));
    println!("Part 2: {}", part2(&rucksacks));
}

fn find_matching_characters_helper(x: impl AsRef<str>, y: impl AsRef<str>) -> String {
    let mut found = String::new();
    for x in x.as_ref().chars() {
        for y in y.as_ref().chars() {
            if x == y {
                found.push(x);
            }
        }
    }
    found
}

fn find_matching_characters(samples: impl AsRef<Vec<String>>) -> Option<char> {
    let samples = samples.as_ref();
    if samples.len() < 2 {
        None
    } else {
        let mut current_equals = samples[0].clone();
        for idx in 1..samples.len() {
            current_equals = find_matching_characters_helper(&samples[idx], &current_equals);
        }
        current_equals.chars().next()
    }
}

fn priority(x: &char) -> usize {
    match x {
        'a'..='z' => (*x as usize) - 96,
        'A'..='Z' => (*x as usize) - 38,
        _ => 0,
    }
}

fn part1(rucksacks: &Vec<Rucksack>) -> usize {
    rucksacks
        .iter()
        .filter_map(|rucksack| {
            let (x, y) = rucksack.split();
            find_matching_characters(vec![x.to_owned(), y.to_owned()])
        })
        .map(|x| priority(&x))
        .sum()
}

fn part2(rucksacks: &Vec<Rucksack>) -> usize {
    rucksacks
        .chunks(3)
        .filter_map(|chunk| {
            let rucksacks: Vec<String> = chunk.iter().map(|rucksack| rucksack.0.clone()).collect();
            find_matching_characters(&rucksacks)
        })
        .map(|x| priority(&x))
        .sum()
}

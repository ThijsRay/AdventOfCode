use std::fs::File;
use std::io::{BufRead, BufReader};

fn prepare() -> Vec<usize> {
    let f = File::open("input").unwrap();
    let f = BufReader::new(f);

    let mut elves = Vec::<usize>::new();
    let mut elf = 0;

    for line in f.lines() {
        let line = line.unwrap();
        if let Ok(calories) = usize::from_str_radix(&line, 10) {
            elf += calories;
        } else {
            elves.push(elf);
            elf = 0;
        }
    }
    elves.sort();
    elves.reverse();
    elves
}

fn main() {
    let mut elves = prepare();
    println!("Star 1: {}", elves.first().unwrap());
    println!("Star 2: {}", elves.drain(..3).sum::<usize>());
}

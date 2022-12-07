use std::{
    fs::File,
    io::{BufRead, BufReader},
};

struct SectionAssignment {
    start: usize,
    end: usize,
}

impl SectionAssignment {
    fn contains(&self, other: &Self) -> bool {
        self.start <= other.start && self.end >= other.end
    }
    fn overlaps(&self, other: &Self) -> bool {
        (self.start..=self.end).contains(&other.start)
            || (self.start..=self.end).contains(&other.end)
    }
}

fn main() {
    let f = File::open("input.txt").unwrap();
    let f = BufReader::new(f);

    let mut assignments = Vec::new();

    for line in f.lines() {
        let line = line.unwrap();
        let (f, s) = line.split_once(',').unwrap();

        for x in [f, s] {
            let (start, end) = x.split_once('-').unwrap();
            let start = usize::from_str_radix(start, 10).unwrap();
            let end = usize::from_str_radix(end, 10).unwrap();
            assignments.push(SectionAssignment { start, end })
        }
    }
    println!("Part 1: {}", part1(&assignments));
    println!("Part 2: {}", part2(&assignments));
}

fn part1(assignments: &[SectionAssignment]) -> usize {
    assignments
        .chunks_exact(2)
        .map(|chunks| {
            let f = &chunks[0];
            let s = &chunks[1];

            if f.contains(&s) || s.contains(&f) {
                1
            } else {
                0
            }
        })
        .sum()
}

fn part2(assignments: &[SectionAssignment]) -> usize {
    assignments
        .chunks_exact(2)
        .map(|chunks| {
            let f = &chunks[0];
            let s = &chunks[1];

            if f.overlaps(&s) || s.overlaps(&f) {
                1
            } else {
                0
            }
        })
        .sum()
}

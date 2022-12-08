use std::{
    collections::VecDeque,
    fs::File,
    io::{BufRead, BufReader},
};

#[derive(Debug, Clone)]
struct Stacks(Vec<Vec<char>>);

fn read_stacks(f: &mut BufReader<File>) -> Option<Stacks> {
    let mut stacks_raw = Vec::new();

    for line in f.lines() {
        let line = line.ok()?;
        if line.is_empty() {
            break;
        } else {
            stacks_raw.push(line);
        }
    }

    let amount_of_stacks =
        usize::from_str_radix(stacks_raw.last()?.rsplit(' ').skip(1).next()?, 10).ok()?;

    let mut stacks = Vec::new();
    for _ in 0..amount_of_stacks {
        stacks.push(Vec::new());
    }

    for level in stacks_raw.iter().rev().skip(1) {
        let s = level.as_bytes().chunks(4);
        for (idx, item) in s.enumerate() {
            let char = item
                .iter()
                .filter(|c| match **c as char {
                    'A'..='Z' => true,
                    _ => false,
                })
                .map(|x| *x as char)
                .next();

            if let Some(char) = char {
                stacks[idx].push(char);
            }
        }
    }

    Some(Stacks(stacks))
}

#[derive(Debug)]
struct Instruction {
    amount: usize,
    from: usize,
    to: usize,
}

fn read_instructions(f: &mut BufReader<File>) -> Vec<Instruction> {
    f.lines()
        .filter_map(|line| {
            let line = line.ok()?;
            let mut words = line.split_whitespace().skip(1);

            let amount = usize::from_str_radix(words.next()?, 10).ok()?;
            words.next();
            let from = usize::from_str_radix(words.next()?, 10).ok()? - 1;
            let to = usize::from_str_radix(words.skip(1).next()?, 10).ok()? - 1;

            Some(Instruction { amount, from, to })
        })
        .collect()
}

fn main() {
    let f = File::open("input.txt").unwrap();
    let mut f = BufReader::new(f);

    let stacks = read_stacks(&mut f).unwrap();
    let instructions = read_instructions(&mut f);

    println!("Part 1: {}", part1(stacks.clone(), &instructions));
    println!("Part 2: {}", part2(stacks.clone(), &instructions));
}

fn read_top_of_stack(stacks: &Stacks) -> String {
    stacks
        .0
        .iter()
        .filter_map(|stack| stack.last())
        .fold(String::new(), |acc: String, x: &char| acc + &x.to_string())
}

fn part1(mut stacks: Stacks, instructions: &Vec<Instruction>) -> String {
    for instruction in instructions {
        for _ in 0..instruction.amount {
            if let Some(element) = stacks.0[instruction.from].pop() {
                stacks.0[instruction.to].push(element);
            }
        }
    }
    read_top_of_stack(&stacks)
}

fn part2(mut stacks: Stacks, instructions: &Vec<Instruction>) -> String {
    for instruction in instructions {
        let mut temporary = Vec::new();
        for _ in 0..instruction.amount {
            if let Some(element) = stacks.0[instruction.from].pop() {
                temporary.push(element);
            }
        }
        for _ in 0..instruction.amount {
            while let Some(element) = temporary.pop() {
                stacks.0[instruction.to].push(element);
            }
        }
    }
    read_top_of_stack(&stacks)
}

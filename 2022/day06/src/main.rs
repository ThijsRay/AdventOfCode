use std::{
    collections::{HashSet, VecDeque},
    fs::File,
    io::{BufRead, BufReader},
};

fn main() {
    let f = File::open("input.txt").unwrap();
    let mut f = BufReader::new(f);

    let mut data = String::new();
    f.read_line(&mut data);

    println!("Part 1: {}", part1(&data));
    println!("Part 2: {}", part2(&data));
}

fn part1(input: impl AsRef<str>) -> usize {
    let input = input.as_ref().as_bytes();
    for idx in 3..input.len() {
        let a = input[idx - 3];
        let b = input[idx - 2];
        let c = input[idx - 1];
        let d = input[idx];

        if d == c || d == b || d == a || c == b || c == a || b == a {
            continue;
        } else {
            return idx + 1;
        }
    }
    0
}

fn part2(input: impl AsRef<str>) -> usize {
    let input = input.as_ref().as_bytes();
    for idx in 13..input.len() {
        let mut set = HashSet::with_capacity(14);
        let mut duplicate = false;

        for i in 0..14 {
            let element = input[idx - i];
            if set.contains(&element) {
                duplicate = true;
            } else {
                set.insert(element);
            }
        }

        if !duplicate {
            return idx + 1;
        }
    }
    0
}

#[cfg(test)]
mod tests {
    use crate::{part1, part2};

    #[test]
    fn test_part1() {
        assert_eq!(part1("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5);
        assert_eq!(part1("nppdvjthqldpwncqszvftbrmjlhg"), 6);
        assert_eq!(part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 10);
        assert_eq!(part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 11);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 19);
        assert_eq!(part2("bvwbjplbgvbhsrlpgdmjqwftvncz"), 23);
        assert_eq!(part2("nppdvjthqldpwncqszvftbrmjlhg"), 23);
        assert_eq!(part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 29);
        assert_eq!(part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 26);
    }
}

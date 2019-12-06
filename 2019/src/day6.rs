use aoc_runner_derive::{aoc, aoc_generator};
use std::collections::HashMap;
use std::collections::HashSet;

type OrbitMap = HashMap<String, String>;
const CENTER_OF_MASS: &str = "COM";

#[aoc_generator(day6)]
pub fn generator(input: &str) -> OrbitMap {
    let mut orbit_map = HashMap::new();

    for line in input.lines() {
        let elements: Vec<&str> = line.split(")").collect();
        orbit_map.insert(elements[1].to_string(), elements[0].to_string());
    }

    orbit_map
}

fn orbit_len(element: &str, map: &OrbitMap) -> usize {
    orbit_list(element, CENTER_OF_MASS, map).len()
}

fn orbit_list(element: &str, dest: &str, map: &OrbitMap) -> HashSet<String> {
    let mut element = element;
    let mut list = HashSet::new();
    loop {
        if let Some(orbiting) = map.get(element) {
            list.insert(orbiting.clone());
            if orbiting == dest {
                break;
            }
            element = orbiting
        } else {
            break;
        }
    }
    list
}

#[aoc(day6, part1)]
pub fn part1(input: &OrbitMap) -> usize {
    input
        .iter()
        .map(|x| orbit_len(x.0, input))
        .fold(0, |acc, x| acc + x)
}

#[aoc(day6, part2)]
pub fn part2(input: &OrbitMap) -> usize {
    let you = orbit_list("YOU", CENTER_OF_MASS, input);
    let santa = orbit_list("SAN", CENTER_OF_MASS, input);

    let mut max_length = 0;
    let mut max_element = "YOU";
    for element in you.intersection(&santa) {
        let length = orbit_list(element, CENTER_OF_MASS, input).len();
        if length > max_length {
            max_length = length;
            max_element = element;
        }
    }

    let you_to_common = orbit_list("YOU", max_element, input).len() - 1;
    let santa_to_common = orbit_list("SAN", max_element, input).len() - 1;

    you_to_common + santa_to_common
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1_example() {
        let x = generator(
            "COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L",
        );

        assert_eq!(orbit_len("D", &x), 3);
        assert_eq!(orbit_len("L", &x), 7);
        assert_eq!(part1(&x), 42)
    }

    #[test]
    fn test_part2_example() {
        let x = generator(
            "COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN",
        );

        assert_eq!(part2(&x), 4);
    }
}

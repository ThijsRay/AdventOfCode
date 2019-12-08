use crate::day5;
use aoc_runner_derive::{aoc, aoc_generator};
use permutohedron::heap_recursive;

#[aoc_generator(day7)]
pub fn generator(input: &str) -> Vec<isize> {
    day5::generator(input)
}

#[aoc(day7, part1)]
pub fn part1(input: &Vec<isize>) -> isize {
    let mut phase_settings = [0, 1, 2, 3, 4];
    let mut permutations = Vec::new();
    heap_recursive(&mut phase_settings, |permutation| {
        permutations.push(permutation.to_vec())
    });

    permutations
        .iter()
        .map(|x| {
            let mut accumulator = 0;
            for phase_setting in x.iter() {
                accumulator = day5::intcode(vec![accumulator, *phase_setting], input.clone());
            }
            accumulator
        })
        .max()
        .unwrap()
}

#[aoc(day7, part2)]
pub fn part2(input: &Vec<isize>) -> isize {
    0
    //    let mut phase_settings = [5, 6, 7, 8, 9];
    //    let mut permutations = Vec::new();
    //    heap_recursive(&mut phase_settings, |permutation| {
    //        permutations.push(permutation.to_vec())
    //    });
    //
    //    permutations
    //        .iter()
    //        .map(|phase_setting| {
    //            let mut saved_settings = Vec::new();
    //            saved_settings.push(day5::intcode_raw(
    //                vec![0, phase_setting[0]],
    //                input.clone(),
    //                0,
    //                0,
    //            ));
    //            for i in 0..4 {
    //                saved_settings.push(day5::intcode_raw(
    //                    vec![saved_settings[i].output, phase_setting[i + 1]],
    //                    input.clone(),
    //                    0,
    //                    0,
    //                ));
    //            }
    //
    //            while None != saved_settings[4].code {
    //                for i in 0..4 {
    //                    let prev_output = saved_settings[(i + 4) % 5].output;
    //                    saved_settings[i].input.push(prev_output);
    //                    let s_input = saved_settings[i].input.clone();
    //                    let s_code = saved_settings[i].code.clone().unwrap();
    //                    let s_ip = saved_settings[i].instruction_pointer;
    //                    let s_output = saved_settings[i].output;
    //                    saved_settings[i] = day5::intcode_raw(s_input, s_code, s_ip, s_output)
    //                }
    //            }
    //            saved_settings[4].output
    //        })
    //        .max()
    //        .unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_p1_example1() {
        assert_eq!(
            part1(&generator("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0")),
            43210
        );
    }

    #[test]
    fn test_p1_example2() {
        assert_eq!(
            part1(&generator(
                "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
            )),
            54321
        );
    }

    #[test]
    fn test_p1_example3() {
        assert_eq!(
            part1(&generator("3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0")),
            65210
        );
    }

    #[test]
    fn test_p2_example1() {
        assert_eq!(
            part2(&generator("3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5")),
            139629729
        );
    }

    #[test]
    fn test_p2_example2() {
        assert_eq!(
        part2(&generator("3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10")),
            18216
        );
    }
}

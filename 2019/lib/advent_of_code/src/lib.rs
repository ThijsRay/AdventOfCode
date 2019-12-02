use std::io::BufRead;

pub fn read_stdin() -> Vec<String> {
    std::io::stdin()
        .lock()
        .lines()
        .map(|x| x.unwrap())
        .collect()
}

use std::io::BufRead;

pub fn read_stdin() -> Vec<String> {
    return std::io::stdin()
        .lock()
        .lines()
        .map(|x| x.unwrap())
        .collect();
}

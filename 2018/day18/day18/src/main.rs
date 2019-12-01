use std::fs::File;
use std::io::BufReader;
use std::io::Read;

fn main() {
    let start = read_file("/home/thijs/Projects/AdventOfCode/day18/input").unwrap();

    let mut grid = start.into_bytes();
    let mut new_grid = grid.clone();
    let line_size = 49;

    print(&grid, line_size);

    for _ in 0..100_000 {
        for y in 0..=line_size {
            for x in 0..=line_size {
                new_grid[index(line_size, x, y)] = new_state(&grid, line_size, x, y);
            }
        }

//        print(&new_grid, line_size);
        grid = new_grid.clone();

        let mut wood = 0;
        let mut lumberyard = 0;

        for x in &grid {
            match x {
                35 => {
                    lumberyard += 1
                },
                124 => {
                    wood += 1
                }
                _ => {}
            }
        }

        println!("{}*{}={}", wood, lumberyard, wood*lumberyard);
    }

    let mut wood = 0;
    let mut lumberyard = 0;

    for x in grid {
        match x {
            35 => {
                lumberyard += 1
            },
            124 => {
                wood += 1
            }
            _ => {}
        }
    }

    println!("{}*{}={}", wood, lumberyard, wood*lumberyard);

}

fn print(grid: &Vec<u8>, line_size: isize) {
    let mut gridString = String::new();
    for y in 0..=line_size {
        for x in 0..=line_size {
            gridString.push(grid[index(line_size, x, y)] as char);
        }
        gridString.push('\n');
    }
    println!("{}", gridString);
}

#[inline]
fn new_state(grid: &Vec<u8>, line_size: isize, x: isize, y: isize) -> u8 {
    let adjacent = get_adjacent(&grid, line_size, x, y);
    let current_position = get(&grid, line_size, x, y).unwrap();

    let mut trees = 0;
    let mut lumberyard = 0;

    for x in adjacent {
        match *x as char {
            '.' => open += 1,
            '|' => trees += 1,
            '#' => lumberyard += 1,
            _ => {}
        }
    }

    match *current_position as char {
        '.' => {
            if trees >= 3 {
                '|' as u8
            } else {
                '.' as u8
            }
        },
        '|' => {
            if lumberyard >= 3 {
                '#' as u8
            } else {
                '|' as u8
            }
        }
        '#' => {
            if lumberyard >= 1 && trees >= 1 {
                '#' as u8
            } else {
                '.' as u8
            }
        }
        _ => {
            0
        }
    }
}

#[inline]
fn get_adjacent(grid: &Vec<u8>, line_size: isize, x: isize, y: isize) -> Vec<&u8> {
    let mut returnVector: Vec<&u8> = Vec::new();

    if x > line_size || y > line_size {
        return returnVector;
    }

    for y_offset in -1..=1 {
        for x_offset in -1..=1 {
            if x_offset == 0 && y_offset == 0 {
                continue;
            }

            if let Some(result) = get(&grid, line_size, x + x_offset, y + y_offset) {
                returnVector.push(result);
            }
        }
    }

    returnVector
}

#[inline]
fn get(grid: &Vec<u8>, line_size: isize, x: isize, y: isize) -> Option<&u8> {
    if x < 0 || y < 0 || x > line_size || y > line_size {
        return None;
    }
    grid.get(index(line_size, x, y))
}

#[inline]
fn index(line_size: isize, x: isize, y: isize) -> usize {
    (x as usize + ((y as usize) * (line_size as usize)) + ((y * 2) as usize))
}

fn read_file(filename: &str) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let mut buf_reader = BufReader::new(file);
    let mut contents = String::new();

    buf_reader.read_to_string(&mut contents)?;
    Ok(contents)
}

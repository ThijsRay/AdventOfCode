use std::fs::File;
use std::io::BufReader;
use std::io::Read;

fn main() {
    let content = read_file("/home/thijs/Projects/AdventOfCode/day6/input").unwrap();

    let grid_dimension = 351;
    let mut grid: Vec<Vec<char>> = Vec::new();
    for _ in 1..grid_dimension {
        let mut row_vec: Vec<char> = Vec::new();
        for _ in 1..grid_dimension {
            row_vec.push('.');
        }
        grid.push(row_vec);
    }

    let mut index = 47;
    let mut coordinates: Vec<Vec<usize>> = Vec::new();
    for x in content.lines() {
        coordinates.push(add_to_grid(&mut grid, x, index));
        index += 1;
    }

    let mut y_index = 0;
    for y in &mut grid {
        for x in y  {
            let mut min_distance = 10000;
            let mut min_coordinate: Vec<usize> = Vec::new();
            for coordinate in &coordinates {
                let distance = manhattan_distance(coordinate, &char_vec_to_coordinates(&vec![*x, y]));
                if distance < min_distance {
                    min_distance = distance;
                    min_coordinate = *coordinate;
                }
                if distance == min_distance {
                    min_coordinate = vec![10000, 10000];
                    break;
                }
            }
        }
    }

}

fn char_vec_to_coordinates<T>(char_vec: &Vec<T>) -> Vec<usize> {
    let mut return_vector: Vec<usize> = Vec::new();
    return_vector.push(char_vec[0].parse::<usize>().unwrap());
    return_vector.push(char_vec[1].parse::<usize>().unwrap());

    return_vector

}

fn add_to_grid(grid: &mut Vec<Vec<char>>, line: &str, index: u8) -> Vec<usize> {
    let coordinates: Vec<&str> = line.split(", ").collect();
    let mut return_vector: Vec<usize> = char_vec_to_coordinates(&coordinates);

    grid[return_vector[1]][return_vector[0]] = char::from(index);

    return_vector
}

fn print_grid(grid: &Vec<Vec<char>>) {
    let mut output = String::new();
    for y in grid {
        for x in y  {
            output.push(*x);
        }
        output.push('\n');
    }
    println!("{}", output);
}

fn manhattan_distance(coord1: &Vec<usize>, coord2: &Vec<usize>) -> usize {
    let mut x_diff = 0;
    if let Some(x) = coord1[0].checked_sub(coord2[0]) {
        x_diff = x;
    } else if let Some(x) = coord2[0].checked_sub(coord1[0]){
        x_diff = x;
    }
    let mut y_diff = 0;
    if let Some(y) = coord1[1].checked_sub(coord2[1]) {
        y_diff = y;
    } else if let Some(y) = coord2[1].checked_sub(coord1[1]){
        y_diff = y;
    }

    x_diff + y_diff
}

fn read_file(filename: &str) -> std::io::Result<String> {
    let file = File::open(filename)?;
    let mut buf_reader = BufReader::new(file);
    let mut content = String::new();

    buf_reader.read_to_string(&mut content)?;
    Ok(content)
}

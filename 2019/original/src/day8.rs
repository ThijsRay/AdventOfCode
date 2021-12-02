use aoc_runner_derive::{aoc, aoc_generator};

pub struct Layer {
    width: usize,
    height: usize,
    pixels: Vec<usize>,
}

impl std::fmt::Display for Layer {
    fn fmt(&self, fmt: &mut std::fmt::Formatter) -> Result<(), std::fmt::Error> {
        write!(fmt, "{}", '\n')?;
        for h in 0..(self.height) {
            for w in 0..(self.width) {
                write!(fmt, "{}", self.pixels.get((h * self.width) + w).unwrap())?;
            }
            write!(fmt, "{}", '\n')?;
        }
        Ok(())
    }
}

fn chunks(input: &str, size: usize) -> Vec<String> {
    if size == 0 {
        return Vec::new();
    }

    let mut chunk_vector = Vec::with_capacity(input.len() / size);
    let mut tail = input;
    while tail.len() >= size {
        let (head, new_tail) = tail.split_at(size);
        tail = new_tail;

        chunk_vector.push(head.to_string());
    }

    chunk_vector
}

#[aoc_generator(day8)]
pub fn generator(input: &str) -> Vec<Layer> {
    let width = 25;
    let height = 6;

    let mut layers = Vec::new();
    for layer in chunks(input, width * height) {
        let pixels: Vec<usize> = layer.chars().map(|x| (x as u8 - 0x30) as usize).collect();
        layers.push(Layer {
            width,
            height,
            pixels,
        });
    }
    layers
}

fn count(input: &Vec<usize>, key: usize) -> usize {
    input
        .iter()
        .fold(0, |acc, x| if *x == key { acc + 1 } else { acc })
}

#[aoc(day8, part1)]
pub fn part1(layers: &Vec<Layer>) -> usize {
    let min = layers
        .iter()
        .map(|layer| (count(&layer.pixels, 0), layer))
        .fold((usize::max_value(), None), |acc, (zeroes, layer)| {
            if zeroes < acc.0 {
                (zeroes, Some(layer))
            } else {
                acc
            }
        })
        .1
        .unwrap();

    let ones = count(&min.pixels, 1);
    let twos = count(&min.pixels, 2);
    ones * twos
}

#[aoc(day8, part2)]
pub fn part2(layers: &Vec<Layer>) -> String {
    let size = layers[0].pixels.len();

    let mut image = Vec::with_capacity(size);
    for i in 0..size {
        for layer in layers {
            let pixel = layer.pixels[i];

            if pixel != 2 {
                image.push(pixel);
                break;
            }
        }
        if image.get(i) == None {
            image.push(2);
        }
    }

    let image = Layer {
        width: layers[0].width,
        height: layers[1].height,
        pixels: image,
    };

    image.to_string().replace("0", " ").replace("1", "█")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_chunks_zero_size() {
        let empty: Vec<String> = Vec::new();
        assert_eq!(chunks("abcde", 0), empty);
    }

    #[test]
    fn test_chunks_one_size() {
        let result: Vec<String> = vec!["a", "b", "c", "d", "e"]
            .iter()
            .map(|x| x.to_string())
            .collect();
        assert_eq!(chunks("abcde", 1), result);
    }

    #[test]
    fn test_chunks_three_size() {
        let result: Vec<String> = vec!["abc".to_string()];
        assert_eq!(chunks("abcde", 3), result);
    }

    #[test]
    fn test_chunks_six_size() {
        let result: Vec<String> = vec![];
        assert_eq!(chunks("abcde", 6), result);
    }
}

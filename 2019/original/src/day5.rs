use aoc_runner_derive::{aoc, aoc_generator};

#[aoc_generator(day5)]
pub fn generator(input: &str) -> Vec<isize> {
    input
        .lines()
        .flat_map(|x| x.split(','))
        .map(|x| x.parse::<isize>().unwrap())
        .collect()
}

#[derive(Debug)]
enum AddressingMode {
    Position,
    Immediate,
}

impl AddressingMode {
    fn from_int(number: u8) -> Self {
        match number {
            0 => Self::Position,
            1 => Self::Immediate,
            _ => panic!("Unknown addressing mode"),
        }
    }

    fn get_value(&self, code: &Vec<isize>, index: usize) -> isize {
        match self {
            Self::Position => code[code[index] as usize],
            Self::Immediate => code[index],
        }
    }

    fn set_value(&self, code: &mut Vec<isize>, index: usize, value: isize) {
        match self {
            Self::Position => {
                let location = code[index] as usize;
                code[location] = value
            }
            Self::Immediate => code[index] = value,
        }
    }
}

#[derive(Debug)]
enum InstructionType {
    Add,
    Multiply,
    Input,
    Output,
    JumpIfTrue,
    JumpIfFalse,
    LessThan,
    Equals,
    Halt,
}

impl InstructionType {
    fn from_int(number: u8) -> Self {
        match number {
            1 => Self::Add,
            2 => Self::Multiply,
            3 => Self::Input,
            4 => Self::Output,
            5 => Self::JumpIfTrue,
            6 => Self::JumpIfFalse,
            7 => Self::LessThan,
            8 => Self::Equals,
            99 => Self::Halt,
            _ => panic!("Unknown instruction"),
        }
    }

    fn width(&self) -> usize {
        match self {
            Self::Add => 3,
            Self::Multiply => 3,
            Self::Input => 1,
            Self::Output => 1,
            Self::JumpIfTrue => 2,
            Self::JumpIfFalse => 2,
            Self::LessThan => 3,
            Self::Equals => 3,
            Self::Halt => 0,
        }
    }
}

#[derive(Debug)]
struct Instruction {
    instruction: InstructionType,
    addressing: Vec<AddressingMode>,
}

impl Instruction {
    fn from_int(number: isize) -> Self {
        let mut bytes = number.to_string().into_bytes();
        bytes.reverse();
        bytes.resize(5, 0x30);
        bytes.reverse();

        // Character values of 0,1,2,3,... in ASCII - 0x30 are the values 0,1,2,3,...
        let numbers: Vec<u8> = bytes.iter().map(|x| *x - 0x30).collect();

        let instruction = InstructionType::from_int((numbers[3] * 10) + numbers[4]);
        let mut addressing: Vec<AddressingMode> = numbers[..3]
            .iter()
            .map(|x| AddressingMode::from_int(*x))
            .collect();
        addressing.reverse();

        Instruction {
            instruction,
            addressing,
        }
    }
}

#[aoc(day5, part1)]
pub fn part1(input: &Vec<isize>) -> isize {
    let input = input.clone();
    intcode(vec![1], input)
}

#[aoc(day5, part2)]
pub fn part2(input: &Vec<isize>) -> isize {
    let input = input.clone();
    intcode(vec![5], input)
}

pub struct Intcode {
    pub code: Option<Vec<isize>>,
    pub input: Vec<isize>,
    pub output: isize,
    pub instruction_pointer: usize,
}

pub fn intcode_raw(
    mut input: Vec<isize>,
    mut code: Vec<isize>,
    ip: usize,
    last_output: isize,
) -> Intcode {
    let mut output = last_output;
    let mut i: usize = ip;
    loop {
        if i >= code.len() {
            break;
        }

        let instr = Instruction::from_int(code[i]);

        i += 1;

        macro_rules! get_value {
            ( $x:expr ) => {
                instr.addressing[$x].get_value(&code, i + $x)
            };
        }

        macro_rules! set_value {
            ( $x:expr, $value:expr ) => {
                instr.addressing[$x].set_value(&mut code, i + $x, $value)
            };
        }

        match instr.instruction {
            InstructionType::Add => {
                let x = get_value!(0);
                let y = get_value!(1);
                let value = x + y;

                set_value!(2, value)
            }
            InstructionType::Multiply => {
                let x = get_value!(0);
                let y = get_value!(1);
                let value = x * y;

                set_value!(2, value)
            }
            InstructionType::Input => set_value!(0, input.pop().unwrap()),
            InstructionType::Output => {
                output = get_value!(0);
                return Intcode {
                    code: Some(code),
                    input,
                    output,
                    instruction_pointer: i + instr.instruction.width(),
                };
            }
            InstructionType::JumpIfTrue => {
                if get_value!(0) != 0 {
                    let new_ip = get_value!(1);
                    i = new_ip as usize;
                    continue;
                }
            }
            InstructionType::JumpIfFalse => {
                if get_value!(0) == 0 {
                    let new_ip = get_value!(1);
                    i = new_ip as usize;
                    continue;
                }
            }
            InstructionType::LessThan => {
                let mut value = 0;
                let first = get_value!(0);
                let second = get_value!(1);
                if first < second {
                    value = 1
                }
                set_value!(2, value)
            }
            InstructionType::Equals => {
                let mut value = 0;
                let first = get_value!(0);
                let second = get_value!(1);
                if first == second {
                    value = 1
                }
                set_value!(2, value)
            }
            InstructionType::Halt => {
                return Intcode {
                    code: None,
                    input,
                    output,
                    instruction_pointer: i + instr.instruction.width(),
                }
            }
        };
        i += instr.instruction.width();
    }
    Intcode {
        code: None,
        input,
        output,
        instruction_pointer: i,
    }
}

pub fn intcode(input: Vec<isize>, code: Vec<isize>) -> isize {
    let mut x = intcode_raw(input, code, 0, 0);
    while let Some(code) = x.code {
        x = intcode_raw(x.input, code, x.instruction_pointer, x.output);
    }
    x.output
}

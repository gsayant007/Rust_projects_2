// use ferris_says::say;
// use std::io::{self, BufWriter};
mod formatted_print;
pub use crate::formatted_print::add;
pub use crate::formatted_print::format_print;
mod guessing_game;
use crate::guessing_game::guess_func;

pub fn main() {
    println!("hello world!");
    println!("I am a fellow Rustacean!");
    let x = 5;
    println!("the value of x= {}",x);
    add(2, 3);
    format_print();
    guess_func();
}

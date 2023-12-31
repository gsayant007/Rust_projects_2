// use ferris_says::say;
// use std::io::{self, BufWriter};
mod formatted_print;
pub use crate::formatted_print::add;
pub use crate::formatted_print::format_print;
mod guessing_game;
// use crate::guessing_game::guess_func;
mod flow_of_control;
use crate::flow_of_control::{if_else,break_continue,return_from_loops};
mod reading_file;
use crate::reading_file::read_file;
mod todo_app;
mod read_env_args;
use read_env_args::read_env_args_func;
mod handling_command_line_arguments;
use handling_command_line_arguments::handling_env_cmd;

pub fn main() {
    println!("hello world!");
    println!("I am a fellow Rustacean!");
    let x = 5;
    println!("the value of x= {}",x);
    add(2, 3);
    format_print();
    // guess_func();
    println!("{}",if_else());
    break_continue();
    println!("{:?}",return_from_loops());
    read_file();
    read_env_args_func();
    handling_env_cmd();
}

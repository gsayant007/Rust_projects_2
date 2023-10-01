// use std::{io, cmp::Ordering};
use rand::{self, Rng};
use std::io;

pub fn guess_func(){
    let secret_number = rand::thread_rng().gen_range(0..10);  // to generate random numbers in between 0-10
    let number_of_chances:i32 = 5;
    println!("the secret number is {}",secret_number);
    println!("hello! welcome to the guessing game!");
    println!("please input your guess!");
    // let mut guess = String::new();
    // io::stdin().read_line(&mut guess).expect("Failed to read line");

    // let guess: u32 = guess.trim().parse().expect("Please type a number!");

    // match guess.cmp(&secret_number) {
    //     Ordering::Less => println!("Too small!"),
    //     Ordering::Greater => println!("Too big!"),
    //     Ordering::Equal => println!("You win!"),
    //     }
    let mut t: i32 = 0;
    while t < number_of_chances {
        let mut guess = String::new();
        io::stdin().read_line(&mut guess).expect("Failed to read line");
    
        let guess: u32 = guess.trim().parse().expect("Please type a number!");
    }
    if guess == secret_number {
        
    }
}
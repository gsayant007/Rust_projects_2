use rand::Rng;
// use std::cmp::Ordering;
use std::io;
// pub fn guess_func(){
//     let secret_number = rand::thread_rng().gen_range(0..10);  // to generate random numbers in between 0-10
//     // let number_of_chances:i32 = 5;
//     println!("hello! welcome to the guessing game!");
//     loop {
//         println!("please input your guess!");
//         let mut guess = String::new();
//         io::stdin().read_line(&mut guess).expect("Failed to read line");
    
//         let guess: u32 = guess.trim().parse().expect("Please type a number!");
    
//         match guess.cmp(&secret_number) {
//             Ordering::Less => println!("Too small!"),
//             Ordering::Greater => println!("Too big!"),
//             Ordering::Equal => {
//                 println!("You win!");
//                 break;
//             }
//             }
//     }
// }

pub fn guess_func() {
    let secret_number = rand::thread_rng().gen_range(1..10);
    let mut cnt = 0;
    let number_of_chances = 5;
    while cnt < number_of_chances{
        let mut guess = String::new();
        io::stdin().read_line(&mut guess).expect("Failed to read line");
    
        let guess: u32 = guess.trim().parse().expect("Please type a number!");
        if guess == secret_number {
            println!("you win! you guessed at {} guesses and the secret number was {}",cnt,secret_number);
            break;
        }
        else if guess > secret_number {
            println!("too big!");
        }
        else if guess < secret_number{
            println!("too low!");
        }
        cnt = cnt+1;
        if cnt == number_of_chances {
            println!("try again later! the secret number was {}",secret_number);
        }
    }
}
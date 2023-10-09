// pub fn if_else(){
//     let n = 5;
//     if n < 0 {
//         println!("{} is negative", n);
//     } else if n > 0 {
//         println!("{} is positive", n);
//     } else {
//         println!("{} is zero", n);
//     }
//     let big_n =
//     if n < 10 && n > -10 {
//         println!(", and is a small number, increase ten-fold");

//         // This expression returns an `i32`.
//         10 * n
//     } else {
//         println!(", and is a big number, halve the number");

//         // This expression must return an `i32` as well.
//         n / 2
//         // TODO ^ Try suppressing this expression with a semicolon.
//     };
// //   ^ Don't forget to put a semicolon here! All `let` bindings need it.

// println!("{} -> {}", n, big_n);
// }

// pub fn if_else()->&'static str {
//     if 1 > 2 {
//         return "hello!";
//     }
//     else {
//         return "hi!";
//     }
// }

pub fn if_else()->&'static str{
    if 1 > 2 {
        "hello!"
    }
    else {
        "hi!"
    }
}

pub fn break_continue() {
    let mut count = 0u32;
    println!("Let's count until infinity!");
    loop {
        count = count+1;
        if count == 3 {
            println!("here we skip!");
            continue;
        }
        println!("{}",count);

        if count == 5 {
            println!("ok, that's enough!");
            break;
        }
    }
}

pub fn return_from_loops() {
    let mut cnt = 0;
    let result = loop {
        cnt = cnt + 1;
        if cnt == 10{
            break cnt*2;
        }
    };
    assert_eq!(result,20);
}
// use ferris_says::say;
// use std::io::{self, BufWriter};

fn add(a:i32,b:i32)->(i32,i32,i32){
    return (a+b,a-b,a*b);
}

fn fib(n:i32)->i32{
    let mut k = 1;
    for i in 1..n+1{
        k = k*i;
    }
    return k;
}
fn main() {
    println!("{}",add(2,3));
    println!("{}",fib(5));
}

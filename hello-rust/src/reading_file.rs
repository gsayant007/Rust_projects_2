use std::fs;

pub fn read_file(){
    let file_path = "../poem.txt";
    let contents = fs::read_to_string(&file_path).expect("Should have been able to read the file");
    println!("{}",contents);
    // println!("{}",contents[0..0]);
}
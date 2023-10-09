use std::collections::HashMap;

struct Todo{
    // use rust built in HashMap to store key - val pairs
    map : HashMap<String,bool>,
}

impl Todo {
        fn insert(&mut self,key:String){
        // insert a new item into our map.
        // we pass true as value
        self.map.insert(key, true);

impl Todo {
    fn save(self) -> Result<(), std::io::Error> {
        let mut content = String::new();
        for (k, v) in self.map {
            let mut record = format!("{}\t{}\n", k, v);
            content.push_str(&record);
        }
        std::fs::write("db.txt", content)
    }
}
        // Two very important piece of information:
        // mut [doc] makes a variable mutable.
        // In Rust every variable is immutable by default. If you want to update a value, you need to opt-in mutability using the mut keyword. Since with our function we are effectively changing our map by adding a new value, we need it to be declared as mutable.

        // & [doc] indicates a reference.
        // You can imagine the varaible as a pointer to the memory location where the value is stored, rather the being the "value" itself.

        // In Rust terms this is referred to as a borrow, meaning that the function doesn't actually own this value, but it's merely pointing to the location where it's stored.

        // A Brief Overview of Rust's Ownership System
        // With the previous hint about borrow and reference, it's now a good time to briefly talk about ownership.

        // Ownership is Rust's most unique feature. It enables Rust programmers to write programs without needing to manually allocate memory (like in C/C++) while still being able to run without a Garbage Collector (like in JavaScript or Python) that constantly looks at the program's memory to free resources not in use.

        // The ownership system has three rules:

        // Each value in Rust has a variable: its owner.
        // There can only be one owner at a time for each value.
        // When the owner goes out of scope, the value will be dropped.



        }
}
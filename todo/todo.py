import datetime
import sys
import json

# def say_hi():
#     print("hello world!")

# def add(x:float,y:float):
#     print(x+y)

class Todo:
    def printHelp(self):
        sa = """Usage :-
        $ ./todo add "todo item"  # Add a new todo
        $ ./todo ls               # Show remaining todos
        $ ./todo del NUMBER       # Delete a todo
        $ ./todo done NUMBER      # Complete a todo
        $ ./todo help             # Show usage
        $ ./todo report           # Statistics"""
        sys.stdout.buffer.write(sa.encode('utf-8'))

        
    def add(self):
        """Add a new todo
        it will only add if you add a new unique task otherwise if the same task alrady exists in the file it will 
        pass the add process, currently we will do it without parsing"""
        self.printHelp()
        usr_input = sys.argv[2]
        with open("todo.txt","r+") as f:
            data = f.read().splitlines()
        if usr_input not in data:
            with open("todo.txt","a+") as f:
                f.write(usr_input)
                f.write("\n")
            return self.ls()
        else:
            return self.ls()
        
    def ls(self):
        """Show remaining todos"""
        print("you have these todos' in your list:")
        with open("todo.txt","r+") as f:
             print(f.read())


    def done(self):
        """NUMBER , Complete a todo"""
        usr_input = sys.argv[2]
        with open("todo.txt","r") as f:
            data = f.read().splitlines()
        if usr_input in data:
            print("you have completed a task!")
            print("deleting the task from todo list")
            self.delete_item()
        else:
            print("the task that you have entered is not in the todo list, please verify!")

    def delete_item(self):
        """NUMBER ,  Delete a todo
        this function will only be called if an user completes a task"""
        usr_input = sys.argv[2]
        with open("todo.txt","r+") as f:
            data = set(f.read().splitlines())
        data = data - {usr_input}
        with open("todo.txt","w+") as f:
            f.write()


#     def report(self):
#         """statistics"""

if __name__ == "__main__":
    t = Todo()
    if sys.argv.__len__() == 1: # this indicates user doesn't give any commands for the app
        t.printHelp()
    elif sys.argv[1] == "help":
        t.printHelp()
    else:
        sys.stdout.buffer.write('Too Many Arguments for help! Please use "./todo help" for Usage Information'.encode('utf-8'))

    if sys.argv[1] == "add":
        t.add()
    else:
        sys.stdout.buffer.write('Too Many Arguments for help! Please use "./todo help" for Usage Information'.encode('utf-8'))

    if sys.argv[1] == "done":
        t.done()

    

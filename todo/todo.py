import datetime
import sys
import json

class Todo:

    def help(self):
        sa = """Usage :-
        $ ./todo add "todo item"  # Add a new todo
        $ ./todo ls               # Show remaining todos
        $ ./todo del NUMBER       # Delete a todo
        $ ./todo done NUMBER      # Complete a todo
        $ ./todo help             # Show usage
        $ ./todo report           # Statistics"""
        sys.stdout.buffer.write(sa.encode('utf8'))

    def parse_input(self,s:str)->str:
        """this will parse the input from any format to a particular
        format from the user, some limited parsing is allowed for now"""
        return s.strip().replace(" ","").replace("  ","")
    
    def current_task(self):
        """this shows the current task that is in todo.txt"""

    def add(self,s:str):
        """we will add it to todo.txt if it doesn't exist in the file else pass"""
        with open("./todo/todo.txt","r+",encoding="utf-8") as f:
            data = set(f.read().splitlines())  # unique set of todos
            data1 = dict(enumerate(data))
            print(data1)
            if s not in data:
                f.write(s)
                f.write("\n")
                print("task added!")
            else: pass
        return data1
    
    def del_item(self):
        """delete the todo item from the list"""
        with open("./todo/todo.txt","r+") as f:
            data = set(f.read().splitlines())
        if self.done():
            usr_input = str(input("Enter the task name you've completed:  "))
            s1 = data - {self.parse_input(usr_input)}
            with open("./todo/todo.txt","r+") as f:
                f.truncate(0)
                for x in s1:
                    f.write(x)
                    f.write("\n")
        else:pass

    def done(self) -> bool:
        """add the todo item from todo.txt to done.txt
        and simultaneously delete the todo item from todo.txt"""
        print("have you completed any of the previous task?")
        usr_input = str(input("type y or n for yes or no respectively:  "))
        if usr_input == "y":
            return True
        else:
            return False
            
if __name__ == "__main__":
    user_inp = str(input("enter some task:  "))
    t = Todo()
    parse_inp = t.parse_input(s=user_inp)
    print(parse_inp)
    t.add(s=parse_inp)
    t.del_item()
# Imports Node class from node.py
from node import Node

# Initializes the Stack class
class Stack:
    def __init__(self):
        self.top = None

    # Adds an action to the top of the stack
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    # Removes and returns the most recent action from the stack
    def pop(self):
        if not self.top:
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node.value

    # Returns the most recent action without removing it from the stack
    def peek(self):
        if self.top:
            return self.top.value
        else:
            return None

    # Prints all actions currently in the stack
    def print_stack(self):
        current = self.top
        if not current:
            print("Stack is empty")
            return
        while current:
            print(f"- {current.value}")
            current = current.next

# Runs the interactive undo/redo manager
def run_undo_redo():
    # Creates separate stacks to store undo and redo actions
    undo_stack = Stack()
    redo_stack = Stack()


    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        # Perform an action
        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            undo_stack.push(action)
            redo_stack = Stack()

            print(f"Action performed: {action}.")

        # Undo an action
        elif choice == "2":
            action = undo_stack.pop()

            if action:
                redo_stack.push(action)
                print(f"{action} has been undone.")

            else:
                print("No actions to undo.")

        # Redo an action
        elif choice == "3":
            action = redo_stack.pop()

            if action:
                undo_stack.push(action)
                print(f"{action} has been redone.")

            else:
                print("No actions to redo.")

        # Print the undo stack
        elif choice == "4":
            print("\nUndo Stack:")
            undo_stack.print_stack()
            
        # Print the redo stack
        elif choice == "5":
            print("\nRedo Stack:")
            redo_stack.print_stack()
            
        # Exit the Undo/Redo Manager      
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()


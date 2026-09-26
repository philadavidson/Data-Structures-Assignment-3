# Imports the Node class from node.py
from node import Node

# Initializes the Queue class
class Queue:
    def __init__(self):
       self.front = None
       self.rear = None

    # Adds a customer to the end of the queue
    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Removes and returns the customer at the front of the queue
    def dequeue(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next

        if not self.front:
            self.rear = None 
        return removed_node.value

    # Returns the first customer in line without removing them
    def peek(self):
        if self.front:
            return self.front.value
        else:
            return None

    # Prints the current customer queue
    def print_queue(self):
        current = self.front
        if not current:
            print("Queue is empty")
            return
        while current:
            print(f"- {current.value}")
            current = current.next


# Runs the interactive help desk queue
def run_help_desk():
    # Creates an instance of the Queue class
    queue = Queue()
    

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        # Adds a customer
        if choice == "1":
            name = input("Enter customer name: ")
            queue.enqueue(name)
            
            print(f"{name} added to the queue.")
        
        # Removes and returns the customer at the front of the queue
        elif choice == "2":
            name = queue.dequeue()
            if name:
                print(f"{name} has been helped.")
            else:
                print("No customers are waiting.")

        # Views the first customer without removing them from the queue
        elif choice == "3":
            name = queue.peek()
            if name:
                print(f"{name} is next in line.")
            else:
                print("No customers are waiting.")

        # Print all customers in the queue
        elif choice == "4":
            print("\nWaiting customers:")
            queue.print_queue()
            
        # Exits the help desk queue
        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()

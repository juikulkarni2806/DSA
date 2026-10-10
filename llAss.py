class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List (Append node to the end)
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # 2. Traverse and print the node values
    def traverse(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "List is empty")

    # 3. Insert node at a specific position (0-indexed)
    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next
            
        if current is None:
            print("Position out of bounds")
            return
            
        new_node.next = current.next
        current.next = new_node

    # 4. Find Middle node and print its value
    def print_middle(self):
        if not self.head:
            print("List is empty")
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(f"Middle node value: {slow.data}")

    # 5. Delete node by value
    def delete_node(self, key):
        current = self.head
        
        # If head node itself holds the key to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If key was not present in linked list
        if current is None:
            print(f"Value {key} not found")
            return

        prev.next = current.next
        current = None

    # 6. Reverse list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 7. Calculate the sum of every two consecutive node values
    def print_consecutive_sums(self):
        if not self.head or not self.head.next:
            print("Not enough nodes to calculate consecutive sums")
            return
        
        current = self.head
        sums = []
        while current and current.next:
            consecutive_sum = current.data + current.next.data
            sums.append(str(consecutive_sum))
            current = current.next  # Moves to the next node for overlapping pairs
            
        print("Consecutive sums: " + ", ".join(sums))


# --- Full Execution Demonstration ---
if __name__ == "__main__":
    ll = SinglyLinkedList()
    
    # Complete sample data to fix the input loop error
    input_values = [10, 20, 30, 40, 50]
    
    # Operation 1 & 2: Create (Append) and Traverse
    print("Operations 1 & 2: Create & Traverse")
    for val in input_values:
        ll.append(val)
    print("Initial List:")
    ll.traverse() 
    
    # Operation 3: Insert at position
    print("\nOperation 3: Insert at Position 2")
    print("Inserting 25 at position 2:")
    ll.insert_at_position(25, 2)
    ll.traverse() 
    
    # Operation 4: Find Middle node
    print("\nOperation 4: Find Middle")
    ll.print_middle() 
    
    # Operation 5: Delete node by value
    print("\n Operation 5: Delete Node")
    print("Deleting node with value 25:")
    ll.delete_node(25)
    ll.traverse()
    
     # Operation 6: Reverse the linked list
    print("\n Operation 6: Reverse List")
    print("Reversing the list:")
    ll.reverse()
    ll.traverse() 
    
    # Operation 7: Calculate consecutive sums
    print("\nOperation 7: Consecutive Sums ")
    ll.print_consecutive_sums()
    
    

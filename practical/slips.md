# Python Programming Slips Solutions



---

## Slip 1

### Q1) Programs for understanding Data Types, Control Flow, Blocks, and Loops.
**A) Data Type**
**B) Control Flow Statement**

```python
def data_types_and_control_flow():
    print("--- Part A: Data Types ---")
    # Numeric
    num_int = 10
    num_float = 10.5
    print(f"Integer: {num_int}, Type: {type(num_int)}")
    print(f"Float: {num_float}, Type: {type(num_float)}")

    # Sequence
    my_str = "Hello Python"
    my_list = [1, 2, 3, "Apple"]
    my_tuple = (10, 20, 30)
    print(f"String: {my_str}")
    print(f"List: {my_list}")
    print(f"Tuple: {my_tuple}")

    # Mapping
    my_dict = {"name": "Alice", "age": 25}
    print(f"Dictionary: {my_dict}")

    print("\n--- Part B: Control Flow Statements ---")
    
    # If-Else (Conditional)
    x = 15
    if x > 10:
        print(f"{x} is greater than 10")
    elif x == 10:
        print(f"{x} is equal to 10")
    else:
        print(f"{x} is less than 10")

    # For Loop
    print("For Loop (Iterating over list):")
    for item in my_list:
        print(item, end=" ")
    print()

    # While Loop
    print("While Loop (Count down):")
    count = 3
    while count > 0:
        print(count)
        count -= 1

if __name__ == "__main__":
    data_types_and_control_flow()
```

### Q2) Write a program to demonstrate singly linked list with following operations Create, Insert, Delete, Display, Reverse.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Inserts at the end"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(f"Inserted {data}")

    def delete(self, key):
        """Deletes the first occurrence of key"""
        temp = self.head
        
        # If head holds the key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                print(f"Deleted {key}")
                return

        # Search for key
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            print("Key not found")
            return

        prev.next = temp.next
        temp = None
        print(f"Deleted {key}")

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("List Reversed")

    def display(self):
        temp = self.head
        if not temp:
            print("List is empty")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Driver Code
sll = SinglyLinkedList()
sll.insert(10)
sll.insert(20)
sll.insert(30)
sll.display()

sll.delete(20)
sll.display()

sll.reverse()
sll.display()
```

---

## Slip 2

### Q1) Programs for understanding functions, use of built in functions, user defined functions
**A) Built in Function**
**B) User Defined**

```python
# Program to demonstrate Functions

# Part A: Built-in Functions
def demonstrate_builtin():
    print("--- Built-in Functions ---")
    nums = [10, 50, 20, 5]
    print(f"Original list: {nums}")
    print(f"Max: {max(nums)}")
    print(f"Min: {min(nums)}")
    print(f"Length: {len(nums)}")
    print(f"Sorted: {sorted(nums)}")
    print(f"Sum: {sum(nums)}")

# Part B: User Defined Functions
def calculate_area(length, width):
    """User defined function to calculate area of rectangle"""
    return length * width

# Driver Code
if __name__ == "__main__":
    demonstrate_builtin()
    
    print("\n--- User Defined Function ---")
    l = 5
    w = 3
    area = calculate_area(l, w)
    print(f"Area of rectangle ({l}x{w}) is: {area}")
```

### Q2) Write a program to implement linear search.

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i # Return index if found
    return -1 # Return -1 if not found

# Driver Code
data = [10, 50, 30, 70, 80, 20]
key = int(input("Enter number to search: "))

index = linear_search(data, key)

if index != -1:
    print(f"Element {key} found at index {index}.")
else:
    print(f"Element {key} not found.")
```

---

## Slip 3

### Q1) Programs for implementations of all object-oriented concepts like class, method, inheritance, polymorphism etc.
**A) Class and method**
**B) Inheritance**
**C) Polymorphism**

```python
# 1. Class and Method (Real life: Car)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def drive(self):
        print(f"Driving the {self.brand} {self.model}")

# 2. Inheritance (Real life: Animal -> Dog)
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Dog barks")

# 3. Polymorphism (Real life: Different objects reacting to same method)
class Bird:
    def fly(self):
        print("Bird can fly")

class Airplane:
    def fly(self):
        print("Airplane can fly mechanically")

def lets_fly(obj):
    obj.fly()

# Driver Code
print("--- Class and Method ---")
my_car = Car("Toyota", "Corolla")
my_car.drive()

print("\n--- Inheritance & Polymorphism ---")
animal = Animal()
dog = Dog()
animal.speak()
dog.speak()  # Overridden method

print("\n--- Polymorphism Function ---")
sparrow = Bird()
boeing = Airplane()
lets_fly(sparrow)
lets_fly(boeing)
```

### Q2) Write a program to find transpose of matrix.

```python
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create empty matrix for result
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
            
    return result

# Driver Code
A = [
    [1, 2, 3],
    [4, 5, 6]
]

print("Original Matrix:")
for row in A:
    print(row)

T = transpose_matrix(A)

print("\nTranspose Matrix:")
for row in T:
    print(row)
```

---

## Slip 4

### Q1) Programs covering all the aspects of Exception handling, user defined exception, Multithreading should be covered.
**A) Built in Exception**
**B) User defined exception**
**C) Multithreading**

```python
import threading
import time

# A) Built-in Exception
def divide_numbers(a, b):
    try:
        res = a / b
        print(f"Result: {res}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

# B) User Defined Exception
class TooYoungError(Exception):
    pass

def check_age(age):
    try:
        if age < 18:
            raise TooYoungError("Age is less than 18, access denied.")
        else:
            print("Access granted.")
    except TooYoungError as e:
        print(f"Custom Exception: {e}")

# C) Multithreading
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(0.5)

def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        print(f"Letter: {letter}")
        time.sleep(0.5)

# Driver Code
if __name__ == "__main__":
    print("--- Built-in Exception ---")
    divide_numbers(10, 0)

    print("\n--- User Defined Exception ---")
    check_age(15)

    print("\n--- Multithreading ---")
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    print("Done")
```

### Q2) Write a python program for Merge sort.

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merging temp arrays
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Driver Code
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)
```

---

## Slip 5

### Q1) Program for performing CRUD operation with MongoDB and Python
**A) Create**
**B) Read**
**C) Update**
**D) Delete**

```python
import pymongo

# Connect to MongoDB (Default localhost)
# NOTE: Ensure MongoDB service is running
try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["test_database"]
    collection = db["students"]

    # A) Create (Insert)
    student1 = {"name": "John", "age": 21, "city": "New York"}
    collection.insert_one(student1)
    print("Document Inserted")

    # B) Read (Find)
    print("Reading Data:")
    for x in collection.find({"name": "John"}):
        print(x)

    # C) Update
    query = {"name": "John"}
    new_values = {"$set": {"age": 22}}
    collection.update_one(query, new_values)
    print("Document Updated")

    # D) Delete
    collection.delete_one({"name": "John"})
    print("Document Deleted")

except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
```

### Q2) Write a python program for Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Driver Code
data = [64, 34, 25, 12, 22, 11, 90]
print("Original:", data)
bubble_sort(data)
print("Sorted:", data)
```

---

## Slip 6

### Q1) Programs covering all the aspects of Exception handling, user defined exception, Multithreading should be covered.
*(Same as Slip 4 Q1 - Refer to Slip 4 for code)*

### Q2) Write a python program to implement a circular singly linked list.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Head)")

# Driver Code
cll = CircularLinkedList()
cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.display()
```

---

## Slip 7

### Q1) Programs for implementations of all object-oriented concepts like class, method, inheritance, polymorphism etc.
*(Same as Slip 3 Q1 - Refer to Slip 3 for code)*

### Q2) Write a program to convert infix expression to postfix expression.

```python
def is_operand(char):
    return char.isalnum()

def precedence(char):
    if char == '^': return 3
    if char in ('*', '/'): return 2
    if char in ('+', '-'): return 1
    return 0

def infix_to_postfix(expression):
    stack = []
    output = []
    
    for char in expression:
        if is_operand(char):
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop() # Pop '('
        else: # Operator
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)
            
    while stack:
        output.append(stack.pop())
        
    return "".join(output)

# Driver Code
exp = "a+b*(c^d-e)^f+g*h-i"
print(f"Infix: {exp}")
print(f"Postfix: {infix_to_postfix(exp)}")
```

---

## Slip 8

### Q1) Write a class with following criteria: class name: Flower, objects :lily,rose,hibiscus properties: price: colour smell , methods:get(),display()

```python
class Flower:
    def __init__(self, name, price, color, smell):
        self.name = name
        self.price = price
        self.color = color
        self.smell = smell
    
    def get(self):
        # In a real scenario, this might take user input. 
        # Here we just acknowledge data is set via constructor.
        pass 

    def display(self):
        print(f"Flower: {self.name}")
        print(f"  Price: {self.price}")
        print(f"  Color: {self.color}")
        print(f"  Smell: {self.smell}")
        print("-" * 20)

# Creating Objects
lily = Flower("Lily", 50, "White", "Sweet")
rose = Flower("Rose", 20, "Red", "Romantic")
hibiscus = Flower("Hibiscus", 10, "Red", "Mild")

# Displaying
lily.display()
rose.display()
hibiscus.display()
```

### Q2) Write a python program for implementation of queue using linked list.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"Enqueued {data}")

    def dequeue(self):
        if self.front is None:
            print("Queue Empty")
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        print(f"Dequeued {temp.data}")

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Driver Code
q = QueueLL()
q.enqueue(10)
q.enqueue(20)
q.display()
q.dequeue()
q.display()
```

---

## Slip 9

### Q1) Program for performing CRUD operation with MongoDB and Python
*(Same as Slip 5 Q1 - Refer to Slip 5 for code)*

### Q2) Write a python program to accept vertices and edges for a graph and represent it as adjacency list.

```python
def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    
    graph[u].append(v)
    graph[v].append(u) # For undirected graph

def display_graph(graph):
    for vertex in graph:
        print(f"{vertex} -> {graph[vertex]}")

# Driver Code
graph = {}
# Accepting simplistic hardcoded input for demo
print("Adding edges (A-B), (A-C), (B-D)")
add_edge(graph, 'A', 'B')
add_edge(graph, 'A', 'C')
add_edge(graph, 'B', 'D')

print("\nAdjacency List Representation:")
display_graph(graph)
```

---

## Slip 10

### Q1) Programs for understanding functions, use of built in functions, user defined functions
*(Same as Slip 2 Q1 - Refer to Slip 2 for code)*

### Q2) Write a program to implement Circular Queue using linked list with INSERT, DELETE and DISPLAY operations

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.front:
            self.front = new_node
        else:
            self.rear.next = new_node
        
        self.rear = new_node
        self.rear.next = self.front # Link rear back to front
        print(f"Inserted {data}")

    def dequeue(self):
        if not self.front:
            print("Queue Underflow")
            return
        
        if self.front == self.rear: # Only one element
            value = self.front.data
            self.front = None
            self.rear = None
        else:
            value = self.front.data
            self.front = self.front.next
            self.rear.next = self.front
            
        print(f"Deleted {value}")

    def display(self):
        if not self.front:
            print("Queue Empty")
            return
        temp = self.front
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.front:
                break
        print("(Back to Front)")

# Driver
cq = CircularQueue()
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()
cq.dequeue()
cq.display()
```

---

## Slip 11

### Q1) Programs for understanding functions, use of built in functions, user defined functions
*(Same as Slip 2 Q1 - Refer to Slip 2 for code)*

### Q2) Write a python program for Bubble Sort.
*(Same as Slip 5 Q2 - Refer to Slip 5 for code)*

---

## Slip 12

### Q1) Programs for understanding the data types, control flow statements, blocks and loops.
*(Same as Slip 1 Q1 - Refer to Slip 1 for code)*

### Q2) Write a python program for Quick Sort.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        # Elements less than pivot
        less = [x for x in arr[1:] if x <= pivot]
        # Elements greater than pivot
        greater = [x for x in arr[1:] if x > pivot]
        
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Driver Code
arr = [10, 7, 8, 9, 1, 5]
print("Original:", arr)
sorted_arr = quick_sort(arr)
print("Sorted:", sorted_arr)
```

---

## Slip 13

### Q1) Programs for understanding the data types, control flow statements, blocks and loops.
*(Same as Slip 1 Q1 - Refer to Slip 1 for code)*

### Q2) Write a recursive python program for Binary Search.

```python
def binary_search_recursive(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_recursive(arr, low, mid - 1, target)
        else:
            return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return -1

# Driver Code
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search_recursive(arr, 0, len(arr)-1, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
```

---

## Slip 14

### Q1) Write a class with following criteria: Flower...
*(Same as Slip 8 Q1 - Refer to Slip 8 for code)*

### Q2) Write a program in python to convert matrix to sparse matrix.

```python
def convert_to_sparse(matrix):
    sparse_matrix = []
    # Header: Row, Col, Value
    print("Row\tCol\tValue")
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != 0:
                sparse_matrix.append([r, c, matrix[r][c]])
                print(f"{r}\t{c}\t{matrix[r][c]}")
    return sparse_matrix

# Driver Code
matrix = [
    [0, 0, 3],
    [0, 5, 0],
    [9, 0, 0]
]
print("Sparse Matrix representation (Non-zero elements):")
sm = convert_to_sparse(matrix)
```

---

## Slip 15

### Q1) Programs for understanding the data types, control flow statements, blocks and loops.
*(Same as Slip 1 Q1 - Refer to Slip 1 for code)*

### Q2) Write a python program for implementation of static stack (using Arrays).

```python
class StaticStack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        
    def push(self, element):
        if len(self.stack) >= self.size:
            print("Stack Overflow")
        else:
            self.stack.append(element)
            print(f"Pushed {element}")
            
    def pop(self):
        if not self.stack:
            print("Stack Underflow")
        else:
            val = self.stack.pop()
            print(f"Popped {val}")
            
    def display(self):
        print("Stack:", self.stack)

# Driver Code
s = StaticStack(3) # Max size 3
s.push(10)
s.push(20)
s.push(30)
s.push(40) # Should fail
s.display()
s.pop()
s.display()
```

---

## Slip 16

### Q1) Programs for understanding the data types, control flow statements, blocks and loops.
*(Same as Slip 1 Q1 - Refer to Slip 1 for code)*

### Q2) Write a python program for Quick Sort.
*(Same as Slip 12 Q2 - Refer to Slip 12 for code)*

---

## Slip 17

### Q1) Create a class employee with data members: name, department and salary. Create suitable methods for reading and printing employee information.

```python
class Employee:
    def __init__(self):
        self.name = ""
        self.department = ""
        self.salary = 0.0

    def read_info(self):
        self.name = input("Enter Name: ")
        self.department = input("Enter Department: ")
        self.salary = float(input("Enter Salary: "))

    def print_info(self):
        print("\n--- Employee Details ---")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

# Driver Code
emp = Employee()
# Uncomment below lines to run interaction
# emp.read_info() 
# emp.print_info()

# Demonstration with direct assignment (for non-interactive run)
emp.name = "John Doe"
emp.department = "IT"
emp.salary = 50000
emp.print_info()
```

### Q2) Write a program in python to create a graph and represent using adjacency list and traverse in DFS order.

```python
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(start)
        print(start, end=" ")

        if start in self.graph:
            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    self.dfs(neighbor, visited)

# Driver Code
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS Traversal starting from vertex 2:")
g.dfs(2)
```
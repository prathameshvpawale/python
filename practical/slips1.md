# Python Practical Slips Solutions

This document contains Python programs for Slips 1 through 17.

---

## Slip 1

### Q. 1) Programs for understanding Data Types, Control Flow, Blocks, and Loops
```python
def demonstrate_basics():
    # A) Data Types
    integer_var = 10
    float_var = 10.5
    string_var = "Hello"
    list_var = [1, 2, 3]
    
    print(f"Int: {integer_var}, Float: {float_var}, String: {string_var}")
    print(f"List: {list_var}")

    # B) Control Flow (if-else) & Loops
    num = int(input("Enter a number to check even/odd: "))
    
    # Block start
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
    # Block end

    print("Counting to 5 using loop:")
    for i in range(1, 6):
        print(i, end=" ")
    print()

if __name__ == "__main__":
    demonstrate_basics()
Q. 2) Singly Linked List (Create, Insert, Delete, Display, Reverse)
Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f"Inserted {data}")

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        print(f"Deleted {key}")

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("List Reversed")

# Driver Code
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()
ll.reverse()
ll.display()
ll.delete(20)
ll.display()
Q. 3) Employee Class
Python

class Employee:
    def __init__(self):
        self.name = ""
        self.department = ""
        self.salary = 0.0

    def read_data(self):
        self.name = input("Enter Name: ")
        self.department = input("Enter Department: ")
        self.salary = float(input("Enter Salary: "))

    def print_data(self):
        print("\n--- Employee Details ---")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

emp = Employee()
emp.read_data()
emp.print_data()
Q. 4) Recursive Binary Search
Python

def binary_search_recursive(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)
        else:
            return binary_search_recursive(arr, mid + 1, high, x)
    else:
        return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search_recursive(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
Slip 2
Q. 1) Functions (Built-in and User-defined)
Python

import math

# B) User Defined Function
def calculate_area(radius):
    # A) Built-in Function (math.pi, pow)
    return math.pi * pow(radius, 2)

r = 5
print(f"Radius: {r}")
print(f"Area (using built-in pi and pow): {calculate_area(r):.2f}")
print(f"Max of 10 and 20 (Built-in): {max(10, 20)}")
Q. 2) Linear Search
Python

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [10, 20, 80, 30, 60, 50]
x = 30
result = linear_search(arr, x)
if result != -1:
    print(f"Element {x} found at index {result}")
else:
    print("Element not found")
Q. 3) Modules and Packages
(Note: In a real scenario, these are separate files. Here is the code structure.)

Python

# File: mymodule.py
def greet(name):
    return f"Hello, {name} from Module!"

# File: main.py
# import mymodule
# print(mymodule.greet("User"))

# Demonstration
print("This explains modules: A module is a .py file containing functions.")
print("A package is a directory with __init__.py.")
Q. 4) Graph Adjacency List
Python

def create_graph():
    graph = {}
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    for _ in range(e):
        u, v = input("Enter edge (u v): ").split()
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append(v)
        graph[v].append(u) # Remove this line if directed graph

    print("Adjacency List:")
    for vertex, edges in graph.items():
        print(f"{vertex} -> {edges}")

# create_graph() # Uncomment to run interactively
Slip 3
Q. 1) OOP Concepts (Class, Inheritance, Polymorphism)
Python

# A) Class and Method
class Animal:
    def speak(self):
        pass

# B) Inheritance
class Dog(Animal):
    # C) Polymorphism (Overriding speak)
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
Q. 2) Matrix Transpose
Python

X = [[12, 7],
     [4, 5],
     [3, 8]]

result = [[0, 0, 0],
          [0, 0, 0]]

# Iterate through rows
for i in range(len(X)):
    # Iterate through columns
    for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)
Q. 3) Threading in Python
Python

import threading
import time

def worker(num):
    print(f"Thread {num} starting")
    time.sleep(1)
    print(f"Thread {num} finished")

threads = []
for i in range(2):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print("All threads done")
Q. 4) Graph DFS
Python

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

print("DFS Traversal:")
dfs(graph, '0')
print()
Slip 4
Q. 1) Exceptions & Multithreading
Python

import threading

# A) Built-in Exception
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Built-in Exception caught: {e}")

# B) User Defined Exception
class MyError(Exception):
    pass

try:
    raise MyError("Something went wrong")
except MyError as e:
    print(f"User Defined Exception: {e}")

# C) Multithreading (covered in Slip 3 Q3)
Q. 2) Merge Sort
Python

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print(f"Sorted array: {arr}")
Q. 3) Flower Class
Python

class Flower:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.colour = ""
        self.smell = ""

    def get(self, name, price, colour, smell):
        self.name = name
        self.price = price
        self.colour = colour
        self.smell = smell

    def display(self):
        print(f"Flower: {self.name}, Price: {self.price}, Color: {self.colour}, Smell: {self.smell}")

lily = Flower()
lily.get("Lily", 100, "White", "Sweet")
lily.display()

rose = Flower()
rose.get("Rose", 50, "Red", "Rosy")
rose.display()
Q. 4) Delete Node from Front (Linked List)
(Using class from Slip 1)

Python

# Assuming LinkedList class exists
def delete_front(self):
    if self.head:
        print(f"Deleting {self.head.data}")
        self.head = self.head.next
    else:
        print("List is empty")

# Add this method to the LinkedList class in Slip 1
Slip 5
Q. 1) MongoDB CRUD
(Requires pymongo installed)

Python

# import pymongo
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["testdb"]
# col = db["students"]

# # A) Create
# col.insert_one({"name": "John", "age": 20})

# # B) Read
# x = col.find_one()
# print(x)

# # C) Update
# col.update_one({"name": "John"}, {"$set": {"age": 21}})

# # D) Delete
# col.delete_one({"name": "John"})
print("MongoDB CRUD code provided (requires pymongo setup).")
Q. 2) Bubble Sort
Python

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)
Q. 3) OOP Concepts
(Refer to Slip 3, Q1)

Q. 4) Singly Linked List
(Refer to Slip 1, Q2)

Slip 6
Q. 1) Exception Handling & Multithreading
(Refer to Slip 4, Q1)

Q. 2) Circular Singly Linked List
Python

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
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head: return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head: break
        print("(Head)")

cll = CircularLinkedList()
cll.insert(1)
cll.insert(2)
cll.insert(3)
cll.display()
Q. 3) Functions
(Refer to Slip 2, Q1)

Q. 4) Reverse Linked List
(Refer to Slip 1, Q2)

Slip 7
Q. 1) OOP Concepts
(Refer to Slip 3, Q1)

Q. 2) Infix to Postfix
Python

def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = []
    output = []
    
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence.get(char, 0) <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)
            
    while stack:
        output.append(stack.pop())
        
    return "".join(output)

exp = "a+b*(c^d-e)^f+g*h"
print(f"Infix: {exp}")
print(f"Postfix: {infix_to_postfix(exp)}")
Q. 3) Exceptions
(Refer to Slip 4, Q1)

Q. 4) Static Stack (using Arrays/List)
Python

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item}")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack Empty"

    def is_empty(self):
        return len(self.stack) == 0

s = Stack()
s.push(10)
s.push(20)
print(s.pop())
Slip 8
Q. 1) Flower Class
(Refer to Slip 4, Q3)

Q. 2) Queue using Linked List
Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLL:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, item):
        temp = Node(item)
        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
        print(f"Enqueued {item}")

    def dequeue(self):
        if self.front is None:
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        print(f"Dequeued {temp.data}")

q = QueueLL()
q.enqueue(10)
q.enqueue(20)
q.dequeue()
Q. 3) Exceptions
(Refer to Slip 4, Q1)

Q. 4) Recursive Binary Search
(Refer to Slip 1, Q4)

Slip 9
Q. 1) MongoDB CRUD
(Refer to Slip 5, Q1)

Q. 2) Graph Adjacency List
(Refer to Slip 2, Q4)

Q. 3) Exceptions
(Refer to Slip 4, Q1)

Q. 4) Quick Sort
Python

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

data = [8, 7, 2, 1, 0, 9, 6]
quick_sort(data, 0, len(data) - 1)
print(f"Sorted Array: {data}")
Slip 10
Q. 1) Functions
(Refer to Slip 2, Q1)

Q. 2) Circular Queue using Linked List
Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.rear.next = self.front

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        if self.front == self.rear:
            value = self.front.data
            self.front = None
            self.rear = None
        else:
            temp = self.front
            value = temp.data
            self.front = self.front.next
            self.rear.next = self.front
        print(f"Dequeued {value}")

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.front: break
        print()

cq = CircularQueue()
cq.enqueue(1)
cq.enqueue(2)
cq.display()
cq.dequeue()
cq.display()
Q. 3) OOP Concepts
(Refer to Slip 3, Q1)

Q. 4) Graph Adjacency List
(Refer to Slip 2, Q4)

Slip 11
Q. 1) Functions
(Refer to Slip 2, Q1)

Q. 2) Bubble Sort
(Refer to Slip 5, Q2)

Q. 3) OOP Concepts
(Refer to Slip 3, Q1)

Q. 4) Graph DFS
(Refer to Slip 3, Q4)

Slip 12
Q. 1) Basics (Data Types, Control Flow)
(Refer to Slip 1, Q1)

Q. 2) Quick Sort
(Refer to Slip 9, Q4)

Q. 3) Email Validation Regex
Python

import re

def validate_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        print("Valid Email")
    else:
        print("Invalid Email")

validate_email("test@example.com")
validate_email("invalid-email")
Q. 4) Graph DFS
(Refer to Slip 3, Q4)

Slip 13
Q. 1) Basics
(Refer to Slip 1, Q1)

Q. 2) Recursive Binary Search
(Refer to Slip 1, Q4)

Q. 3) Email Validation Regex
(Refer to Slip 12, Q3)

Q. 4) Circular Singly Linked List
(Refer to Slip 6, Q2)

Slip 14
Q. 1) Flower Class
(Refer to Slip 4, Q3)

Q. 2) Matrix to Sparse Matrix
Python

matrix = [
    [0, 0, 3, 0],
    [5, 0, 0, 0],
    [0, 0, 0, 1]
]

sparse_matrix = []
print("Row\tCol\tValue")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] != 0:
            sparse_matrix.append((i, j, matrix[i][j]))
            print(f"{i}\t{j}\t{matrix[i][j]}")
Q. 3) Functions
(Refer to Slip 2, Q1)

Q. 4) Merge Sort
(Refer to Slip 4, Q2)

Slip 15
Q. 1) Basics
(Refer to Slip 1, Q1)

Q. 2) Static Stack
(Refer to Slip 7, Q4)

Q. 3) Threading
(Refer to Slip 3, Q3)

Q. 4) Delete Node from Front (Linked List)
(Refer to Slip 4, Q4)

Slip 16
Q. 1) Basics
(Refer to Slip 1, Q1)

Q. 2) Quick Sort
(Refer to Slip 9, Q4)

Q. 3) Threading
(Refer to Slip 3, Q3)

Q. 4) Infix to Postfix
(Refer to Slip 7, Q2)

Slip 17
Q. 1) Employee Class
(Refer to Slip 1, Q3)

Q. 2) Graph DFS
(Refer to Slip 3, Q4)

Q. 3) Threading
(Refer to Slip 3, Q3)

Q. 4) Delete Node from Front (Linked List)
(Refer to Slip 4, Q4)
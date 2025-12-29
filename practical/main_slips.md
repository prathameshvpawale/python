
# Python Practical Slips – Solved Programs

---

## SLIP 1

### Q1) Data Types and Control Flow
```python
a = 10
b = 2.5
c = "Python"
d = True
print(type(a), type(b), type(c), type(d))

if a > 5:
    print("Greater than 5")
else:
    print("Less than or equal to 5")

for i in range(1, 6):
    print(i)
```

### Q2) Singly Linked List Operations
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def delete(self):
        if self.head:
            self.head = self.head.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
```

### Q3) Employee Class
```python
class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary

    def display(self):
        print(self.name, self.dept, self.salary)

e = Employee("Amit", "IT", 50000)
e.display()
```

### Q4) Recursive Binary Search
```python
def binary_search(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            return binary_search(arr, low, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, high, key)
    return -1
```

---

## SLIP 2

### Q1) Built-in and User Defined Functions
```python
print(len("Python"))

def add(a, b):
    return a + b

print(add(5, 3))
```

### Q2) Linear Search
```python
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
```

### Q3) Module and Package
```python
# module.py
def greet():
    print("Hello")

# main.py
import module
module.greet()
```

### Q4) Graph – Adjacency List
```python
graph = {}
edges = [(1,2),(1,3),(2,4)]
for u,v in edges:
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)
print(graph)
```

---

## SLIP 3

### Q1) OOP Concepts
```python
class Vehicle:
    def speed(self):
        print("Normal speed")

class Car(Vehicle):
    def speed(self):
        print("Fast speed")

v = Vehicle()
c = Car()
v.speed()
c.speed()
```

### Q2) Transpose of Matrix
```python
matrix = [[1,2],[3,4]]
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(transpose)
```

### Q3) Multithreading
```python
import threading

def task():
    print("Thread running")

t = threading.Thread(target=task)
t.start()
t.join()
```

### Q4) DFS Traversal
```python
def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for n in graph[node]:
            dfs(graph, n, visited)
```

---

## SLIP 4

### Q1) Exception Handling & Multithreading
```python
class MyError(Exception):
    pass

try:
    raise MyError("User defined exception")
except MyError as e:
    print(e)
```

### Q2) Merge Sort
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k]=L[i]; i+=1
            else:
                arr[k]=R[j]; j+=1
            k+=1
        arr[k:] = L[i:] + R[j:]
```

### Q3) Flower Class
```python
class Flower:
    def get(self, price, colour, smell):
        self.price = price
        self.colour = colour
        self.smell = smell

    def display(self):
        print(self.price, self.colour, self.smell)

rose = Flower()
rose.get(50, "Red", "Good")
rose.display()
```

### Q4) Delete Node from Front
```python
def delete_front(head):
    if head:
        return head.next
```

---


---

## SLIP 5

### Q1) MongoDB CRUD Operations
```python
from pymongo import MongoClient
client = MongoClient()
db = client.college
col = db.students

# Create
col.insert_one({"name":"Rahul","age":21})

# Read
print(list(col.find()))

# Update
col.update_one({"name":"Rahul"},{"$set":{"age":22}})

# Delete
col.delete_one({"name":"Rahul"})
```

### Q2) Bubble Sort
```python
arr = [5,3,1,4]
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)
```

### Q3) OOP Concepts
```python
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

a = Animal()
d = Dog()
a.sound()
d.sound()
```

### Q4) Singly Linked List
```python
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
```

---

## SLIP 6

### Q1) Exception Handling & Multithreading
```python
try:
    x = int("abc")
except ValueError:
    print("Invalid conversion")
```

### Q2) Circular Singly Linked List
```python
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
```

### Q3) Built-in & User Defined Functions
```python
print(abs(-10))

def square(x):
    return x*x

print(square(5))
```

### Q4) Reverse Linked List
```python
def reverse(head):
    prev=None
    curr=head
    while curr:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    return prev
```

---

## SLIP 7

### Q1) OOP Concepts
```python
class Shape:
    def area(self):
        print("Area")

class Square(Shape):
    def area(self):
        print("Square Area")
```

### Q2) Infix to Postfix
```python
def infix_to_postfix(expr):
    stack=[]
    output=[]
    prec={'+':1,'-':1,'*':2,'/':2}
    for ch in expr:
        if ch.isalnum():
            output.append(ch)
        else:
            while stack and prec.get(stack[-1],0)>=prec.get(ch,0):
                output.append(stack.pop())
            stack.append(ch)
    while stack:
        output.append(stack.pop())
    return ''.join(output)
```

### Q3) Exception Handling & Threads
```python
import threading
def task():
    print("Thread running")
t=threading.Thread(target=task)
t.start()
```

### Q4) Stack using Array
```python
stack=[]
stack.append(10)
stack.pop()
```

---

## SLIP 8

### Q1) Flower Class
```python
class Flower:
    def get(self,price,colour,smell):
        self.price=price
        self.colour=colour
        self.smell=smell
    def display(self):
        print(self.price,self.colour,self.smell)
```

### Q2) Queue using Linked List
```python
class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,x):
        self.items.append(x)
    def dequeue(self):
        return self.items.pop(0)
```

### Q3) Exception Handling
```python
try:
    print(10/0)
except ZeroDivisionError:
    print("Divide by zero")
```

### Q4) Recursive Binary Search
```python
def binary_search(arr,l,h,key):
    if l<=h:
        m=(l+h)//2
        if arr[m]==key:
            return m
        elif key<arr[m]:
            return binary_search(arr,l,m-1,key)
        else:
            return binary_search(arr,m+1,h,key)
    return -1
```

---

## SLIP 9

### Q1) MongoDB CRUD – Same as Slip 5

### Q2) Graph Adjacency List
```python
graph={}
edges=[(1,2),(2,3)]
for u,v in edges:
    graph.setdefault(u,[]).append(v)
    graph.setdefault(v,[]).append(u)
print(graph)
```

### Q3) Exception Handling
```python
try:
    open("abc.txt")
except FileNotFoundError:
    print("File not found")
```

### Q4) Quick Sort
```python
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr[1:] if x<=pivot]
    right=[x for x in arr[1:] if x>pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
```

---

## SLIP 10

### Q1) Functions – Same as Slip 2

### Q2) Circular Queue using Linked List
```python
class CircularQueue:
    def __init__(self):
        self.items=[]
```

### Q3) OOP Concepts – Same as Slip 3

### Q4) Graph Adjacency List – Same as Slip 2

---

## SLIP 11

### Q1) Functions – Same as Slip 2

### Q2) Bubble Sort – Same as Slip 5

### Q3) OOP Concepts – Same as Slip 3

### Q4) DFS Traversal – Same as Slip 3

---

## SLIP 12

### Q1) Data Types & Control Flow – Same as Slip 1

### Q2) Quick Sort – Same as Slip 9

### Q3) Email Validation
```python
import re
email="test@gmail.com"
if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$',email):
    print("Valid")
```

### Q4) DFS Traversal – Same as Slip 3

---

## SLIP 13

### Q1) Data Types – Same as Slip 1

### Q2) Recursive Binary Search – Same as Slip 8

### Q3) Email Validation – Same as Slip 12

### Q4) Circular Linked List – Same as Slip 6

---

## SLIP 14

### Q1) Flower Class – Same as Slip 8

### Q2) Sparse Matrix
```python
matrix=[[0,0,3],[0,4,0]]
sparse=[]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]!=0:
            sparse.append((i,j,matrix[i][j]))
print(sparse)
```

### Q3) Functions – Same as Slip 2

### Q4) Merge Sort – Same as Slip 4

---

## SLIP 15

### Q1) Data Types – Same as Slip 1

### Q2) Stack using Array – Same as Slip 7

### Q3) Multithreading – Same as Slip 3

### Q4) Delete Node from Front – Same as Slip 4

---

## SLIP 16

### Q1) Data Types – Same as Slip 1

### Q2) Quick Sort – Same as Slip 9

### Q3) Multithreading – Same as Slip 3

### Q4) Infix to Postfix – Same as Slip 7

---

## SLIP 17

### Q1) Employee Class – Same as Slip 1

### Q2) DFS Traversal – Same as Slip 3

### Q3) Multithreading – Same as Slip 3

### Q4) Delete Node from Front – Same as Slip 4

---

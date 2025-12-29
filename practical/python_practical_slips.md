
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

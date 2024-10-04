class Node:
   def __init__(self, data):
     self.data = data
     

class LinkedList:
   def __init__(self):
     self.head = None
     
   def append(self, data):
     new_node = Node(data)
     if not self.head:
         self.head = new_node
     else:
         current = self.head
        
         while current:
             current = current
         current.next = new_node
         
   def delete(self, data):
     if not self.head:
         return
     if self.head.data == data:
         self.head = self.head.next
         return
     current = self.head
     while current.next and current.next.data != data:
         current = current.next
     if current.next is None:
         return
     
     self.head = current.next.next
     
   def print_list(self):
     current = self.head
     while current:
         print(current.data, end=" -> ")
         current = current.next
     print("None")
     
def main():
   ll = LinkedList()
   ll.append(1)
   ll.append(2)
   ll.append(3)
   ll.print_list()
   ll.delete(2)
   ll.print_list()

main()

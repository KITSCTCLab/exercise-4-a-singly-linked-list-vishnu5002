from typing import Optional
class Node:
   
    def __init__(self, data=None, next=None):
       
        self.data = data
        self.next = next
class LinkedList: 
    def __init__(self):  
        self.head = None
    def insert_at_end(self, data):
        
        new = Node(data, None)
        current = self.head
        if current is None:
            self.head = new
        else:
            while current.next is not None:
                current = current.next
            current.next = new
    def status(self):
        
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)
class Solution:
    
    def addTwoNumbers(self, first_list: Optional[LinkedList], second_list: Optional[LinkedList]) -> Optional[
        LinkedList]:
       
        result = self.get_num(first_list) + self.get_num(second_list)
        sum_list = LinkedList()
        for digit in list(map(int, str(result)[::-1])):
            sum_list.insert_at_end(digit)
        return sum_list
    def get_num(self, l: Optional[LinkedList]) -> int:
        
        curr = l.head
        if curr is None:
            return 0
        num = ""
        while curr is not None:
            num = str(curr.data) + num
            curr = curr.next
        return int(num)

first_list = LinkedList()
second_list = LinkedList()
data_for_first_list = list(map(int, input().strip().split(" ")))
for data in data_for_first_list:
    first_list.insert_at_end(data)
data_for_second_list = list(map(int, input().strip().split(" ")))
for data in data_for_second_list:
    second_list.insert_at_end(data)
solution = Solution()
new_list = solution.addTwoNumbers(first_list, second_list)
new_list.status()

from cmath import pi
from node import Node

class Stack:

	def __init__(self, max_size = 100):

		self.size = 0
		self.max_size = max_size
		self.top_item = None

	def is_empty(self):

		return self.size == 0

	def has_space(self):

		return self.size < self.max_size

	def push(self, value):

		if self.has_space():

			item_to_add = Node(value)
			item_to_add.set_next_node(self.top_item)
			self.top_item = item_to_add
			self.size += 1
			print("Adding pizza {} to the pizza stack.".format(value))

		else:

			print("Sorry, no more room for pizza {}.".format(value))

	def pop(self):

		if not self.is_empty():

			item_to_remove = self.top_item
			self.top_item = self.top_item.get_next_node()
			self.size -= 1

			print("Delivering pizza {}.".format(item_to_remove.get_value()))

		else:

			print("The stack is totally empty!")

	def peek(self):

		if not self.is_empty():

			print("The pizza {} is waiting.".format(self.top_item.get_value()))

		else:

			print("Nothing to see here!")

pizza_delivery = Stack(8)

for i in range(10):

	pizza_delivery.push(i)

pizza_delivery.peek()

for i in range(5):

	pizza_delivery.pop()

pizza_delivery.peek()

for i in range(4):

	pizza_delivery.pop()

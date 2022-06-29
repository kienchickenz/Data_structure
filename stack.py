from node import Node

class Stack:

	def __init__(self, max_size = 100):

		self.size = 0
		self.max = max_size
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

		else:

			return "Sorry, no more room for " + item_to_add.get_value()

	def pop(self):

		if not self.is_empty():

			item_to_remove = self.top_item
			self.top_item = self.top_item.get_next_node()
			self.size -= 1

			return item_to_remove.get_value()

		else:

			return "The stack is totally empty!"

	def peek(self):

		if not self.is_empty():

			return self.top_item.get_value()

		else:

			return "Nothing to see here!"
from node import Node

class Queue:

	def __init__(self, max_size = 10):

		self.size = 0
		self.max = max_size
		self.head_node = None
		self.tail_node = None

	def has_space(self):

		return self.size < self.max_size

	def is_empty(self):

		return self.size == 0

	def enqueue(self, value):

		if self.has_space():

			if not self.is_empty():

				item_to_add = Node(value)
				self.tail_node.set_next_node(item_to_add)
				self.tail_node = item_to_add
			
			else:

				self.head_node = item_to_add
				self.tail_node = item_to_add

			self.size += 1

		else:

			return "Sorry, no more room for " + item_to_add.get_value()

	def dequeue(self, value):

		if not self.is_empty():

			item_to_remove = self.head_node

			if self.size == 1:

				self.head_node = None
				self.tail_node = None

			else:

				self.head_node = self.head_node.get_next_node()

			self.size -= 1

			return item_to_remove.get_value()

		else:

			return "The queue is totally empty!"

	def peek(self):

		if not self.is_empty():

			return self.head_node.get_value()

		else:

			return "Nothing to see here!"
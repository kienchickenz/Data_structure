class Node:

	def __init__(self, value, next_node = None, prev_node = None):

		self.value = value
		self.next_node = next_node
		self.prev_node = prev_node

	def get_value(self):

		return self.value

	def get_next_node(self):

		return self.next_node

	def get_prev_node(self):

		return self.prev_node

	def set_next_node(self, next_node):

		self.next_node = next_node

	def set_prev_node(self, prev_node):

		self.prev_node = prev_node

class DoublyLinkedList:

	def __init__ (self):

		self.head_node = None
		self.tail_node = None

	def add_to_head(self, new_value):

		new_head = Node(new_value)
		current_head = self.head_node

		if self.head_node != None:

			new_head.set_next_node(current_head)
			current_head.set_prev_node(new_head)

		self.head_node = new_head

		if self.tail_node == None:

			self.tail_node = new_head

	def add_to_tail(self, new_value):

		new_tail = Node(new_value)
		current_tail = self.tail_node

		if self.tail_node != None:

			new_tail.set_prev_node(current_tail)
			current_tail.set_next_node(new_tail)

		self.tail_node = new_tail

		if self.head_node == None:

			self.head_node = new_tail

	def remove_head(self):

		removed_head = self.head_node

		if self.head_node == None:

			return None

		self.head = removed_head.get_next_node()

		if self.head_node != None:

			self.head_node.set_prev_node(None)

		if self.tail_node == removed_head:

			self.remove_tail()

		return removed_head.get_value()

	def remove_tail(self):

		removed_tail = self.tail_node

		if self.tail_node == None:

			return None

		self.tail = removed_tail.get_prev_node()

		if self.tail_node != None:

			self.tail_node.set_prev_node(None)

		if self.head_node == removed_tail:

			self.remove_head()

		return removed_tail.get_value()

	def remove_by_value(self, value_to_remove):

		node_to_remove = None

		current_node = self.head_node

		while current_node != None:

			if current_node.get_value() == value_to_remove:

				node_to_remove = current_node
				break

			current_node = current_node.get_next_node()

		if node_to_remove == None:

			return None

		if self.head_node == node_to_remove:

			self.remove_head()

		elif self.tail_node == node_to_remove:

			self.remove_tail()

		else:

			next_node = node_to_remove.get_next_node()
			prev_node = node_to_remove.get_prev_node()

			next_node.set_prev_node(prev_node)
			prev_node.set_next_node(next_node)

			return node_to_remove.get_value()

	def stringify_list(self):

		string_list = ""

		current_node = self.head_node

		while current_node:

			if current_node != None:

				string_list += str(current_node.get_value())

				current_node = current_node.get_next_node()

		return string_list 
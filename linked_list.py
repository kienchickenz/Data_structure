from node import Node

class LinkedList:

	def __init__(self, value = None):

		self.head_node = Node(value)

	def get_head_node(self):

		return self.head_node

	def insert_beginning(self, new_value):

		new_node = Node(new_value)
		new_node.set_next_node(self.head_node)
		self.head_node = new_node

	def stringify_list(self):

		string_list = ""
		current_node = self.head_node

		while current_node:

			if current_node.get_value() == None:

				current_node = current_node.get_next_node()

			else:

				string_list += str(current_node.get_value()) + "\n"

			return string_list

	def remove_node(self, value_to_remove):

		current_node = self.head_node

		if self.head_node.get_value() == value_to_remove:

			self.head_node = current_node.get_next_node()

		else:

			while current_node:

				next_node = current_node.get_netx_node()

				if current_node.get_next_node().get_value() == value_to_remove:

					current_node.set_next_node(next_node.get_next_node())
					current_node = None

				else:

					current_node = next_node

	def swap_node(self, value_1, value_2):

		if value_1 == value_2:

			return "Elements are the same - no swap needed"

		node_1 = self.head_node
		prev_node_1 = None

		node_2 = self.head_node
		prev_node_2 = None

		while node_1 != None:

			if node_1.get_value() == value_1:

				break

			node_1 = node_1.get_next_node()
			prev_node_1 = node_1

		while node_2 != None:

			if node_2.get_value() == value_2:

				break

			node_2 = node_2.get_next_node()
			prev_node_2 = node_2

		if node_1 == None or node_2 == None:

			return "Swap not possible - one or more element is not in the list"

		# Update the front pointer
		if prev_node_1 == None:

			self.head_node = node_2

		else:

			prev_node_1.set_next_node(node_2)

		if prev_node_2 == None:

			self.head_node = node_1

		else:

			prev_node_2.set_next_node(node_1)

		# Update the back pointer
		temp = node_1.get_next_node() # After updating the back pointer, node_1 is no longer a node_1 but node_2
		node_1.set_next_node(node_2.get_next_node())
		node_2.set_next_node(temp) 
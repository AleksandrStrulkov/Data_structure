class Node:
	"""Класс для узла очереди"""

	def __init__(self, data):
		"""
		Конструктор класса Node

		:param data: данные, которые будут храниться в узле
		"""
		self.data = data
		self.next_node = None


class Queue:
	"""Класс для очереди"""

	def __init__(self) -> object:
		"""Конструктор класса Queue
		:rtype: object
		"""
		self.head = None
		self.tail = None

	def enqueue(self, data):
		"""Добавляет элемент в конец очереди"""
		new_node = Node(data)
		if self.tail is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next_node = new_node
			self.tail = new_node

	def dequeue(self):
		"""Удаляет элемент из начала очереди и возвращает его"""
		if self.head is None:
			return None

		data = self.head.data
		self.head = self.head.next_node
		if self.head is None:
			self.tail = None
		return data


if __name__ == '__main__':
	queue = Queue()
	queue.enqueue(1)
	queue.enqueue(2)
	queue.enqueue(3)
	queue.enqueue(4)
	queue.enqueue(5)
	print(queue.dequeue())
	print(queue.dequeue())
	print(queue.dequeue())
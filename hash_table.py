class Node:
	def __init__(self, key, value):
		self.key = key
		self.val = value
		self.next = None
#capacity  is size of hash table(bucket) .every index of bucket can contain infinite length of loop. size is total number of node in has
# table.  key is string and val is int. string converets to a number (index)
class Hash_Table:
	def __init__(self,capacity):
		self.capacity = capacity
		self.size = 0
		self.bucket = [None]*self.capacity

	def hash_val(self,key):
		tmp = len(key)
		hash_val = 0
		for i in range(len(key)):
			hash_val += (i + tmp) ** ord(key[i])
		return hash_val % self.capacity

	def insert(self,key,val):
		self.size += 1
		index = self.hash_val(key)
		node = self.bucket[index]
		if node == None:
			self.bucket[index] = Node(key,val)
			return
		#prev =None
		while node != None:
			prev = node
			node = node.next
		prev.next = Node(key,val)


	def find(self,key):
		index = self.hash_val(key)
		node = self.bucket[index]
		if  node == None:
			print("Not exist")
			return
		else:
			while node!=None:
				if node.key == key:
					print("value: ", node.val)
					return
				node = node.next
			print("not exist")
			return

	def remove(self,key):
		index = self.hash_val(key)
		node = self.bucket[index]
		if node == None:
			print("not exist")
			return
		prev = None
		while node:
			if node.key == key:
				break
			else:
				prev = node
				node = node.next
		if node == None:
			print("not exist")
			return
		if prev == None:
			self.bucket[index] = node.next
		else:
			prev.next = node.next
		self.size -= 1
		print("deleted")
		return


	def print_hash_table(self):
		for index in range(self.capacity):
			if self.bucket[index]:
				node = self.bucket[index]
				while node:
					print(node.key, node.val)
					node = node.next




object = Hash_Table(20)
object.insert("anu",11)
object.insert("labu",23)
object.find("labu")
object.insert("tanu",34)
object.find("anu")
object.find("tnu")
print(object.size)
object.remove("anu")
object.find("anu")
print(object.size)
object.print_hash_table()



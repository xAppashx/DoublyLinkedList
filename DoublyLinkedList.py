class Node: 
	def __init__(self, ID, Name, Value):
		self.id = ID
		self.name = Name
		self.value = Value
		self.next = None
		self.prev = None
	#def __init__
#class Node

class DoublyLinkedList:
	
	def __init__(self):
		self.head = None
	#def __init__
	
	
	
	# --- Function to find a node with given ID
	def Find_Node(self, ID):
		
		head_value = self.head
		
		# If List is empty
		if (head_value is None):
			return None
		#if 
		
		while (head_value is not None):
			
			#if ID is found
			if (head_value.id == ID):
				return head_value
				break
			#if
			
			head_value = head_value.next
		#while
		
		# If ID wasn't found in List
		return None
		
	#def Find_Node
	
	
	
	
	# --- Function to insert a new node
	def Insert_New_Node(self, ID, Name, Value):
		
		#Check if ID exists or not
		ID_exists = self.Find_Node(ID)
		
		if (ID_exists is not None):
			print("ID already exists in List.")
			return
		#if
		
		#if ID doesn't exist yet
		
		# If List is empty
		if (self.head is None):
			new_node = Node(ID, Name, Value)
			self.head = new_node
		#if
		
		# If List has elements
		else: 
			current_node = self.head
			
			# Get to the end of the list
			while (current_node.next is not None):
				current_node = current_node.next
			#while
			# Insert new Node
			new_node = Node(ID, Name, Value)
			current_node.next = new_node
			new_node.prev = current_node
		#else
		
	#def Insert_New_Node
	
	
	
	# --- Prints the whole List
	def List_Print(self):
		current_node = self.head
		
		if (current_node is None):
			print("List is empty.\n")
		# if
		
		while (current_node is not None):
			print("")
			print("ID:", current_node.id)
			print("Name:", current_node.name)
			print("Value:", current_node.value)
			current_node = current_node.next
		#while
		
	#def List_Print
	
	
	
	# --- Function to delete a Node of given ID
	def Remove_Node(self, ID):
		
		# Verify if ID exists
		remove_ID = self.Find_Node(ID)
		
		if (remove_ID is None):
			print("The given ID doesn't exists in List.")
			return
		#if
		
		# if ID does exists
		
		# if there is NOT a previous Node
		if (remove_ID == self.head):
			self.head = remove_ID.next
			
			# if there is a following Node
			if (self.head is not None):
				self.head.prev = None
			#if
			
			return
		#if
		
		# if there is a previous Node
		
		previous_node = remove_ID.prev
		next_node = remove_ID.next
		
		# if there is NOT a following Node
		if (next_node is None):
			previous_node.next = None
			return 
		#if
		
		# if there is a following Node
		previous_node.next = next_node
		next_node.prev = previous_node
		
		return
		
	#def Remove_Node
	
	
	
	# --- Function that modify the value fo the element with given ID
	def Modify_Value(self, ID):
		
		#Verify if ID exists
		current_node = self.Find_Node(ID)
		
		if (current_node is None):
			print("The given ID doesn't exists in List.")
			return
		#if
		
		# if ID does exists
		
		print("You are about to modify the value of the element called ", current_node.name)
		print("Please enter a new value:")
		current_node.value = input()
		print("Task complete.")
		
	#def Modify_Value
	
	
	
#class DoublyLinkedList
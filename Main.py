import DoublyLinkedList

def Table(): 
	print("\nPlease choose an option: ")
	print("1) Print the List")
	print("2) Insert a new node")
	print("3) Remove a node")
	print("4) Modify a node")
	print("5) Exit")
	print("Insert your option here: ", end="")
	
	option = input()
	return option
# def Table

# Main:

List = DoublyLinkedList.DoublyLinkedList()

option = Table()

while (option != "5"): 
	
	if (option == "1"):
		List.List_Print()
		
		option = Table()
	# option == 1
	
	elif (option == "2"):
		print("Please insert the ID of the node: ", end="")
		NodeID = input()
		
		print("Now input the name of the node: ", end="")
		NodeName = input()
		
		print("Finally, input the value of the node: ", end="")
		NodeValue = input()
		
		List.Insert_New_Node(NodeID, NodeName, NodeValue)
		
		option = Table()
	# option == 2
	
	elif (option == "3"):
		
		print("Please insert the ID of the node to delete: ", end="")
		IDtoDelete = input()
		
		List.Remove_Node(IDtoDelete)
		
		option = Table()
	# option == 3
	
	elif (option == "4"):
		print("Please insert the ID of the node to modify: ", end="")
		IDtoModify = input()
		
		List.Modify_Value(IDtoModify)
		
		option = Table()
	# option == 4
	
	else: 
		print("Invalid input !")
		option = Table()
	#else
	
# while

print("Alright, goodbye!")
# Load test of the DoublyLinkedList

from time import perf_counter    				#Necesarry to precisely time the execution
import matplotlib.pyplot as plt     				#Necesarry to graph the final result
import matplotlib.patches as mpatches 			#Also for the graph
import numpy as np								#To calculate an average

import DoublyLinkedList
List = DoublyLinkedList.DoublyLinkedList()



# -- Speed test of the Insert function
def SpeedInsertNode():
	
	# We are going to insert n nodes and register how much time each took to be inserted
	# As we are inserting new nodes at the end of the List, we expect a O(n) efficiency
	
	n = 1000
	
	SpeedInsertTimes = [None] * n
	SpeedSearchNode = [None] * n
	xAxis = [None] * n
	
	for Loop in range(n):
		
		TimeStart = perf_counter()
		
		List.Insert_New_Node(Loop + 1, "Name", "Value")
		
		TimeFinish = perf_counter()
		TtlTime = TimeFinish - TimeStart
		SpeedInsertTimes[Loop] = TtlTime
		
		SpeedSearchNode[Loop] = SearchNode(Loop + 1)
		
		xAxis[Loop] = Loop + 1
	# for Loop
	
	
	#Plotting the graph of Inserts
	fig, ax = plt.subplots()
	Red = mpatches.Patch(color='red', label='Insert Node Function')
	ax.legend(handles=[Red])
	
	plt.title("Time of inserting a Node in Doubly Linked List")
	plt.scatter(xAxis, SpeedInsertTimes, s=15, c='red')
	
	plt.xlabel("Number of Nodes Inserted")
	plt.ylabel("Time in seconds to insert a Node")
	
	#plt.show()
	
	#Plotting the graph of Seaching
	fig, ax = plt.subplots()
	Red = mpatches.Patch(color='red', label='Search Node Function')
	ax.legend(handles=[Red])
	
	plt.title("Averages time of searching a Node with n Nodes in List")
	plt.scatter(xAxis, SpeedSearchNode, s=15, c='red')
	
	plt.xlabel("Total Number of Nodes in List")
	plt.ylabel("Avergae time in seconds to search a Node")
	
	plt.show()
	
# def SpeedInsertNode







# -- Speed test of the search function
def SearchNode(n):
	
	SpeedSearchNode = [None] * n
	
	for Loop in range(n):
		
		TimeStart = perf_counter()
		
		List.Find_Node(Loop)
		
		TimeFinish = perf_counter()
		TtlTime = TimeFinish - TimeStart
		SpeedSearchNode[Loop] = TtlTime
		
	# for Loop
	
	# We calculate the average
	
	return np.mean(SpeedSearchNode)
# def SearchNode


SpeedInsertNode()





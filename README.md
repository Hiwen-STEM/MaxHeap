# Max - Binary Heap Implementation - Beta Version (More Testing Coming)
PYPI module that provides Max, Binary Heap, functionality. This is the beta version, and thus requires a few more tests. This implementation utilizes the numpy.memmap so overall memory consumption can be greatly reduced.

#Overview
Documentation for the Max - Binary Heap Implementation:

# 1. Core Functions:

  How to use: <br/>
      from MaxHeap import FUNCTION_NAME

  ## def createBTO(filename)
      +Creates a memmap matrix and returns a list containing the following: [memmap list, # of Levels, Largest Index, Number of Nodes]
      	       +filename = String variable describing the file name of a numpy.memmap


  ## def createBTT(filename, numElements)
      +Has the same functionality as createBTO, only it allows users to input how many elements he/she wants...

  ## def BreadthFS(BT, value)</br>
      +Takes the list of memmap references and searches for a particular value given by the user.
       The return values are three components: x, y, z that make up the index...
       	   +BT = memmap list
	       	   +value = The value to search for...

  ## def getHeightTwo(value, INDEX, LEVEL, BT)
      +Takes an index value provided by the user and returns the level of the tree that the index is on.
       If the provided index is not in the range 0 - INDEX, -1 will be returned...
       	  +value = The value to return the height of. (returns -1 if the value can't be found)
       	  +INDEX = The max index value of the binary heap that is occupied by a value...
	  	   +LEVEL = The number of levels the binary heap has...
		   +BT = memmap list

  ## def isFull(NUMNODES, LEVEL)
      +Returns 1 if the binary heap is a full tree, or -1 if not...
      	       +NUMNODES = The number of occupied nodes in the binary heap...
	       	+LEVEL = The highest level of the current binary heap...

  ## def ExtractMax(BT, INDEX, LEVEL)
      +Returns the extracted max value, new max INDEX value, and LEVEL value respectively in that order.
      	      +INDEX = The max index value of the binary heap that is occupied by a value...
	       	      +LEVEL = The number of levels the binary heap has...

  ## def MAXBTAdd(BT, LEVEL, INDEX, NUMNODES, value)
      +Adds a new given value to the binary heap and returns the new LEVEL, max INDEX value, and number of nodes in that order.
      	    +BT = Memmap list
	    	+LEVEL = The number of levels the binary heap has...
		+INDEX = The max INDEX value of the binary heap.
		+NUMNODES = The number of nodes currently occupied within the binary heap.
		+value = The value to add to the binary heap.
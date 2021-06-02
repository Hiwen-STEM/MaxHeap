# Max - Binary Heap Implementation - Beta Version (More Testing Coming)
PYPI module that provides Max, Binary Heap, functionality. This is the beta version, and thus requires a few more tests. This implementation utilizes the numpy.memmap so overall memory consumption can be greatly reduced.

#Overview
Documentation for the Max - Binary Heap Implementation:
# 0. Preliminary Information

     Upon Creating a memmap with one of the two build_heap functions, a directory that will hold the memmap files
     will be created. After the build_heap function is finished, an information list will be returned containing
     the following elements in order: 1. memmap list, 2. # of Levels, 3. Max Occupied Index value, 4. # of Nodes, 5. Data File reference.
     The Developer should not mess with any of these information list elements. Should the developer accidentally tamper with the list values,
     there is a recalibration function that will restore the information list; this assumes that the developer does not mess with the
     files within the created directory. Should the Data file or any other file be erased, the recalibration function will no longer work,
     and the developer should start over with creating a heap.

     Additionally, since the heap elements are stored in files, the developer can add any elements he/she wants and continue on the next day
     by using the recalibration function to restore the information list.

# 1. Core Functions:

  How to use: <br/>
      from MaxHeap import FUNCTION_NAME or from MaxHeap import *

  ## def createBTO()
      +Creates a memmap matrix and returns an INFO list containing the following: [memmap list, # of Levels, Largest Index, Number of Nodes, Data File]
      	       +filename = String variable describing the file name of a numpy.memmap


  ## def createBTT(numElements)
     +Has the same functionality as createBTO, only this time, the developer can specify how many pre-made cells he/she wants.

  ## def getHeightThree(INFO, value)
     +Returns the height of a certain value within the tree or -1 if it can't be found...
     	      +INFO = information list
	      	      +value = the node value that will be searched for...

  ## def reCalibrateInfo()
     +This function only requires that the user be within the binary tree directory initially created; if not -1 is returned.
     	   + No arguments required...

  ## def isFullTree(INFO)
     +Returns 1 if the tree is a full tree...
     	      +INFO = information list

  ## def BreadthFirstOne(INFO, value)
     +This function uses the breadth first search algorithm to find a specified node value. Three non-negative values will
      be returned if the search is successful: x = memmap list component, y = row, z = column -> Or -1, -1, -1 if unseccussful.
     	   +INFO = information list
	   	   +value = node value to be searched for...

  ## def getMaxValue(INFO)
     +returns the max value or -1 if no values are present.
     	      +INFO = information list

  ## def ExtractMaxValue(INFO)
     +Retruns the max value and deletes it from the tree or returns None if no values are present.
     	      +INFO = information list

  ## def AddValue(INFO, Value)
     +Adds a value to the tree and re-organizes accordingly...
     	   +INFO = information list
	   	   +Value = The value to be added...
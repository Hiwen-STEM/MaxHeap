# Max - Binary Heap Implementation
PYPI module that provides Max, Binary Heap, functionality.

# How it Works:
The purpose of this project is to create an efficient binary heap that re-directs the majority of what would be memory related consumption towards storage; this is done by creating a file in storage that will contain all the data. This way a reference to the storage file can be made and used to access small parts of the file in storage. The size of the storage files are kept at 1000x1000 matrice segments. Once a matrix is filled up, then another 1000x1000 matrix file will be created in storage. By doing this we can also keep the amount of storage used at a minimal amount, but this does assume that the file associated with a 1000x1000 matrix is not that big. For many it isn't considering the amount of storage most computers come with these days, but for some it could be a problem; so keep this into consideration before using. On a Mac system for instance, a 1000x1000 numpy memmap file utilizes about 4 MB of storage...

# Overview
Documentation for the Max - Binary Heap Implementation:
# 0. Preliminary Information

     Upon Creating a memmap with the build_heap function, a directory that will hold the memmap files
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
      +Creates a memmap matrix of shape:1000 x 1000 and returns an INFO list
       containing the following: [memmap list, # of Levels, Largest Index, Number of Nodes, Data File]

  ## def getHeightThree(INFO, value)
     +Returns the height of a certain value within the tree or None if it can't be found...
     	      +INFO = information list
	      	      +value = the node value that will be searched for...

  ## def reCalibrateInfo()
     +This function only requires that the user be within the binary tree directory initially created; if not -1 is returned.
      -1 is also returned if all of the files within are deleted...
     	   + No arguments required...

  ## def isPerfect(INFO)
     +Returns 1 if the tree is a perfect tree or -1 if not...
     	      +INFO = information list

  ## def isFullTree(INFO)
     +Retruns 1 if all nodes in the tree have 0 or 2 children; -1 if not...
     	      +INFO = information list

  ## def BreadthFirstOne(INFO, value)
     +This function uses the breadth first search algorithm to find a specified node value. Three non-negative values will
      be returned if the search is successful: x = memmap list component, y = row, z = column -> Or -1, -1, -1 if unseccussful.
     	   +INFO = information list
	   	   +value = node value to be searched for...

  ## def getMaxValue(INFO)
     +returns the max value or None if no values are present.
     	      +INFO = information list

  ## def ExtractMaxValue(INFO)
     +Retruns the max value and deletes it from the tree or returns None if no values are present.
     	      +INFO = information list

  ## def AddValue(INFO, Value)
     +Adds a value to the tree and re-organizes accordingly; returns 'Value' if successful or None if not...
     	   +INFO = information list
	   	   +Value = The value to be added...

# Example1:

	A = createBTO() # A is the information list

	#add a value
	code = AddValue(A, 100) # code will be 100
	code = AddValue(A, 'Bat') # code will be None ('Bat' isn't added)

	#extract a value...
	value = ExtractMaxValue(A) # value will be 100

	#add a value
	code = AddValue(A, 400) # code will be 400
	code = AddValue(A, 100.56) # code will be 100.56

	#get max value...
	value = getMaxValue(A)

	#see if it is a full tree...
	full = isFullTree(A)

	#perform a breadth first search...
	a, b, c = BreadthFirstOne(A, 3000) # will return -1, -1, -1 since 3000 was not added...

# Example2:

	Say we have the structure from example 1. We have two values: 400 and 100.56...
	If we wish to quit our work right now and return tomorrow, all we have to do is
	simply quit; when we wish to continue again, the reCalibrateInfo() function can
	be used to restore the original information list...

	1. We have just quit...
	2. In our current directory, we will see another directory of the form
	   Max_Heap_Tree_Files(NUMBER).BinaryT...
	3. Traverse to the Max Heap directory of the form above...
	4. Perform the following line:
	   A = reCalibrateInfo() # A is the information list...
	   Upon creating a Max-Heap for the first time, developers won't have to worry
	   about changing to the newly created directory, as createBTO() does it for
	   them. However, if resetting an information list after an event that involved
	   quitting and leaving the directory, developers will have to traverse back to
	   the directory via additional code (the os.chdir("PATH") function works well).
	5. Should there be any deleted files from the directory, an error code will be returned...


# History:

	Version 2.2: Fixed a small bug in the downward traversal function.

	Version 3.0: Has getMaxValue return None if no values are present in the tree
		     rather than -1; code in the downward traversal function has been
		     reduced; AddValue returns None if unsuccessful or the same value
		     that was just added if successful...

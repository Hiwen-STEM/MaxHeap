#Author: HarAold J. Iwen
#Non-Profit Company: Inventorsniche L.L.C
#Project: Memmap Based Binary Tree
#Date Created: May 10th, 2021

#Purpose: The purpose of this project is to create an efficient binary heap
#         that consumes little storage and consumes minimal memory.
#
#Functionality:


#Import all required modules for the efficient Binary Tree...
#############################################################
#############################################################
#
#The numpy module contains the memmap that will be used...
import numpy as np
#
#############################################################

#This section is reserved for all core functions and helper functions...
########################################################################
########################################################################

#The first implementation of the createBT (BT = Binary Tree) function,
#by default, creates a 1000x1 (1000 rows, 1 column) memmap matrix.
#This matrix will be capable of holding a max of 1000 binary tree
#elements. ***NOTE: Upon adding more than 1000 elements, the matrix will
#resize automatically.
def createBTO(filename):

    #binary tree array...
    BT = []

    #binary tree info array...
    INFO = []
    
    #make sure that the filename is an authentic string
    #type...
    if(type(filename) == type("")):

        #create a 1000x1 memmap matrix for the efficient binary tree
        #implementation...
        tree = np.memmap(filename, dtype='float32', mode='w+', shape=(1000,1))

        #append tree to the global BT variable...
        BT.append(tree)

        #append BT to the info array...
        INFO.append(BT)

        #append 0, for LEVEL 0...
        INFO.append(0)

        #append 0, for INDEX 0...
        INFO.append(-1)

        #append 0, for 0 nodes...
        INFO.append(0)

        #return INFO...
        return INFO
        
    else:

        #print error message...
        print("Sorry, but the filename you have provided is not a string...")

        #return negative -1...
        return -1

#The second implementation of createBT (BT = Binary Tree) function takes
#an argument pertaining to how many elements the user wants within his/her
#tree; it also takes an argument for a filename...
def createBTT(filename, numElements):

    #temporary tree variable to hold a reference to memmap...
    tree = None

    #binary tree array...
    BT = []

    #binary tree info array...
    INFO = []
    
    #make sure that the filename is an authentic string
    #type...
    if(type(filename) == type("")):

        #check how large numElements is...
        if(numElements > 1000 and numElements <= 1000000):
            
            #see how many columns will be needed...
            for x in range(1,1001):

                #check if sum is greater than numElements...
                if((x * 1000) >= numElements):

                    #create memmap...
                    tree =  np.memmap(filename, dtype='float32', mode='w+', shape=(1000,x))

                    #now append tree to BT
                    BT.append(tree)

                    #break from the for loop...
                    break

        elif(numElements > 1000000):

            #In the case of more than 1000000, two or more memmaps will be created...

            #file counter variable...
            counter = 1
            
            #use a while loop to analyze the situation...
            while(True):

                #Create the first memmap...
                tree =  np.memmap(filename + str(counter), dtype='float32', mode='w+', shape=(1000,1000))

                #increment the file counter variable...
                counter = counter + 1
                
                #append tree to the memmap list BT...
                BT.append(tree)

                #Now subtract 1000000 from numElements...
                numElements = numElements - 1000000

                #check to see if numElements is still greater than 1000000
                if(numElements < 1000000):

                    #break from the while loop...
                    break

            #Now create the last memmap...
            #But first find out how many columns will be needed if
            #numElements is greater than 1000...
            if(numElements > 1000):
                
                #columns variable...
                cols = None

                #***NOTE: The columns variable won't intially hold the number
                #of columns the memmap should have. First the number of digits
                #that must be extracted will be computed and assigned to cols.
                #This value will then be used to extract all digits in front of
                #the three zeros (with three being the most). The extracted digits
                #will then be concatenated in string form and then converted to
                #type integer -> This final number will be the number of columns needed...

                #compute number of columns...
                if(len(str(numElements)) % 3 == 0):

                    #three columns will be needed...
                    cols = 3

                elif(len(str(numElements)) == 5):

                    #two colums will be needed...
                    cols = 2

                else:

                    #one column will be needed...
                    cols = 1

                #make a copy of cols...
                copy = cols
                    
                #Now extract the digits...
                cols = int(str(numElements)[0:cols])
                
                #extract leftovers...
                leftover = int(str(numElements)[copy:])
                
                #add the correct number of columns...
                if(leftover > 0):

                    #now create the last memmap...
                    tree = np.memmap(filename + str(counter), dtype='float32', mode='w+', shape=(1000,cols+1))

                else:

                    #now create the last memmap...
                    tree = np.memmap(filename + str(counter), dtype='float32', mode='w+', shape=(1000,cols))

                #increment the counter...
                counter = counter + 1
                
                #Now append the tree to the BT list...
                BT.append(tree)
            
        elif(numElements != 0):

            #create a 1000x1 memmap matrix for the efficient binary tree
            #implementation...
            tree = np.memmap(filename, dtype='float32', mode='w+', shape=(1000,1))
            
            #append tree to the global BT variable...
            BT.append(tree)

        #append BT to the info array...
        INFO.append(BT)

        #append 0, for LEVEL 0...
        INFO.append(0)

        #append 0, for INDEX 0...
        INFO.append(-1)

        #append 0, for 0 nodes...
        INFO.append(0)

        #return INFO...
        return INFO

#Breadth first search algorithm...
def BreadthFS(BT, value):

    #Value found flag...
    flag = 0
    
    #go through all memmap cells in a linear format...
    for x in range(len(BT)):

        #catch any out of bounds exceptions...
        try:
        
            #loop through all possible cells...
            for t in range(1000):
                for y in range(1000):

                    #check the given value against the current
                    #cell value...
                    if(BT[x][y][t] == float(value)):

                        #set the flag variable to 1...
                        flag = 1
                        
                        #return 1 since the value was found...
                        return x,y,t

        
        except:

            #return -1 since no value was found...
            return -1, -1, -1

#Get the height of a particular node index...
def getHeightOne(index, INDEX, LEVEL):

    #First check to see if the index is valid...
    if(not(index >= 0 and index <= INDEX)):

        #return value of -1 since the index is not
        #valid...
        return -1
        
    #check to see if index == 0
    if(index == 0):

        #return level zero
        return 0
    
    #sum variable...
    sum = 0
        
    #See what level the index is on...
    for x in range(1, LEVEL + 1):

        #sum the number of nodes on each level...
        sum = sum + 2**x

        #check if the index is on the current level...
        if(index <= sum):

            #return the level number...
            return x

#Get the height of a particular node value...
def getHeightTwo(value, INDEX, LEVEL, BT):

    #Use Breadth first search to find the value...
    a, b, c = BreadthFS(BT, value)
    
    #get the final height of the value, but first make sure
    #the value is valid...
    if(a != -1):
        
        #compute the index based on the three components a,b,c...
        index = ((c*1000) + b) + (a*1000000)

        #get the final height of the value...
        height = getHeightOne(index, INDEX, LEVEL)

        #return the retrieved height...
        return height

    #return -1 if the value could not be found...
    return -1

#Resize the memmap if more room needs to be made...
def MResize(BT):

    #first get the length of the BT list...
    length = len(BT)

    #Now get the shape of the last memmap in the list...
    shape = BT[length - 1].shape

    #Extract the number of columns...
    cols = shape[1]

    #See if the memmap is at the max size...
    if(cols == 1000):

        #since cols == 1000, we need a whole new memmap...
        tree = np.memmap("NewMemmapOResize"+str(length+1), dtype='float32', mode='w+', shape=(1000,1))

        #Now append the new memmap to the BT list...
        BT.append(tree)

    else:

        #since the memmap is not at full capacity, a simple resize function will be
        #utilized...
        BT[length - 1] = np.memmap(BT[length-1].filename, dtype='float32', mode='r+', shape=(1000,cols+1))
    
#Check if the binary tree is complete...
def isFull(NUMNODES, LEVEL):

    #sum variable...
    sum = 0
    
    #Check if NUMNODES is equal to the summation of 2^n from n=0 to n = level...
    for x in range(LEVEL + 1):

        #add 2^x to sum...
        sum = sum + (2**x)

    #check if sum is equal to NUMNODES...
    if(NUMNODES == sum):

        #return 1 since the tree is full
        return 1

    else:

        #return -1 since the tree is not full
        return -1

#Breadth first search based on index...
def BreadthFirstSelect(BT, start, INDEX, value):

    #use a for loop to iterate across all index values...
    for x in range((INDEX - start) + 1):

        #decompose the current index...
        x, y, z = decomp(start + x)
        
        #now make the comparison...
        if(BT[x][y][z] == value):

            #return the index values associated with
            #the matched value...
            return x, y, z

    #return -1 since no match was made...
    return -1, -1, -1

#Decompose Index...                                                         
def Decomp(index):

    #convert index to string...                                             
    index = str(index)

    #get the length of string index...                                         
    length = len(index)

    #segment length variable...                                             
    seg = None

    #row, column, and memmap # variables...                                      
    row = None
    col = None
    memNum = None

    #flag variable representing a length less than 3...                                 
    flag = 0

    #get row number...                                                      
    if(length >= 3):

        #assign 3                                                           
        seg = 3

    elif(length < 3):

        #assign length to seg...                                            
        seg = length

        #set flag to 1...                                                   
        flag = 1

    #now extract the row...                                                 
    row = index[(length - seg):]
    
    #make sure a column can be extracted...                                 
    if(flag != 1):

        #get column number...                                               
        if(length >= 6):

            #assign 6                                                       
            seg = 3

        elif(length > 3):

            #assign length - 3                                              
            seg = length - 3

        #assign column number...                                            
        col = index[(length - 3) - seg:length - 3]

        #check if col is empty string..
        if(col == ""):

            #set col to zero
            col = 0

    else:

        #assign zero value to col...                                        
        col = 0

    #now get the memmap number...                                           
    if(length > 6):

        #assign value to memNum...                                          
        memNum = index[0:length - 6]

    else:

        #assign value zero to memNum...                                     
        memNum = 0

    #now return all three values...                                         
    return memNum, row, col

#return the max value of the max-heap...
def getMax(BT):

    #return the root node value...
    return BT[0][0][0]

#Traverse left...                                                           
def LeftChild(index):

    #compute the child index...                                             
    left = (index*2) + 1

    #return the computed index...                                           
    return left

#Traverse right...                                                          
def RightChild(index):

    #compute the child index...                                             
    right = (index*2) + 2

    #return the computed index...                                                                              
    return right

#extract the max value...
def ExtractMax(BT, INDEX, LEVEL):

    #remove value from supernode (root)
    value = BT[0][0][0]

    #move downwards until an appropriate place
    #for the root replacement is found.

    #first decompose the last index location...
    a, b, c = Decomp(INDEX)

    #Replace root with last index value...
    BT[0][0][0] = BT[int(a)][int(b)][int(c)]

    #decrement index...
    INDEX = INDEX - 1

    #update the LEVEL variable...
    if(INDEX == 0):

        LEVEL = 0

    else:
    
        #see if LEVEL needs to be incremented...
        sum = 0

        #sum all the way to LEVEL...
        for x in range(1, LEVEL+1):

            #increment sum...
            sum = sum + 2**x

            #increment LEVEL based on sum...
            if(INDEX <= sum):

                #increment LEVEL...
                LEVEL = x

                #break out of for loop...
                break

    #start value for while loop...
    index = 0

    #index components that will keep track of the
    #new root node value...
    x, y, z = 0, 0, 0
    
    #use while loop to move the new root value to it's
    #appropriate place...
    while(True):

        #start traversing downwards...
        temp = LeftChild(index)

        #see if the new index is valid...
        if(temp <= INDEX):

            #decompose index value...
            a, b, c = Decomp(temp)

            #see if new root value is in the right spot...
            if(BT[int(x)][int(y)][int(z)] < BT[int(a)][int(b)][int(c)]):

                #switch the values...
                val = BT[int(x)][int(y)][int(z)]

                #assign the larger value...
                BT[int(x)][int(y)][int(z)] = BT[int(a)][int(b)][int(c)]

                #assign val to BT[a][b][c]
                BT[int(a)][int(b)][int(c)] = val

                #copy the index components a,b,c
                x, y, z = a, b, c

                #assign temp to index...
                index = temp

                #continue early on...
                continue

        #perform the same sequence of actions on the right
        #node...
        temp = RightChild(index)

        #see if the new index is valid...
        if(temp <= INDEX):

            #decompose index value...
            a, b, c = Decomp(temp)

            #see if new root value is in the right spot...
            if(BT[int(x)][int(y)][int(z)] < BT[int(a)][int(b)][int(c)]):

                #switch the values...
                val = BT[int(x)][int(y)][int(z)]

                #assign the larger value...
                BT[int(x)][int(y)][int(z)] = BT[int(a)][int(b)][int(c)]

                #assign val to BT[a][b][c]
                BT[int(a)][int(b)][int(c)] = val

                #copy the index components a,b,c
                x, y, z = a, b, c

                #assign temp to index...
                index = temp

                #continue early on...
                continue

        #return the INDEX value and MAX value...
        return value, INDEX, LEVEL

#add value to the MAX-Binary-Heap...
def MAXBTAdd(BT, LEVEL, INDEX, NUMNODES, value):

    #see if resizing is necessary...
    if(NUMNODES+1 > BT[len(BT)-1].shape[1]*1000):

        #resize the memmap...
        MResize(BT)
    
    #first add the value to the position
    #INDEX + 1

    #decompose INDEX + 1 so it's position can
    #be accessed...
    a, b, c = Decomp(INDEX + 1)

    #starting index for upward traversal...
    index = INDEX + 1

    #see if LEVEL needs to be incremented...
    sum = 0

    #sum all the way to LEVEL...
    for x in range(1, LEVEL+1):

        #increment sum...
        sum = sum + 2**x

    #increment LEVEL based on sum...
    if(INDEX+1 > sum):

        #increment LEVEL...
        LEVEL = LEVEL + 1

    #assign value to position BT[a][b][c]
    BT[int(a)][int(b)][int(c)] = float(value)

    #use while loop to traverse upwards...
    while(True):

        #first try backtracking from the left...
        temp = LeftBack(index)

        #see if it is a decimal or not...
        if(temp < 0 or int(str(temp)[str(temp).index('.')+1:]) != 0):

            #change temp...
            temp = RightBack(index)

        #make sure temp is not negative...
        #The following is a flag variable...
        flag = None
        
        #The comparison to see if temp is less than
        #zero...
        if(temp < 0):

            #set flag to 1...
            flag = 1

        else:
            
            #decompose temp...
            x, y, z = Decomp(int(temp))
            
        #make comparison to see if upwards
        #traversal is necessary...
        if((flag != 1) and (BT[int(x)][int(y)][int(z)] < value)):

            #exchange values...
            history = BT[int(x)][int(y)][int(z)]

            #assign value to x, y, z location...
            BT[int(x)][int(y)][int(z)] = value

            #assign history to a, b, c location...
            BT[int(a)][int(b)][int(c)] = history

            #update index components...
            a, b, c = x, y, z

            #update index...
            index = temp

            #continue..
            continue

        #break from the loop if this point is reached...
        break

    #return  the new INDEX and LEVEL...
    return LEVEL, (INDEX + 1), (NUMNODES + 1)
        
#Traverse Back left...                                                                                                                                                                                           
def LeftBack(index):

    #compute the parent index...                                                                                                                                                                     
    parent = (index - 1) / 2

    #return parent                                                                                                                                                                       
    return parent

#Traverse Back right...                                                                                                                                                                         
def RightBack(index):

    #compute the parent index...                                                                                                                                                                                 
    parent = (index - 2) / 2

    #return the parent index                                                                                                                                             
    return parent

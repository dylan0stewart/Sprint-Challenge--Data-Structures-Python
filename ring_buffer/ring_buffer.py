 
class RingBuffer:
  def __init__(self, capacity):
    '''
    initialize with base values needed
    '''
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    self.rear = -1
    self.front = -1

  def append(self, item):
   if self.current < self.capacity: #if its less
      oldest = self.storage.pop(self.current) #instantiate oldest
      self.storage.insert(self.current, item) #insert new
      print("After: ", self.storage, "Removed Item: ", oldest)#print changes
      self.current = self.current + 1 #add 1 every time to make sure it resets the loop below

      if self.current == self.capacity: #when current gets to capacity
        self.current = 0 #reset current to 0


  def get(self):
    templist = [] #creates empty list
    for item in self.storage: #iterates through storage
      if item != None: #if item exists
        templist.append(item) #append the item
    return templist #return list when done iterating


'''Copied over mini-test to check as i go'''
# buffer = RingBuffer(3)

# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']
class Node:
   def __init__(self, Data):
      self.left = None
      self.right = None

      self.Data = Data

   def Insert(self, Data):
      if self.Data:
         if Data < self.Data:
            if self.left is None:
               self.left = Node(Data)
            else:
               self.left.Insert(Data)
         elif Data > self.Data:
            if self.right is None:
               self.right = Node(Data)
            else:
               self.right.Insert(Data)

   def FindValue(self, Val):
      if Val < self.Data:
         if self.left is None:
            return str(Val) + " Not Found"
         
         return self.left.FindValue(Val)
      
      elif Val > self.Data:
         if self.right is None:
            return str(Val) + " Not Found"
         
         return self.right.FindValue(Val)
      else:
         return str(self.Data) + " Is Found"

   def PrintTree(self, Padding = None):
      Padding = Padding if Padding != None else ""

      print(Padding + str(self.Data))

      if self.left:
         self.left.PrintTree(Padding = Padding + "-")

      if self.right:
         self.right.PrintTree(Padding = Padding + "-")

root = Node(12)

root.Insert(6)

root.Insert(14)

root.Insert(3)

root.PrintTree()

print(root.FindValue(0))
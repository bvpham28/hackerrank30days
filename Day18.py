#create a stack and queue for our palindrome
def __init__(self):
    self.stack = []
    self.queue = []

#pushes a character onto a stack.
def popCharacter(self):
    #return void for the stack pop
    return self.stack.pop()

#add the character into a stack
def pushCharacter(self, char):
    self.stack.append(char)

#comparing the two elments to see if its a palindrome

def dequeueCharacher(self):
    char = self.queue[0]
    self.queue = self.queue[1:]
    return char

#add the queue to the list

def enqueueCharacter(self, char):
    self.queue.append(char)


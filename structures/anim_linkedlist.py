import sys
sys.path.append('../')

from structures.linkedlist import *

class A_LinkedList(LinkedList):
    """
    Animated extension of the linked list

    Every operation has its operation
    """
    # side to which animation is sticked
    stick = "left"

    def __init__(self, canvas, values=None):
        """
        Initialise the linked list with optional values

        :param canvas: canvas for showing the structure
        :param values: initial values to be put to the list
        :type canvas: ResizingCanvas
        :type values: int[]
        """
        super(A_LinkedList, self).__init__(values)

        # graphical representation of the linked list
        self.canvas = canvas
        self.graphic = []        

        for i, node in enumerate(self):
            # node
            self.canvas.create_rectangle(100*i+50,\
                                         self.canvas.winfo_reqheight()//2-25,\
                                         100*i+100,\
                                         self.canvas.winfo_reqheight()//2+25,\
                                         fill="white")
            # value in the node
            self.canvas.create_text(100*i+75,\
                                    self.canvas.winfo_reqheight()//2,\
                                    text=str(node.val))

            if i < self.length-1:
                # arrow between nodes
                self._draw_arrow(100*i+100, self.canvas.winfo_reqheight()//2)


    def lookup(self, index):
        """Call lookup of linkedlist and animation"""
        self._lookup_animation(index)
        
        return super(A_LinkedList, self).lookup(index)


    def insert(self, value, node): 
        """Call insert of linkedlist and animation"""
        self._insert_animation(value, node)
        
        super(A_LinkedList, self).insert(value, node)


    def insertFirst(self, value):
        """Call insertFirst of linkedlist and animation"""
        self._insertFirst_animation(value)
        
        super(A_LinkedList, self).insertFirst(value)


    def remove(self, node):        
        """Call remove of linkedlist and animation"""
        self._remove_animation(node)
        
        super(A_LinkedList, self).remove(node)


    def removeFirst(self):        
        """Call removeFirst of linkedlist and animation"""
        self._removeFirst_animation()
        
        super(A_LinkedList, self).removeFirst()


    def delete(self, value):        
        """Call delete of linkedlist and animation"""
        self._delete_animation(value)
        
        super(A_LinkedList, self).delete(value)


    def _lookup_animation(self, index):
        """Animation of the lookup operation"""
        pass


    def _insert_animation(self, value, node):
        """Animation of the insert operation"""
        pass


    def _insertFirst_animation(self, value):
        """Animation of the insertFirst operation"""
        self._insert_animation(value, 0)


    def _remove_animation(self, node):
        """Animation of the remove operation"""
        pass


    def _removeFirst_animation(self):
        """Animation of the removeFirst operation"""
        self._remove_animation(0)


    def _delete_animation(self, value):
        """Animation of the delete operation"""
        pass


    def _draw_arrow(self, start_x, start_y):
        """Draw an arrow from one place to another"""
        self.canvas.create_line((start_x, start_y), (start_x+50, start_y))
        self.canvas.create_polygon((start_x+37, start_y+5), (start_x+50, start_y), (start_x+37, start_y-5))


    animations = [
        lookup,
        insert,
        insertFirst,
        remove,
        removeFirst,
        delete
    ]
    
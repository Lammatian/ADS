import sys
import math
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
        self._length = len(values)

        # graphical representation of the linked list
        self.canvas = canvas
        self.nodes = []
        self.arrows = []        

        for i, node in enumerate(self):
            # node
            rect = self.canvas.create_rectangle(100*i+50,\
                                         self.canvas.winfo_reqheight()//2-25,\
                                         100*i+100,\
                                         self.canvas.winfo_reqheight()//2+25,\
                                         fill="white")
            # value in the node
            text = self.canvas.create_text(100*i+75,\
                                    self.canvas.winfo_reqheight()//2,\
                                    text=str(node.val))
            self.nodes.append((rect, text))

            if i < self.length-1:
                # arrow between nodes
                arrow = self._draw_arrow(100*i+100,\
                                         self.canvas.winfo_reqheight()//2,\
                                         100*i+150,\
                                         self.canvas.winfo_reqheight()//2)
                self.arrows.append(arrow)


    def lookup(self, index):
        """Call lookup of linkedlist and animation"""
        self._lookup_animation(index, 0, 0)
        
        return super(A_LinkedList, self).lookup(index)


    def insert(self, value, node): 
        """Call insert of linkedlist and animation"""
        self._insert_animation(value, node, 0)
        
        super(A_LinkedList, self).insert(value, self._nodeAt(node))


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


    def _lookup_animation(self, index, n, step):
        """Animation of the lookup operation"""
        if index < 0 or index >= self.length:
            return

        if n < index:
            if step == 0:
                self._swap_color("rect", n, "yellow")
                self.canvas.after(250, self._lookup_animation, index, n, 1)
            elif step == 1:
                self._swap_color("rect", n, "white")
                self._swap_color("arr", n, "yellow")
                self.canvas.after(250, self._lookup_animation, index, n, 2)
            elif step == 2:
                self._swap_color("arr", n, "black")
                self.canvas.after(250, self._lookup_animation, index, n+1, 0)
        elif n == index:
            if step == 0:
                self._swap_color("rect", n, "green")
                self.canvas.after(500, self._lookup_animation, index, n, 1)
            elif step == 1:
                self._swap_color("rect", n, "white")
                return


    def _insert_animation(self, value, node, step):
        """Animation of the insert operation"""
        if node < self.length:
            if step == 0:
                # new node
                rect = self.canvas.create_rectangle(100*(node+1),\
                                                    self.canvas.winfo_reqheight()//2-100,\
                                                    100*(node+1)+50,\
                                                    self.canvas.winfo_reqheight()//2-50,\
                                                    fill="green",\
                                                    tag="new")
                text = self.canvas.create_text(100*(node+1)+25,\
                                               self.canvas.winfo_reqheight()//2-75,\
                                               text=str(value),\
                                               tag="new")
                self.nodes.insert(node, (rect, text))
                self.canvas.after(300, self._insert_animation, value, node, 1)
            elif step == 1:
                # delete old and add new arrows
                if node >= 0 and node < self._length-1:
                    self.canvas.delete(*self.arrows[node])

                # from previous
                if node >= 0:
                    arrow = self._draw_arrow(100*(node+1)-25,\
                                             self.canvas.winfo_reqheight()//2-25,\
                                             100*(node+1),\
                                             self.canvas.winfo_reqheight()//2-75,
                                             tag="temp")

                # to next
                if node < self._length-1:
                    arrow = self._draw_arrow(100*(node+1)+50,\
                                             self.canvas.winfo_reqheight()//2-75,\
                                             100*(node+1)+75,\
                                             self.canvas.winfo_reqheight()//2-25,
                                             tag="temp")

                self.canvas.after(300, self._insert_animation, value, node, 2)
            elif step == 2:
                # move the node to its place and finish
                # move all items after inserted one to the left
                end_x = self.canvas.coords(self.nodes[-1][0])[2]
                self.canvas.addtag_overlapping("move",\
                                               100*(node+1)+50,\
                                               self.canvas.winfo_reqheight()//2+10,\
                                               end_x,\
                                               self.canvas.winfo_reqheight()//2-10)

                self.canvas.move("move", 100, 0)

                # remove arrows and clean up tags
                self.canvas.delete("temp")
                self.canvas.dtag("move", "move")

                # move new node to its position
                self.canvas.move("new", 50, 75)
                self.canvas.dtag("new", "new")

                # draw new arrows
                if node >= 0:
                    arrow = self._draw_arrow(100*(node+1),\
                                             self.canvas.winfo_reqheight()//2,\
                                             100*(node+1)+50,\
                                             self.canvas.winfo_reqheight()//2)

                    self.arrows.insert(node, arrow)

                if node < self._length-1:
                    arrow = self._draw_arrow(100*(node+2),\
                                             self.canvas.winfo_reqheight()//2,\
                                             100*(node+2)+50,\
                                             self.canvas.winfo_reqheight()//2)

                    self.arrows.insert(node+1, arrow)

                self._length += 1
                self.canvas.after(300, self._insert_animation, value, node, 3)
            elif step == 3:
                self._swap_color("rect", node, "white")
                return


    def _insertFirst_animation(self, value):
        """Animation of the insertFirst operation"""
        pass


    def _remove_animation(self, node):
        """Animation of the remove operation"""
        pass


    def _removeFirst_animation(self):
        """Animation of the removeFirst operation"""
        self._remove_animation(0)


    def _delete_animation(self, value):
        """Animation of the delete operation"""
        pass


    def _draw_arrow(self, x1, y1, x2, y2, tag=None):
        """Draw an arrow from one place to another"""
        line = self.canvas.create_line((x1, y1), (x2, y2))
        poly = self.canvas.create_polygon((x2-13, y2+5),\
                                          (x2, y2),\
                                          (x2-13, y2-5))

        if y2 != y1:
            # negative because the coords of window are oriented the other way
            turn = -math.atan((y2-y1)/(x2-x1))
        else:
            turn = 0

        x0, y0 = self.canvas.coords(poly)[:2]
        x1, y1 = self.canvas.coords(poly)[2:4]
        x2, y2 = self.canvas.coords(poly)[4:]
        # rotating about the arrowhead
        cx, cy = x1, y1

        if turn != 0:
            # translate to center
            x0 = x0 - cx
            y0 = y0 - cy
            # rotate
            _x0 = x0 * math.cos(turn) + y0 * math.sin(turn)
            _y0 = -x0 * math.sin(turn) + y0 * math.cos(turn)

            # translate to center
            x2 = x2 - cx
            y2 = y2 - cy
            # rotate
            _x2 = x2 * math.cos(turn) + y2 * math.sin(turn)
            _y2 = -x2 * math.sin(turn) + y2 * math.cos(turn)

            # set the coordinates to the rotated ones
            self.canvas.coords(poly, [_x0 + cx, _y0 + cy, x1, y1, _x2 + cx, _y2 + cy])

        if tag:
            self.canvas.itemconfig(line, tag=tag)
            self.canvas.itemconfig(poly, tag=tag)

        return (line, poly)


    def _swap_color(self, shape, index, color):
        """Swap a color of a shape at given index"""
        if shape == "rect":
            self.canvas.itemconfig(self.nodes[index][0], fill=color)
        elif shape == "arr":
            self.canvas.itemconfig(self.arrows[index][0], fill=color)
            self.canvas.itemconfig(self.arrows[index][1], fill=color)


    def _nodeAt(self, index):
        """
        Returns node at given index
        Necessary to call super methods
        """
        dummy = self.head

        while index > 0:
            self.head = self.head.next
            index -= 1

        node = self.head
        self.head = dummy

        return node


    animations = [
        lookup,
        insert,
        insertFirst,
        remove,
        removeFirst,
        delete
    ]
    
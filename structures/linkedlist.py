class LinkedList(object):
    """Implementation of linked list with standard methods"""
    _title = "Linked list"

    class Node(object):
        """Single node of the linked list with a value"""
        def __init__(self, val):
            """
            Initialise a node

            :param val: data held in the node
            :type val: T
            """
            self.val = val
            self.next = None


    def __init__(self, vals=[]):
        """
        Initialise a linked list given an array of values

        :param vals: values for the list
        :type vals: T[]
        """
        self.length = len(vals)

        if not vals:
            self.head = None
            return

        self.head = LinkedList.Node(vals[0])

        dummy = self.head

        for v in vals[1:]:
            self.head.next = LinkedList.Node(v)
            self.head = self.head.next

        self.head = dummy
        self.iter = self.head


    def __iter__(self):
        """Iterator"""
        self.iter = self.head
        return self


    def __next__(self):
        """For iterator"""
        if not self.iter:
            raise StopIteration
        else:
            prev = self.iter
            self.iter = self.iter.next
            return prev


    def __repr__(self):
        """Return representation of the linked list"""
        return "LinkedList([" + ','.join([str(n.val) for n in self]) + "])"


    def __str__(self):
        """Return str(self)"""
        return ' -> '.join([str(n.val) for n in self])


    def lookup(self, n):
        """
        Find the n-th value in the list

        Returns an error if n is out of bounds of the linked list

        :param n: index to get
        :type n: int
        """
        if n > self.length-1:
            raise IndexError("index out of range")
        else:
            dummy = self.head

            for i in range(n):
                dummy = dummy.next

            return dummy.val


    def insert(self, val, p): 
        """
        Insert a value to a new node after the given node p

        :param val: value to be inserted
        :param p: predecessor node
        :type val: T
        :type p: Node
        """
        current_successor = p.next
        p.next = LinkedList.Node(val)
        p.next.next = current_successor

        self.length += 1


    def insertFirst(self, val):
        """
        Insert a value at the beginning of the list

        :param val: value to be inserted
        :type val: T
        """
        new_head = LinkedList.Node(val)
        new_head.next = self.head
        self.head = new_head

        self.length += 1


    def remove(self, p):
        """
        Remove a node after the given node if it exists

        :param p: predecessor node
        :type p: Node
        """
        if p.next:
            p.next = p.next.next
            self.length -= 1


    def removeFirst(self):
        """Remove the first node of the list if it exists"""
        if self.head:
            self.head = self.head.next
            self.length -= 1


    def delete(self, target):
        """
        Delete the first value val if it can be found in the list

        :param target: value to be deleted
        :type target: T
        """
        dummy = self.head

        if self.head.val == target:
            self.head = self.head.next
            self.length -= 1
        else:
            while self.head.next:
                if self.head.next.val == target:
                    self.head.next = self.head.next.next
                    self.length -= 1
                    break

                self.head = self.head.next

            self.head = dummy


    def _show(self, canvas):
        """Show the linked list in canvas"""
        # function for drawing an arrow
        def draw_arrow(start_x, start_y):
            canvas.create_line((start_x, start_y), (start_x+50, start_y))
            canvas.create_polygon((start_x+37, start_y+5), (start_x+50, start_y), (start_x+37, start_y-5))

        for i, node in enumerate(self):
            # node
            canvas.create_rectangle(100*i+50, canvas.winfo_reqheight()//2-25, 100*i+100, canvas.winfo_reqheight()//2+25, fill="white")
            # value in the node
            canvas.create_text(100*i+75, canvas.winfo_reqheight()//2, text=str(node.val))

            if i < self.length-1:
                # arrow between nodes
                draw_arrow(100*i+100, canvas.winfo_reqheight()//2)
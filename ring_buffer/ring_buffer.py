from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check to see if the capacity is greater than the length of nodes in the dll
        if self.capacity > self.storage.length:
            # if it is  than we can add to the storage
            # we would add to the tail(newest)
            self.storage.add_to_tail(item)
            # then the head(oldest) would become current
            self.current = self.storage.head

        # elif if capacity and storage are equal we need to
        elif self.capacity == self.storage.length:
            # remove the head
            self.storage.remove_from_head()
        # add new item to the head
            self.storage.add_to_head(item)
        # head equals new item
            self.storage.head = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # we need to return the list of all the items value
        # run a loop while there is a head
        var_head = self.storage.head
        # we want to kick out of loop once there is no next, so eventual var_head will = None at the end of the loop
        while var_head is not None:
            # append the head to the list
            list_buffer_contents.append(var_head)
        # run through the head.next
            var_head = var_head.next
        # return the list
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

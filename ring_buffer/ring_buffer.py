from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def __repr__(self):
        return f"cap:{self.capacity}, curr:{self.current}, stor:{self.storage}"

    def append(self, item):
        # check to see if the capacity is greater than the length of nodes in the dll
        if self.capacity > self.storage.length:
            # if it is  than we can add to the storage
            # we would add to the tail(newest) until we hit capacity
            self.storage.add_to_tail(item)
            # The head(oldest) would become current
            self.current = self.storage.head

        # elif if capacity and storage are equal we need to
        elif self.capacity == self.storage.length:
            # check to see if capacity is the head
            if self.current == self.storage.head:
                # remove the head
                self.storage.remove_from_head()
                # add new item to the head
                self.storage.add_to_head(item)
                # move current forward one
            elif self.current == self.storage.tail:
                # remove tail
                self.storage.remove_from_tail()
                # insert item to tail
                self.storage.add_to_tail(item)
                # # current becomes head
                # self.current = self.storage.head
            else:

                # insert item after the previous
                self.current.insert_after(item)
                # increase the length since insert does not
                self.storage.length += 1
                # currnt equal current previous
                self.current = self.current.next
                # delent current next
                self.storage.delete(self.current.prev)

            self.current = self.current.next
            if self.current == None:
                self.current = self.storage.head

        # # Version 1 = current is always the newest
        # # while storage is less than capacity
        # if self.storage.length < self.capacity:
        #     # add item to tail
        #     self.storage.add_to_tail(item)
        #     # tail becomes current(newest)
        #     self.current = self.storage.tail

        #     # if storage is equal to capacity
        # elif self.storage.length == self.capacity:

        #     if self.current is self.storage.tail:
        #         # remove oldest item from head
        #         self.storage.remove_from_head()
        #         # add newest item to head
        #         self.storage.add_to_head(item)
        #         # move current forward to head which is newest
        #         self.current = self.storage.head
        #     else:
        #         # insert item after the current
        #         self.current.insert_after(item)
        #         # keep track of increase in storage
        #         self.storage.length += 1
        #         # move current forward to be the newest node
        #         self.current = self.current.next
        #         # delete the node in front(oldest) and delete will auto decrease length of storage
        #         self.storage.delete(self.current.next)

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
            list_buffer_contents.append(var_head.value)

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


# # check to see if the capacity is greater than the length of nodes in the dll
#         if self.capacity > self.storage.length:
#             # if it is  than we can add to the storage
#             # we would add to the tail(newest) until we hit capacity
#             self.storage.add_to_tail(item)
#             # The head(oldest) would become current
#             self.current = self.storage.head

#         # elif if capacity and storage are equal we need to
#         elif self.capacity == self.storage.length:
#             # remove the head
#             self.storage.remove_from_head()
#             # add new item to the head
#             self.storage.add_to_head(item)
#             # move current forward one
#             self.current = self.current.next

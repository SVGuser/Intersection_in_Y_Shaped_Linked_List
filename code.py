class Solution:
    def intersectPoint(self, head1, head2):
        temp1 = head1
        temp2 = head2

        # Traverse until both pointers meet
        while temp1 != temp2:
            temp1 = head2 if temp1 is None else temp1.next
            temp2 = head1 if temp2 is None else temp2.next

        # Return the intersection node (or None if no intersection)
        return temp1

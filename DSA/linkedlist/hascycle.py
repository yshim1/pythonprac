class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # memset = set() This solution is O(n) time and O(n) space
        # curr = head
        # while curr:
        #     if id(curr) in memset:
        #         return True
        #     memset.add(id(curr))
        #     curr = curr.next
        # return False
        fast, slow = head, head
        while fast and fast.next: #We want fast to move twice as fast
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
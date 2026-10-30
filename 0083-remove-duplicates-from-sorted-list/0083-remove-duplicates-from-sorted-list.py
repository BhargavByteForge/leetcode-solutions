class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head is None:                
            return head
        p = head                       
        while p.next:                   
            if p.val == p.next.val:     
                p.next = p.next.next    
            else:
                p = p.next              
        return head                     
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap, res = {}, Node(0)
        nodePtr = res
        while head:
            # create the node
            newNode = Node(head.val)
            nodePtr.next = newNode
            # populate the node map
            nodeMap[head] = newNode
            # advance the pointer
            nodePtr = newNode
            head = head.next
        
        
        for oldNode, newNode in nodeMap.items():
            oldRandom = oldNode.random
            if oldRandom:
                newRandom = nodeMap[oldRandom]
                newNode.random = newRandom
            else:
                newNode.random = None

        return res.next
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        // Edge cases: empty list, single element, or no rotation needed
        if (head == null || head.next == null || k == 0) {
            return head;
        }

        // 1. Compute the length of the list and locate the tail node
        int length = 1;
        ListNode tail = head;
        while (tail.next != null) {
            tail = tail.next;
            length++;
        }

        // 2. Normalize k to prevent unnecessary full rotations
        k = k % length;
        if (k == 0) {
            return head;
        }

        // 3. Connect tail to head to form a cycle
        tail.next = head;

        // 4. Find the new tail: (length - k - 1) steps from head
        int stepsToNewTail = length - k - 1;
        ListNode newTail = head;
        for (int i = 0; i < stepsToNewTail; i++) {
            newTail = newTail.next;
        }

        // 5. Break the cycle and assign the new head
        ListNode newHead = newTail.next;
        newTail.next = null;

        return newHead;
    }
}
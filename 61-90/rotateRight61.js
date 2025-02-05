class ListNode {
    constructor(val) {
        this.val = val;
        this.next = null;
    }

    toString() {
        const result = [];
        let current = this;
        while (current) {
            result.push(current.val);
            current = current.next;
        }
        return result.join("->");
    }
}



class Solution {
    rotateRight(head, k) {
        if (!head || ! head.next || k === 0) return head;

        // count the number of nodes and find the tail
        let count = 1;
        let tail = head;
        while (tail.next) {
            count++;
            tail = tail.next;
        }
        k %= count;
        if (k === 0) return head;
        //find the new tail
        let newTail = head
        for (let i = 0; i < count - k - 1; i++) {
            newTail = newTail.next;
        }
        
        // New head is the next node of the new tail
        const newHead = newTail.next;
        newTail.next = null;
        tail.next = head;
        console.log('newHead', newHead);
        return newHead;

    }
}

function createLinkedList(values) {
    if (!values || values.length === 0) {
        return null;
    }
    const head = new ListNode(values[0]);
    let current = head;
    for (let i = 1; i < values.length; i++) {
        current.next = new ListNode(values[i]);
        current = current.next;
    }
    console.log('head', head);
    return head;
}


function printLinkedList(head) {
    if (!head) {
        console.log("Empty list");
        return;
    }
    console.log(head.toString())
}

(function() {
    const inputList = [1, 2, 3, 4, 5];
    const k = 2;
    const head = createLinkedList(inputList);
    // rotate the list
    const solution = new Solution();
    const rotateHead = solution.rotateRight(head, k);
    printLinkedList(rotateHead);
})();

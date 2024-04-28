# Queue

_**Queue** is a linear data structure, that follows **First In First Out (FIFO)** principle._

Imagine it as a line, where people join at one end and exit from the other end. Similarly, elements are added to the rear of the queue and removed from the front.

Here are some key points about queues:
1. **Basic Operations of a Queue**:
    - **Enqueue (Insert)**: Adds an element to the rear of the queue.
    - **Dequeue (Delete)**: Removes and returns the element from the front of the queue.
    - **Peek**: Returns the element at the front of the queue without removing it.
    - **isEmpty**: Checks if the queue is empty.
    - **isFull**: Checks if the queue is full (though some implementations don't have a fixed size).
  
2. **Applications of Queues**:
    - **Task Scheduling in Operating Systems**: Queues help manage processes waiting to execute.
    - **Data Transfer in Network Communication**: Queues handle data packets waiting for transmission.
    - **Simulation of Real-World Systems**: For example, modeling waiting lines at a bank or supermarket.
    - **Priority Queues**: Used for event processing, where events have different priorities.
  
3. **Implementations**:
    - Queues can be implemented using various data structures:
        - **Arrays**: FIxed-size arrays with pointers to the front and rear.
        - **Linked Lists**: Dynamic queues using singly or doubly linked lists.
        - **Cirular Buffers**: Efficient for bounded-size queues.
        - **Other Variants**: Dequeues (double-ended queues), priority queues, etc.
     
4. **Examples**:
    - Suppose you're building a print job scheduler. Each print job gets added to the queue, and the printer processes them in order.
    - In a messaging app, messages arrive in a queue and are displayed to users in the order they were received.

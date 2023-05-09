package algo

type CircleQueue struct {
	items []any
	head  int
	tail  int
}

func (q *CircleQueue) IsEmpty() bool {
	return q.head == q.tail
}

func (q *CircleQueue) IsFull() bool {
	return (q.tail+1)%len(q.items) == q.head
}

func (q *CircleQueue) Rare() any {
	if q.IsEmpty() {
		return nil
	}

	return q.items[(q.tail-1+len(q.items))%len(q.items)]
}

func (q *CircleQueue) Front() any {
	if q.IsEmpty() {
		return nil
	}

	return q.items[q.head]
}

func (q *CircleQueue) Enqueue(i any) bool {
	if q.IsFull() {
		return false
	}
	q.items[q.tail] = i
	q.tail = (q.tail + 1) % len(q.items)
	return true
}

func (q *CircleQueue) Dequeue() any {
	if q.IsEmpty() {
		return nil
	}

	q.head = (q.head + 1) % len(q.items)
}

package algo

type LinearQueue struct {
	items []int
}

func (q *LinearQueue) Enqueue(i int) bool {
	q.items = append(q.items, i)
	return true
}

func (q *LinearQueue) Dequeue() int {
	toRemove := q.items[0]
	q.items = q.items[1:len(q.items)]
	return toRemove
}

package algo

type Queue interface {
	Enqueue(item any) bool
	Dequeue() any
}

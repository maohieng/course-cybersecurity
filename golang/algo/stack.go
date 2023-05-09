package algo

type Stack struct {
	// define the stack
	items []any
}

func (s *Stack) Push(item any) {
	// append the item to the stack
	s.items = append(s.items, item)
}

func (s *Stack) Pop() any {
	// check if the stack is empty
	if len(s.items) == 0 {
		return -1
	}
	// get the top item
	topItem := s.items[len(s.items)-1]

	// remove the top item
	s.items = s.items[:len(s.items)-1]
	return topItem
}

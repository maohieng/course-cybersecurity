package main

import "github.com/maohieng/cyber-course/algo"

func main() {
	s := algo.Stack{}

	println("Push 1 into stack")
	s.Push(1)

	println("Push 2 into stack")
	s.Push(2)

	println("Push 3 into stack")
	s.Push(3)

	println(s.Pop())
	println(s.Pop())
	println(s.Pop())
	println(s.Pop())
}

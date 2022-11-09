package main

import (
	"fmt"

	ll "github.com/asadlive84/dsa/check"
)

type linked interface {
	Insert(data int)
	ShowData() []int
	GetData(data int) bool
	Pop()
}

type Service struct {
	Linked linked
}

func main() {

	llist := &ll.LinkedList{}

	s := Service{
		Linked: llist,
	}

	s.Linked.Insert(1)
	s.Linked.Insert(2)
	s.Linked.Insert(3)
	s.Linked.Insert(4)
	s.Linked.Insert(5)
	s.Linked.Insert(6)
	fmt.Println(s.Linked.ShowData())

	// l.Pop()
	fmt.Println(s.Linked.ShowData())
	// fmt.Println(l.GetData(3))

}

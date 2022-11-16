package main

import (
	"fmt"

	"github.com/asadlive84/linkedlist/singlelinklist"
)

type LinkedList interface {
	Insert(prevData, data int) bool
	Append(data int)
	Show() []int
	Pop()
	Get(data int) interface{}
	Remove(data int) bool
}

type Server struct {
	LinkedList LinkedList
}

func main() {

	ll := &singlelinklist.LinkedList{}

	s := Server{
		LinkedList: ll,
	}

	s.LinkedList.Append(1)
	s.LinkedList.Append(2)
	s.LinkedList.Append(3)
	// s.LinkedList.Append(2)
	// s.LinkedList.Append(5)
	// s.LinkedList.Append(8)
	// s.LinkedList.Append(9)
	// s.LinkedList.Append(7)
	fmt.Printf("Show %+v\n", s.LinkedList.Show())
	// s.LinkedList.Insert(1,22)
	fmt.Printf("%+v\n", s.LinkedList.Insert(2, 62))
	fmt.Printf("%+v\n", s.LinkedList.Insert(1, 62))
	fmt.Printf("Show %+v\n", s.LinkedList.Show())

}

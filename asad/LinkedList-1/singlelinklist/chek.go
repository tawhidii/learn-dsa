package singlelinklist

import "fmt"

type Node struct {
	Data int
	Next *Node
}

type LinkedList struct {
	Head   *Node
	Length int
}

func (ll *LinkedList) Get(data int) interface{} {
	if ll.Head == nil {
		return false
	}

	tmp := ll.Head

	for i := 0; i <= ll.Length; i++ {
		if tmp != nil {
			if tmp.Data == data {
				return tmp.Data
			}
			tmp = tmp.Next
		}

	}

	return false
}

func (ll *LinkedList) Remove(data int) bool {
	if ll.Head == nil {
		return false
	}
	get := ll.Get(data)
	if _, ok := get.(bool); ok {
		return false
	}

	if _, ok := get.(int); ok {

		tmp := ll.Head
		nextData := tmp.Next
		if tmp.Data == data {
			ll.Head = nextData
			ll.Length--
			tmp = nil
			return true

		}
		prevData := ll.Head
		for i := 0; i < ll.Length; i++ {
			if nextData != nil && nextData.Data == data {
				if nextData.Next == nil {
					prevData.Next = nil
					ll.Length--
					return true
				}
				prevData.Next = nextData.Next
				nextData = nil
				ll.Length--
				return true
			}
			prevData = prevData.Next
			nextData = nextData.Next
		}

		return false
	}

	return false

}

func (ll *LinkedList) Pop() {
	if ll.Head == nil {
		return
	}

	prevData := ll.Head
	nextData := prevData.Next
	for i := 0; i < ll.Length; i++ {
		if nextData != nil {
			prevData = prevData.Next
			nextData = nextData.Next
		}
	}
	prevData.Next = nil
	ll.Length--
	return

}

func (ll *LinkedList) Insert(prevData, data int) bool {
	prevD := ll.Get(prevData)
	if _, ok := prevD.(bool); ok {
		return false
	}

	if _, ok := prevD.(int); ok {
		nextData := ll.Head.Next
		if ll.Head.Data == prevData {
			if nextData != nil {
				node := Node{Data: data, Next: nextData}
				ll.Head.Next = &node
				ll.Length++
				return true
			}
			node := &Node{Data: data, Next: nil}
			ll.Head.Next = node
			ll.Length++
			return true

		}
		tmpData := ll.Head
		for i := 0; i < ll.Length; i++ {
			fmt.Println("======> data, ", tmpData.Data,"===", data)
			if tmpData.Data == prevData {
				fmt.Println("Hello")
				tmpData.Next = &Node{
					Data: data,
					Next: nextData,
				}
				ll.Length++
				return true
			}
			fmt.Printf("tmpData %+v\n", tmpData)
			fmt.Printf("nextData %+v\n", nextData)
			tmpData = tmpData.Next
			if nextData != nil {
				nextData = tmpData.Next
			}
		}
	}

	return false
}

func (ll *LinkedList) Append(data int) {
	node := &Node{
		Data: data,
	}
	if ll.Head == nil {
		ll.Head = node
		ll.Length++
		return
	}

	tmp := ll.Head
	for i := 0; i < ll.Length; i++ {
		if tmp.Next != nil {
			tmp = tmp.Next
		}
	}
	tmp.Next = node
	ll.Length++
	return
}

func (ll *LinkedList) Show() []int {
	data := make([]int, 0, 0)
	if ll.Head == nil {
		return data
	}
	tmp := ll.Head
	for i := 0; i < ll.Length; i++ {
		if tmp != nil {
			data = append(data, tmp.Data)
			tmp = tmp.Next
		}

	}

	return data
}

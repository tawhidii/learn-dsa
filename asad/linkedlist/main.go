package main

// import "fmt"

// type Node struct {
// 	Data int64
// 	Next *Node
// }

// type LinkedList struct {
// 	Head *Node
// 	Len  int64
// }

// func (l *LinkedList) Insert(data int64) {
// 	n := Node{}
// 	n.Data = data

// 	if l.Len == 0 {
// 		l.Head = &n
// 		l.Len++
// 		return
// 	}

// 	ptr := l.Head

// 	for i := 0; i < int(l.Len); i++ {
// 		if ptr.Next == nil {
// 			ptr.Next = &n
// 			l.Len++
// 			return
// 		}
// 		ptr = ptr.Next
// 	}
// }

// func (l *LinkedList) InsertAtBegin(data int64) {
// 	node := &Node{
// 		Data: data,
// 	}
// 	if l.Head == nil {
// 		l.Head = node
// 		l.Head.Next = nil
// 		l.Len++
// 		return
// 	}

// 	tmp := l.Head
// 	l.Head = node
// 	l.Head.Next = tmp
// 	l.Len++
// 	return

// }

// func (l *LinkedList) Show() string {
// 	if l.Len <= 0 {
// 		return "nothing found"
// 	}

// 	var text string
// 	ptr := l.Head
// 	for i := 0; i < int(l.Len); i++ {
// 		if ptr == nil {
// 			return ""
// 		}
// 		text += fmt.Sprintf("%d--->", ptr.Data)
// 		ptr = ptr.Next
// 	}
// 	return text
// }

// func main() {

// 	ll := LinkedList{}

// 	ll.InsertAtBegin(1)
// 	ll.InsertAtBegin(2)
// 	ll.Insert(88)
// 	// ll.InsertAtBegin(3)
// 	// ll.InsertAtBegin(4)

// 	fmt.Println(ll.Show())

// }

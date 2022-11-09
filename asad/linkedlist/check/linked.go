package check

type Node struct {
	Data int
	Next *Node
}

type LinkedList struct {
	Head   *Node
	Tail   *Node
	Length int
}

// func (l *LinkedList) Prepand(data int) {
// 	if l.Head == nil {
// 		return
// 	}
// 	tmp := l.Head
// 	for i := 0; i < l.Length; i++ {

// 	}
// }

func (l *LinkedList) Insert(data int) {
	node := &Node{}
	node.Data = data
	if l.Head == nil {
		l.Head = node
		l.Tail = node
		l.Length++
		return
	}

	tmp := l.Head
	for i := 0; i < l.Length; i++ {
		if tmp.Next == nil {
			tmp.Next = node
			l.Tail = node
			l.Length++
			return
		}
		tmp = tmp.Next
	}
	return

}

func (l *LinkedList) ShowData() []int {
	tmp := l.Head
	listData := make([]int, 0, 0)
	for i := 0; i < l.Length; i++ {

		listData = append(listData, tmp.Data)
		tmp = tmp.Next
	}
	return listData

}

func (l *LinkedList) GetData(data int) bool {
	tmp := l.Head
	if tmp == nil {
		return false
	}

	for i := 0; i < l.Length; i++ {
		if tmp.Data == data {
			return true
		}
		tmp = tmp.Next
	}
	return false
}

func (l *LinkedList) Pop() {
	if l.Head == nil {
		return
	}
	prevData := l.Head
	nextData := prevData.Next
	for i := 0; i < l.Length; i++ {
		if nextData == nil {
			l.Head = nil
			l.Length--
			return
		}
		if nextData.Next == nil {
			prevData = nil
			l.Length--
			return
		}
		nextData = nextData.Next
		prevData = prevData.Next
	}
	return

}

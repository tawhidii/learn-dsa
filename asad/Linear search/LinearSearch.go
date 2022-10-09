package main

import "fmt"

type MySlice struct {
	AllData []int
	target  int
}

func main() {

	mySlice := MySlice{
		AllData: []int{1, 2, 3, 4, 5, 6, 7, 8, 9},
		target:  2,
	}

	if mySlice.linearSearch() {
		fmt.Println("data is found!")

	} else {
		fmt.Println("data is not found")
	}

}

func (m *MySlice) linearSearch() bool {

	for data := range m.AllData {
		if data == m.target {
			return true
		}
	}
	return false
}

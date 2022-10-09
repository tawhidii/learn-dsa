package main

import (
	"fmt"
	"strings"
)

func ransomNotes(magazine []string, note []string) {
	magazineMap := make(map[string]int)
	for _, value := range magazine {
		if _, ok := magazineMap[value]; ok {
			magazineMap[value] = magazineMap[value] + 1
			continue
		}
		magazineMap[value] = 1

	}
	for _, value := range note {
		if _, ok := magazineMap[value]; !ok {
			fmt.Println("No")
			return
		}
		magazineMap[value] = magazineMap[value] - 1
	}
	// fmt.Println(magazineMap)
	for _, val := range magazineMap {
		if val < 0 {
			fmt.Println("No")
			return
		}
	}

	fmt.Println("Yes")

}

func main() {
	magazine := strings.Split("ive got a lovely bunch of coconuts", "")
	notes := strings.Split("ive got some coconuts", "")
	ransomNotes(magazine, notes)

}

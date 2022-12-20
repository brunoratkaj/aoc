package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error while reading file")
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var sumPriorities int
	for scanner.Scan() {
		hash := make(map[rune]int)
		line := scanner.Text()
		for _, char := range line {
			hash[char] = 1
		}
		scanner.Scan()
		line = scanner.Text()
		for _, char := range line {
			val, ok := hash[char]
			if ok && val == 1 {
				hash[char] = 2
			}
		}
		scanner.Scan()
		line = scanner.Text()
		for _, char := range line {
			val, ok := hash[char]
			if ok && val == 2 {
				hash[char] = 3
			}
		}
		var item rune
		for char, val := range hash {
			if val == 3 {
				item = char
				break
			}
		}
		if item >= 97 && item <= 122 {
			item -= 96
		} else {
			item -= 38
		}
		sumPriorities += int(item)
	}
	fmt.Println(sumPriorities)
}

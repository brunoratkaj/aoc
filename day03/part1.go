package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
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
		line := scanner.Text()
		firstHalf := line[:len(line)/2]
		secondHalf := line[len(line)/2:]
		var item rune
		for _, char := range firstHalf {
			if strings.Contains(secondHalf, string(char)) {
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

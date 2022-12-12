package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var newScoring = map[string]int{
	// 1, // Rock score
	// 2, // Paper score
	// 3, // Scissors score
	"AX": 0 + 3, // Lose against Rock - Scissors
	"AY": 3 + 1, // Draw against Rock - Rock
	"AZ": 6 + 2, // Win against Rock - Paper
	"BX": 0 + 1, // Lose against Paper - Rock
	"BY": 3 + 2,
	"BZ": 6 + 3,
	"CX": 0 + 2, // Lose against Scissors - Paper
	"CY": 3 + 3,
	"CZ": 6 + 1,
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error while reading file")
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	score := 0
	for scanner.Scan() {
		hands := strings.Fields(scanner.Text())
		score += newScoring[hands[0]+hands[1]]
	}
	fmt.Printf("Final score is: %d", score)
}

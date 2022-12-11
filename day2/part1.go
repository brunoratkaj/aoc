package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var scoring = map[string]int{
	"X":  1, // Rock
	"Y":  2, // Paper
	"Z":  3, // Scissors
	"AX": 3, // Rock Rock
	"AY": 6,
	"AZ": 0,
	"BX": 0, // Paper Rock
	"BY": 3,
	"BZ": 6,
	"CX": 6, // Scissors Rock
	"CY": 0,
	"CZ": 3,
}

func result(myHand string, oppHand string) int {
	return scoring[myHand] + scoring[oppHand+myHand]
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
		score += result(hands[1], hands[0])
	}
	fmt.Printf("Final score is: %d", score)
}

package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Monkey struct {
	name            string
	items           []int
	operator        string
	operationNumber int
	divisor         int
	trueMonkey      int
	falseMonkey     int
	inspects        int
}

func extractMonkey(scanner *bufio.Scanner, monkeys *[]Monkey, count int) {
	monkey := Monkey{name: strconv.Itoa(count)}

	scanner.Scan() // Monkey items
	line := scanner.Text()
	r, _ := regexp.Compile(".*:\\s*(?P<items>.*)")
	matches := r.FindStringSubmatch(line)
	itemsStrings := strings.Split(matches[r.SubexpIndex("items")], ", ")
	itemsInts := make([]int, len(itemsStrings))
	for i, s := range itemsStrings {
		itemsInts[i], _ = strconv.Atoi(s)
	}
	monkey.items = itemsInts

	scanner.Scan() // Monkey operation and operation number
	line = scanner.Text()
	r, _ = regexp.Compile(".*(?P<operator>\\*|\\+)\\s*(?P<number>.*)")
	matches = r.FindStringSubmatch(line)
	operator := matches[r.SubexpIndex("operator")]
	operationNumber := matches[r.SubexpIndex("number")]
	var number int
	if operationNumber == "old" {
		number = -1
	} else {
		number, _ = strconv.Atoi(matches[r.SubexpIndex("number")])
	}
	monkey.operator = operator
	monkey.operationNumber = number

	// regex for the next three lines
	r, _ = regexp.Compile(".*?(?P<number>\\d+$)")

	scanner.Scan() // Monkey divisor
	line = scanner.Text()
	matches = r.FindStringSubmatch(line)
	number, _ = strconv.Atoi(matches[r.SubexpIndex("number")])
	monkey.divisor = number

	scanner.Scan() // Monkey to throw to if true
	line = scanner.Text()
	matches = r.FindStringSubmatch(line)
	monkeyName, _ := strconv.Atoi(matches[r.SubexpIndex("number")])
	monkey.trueMonkey = monkeyName

	scanner.Scan() // Monkey to throw to if false
	line = scanner.Text()
	matches = r.FindStringSubmatch(line)
	monkeyName, _ = strconv.Atoi(matches[r.SubexpIndex("number")])
	monkey.falseMonkey = monkeyName

	*monkeys = append(*monkeys, monkey)
}

func processMonkey(monkey Monkey, monkeys *[]Monkey, mod int) Monkey {
	for _, item := range monkey.items {
		var worry int
		var operationNumber int
		if monkey.operationNumber == -1 {
			operationNumber = item
		} else {
			operationNumber = monkey.operationNumber
		}
		if monkey.operator == "*" {
			worry = (item * operationNumber) % mod
		} else {
			worry = (item + operationNumber) % mod
		}
		// fmt.Println(worry)
		rem := worry % monkey.divisor
		if rem == 0 {
			(*monkeys)[monkey.trueMonkey].items = append((*monkeys)[monkey.trueMonkey].items, worry)
		} else {
			(*monkeys)[monkey.falseMonkey].items = append((*monkeys)[monkey.falseMonkey].items, worry)
		}
		monkey.inspects++
	}
	monkey.items = []int{}
	return monkey
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error while reading file")
		panic(err)
	}
	defer file.Close()

	var monkeys []Monkey
	count := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		extractMonkey(scanner, &monkeys, count)
		count++
		scanner.Scan()
	}
	mod := 1
	for _, monkey := range monkeys {
		mod *= monkey.divisor
	}
	for i := 0; i < 10000; i++ {
		for idx, monkey := range monkeys {
			monkey = processMonkey(monkey, &monkeys, mod)
			monkeys[idx] = monkey
		}
	}

	var inspects []int
	for _, monkey := range monkeys {
		inspects = append(inspects, monkey.inspects)
	}
	fmt.Println(inspects)
}

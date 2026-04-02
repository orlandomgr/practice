package main

import (
    "fmt"
    // "bufio"
    // "io"
    // "os"
    // "strconv"
    // "strings"
)

/*
 * Complete the 'permutationEquation' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY p as parameter.
 */

func permutationEquation(p []int32) []int32 {
    // Write your code here
	var n int32 = int32(len(p))
	fmt.Println(n)
	result := make([]int32, n) 
	for _, i := range p {
		result[p[p[i - 1] - 1] - 1] = i
	}
	return result
}	

func main() {
	var p = []int32{2, 3, 1}
	fmt.Println(permutationEquation(p))


}
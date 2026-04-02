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
 * Complete the 'circularArrayRotation' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER k
 *  3. INTEGER_ARRAY queries
 */

func shiftRight(s []int32, n int32) []int32 {
    if len(s) == 0 { return s }
	var lens32 int32 = int32(len(s))
    n = n % lens32
    return append(s[lens32-n:], s[:lens32-n]...)
}

func circularArrayRotation(a []int32, k int32, queries []int32) []int32 {
    // Write your code here
	var result = []int32{}
	var n int32 = int32(len(a))
	k = k % n
	a = shiftRight(a, k)

	for _, i := range queries{
		result = append(result, a[i])
	}

	return result 
}

	
func main() {
	var a = []int32{1, 2, 3}
	var k int32 = 2
	var q = []int32{0, 1, 2}
	var result = circularArrayRotation(a, k, q)
	fmt.Println(result)
}

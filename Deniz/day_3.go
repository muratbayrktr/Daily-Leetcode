package main

import "fmt"

func subsets(nums []int) [][]int {
    result := [][]int{{}}
    
    for _, num := range nums {
        currentSize := len(result)
        for i := 0; i < currentSize; i++ {
            newSubset := make([]int, len(result[i]), len(result[i])+1)
            copy(newSubset, result[i])
            newSubset = append(newSubset, num)

            result = append(result, newSubset)
        }
    }
    
    return result
}
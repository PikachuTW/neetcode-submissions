func hasDuplicate(nums []int) bool {
    occured := map[int]bool{}

    for _, num := range nums {
        if occured[num] {
            return true
        }
        occured[num] = true
    }

    return false
}

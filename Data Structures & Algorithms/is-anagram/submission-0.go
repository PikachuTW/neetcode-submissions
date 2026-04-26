func isAnagram(s string, t string) bool {
    times := map[rune]int{}
    for _, c := range s {
        times[c] += 1
    }
    for _, c := range t {
        times[c] -= 1
        if times[c] == 0 {
            delete(times, c)
        }
    }
    return len(times) == 0
}

impl Solution {
    pub fn min_changes(s: String) -> i32 {
        s.as_bytes()
            .chunks(2)
            .filter(|chunk| chunk[0] != chunk[1])
            .count() as i32
    }
}
var getPermutation = function(n, k) {
    const numbers = [];
    const factorial = [1];
    
    // Precompute factorials and populate numbers array
    for (let i = 1; i <= n; i++) {
        numbers.push(i);
        if (i < n) {
            factorial[i] = factorial[i - 1] * i;
        }
    }
    
    // Convert k to 0-indexed
    k--;
    
    let result = '';
    
    for (let i = n; i > 0; i--) {
        const blockSize = factorial[i - 1];
        const index = Math.floor(k / blockSize);
        
        result += numbers[index];
        numbers.splice(index, 1);
        
        k %= blockSize;
    }
    
    return result;
};
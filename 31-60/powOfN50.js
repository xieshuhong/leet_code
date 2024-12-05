function powOfN(x, n) {

    function helper(x, n) {
        if (x == 0) return 0;
        if (n == 0) return 1;
    
        let res = helper(x*x, n >> 1)
        if (n%2) return x * res;
        else return res;
    }
    let res = helper(x, Math.abs(n));
     return (n >= 0? res : 1 / res)
}

console.log(powOfN(5, 3))


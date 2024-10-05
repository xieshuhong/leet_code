// interview question
const arr = [1, 1, 1, 2, 2, 3, 4, 1, 1, 3, 2, 9];


const counts = arr.reduce((acc, num) => {
        acc[num] = (acc[num] || 0) + 1;
        return acc;
}, {});


// console.log('acc', acc);
// console.log('acc[num]', acc[num]);
// console.log('acc2', acc);

console.log(counts);


const countsecond = {1: 0, 2: 0, 3: 0, 4: 0};

arr.forEach(num => {
    if (countsecond.hasOwnProperty(num)) countsecond[num]++;
});

console.log('countsecond', countsecond);
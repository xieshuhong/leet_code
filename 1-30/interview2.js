// function maxNumber(arr) {
//     let max = arr[0]
    
//     for (let i = 0; i < arr.length; i++) {
//         console.log('arr[i]', arr[i])
//         let num = Math.max(arr[i], max)
//         console.log('num', num);
//         max = num

//     }
//     return max;
// }

// let res = [1, 2, 3, 4, 5];
// let res1 = [-1, -2, -3, -4];
// console.log(maxNumber(res))


function hasTheSameLetter(str1, str2){
    let splitStr1 = str1.split("").sort().join("")
    let splitStr2 = str2.split("").sort().join("")

   return splitStr1 == splitStr2

}


let str1 = "listen";
let str2 = "silent";

let str3 = "hello";
let str4 = "world";
console.log(hasTheSameLetter(str3, str4));


// let arr1 = [1, 2, 3, 1, 2, 4];
// let arr2 = [5, 5, 5, 6, 7];


// function noRepeat(arr) {
//     console.log(Array.from(new Set(arr)));
// }

// noRepeat(arr1)
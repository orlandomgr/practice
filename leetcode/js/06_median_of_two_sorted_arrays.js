/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays2 = function (nums1, nums2) {
    let newArr = nums1.concat(nums2);
    newArr.sort((a, b) => a - b);
    let result = 0;
    let middle = Math.floor(newArr.length / 2);
    console.log(newArr + " " + middle);
    if (newArr.length === 1) {
        result = newArr[0];
    } else if (newArr.length % 2 === 0) {
        result = (newArr[middle - 1] + newArr[middle]) / 2;
    } else {
        result = newArr[middle];
    }
    return result;
};

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
    let newSize = nums1.length + nums2.length;

    if (newSize === 0) return 0;
    if (newSize === 1) {
        if(nums1.length === 1) {
            return nums1[0];
        }else{
            return nums2[0];
        }
    }

    let middle = Math.floor(newSize / 2);
    let newArr = [];
    n1=0;
    n2=0;
    for(let i = 0; i < middle + 1; i++) {
        let num1 = n1 < nums1.length ? nums1[n1] : Infinity;
        let num2 = n2 < nums2.length ? nums2[n2] : Infinity
        if(num1 > num2) {
            newArr.push(num2);
            n2++;
        } else {
            newArr.push(num1);
            n1++;
        }
    }
    if (newSize % 2 === 0) {
        return (newArr[middle - 1] + newArr[middle]) / 2;
    } else {
        return newArr[middle];
    }
};

// console.log(findMedianSortedArrays([1, 3], [2])); // Output: 2.0
// console.log(findMedianSortedArrays([1, 2], [3, 4])); // Output: 2.5
// console.log(findMedianSortedArrays([0, 0], [0, 0])); // Output: 0.0
// console.log(findMedianSortedArrays([], [1])); // Output: 1.0
console.log(findMedianSortedArrays([1,2,3,4,5], [6,7,8,9,10,11,12,13,14,15,16,17])); // Output: 9.0
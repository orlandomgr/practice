function fixHeap(heap) {
    index = heap.length - 1;
    while (index > 0) {
        let parent = Math.floor((index + 1) / 2) - 1;
        if (heap[parent].gain > heap[index].gain) {
            let temp = heap[parent];
            heap[parent] = heap[index];
            heap[index] = temp;
        }
        index = parent;
    }
}

function insertMinHeap(heap, value) {
    heap.push(value);
    fixHeap(heap);
}

function popMinHeap(heap) {
    return heap.shift();
}

function calculateGain(passes, students) {
    let extra = (passes + 1) / (students + 1);
    let current = passes / students;
    return extra - current;
}

/**
 * @param {number[][]} classes
 * @param {number} extraStudents
 * @return {number}
 */
var maxAverageRatio = function (classes, extraStudents) {
    let heap = [];
    let zeroHeap = [];
    let passes, students, gain = 0;
    let skip = classes.length > 1000;
    for (let i = 0; i < classes.length; i++) {
        passes = classes[i][0];
        students = classes[i][1]
        gain = calculateGain(passes, students);
        if (skip && (gain == 0 || students - passes > 10000 || (students > 10000 && students - passes == 1))) {
            zeroHeap.push({ gain, passes, students });
        } else {
            gain *= -1;
            insertMinHeap(heap, { gain, passes, students });
        }
    }
    let missing = 0;
    if (heap.length > 0) {
        while (extraStudents > 0) {
            let classPass = popMinHeap(heap);
            if (classPass) {
                passes = classPass.passes;
                students = classPass.students;
                gain = calculateGain(passes + 1, students + 1) * -1;
                passes++;
                students++;
                insertMinHeap(heap, { gain, passes, students });
            }else{
                missing++;
            }
            extraStudents--;
        }
    }
    if(zeroHeap.length > 0 && missing > 0){
        zeroHeap[0].passes += missing;
        zeroHeap[0].students += missing;
    }
    heap = heap.concat(zeroHeap);
    let totalPassRatio = 0;
    for (let i = 0; i < heap.length; i++) {
        totalPassRatio += (heap[i].passes / heap[i].students);
    }

    return (totalPassRatio / classes.length).toFixed(5);
};

// console.log(maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2)); 
// // 0.78333
// console.log(maxAverageRatio([[2, 4], [3, 9], [4, 5], [2, 10]], 4)); 
// // 0.53485
// console.log(maxAverageRatio([[547, 616], [419, 932], [121, 677], [285, 303], [255, 388], [573, 768], [5, 983], [195, 542], [450, 593], [22, 32], [643, 997], [249, 621], [267, 856], [178, 212], [152, 292], [206, 556], [280, 319], [600, 776], [257, 853], [458, 700], [811, 882], [829, 876], [173, 997], [366, 559], [431, 503], [125, 877], [214, 788], [585, 901], [210, 393], [291, 831], [111, 926], [25, 827], [121, 583], [14, 766], [304, 559], [691, 989], [742, 780], [665, 997], [77, 140], [383, 513], [587, 825], [319, 448], [516, 694], [366, 777], [332, 542], [1, 127], [453, 736], [359, 461], [313, 553], [348, 409], [749, 802], [586, 700], [116, 505], [664, 940], [387, 392], [209, 571], [4, 285], [613, 651], [740, 903], [757, 850], [524, 746], [204, 946], [473, 616], [530, 855], [419, 960], [730, 763], [313, 720], [175, 461], [635, 685], [203, 544], [369, 539], [4, 695], [399, 594], [437, 994], [345, 415], [637, 882], [599, 998]], 5554)); 
// // 0.64523
// console.log(maxAverageRatio([[739, 822], [235, 606], [105, 968], [326, 924], [23, 32], [27, 666], [10, 555]], 8)); 
// // 0.36881

console.log(maxAverageRatio([[13609,17094],[24079,89827]], 22159)); 
// 0.61455

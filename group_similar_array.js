let arr = [1, 2, 4, 591, 392, 391, 2, 5, 10, 2, 1, 1, 1, 20, 20];


arr.sort();

new_arr = [];

arr.reduce(function (r, current_item) {
    if (current_item !== r) {
        new_arr.push([]);
    }
    new_arr[new_arr.length - 1].push(current_item);
    return current_item;
}, undefined);)

// Output: [[1,1,1,1],[2,2],[3,3,3],4,[5,5],6]



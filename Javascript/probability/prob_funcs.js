//returns a number from 1 to num randomly.
function randrange(num) {
    return Math.floor((Math.random() * num) + 1);
}
//returns a number from x to y randomly, throws an error if x is y.
function rand_interval(x, y) {
    if(x===y) throw "Value Error";
    else {
        return Math.floor((Math.random() * y) + x);
    }
}
//returns an array of random numbers from num1 to num2.
function random_list(len, num1, num2) {
    var arr = [];
    for(i=0;i<len;i++) arr.push(rand_interval(num1, num2));
    return arr;
}
//returns a randomly sampled element from an array
function rand_sample(arr) {
    return arr[rand_interval(0, arr.length-1)]
}
//returns a randomly selected value from an object
function rand_obj_sample(obj) {
    var result = Object.keys(obj);
    return obj[result[rand_interval(0, result.length-1)]]
}
//generates a random permutation of a given lst
function rand_permutation(lst) {
    if(lst.length==0) throw "index error";
    else {
        var arr = [];
        for(i=0;i<lst.length;i++) arr.push(rand_sample(lst));
        return arr;
    }
}
//destructively returns a combo of lst. uses pop instead of random sampling
function rand_combo(lst) {
    if(lst.length==0) throw "index error";
    else {
        var arr =[];
        for(i=0;i<lst.length;i++) arr.push(lst.pop(lst[rand_interval(0, lst.length-1)]));
        return arr;
    }
}
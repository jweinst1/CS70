/* This file deals with objects and functions that represent the probability of counting balls and bins.
A ball is a string character, usually "*" or "b"
A bin will always be an array
 */

//object that implements a set of distinct bins.
var distbins = function(amount) {
    for(i=0;i<amount;i++) this[i] = [];
};
//function that returns a set of indisinct bins, as an array of arrays
function indistbins(amount) {
    arr = [];
    for(i=0;i<amount;i++) arr.push([]);
    return arr;
}
//creates an array of indisinct balls for sampling.
function ballset (amount) {
    arr = [];
    for(i=0;i<amount;i++) arr.push("*");
    return arr;
}
//iterator of a container of indistinct balls, useful for sampling.
var balliter = function(amount) {
    this.balls = ballset(amount);
    this.length = this.balls.length;
    this.next = function() {
        if(this.length==0) throw "Stop Iteration";
        else {
            return this.balls.pop();
        }
    }
};









//rand number functions------>>>>
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

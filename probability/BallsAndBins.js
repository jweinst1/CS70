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
    var arr = [];
    for(i=0;i<amount;i++) arr.push("*");
    return arr;
}
//iterator of a container of indistinct balls, useful for sampling.
var balliter = function(amount) {
    this.balls = ballset(amount);
    this.next = function() {
        if(this.length==0) throw "Stop Iteration";
        else {
            return this.balls.pop();
        }
    }
    this.hasnext = function() {
        if(this.balls.length==0) return false;
        else return true;
    }
};
//sets up a process of randomly distributing an indistinct amount of balls to indistinct bins, and
//returns the array of arrays for bins.
//[ [ '*', '*' ], [ '*' ], [ '*', '*', '*' ], [], [], [] ]
function indist_to_bin (balls, bins) {
    var bin = indistbins(bins);
    var machine = new balliter(balls);
    while (machine.hasnext()) bin[rand_interval(0, bin.length-1)].push(machine.next());
    return bin;
}

/* sets up a process similar to above, but with a distinct set of bins as an object. */
function to_dist_bin (balls, bins) {
    var bin = new distbins(bins);
    var machine = new balliter(balls);
    while (machine.hasnext()) bin[Object.keys(bin)[rand_interval(0, bin.length-1)]].push(machine.next());
    return bin;
}









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

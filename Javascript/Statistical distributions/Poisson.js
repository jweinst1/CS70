/**
 * Created by Josh on 12/14/15.
 */

//functions and objects for implementing the poisson distribution.

//creates a set of characters in a string, no qunatitative amoutn
var Char_set = function(string) {
    var chars = string.split("");
    for(var elem in chars) this[chars[elem]] = true;
};

//checks if a character occurs in a string.
function ischar(str, char) {
    var cset = new Char_set(str);
    return char in cset;
}
//splits a string by some partition length, len
function splitstr(string, len) {
    var patt = ".{1," + len.toString() + "}";
    var matcher = new RegExp(patt, "g");
    return string.match(matcher);
}
//gets mean value for lst.
function lst_mean(lst) {
    var n = 0;
    for(var num in lst) n+= lst[num];
    return n/lst.length;
}

//takes a string, and for every segment, calculates the average occurence of an elem
function poissontrial(str, segment, elem) {
    var chops = splitstr(str, segment);
    var counts = [];
    for(i=0;i<chops.length;i++) if(ischar(chops[i], elem)) {
        var occur = 0;
        for(j=0;j<chops[i].length;j++) if(chops[i][j]==elem) occur += 1;
        counts.push(occur);
    } else {
        counts.push(0);
    }
    return lst_mean(counts);
}
//tests for a high point
function hashighpoint(string) {

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

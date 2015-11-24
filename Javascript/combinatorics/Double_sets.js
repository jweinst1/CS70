/*
A double set is a set that contains elements that have more than one quality

Example:
    If { 0:true, 1:true, 2:true } is a single set, then a double set can be
 { red: { '1': true, '2': true, '3': true },
blue: { '4': true, '5': true, '6': true } }
 */



var double_set = function(name1, name2, arr1, arr2) {
    this[name1] = {};
    this[name2] = {};
    for(i=0;i<arr1.length;i++) this[name1][arr1[i]] = true;
    for(i=0;i<arr2.length;i++) this[name2][arr2[i]] = true;
};
//double set functions and operations.
var double_opers = {
    get_parents : function(dbset) {
        return Object.keys(dbset);
    },
    get_roots : function(dbset, parent) {
        return dbset[parent];
    },
    find_root : function(dbset, root) {
        for(var parent in dbset) if(root in dbset[parent]) return parent;
    },
    get_random_root : function (dbset) {
        var choices = Object.keys(dbset);
        choices = dbset[choices[rand_interval(0, choices.length)]];
        var select = Object.keys(choices);
        return choices[select[rand_interval(0, select.length)]];
    }
};






// { red: { '1': true, '2': true, '3': true },
//blue: { '4': true, '5': true, '6': true } }

//returns a number from x to y randomly, throws an error if x is y.
function rand_interval(x, y) {
    if(x===y) throw "Value Error";
    else {
        return Math.floor((Math.random() * y) + x);
    }
}


//impelmentations of basic combinatorial sets and operations on them.
//-------------------

//creates a set of elements, each distinct and non repeating.
var Set = function() {
    for(i=0;i<arguments.length;i++) this[arguments[i]] = true;
};
//converts an array to a set object
var to_set = function(elements) {
    for(i=0;i<elements.length;i++) this[elements[i]] = true;
};
//creates a set of elements, each distinct, non repeaitng, but also ordered.
var Orderedset = function() {
    for(i=0;i<arguments.length;i++) this[arguments[i]] = i;
};
//creates a set of elements, which are quantified to their amounts, but not ordered.
var quantset = function() {
    for(i=0;i<arguments.length;i++) this[arguments[i]] = count_elem(arguments, arguments[i]);
};
//-----------------

//implementation of set operations, like union, intersection, size, etc.
var set_opers = {
    size : function(elem) {
        return Object.keys(elem).length;
    },
    intersection : function(set1, set2) {
        var result = {};
        for(var key in set1) if(key in set2) result[key] = true;
        return result;
    },
    union : function(set1, set2) {
        var result = [];
        for(var key in set1) result.push(key);
        for(var key in set2) result.push(key);
        result = new to_set(result);
        return result;
    },
    union_all : function() {
        var result = [];
        for(var elem in arguments) {
            for(var key in arguments[elem]) result.push(key);
        }
        result = new to_set(result);
        return result;
    },
    intersection_all : function() {
        var input = arguments;
        while(input.length>1) {
            input[0] = set_opers.intersection(input[0], input[1]);
            delete input[1];
        }
        return input[0];
    },
    //deletes the elements in set1 if they are also in set2
    subtract : function(set1, set2) {
        for(var elem in set2) if (elem in set1) delete set1[elem];
        return set1;
    }
};




//returns true if set2 is contained in set1
function contained_in(set1, set2) {
    if(set_opers.size(set1) <= set_opers.size(set2)) return false;
    else {
        for(var key in set2) if (!(key in set1)) return false;
    }
    return true;
}
//----------------






//------Utils--------
//counts the occurences of an element in an array
function count_elem(lst, elem) {
    var count = 0;
    for (var num in lst) if (lst[num] === elem) count++;
    return count;
}
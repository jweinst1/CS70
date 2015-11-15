
//counts the occurences of an element in an array
function count_elem(lst, elem) {
    var count = 0;
    for(var num in lst) if(lst[num] === elem) count++;
    return count;
}
//calculates the prob of picking an element from an array
function picking_prob(lst, elem) {
    var prob = count_elem(lst, elem)/lst.length;
    return prob;
}
/*console.log(picking_prob([1, 2, 3, 3, 3, 3, 3, 3], 2));
 0.125
*/

//returns the complement of picking an element from an array.
function complement_prob(lst, elem) {
    return 1 - picking_prob(lst, elem);
}

//Object that gives the individual probabilities for picking each element in an array
var probability_set = function(lst) {
    for(var num in lst) this[lst[num]] = picking_prob(lst, lst[num]);
};
/*
console.log(new probability_set([1, 2, 2, 4, 5]));
 { '1': 0.2, '2': 0.4, '4': 0.2, '5': 0.2 }
*/


//calculates the conditional probability of picking elem, given first has
//already been picked.
function cond_pick_prob(lst, first, elem) {
    lst.pop(first);
    var prob = count_elem(lst, elem)/lst.length;
    return prob;
}
//returns the condition probability of picking elem, given first has occured uses Baye's Theorem.
function bayes_condprob(lst, first, elem) {
    var given = picking_prob(lst, first);
    var first_and_elem = given*picking_prob(lst, elem);
    return first_and_elem/given;
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
// ------->>>>end
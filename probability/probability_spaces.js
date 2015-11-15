//implementation of a probability space from elements in an array.
//such as [1, 1, 2, 3] -----> { 1:0.5, 2:0.25, 3:0.25 } with methods
var probability_space = function(elements) {
    this.space = new probability_set(elements);
    this.getprob = function(elem) {
        return this.space[elem];
    };
    this.contains = function(elem) {
        return (elem in this.space) ? true : false;
    };
};
/* ----adds two probability spaces together
function add_spaces(space1, space2) {

}
*/

//------Utils--------
//counts the occurences of an element in an array
function count_elem(lst, elem) {
    var count = 0;
    for(var num in lst) if(lst[num] === elem) count++;
    return count;
}
//Object that gives the individual probabilities for picking each element in an array
var probability_set = function(lst) {
    for(var num in lst) this[lst[num]] = picking_prob(lst, lst[num]);
};
//-----------------------
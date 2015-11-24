//contains implementations of logical objects, or mathematical logical objects.

//a defined, string expression as a bool object
var expression = function(term) {
    this.term = term;
    this.bool = eval(term);
};
//takes in a bool function, where an input can be evaluated to see if it works out as true or false.
var var_exp = function() {

};
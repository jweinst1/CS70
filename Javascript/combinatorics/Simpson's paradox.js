/**
 * Created by Josh on 12/14/15.
 */
//functions and objects that deal with comparing ratios


//static frequency of selection from a population
var selection = function(total, chosen) {
    this.total = total;
    this.chosen = chosen;
    this.rate = chosen/total;
};
//dyanmic frequncy of selection from a population.
var Dyn_select = function(total, chosen) {
    this.total = total;
    this.chosen = chosen;
    this.rate = function() {
        return this.total/this.chosen;
    };
    this.addtotal = function(amount) {
        this.total += amount;
    };
    this.addchosen = function(amount) {
        this.chosen += amount;
    };
};

function maxrate(s1, s2) {
    if(s1.rate()>s2.rate()) return s1;
    else if(s1.rate()<s2.rate()) return s2;
    else return "Rates are equal";
}

function maxchosen(s1, s2) {
    if(s1.chosen>s2.chosen) return s1;
    else if(s1.chosen<s2.chosen) return s2;
    else return "Chosen populations are equal"
}
//the difference in rate from s1 to s2
function ratediff(s1, s2) {
    return s1.rate()-s2.rate();
}
function rateequals(s1, s2) {
    return s1.rate()==s2.rate();
}

//takes an array of elements, and finds the most common one.
function getselections(elements) {
    var size = elements.length;
    var counts = {};
    counts[elements.shift()] = 1;
    while (elements.length>0) {
        var elem = elements.shift();
        if(elem in counts) counts[elem] += 1;
        else counts[elem] = 1;
    }
    for(var entry in counts) counts[entry] = counts[entry]/size;
    return counts;
}

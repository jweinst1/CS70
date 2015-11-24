//implementation of Javascript set as a closure.

//unordered, unique set
function Set(elements) {
    var elems = {};
    for(i=0;i<elements.length;i++) elems[elements[i]] = true;
    return {
        size: function () {
            return Object.keys(elems).length;
        },
        collection : function() {
            return Object.keys(elems);
        }
    }
}

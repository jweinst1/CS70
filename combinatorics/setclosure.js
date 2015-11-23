//implementation of Javascript set as a closure.

//unordered, unique set
function Set(elements) {
    var elems = {};
    for(i=0;i<elements.length;i++) elems[elements[i]] = true;
    return {
        size: function () {
            return Object.keys(elems).length;
        },
        intersection: function (set1, set2) {
            var result = {};
            for (var key in set1) if (key in set2) result[key] = true;
            return result;
        },
        union : function(set1, set2) {
            var result = [];
            for(var key in set1) result.push(key);
            for(var key in set2) result.push(key);
            result = new to_set(result);
            return result;
        }
    }
}

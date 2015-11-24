//functions, methods, and objects relating to the geometric distribution.


//gives the probability for up to and including first success
function geo_dist(prob, k) {
    if (0 < prob <= 1) {
        return Math.pow(1 - prob, k - 1) * prob;
    } else throw "prob must be between 0 and 1";
}

//gives the probability for up to and not including first success
function geo_distnot(prob, k) {
    if (0 < prob <= 1) {
        return Math.pow(1 - prob, k) * prob;
    } else throw "prob must be between 0 and 1";
}
//expected value of geometric dist
function geo_expval(prob) {
    return 1/prob;
}
//variance of geometric dist
function geo_var(prob) {
    return (1-prob)/(Math.pow(prob, 2));
}
//CDF function for geometric distribution
function geo_cdf(prob, k) {
    return 1-Math.pow(1-prob, k);
}
//CDF function not including first success
function geo_cdf_not(prob, k) {
    return 1-Math.pow(1-prob, k+1);
}
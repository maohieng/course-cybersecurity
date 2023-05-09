//Matching patterns
let expr = "My Mobile No is 123456789.My age is 20.";
// find numbers in a string without the global flag
let matches = expr.match(/\d+/);
console.log("Will Fetch 1st Occurrence of Digit", matches[0], "\n");

// find numbers in a string using the global flag
matches = expr.match(/\d+/g);
matches.forEach(function (m) {
    console.log(m);
});
console.log("\n");


str = "This is a test of search";
// find the index of the first instance of "is"
pos = str.search(/is/);
console.log("Will Display Index No of search String", pos, "\n");


//Replacing substrings
str = "the baby kicks the ball";
// replace "the" with "a" globally
let newStr = str.replace(/the/g, "a");
console.log("Original String : ", str);
console.log("After Replace String : ", newStr, "\n");


str = "the baby kicks the ball";
//  replace "kicks" with "holds"
newStr = str.replace('kicks', 'holds');
console.log("Original String : ", str);
console.log("After Replace String : ", newStr);
let str = 'Good Morning! How are you? This is John. John is my friend.';
let substrings = str.split(' ');
console.log(substrings + "\n");


//Returning a limited number of substrings
str = 'Good Morning! How are you? This is John. John is my friend.';
substrings = str.split(' ', 4);
console.log(substrings + "\n");


//Splitting a string using a regular expression
let paragraph = 'Good Morning! How are you? This is John. John is my friend.';
let sentences = paragraph.split(/[!,?,.]/);
console.log(sentences);
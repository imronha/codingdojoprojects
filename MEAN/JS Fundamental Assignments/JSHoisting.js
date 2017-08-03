// Assignment: JavaScript Hoisting
// Predict the output of the following snippets. Do not plug these into the interpreter.
//
// Note
// Even if let and const prevent a lot of the confusing behavior of JavaScript's hoisting, these are ES6 constructs and a huge amount of world's live JavaScript code is still ES5. Understanding how ES5 hoists var and the rules of scoping are important for every JavaScript developer!
//
// 1
// console.log(hello);
// var hello = ‘world’;
// should log undefined

// 2
// var needle = ‘haystack’;
// test();
//
// function test(){
// 	var needle = ‘magnet’;
// 	console.log(needle);
// }
// should log magnet?

// 3
// var brendan = ‘super cool’;
// function print(){
// 	brendan = ‘only okay’;
// 	console.log(brendan);
// }
// console.log(brendan);
// should log super cool

// 4
// var food = ‘chicken’;
// console.log(food);
// eat();
// function eat(){
// 	food = ‘half-chicken’;
// 	console.log(food);
// 	var food = ‘gone’;
// }
// should log chicken and half-chicken

// 5
// mean();
// console.log(food);
// var mean = function() {
// 	food = "chicken";
// 	console.log(food);
// 	var food = "fish";
// 	console.log(food);
// }
// console.log(food);
// error

// 6
// console.log(genre);
// var genre = "disco";
// rewind();
// function rewind() {
// 	genre = "rock";
// 	console.log(genre);
// 	var genre = "r&b";
// 	console.log(genre);
// }
// console.log(genre);
// should log undefined,rock,rnb,disco

// 7
// dojo = "san jose";
// console.log(dojo);
// learn();
// function learn() {
// 	dojo = "seattle";
// 	console.log(dojo);
// 	var dojo = "burbank";
// 	console.log(dojo);
// }
// console.log(dojo);
// should log sanjose, settle, burbank, sanjose

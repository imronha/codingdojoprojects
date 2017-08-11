



var myNum: Number = 5;
var myString: String = "Hello Universe";
var myArr: Array<Number> = [1,2,3,4];
const myObj = { name:<string>'Bill'};
var anythingVariable: String = "Hey";
var anythingVariable: Number = 25;
var arrayOne: Array<Boolean> = [true, false, true, true];
var arrayTwo: Any[] = [1, 'abc', true, 2];
const myObj = { x:<number> 5, y:<number> 10 };

// object constructor
class MyNode {
    constructor(val: number) {
        this.val = val;
    }
    doSomething() {
        this._priv = 10;
    }
})

let myNodeInstance = new MyNode(1);
console.log(myNodeInstance.val);

function myFunction(str: String): void{
    console.log("Hello World");
    return;
}
function sendingErrors(str: String): never{
	throw new Error('Error message');
}

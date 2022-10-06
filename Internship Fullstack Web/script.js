// function x() {
//     var a = 7,
//         b = 3;
//     a = a % b;
//     console.log(a);
//     a--;
//     console.log(a);
//     a = 'aa';
//     console.log(a);
//     alert('hello world');
// }


// var fname = 'fozail';
// var lname = 'ahmed';
// console.log(fullname = fname + ' ' + lname);

// var arr = [1, 2, 3, 4, 5];
// console.log(arr);

// var arr1 = new Array('a', 'b', 'c');
// console.log(arr1);

// const myElement = document.getElementById("demo");
// myElement.style.color = "red";


window.onload = function() {
    var display_counter = document.getElementById('counter');
    var localCounter = 0;
    var button = document.getElementById('btn');

    function clicked() {
        console.log("button clicked");
        localCounter++;
        display_counter.innerHTML = localCounter;
    }

    button.addEventListener('click', clicked);
}

class car {
    constructor(name, year) {
        this.name1 = name;
        this.year1 = year;
    }
    age() {
        var today = new Date();
        return today.getFullYear() - this.year1;

    }
}

let mycar1 = new car("ford", 2013);
console.log(mycar1);

console.log('your car is ' + mycar1.age() + ' years old');
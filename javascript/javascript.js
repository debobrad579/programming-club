// 19-04-23
function f(x) {
    return x * x;
}

function g(x) {
    return x ** 0.5;
}

function abs(x) {
    if (x > 0) {
        return x;
    } else {
        return -x;
    }
}

let x = 2;

if (x === "2") {
    var y = 3;
    console.log(y);
}

const z = 5;

console.log(y);

document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("button").onclick = () => {
        let header = document.querySelector("h1");

        if (header.innerHTML === "Hello, world!") {
            header.innerHTML = "Goodbye, world!";
        } else {
            header.innerHTML = "Hello, world!";
        }
    }

    //document.querySelector("#red").onclick = () => {
        //document.querySelector("h1").style.color = "red";
    //}
    //document.querySelector("#blue").onclick = () => {
        //document.querySelector("h1").style.color = "blue";
    //}
    //document.querySelector("#green").onclick = () => {
        //document.querySelector("h1").style.color = "green";
    //}

    //document.querySelectorAll(".color-button").forEach((button) => {
        //button.onclick = () => {
            //document.querySelector("h1").style.color = button.dataset.color;
        //}
    //})

    const buttons = document.querySelectorAll(".color-button");

    for (let i=0; i<buttons.length; i++) {
        const button = buttons[i];
        button.onclick = () => {
            document.querySelector("h1").style.color = button.dataset.color;
        }
    }
});

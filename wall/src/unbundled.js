class Mover {
    constructor() {
        this.posX = 0
        this.posY = 0
    }
}

let header = document.querySelector("h1")

canvas = document.querySelector("canvas")

canvas.height = window.innerHeight;
canvas.width = window.innerWidth;

ctx = canvas.getContext("2d")
player = new Mover()

socket = io();

xWidth = 1920/10;
yWidth = 1080/10;

killSquares = []

function draw() {

    ctx.clearRect(0,0,canvas.width,canvas.height)

    ctx.fillStyle="#656565"
    ctx.strokeStyle="white"

    for (let x = 0; x < 10; x++) {
        for (let y = 0; y < 10; y++) {
            if (killSquares.includes(`${x}:${y}`)) {
                ctx.fillStyle="#C63617"
                ctx.fillRect(scaleX(x*xWidth), scaleY(y*yWidth), scaleX(xWidth), scaleY(yWidth))
                ctx.fillStyle="#656565"
            }
            else 
                ctx.fillRect(scaleX(x*xWidth), scaleY(y*yWidth), scaleX(xWidth), scaleY(yWidth))
            ctx.strokeRect(scaleX(x*xWidth), scaleY(y*yWidth), scaleX(xWidth), scaleY(yWidth))
        }
    }

    ctx.beginPath();
    ctx.fillStyle = "white";
    ctx.arc(
        scaleX(xWidth / 2 + xWidth * player.posX),
        scaleY(yWidth / 2 + yWidth * player.posY),
        (window.innerHeight > window.innerWidth) ? scaleX(xWidth) / 2 : scaleY(yWidth) / 2,
        0,
        Math.PI * 2
    );
    ctx.fill();
    ctx.closePath();
}

function communicate(json) {
    socket.emit("move", json, (response) => {
        if (response['flag']) {
            header.style.display = "block";
            canvas.style.display = "none"
            header.textContent = response['flag']
        }

        response['killSquares'].forEach((killSquare) => {
            addKillSquares(killSquare)
        })

        player.posX = response["position"]["x"]
        player.posY = response["position"]["y"]

        if (response["death"]) {
            location.reload()
        }

        draw()
    });
}

function addKillSquares(killSquare) {
    killSquares.push(killSquare)
}

function getJSON() {
    return {
        canvas: canvas,
        ctx: ctx,
        player: {
            posX: player.posX,
            posY: player.posY,
        },
        recentKey:""
    }
}

function scaleX(x) {
    return window.innerWidth/1920*x;
}

function scaleY(y) {
    return window.innerHeight/1080*y;
}

draw()

let validEventKeys = ["ArrowUp","ArrowDown","ArrowLeft","ArrowRight"]

document.addEventListener("keydown", function(event) {
    if (validEventKeys.includes(event.key)) {
        let json = getJSON()
        json["recentKey"] = validEventKeys.indexOf(event.key)
        communicate(json)
    }
});

window.addEventListener("resize", () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    draw();
});
const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const session = require('express-session');

const sessionMiddleware = session({
  secret: 'bcactf',
  resave: false,
  saveUninitialized: true
});

app.use(sessionMiddleware);

const io = new Server(server);

io.use((socket, next) => {
  sessionMiddleware(socket.request, socket.request.res, next);
});

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    let x = array[j];
    array[j] = array[i]
    array[i] = x;
  }
}

let remainingNodes = []

for (let x = 0; x < 10; x++) {
  for (let y = 0; y < 10; y++) {
    if (x != 7 && !(x == 9 && y == 2)) {
      remainingNodes.push(`${x}:${y}`)
    }
  }
}

let initialNodes = []

for (let y = 0; y < 10; y++) {
  initialNodes.push(`${7}:${y}`)
}

let movements = [[0,-1],[0,1],[-1,0],[1,0]]
let validKeys = [0,1,2,3]

app.use(express.static(__dirname + '/public'));

app.get('/', (req, res) => {
  res.redirect("/bundled.js")
});

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
  req.session.nodes = [...remainingNodes]
  shuffleArray(req.session.nodes)
  req.session.killNodes = [...initialNodes]
});

io.of("/").on('connection', (socket) => {
  socket.on('move', (msg, callback) => {
    let session = socket.request.session;
    
    if (!session.nodes) session.nodes = [...remainingNodes]
    if (!session.killNodes) session.killNodes = [...initialNodes];

    let x = msg.player.posX;
    let y = msg.player.posY;

    let key = msg.recentKey

    if (key == 0 || key == 1 || key == 2 || key == 3) {
      x+=movements[key][0]
      y+=movements[key][1]

      if (x == -1) x = 0;
      if (x == 10) x = 9;
      if (y == -1) y = 0;
      if (y == 10) y = 9;
    }

    let death = false;
    if (session.killNodes.includes(`${x}:${y}`)) death = true;

    if (session.nodes.length == 0 && x == 9 && y == 2) {
      callback({"flag":"camp{1nTerC3pt1ON!_M4SteR}"})
    }

    let square = session.nodes.pop();
    session.killNodes.push(square)

    if (session.nodes.length == remainingNodes.length-1) {
      callback({"killSquares":[...initialNodes, square], "position":{"x":x,"y":y}, "death":death})
    }
    else {
      callback({"killSquares":[square], "position":{"x":x,"y":y}, "death":death})
    }
  });
});

server.listen(3000, () => {
  console.log('http://localhost:3000');
});
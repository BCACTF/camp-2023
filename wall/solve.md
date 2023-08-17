# Wall

The premise of the challenge is to make it to the safe square on the other side of the wall. This is a problem because as soon as the user makes any move, a wall spawns which blocks the user from reaching the safe square. As you look through the javascript or look at network connections, you can see that this game uses websockets.

Websockets are how the game communicates with the server, but you can a proxy, such as [Burp Suite](https://portswigger.net/burp), to intercept and change the messages before they reach the server.

Once intercepted, the message will look like 
```
420["move",{"canvas":{},"ctx":{},"player":{"posX":0,"posY":0},"recentKey":3}]
```

And changing the posX to 9, and posY to 2, and repeatedly spamming the right arrow key will eventually give you the flag once all of the board turned red.
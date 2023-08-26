const express = require('express');
const app = express();
const flag = "camp{YOu_WerENt_5Upp0sE_T0_se3_THI5_55d28b16d94c3}"

app.use(express.static(__dirname + '/public'));
app.use(express.urlencoded({ extended: false }));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.post('/', (req, res) => {
    if (req.body.username == "bcaCTFAdmin2?" && req.body.password == "admin!?!?!?!") {
        res.json({"flag":flag})
    }
    else res.redirect("/")
})

app.listen(3000, () => {
  console.log('http://localhost:3000');
});
const sqlite = require('sqlite3');
const express = require('express');
const fs = require('fs');
const cookieParser = require('cookie-parser');

const app = express();
const db = new sqlite.Database('./data/diseases.sqlite');
const flag = fs.readFileSync('./data/flag.txt', 'utf8');
const TOKEN = fs.readFileSync('./data/supersecretcookie.txt', 'utf8');
const PORT = 31571;

app.set('view engine', 'hbs');
app.set('views', __dirname + '/views');

app.use(express.static(__dirname + '/static'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

//map the patientinfo.txt file into a sql query format
const data = fs.readFileSync('./data/patientinfo.txt', 'utf8').split('\n').map(line => {
    const [name, pwd] = line.split('    ');
    return `('${name}', '${pwd}')`;
}).join(', ');

//reset the db
db.exec('DROP TABLE IF EXISTS info');
db.exec('DROP TABLE IF EXISTS medicalData');

db.exec('CREATE TABLE IF NOT EXISTS info (name TEXT, pwd TEXT)');
db.exec('CREATE TABLE IF NOT EXISTS medicalData (data TEXT, auth INT)');

db.exec(`INSERT INTO info VALUES ${data}`);
db.exec(`INSERT INTO medicalData VALUES ("${flag}",1)`);
db.exec(`INSERT INTO medicalData VALUES ("The Union Jack", 0)`);
db.exec(`INSERT INTO medicalData VALUES ("Oklahoma Flag", 0)`);

app.get('/', (req, res) => {
    res.render('index', { title: 'Patient Portal Login' });
});

app.get('/render', async (req, res) => {
    const sql = 'SELECT data FROM medicalData';
    let myAuth = true;
    if (req.cookies.allowedintotheserver !== TOKEN) 
        myAuth = false;
    await db.all(sql, (err, rows) => {
        if (err) {
           res.render('viewer', { title: 'Patient Portal', data: rows, myauth: myAuth, name: req.query.name });
           return;
        }
        if (rows.length === 0) {
            res.send('No data found');
            return;
        }
        console.log(rows, myAuth);
        res.render('viewer', { title: 'Patient Portal', data: rows, myauth: myAuth, name: req.query.name });
        return;
    });
});

app.post('/login', async (req, res) => {
    const name = req.body.username ?? 'Guest';
    const pwd = req.body.password ?? ' ';
    const sql = `SELECT * FROM info WHERE name='${name}' AND pwd='${pwd}';`;
    await db.all(sql, (err, rows) => {
        if (err) {
            console.log(`SQL error in query: ${sql}`);
            throw err;
        }
        if (rows.length === 0) {
            console.log(`Invalid login attempt: ${name} ${pwd}`);
            console.log(`SQL: ${sql}`);
            res.send('403: Forbidden \n Invalid username or password');
            return;
        }
        res.cookie('allowedintotheserver', TOKEN);
        res.redirect(`/render?name=${name}`);
        return;
    });
});

app.listen(PORT, () => console.log(`Server started at http://localhost:${PORT}`));
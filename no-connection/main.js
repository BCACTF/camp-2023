const form = document.getElementById('login_page');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username === 'dewoirf239bf3n9ddks' && password === '923nfr8idj91ws1m8dumnfed') {
        alert(getFlag());
    }
});

function getFlag() {let fr = ['\x82', 'i', 'q', '|',    't', 'q','k',    '|', 'i', 'x',    '|', 'n','m',    'g', 'd', '8',    'i', '6',':',    'd', '<', 's',    '8', 'n','&',    'H', 'd', 'S',    't', 'd','m',    'y', 'Z', 'f',    'd', '<','s',    '5', 'i', '\x80', 'u', 'r','f',    'h'];let rf = fr.reverse();let o = rf.map((c) => {return String.fromCharCode(c.charCodeAt(0) - 5);});return o.join('');}
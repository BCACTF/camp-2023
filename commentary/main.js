
const FLAG = document.getElementById('flag');

let flags = ['REDACTED', 'you cant have the flag', 'haha no flag here','🚩',
    'bcactf{h3res_an_old_wrong_flag}',
    'flag 2.0',
    'i wish there was a flag here'];
// don't add this one camp{h!Dd3n_in_pL41n_51GhT_fr3b9if3}

// setInteval to swap flags
setInterval(() => {
    FLAG.innerText = flags[Math.floor(Math.random() * flags.length)];
}, 500);
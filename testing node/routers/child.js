const { spawn } = require('child_process');

let cp=(filename)=>{
    filename.split('.')
    const l=filename.split('.')
    var lang=l[1]
    if(lang==="py"){
        var language='python'
    }
    else if(lang==="cpp"){
        language='cpp'
    }
    else if(lang==="js"){
        language="javascript"
    }

    var cp = spawn(language, [filename]);
    
    cp.stdout.on('data', (data) => {
        console.log(`Python output: ${data}`);
    });

    cp.stderr.on('data', (data) => {
        console.error(`Python error: ${data}`);
    });

    cp.on('close', (code) => {
        console.log(`Python child process exited with code ${code}`);
    });

}

module.exports={mag:cp}
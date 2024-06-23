const {spawn}=require("child_process")
var cp=(filename)=>{
    const child=spawn(python,[filename]);
    child.stdout.on('data',(data)=>
    console.log(data));
    child.stderr.on('data',(data)=>
    console.log(data));
    cp.on('close', (code) => {
    console.log(`Python child process exited with code ${code}`);
    });
}
module.exports=cp;
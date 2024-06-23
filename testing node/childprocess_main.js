const express=require("express")
const app=express()
const child=require("./routers/child.js")
//console.log(child.mag('child.py'))


app.get("/",(req,res)=>{
    res.render("")
})
app.listen(1001)
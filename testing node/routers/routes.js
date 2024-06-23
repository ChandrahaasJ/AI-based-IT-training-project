const express = require('express')
const app = express()

app.set("view engine","ejs");

app.get("/",(req,res)=>{
    res.render("upload.html")
})
app.listen(1002)
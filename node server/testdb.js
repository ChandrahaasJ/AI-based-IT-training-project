const mymodel=require("D:\\Projects\\IT training project\\node server\\db.js")
const express =require("express")

const mongoose = require("mongoose")
const app=express()
app.get("/user",async(req,res)=>{
    let userschema=await mymodel.usermodel.create({username:"chan@1",age:19,name:"chandrahaas"})
    //res.send(userschema)
})
app.get("/data",async(req,res)=>{
    let userdata=mymodel.datamodel.create({data1:12,data2:"jk"})
})
app.get('/sathwik',async(req,res)=>{
    let data=await mymodel.usermodel.find({})
    res.send(data)
}) 
app.listen(2939)
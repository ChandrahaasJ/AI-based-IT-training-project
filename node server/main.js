const express= require("express")
const app=express()
const router=require("D:\\Projects\\IT training project\\node server\\routes.js")
const axios=require("axios")
const Mymodel=require("./db")
const geturl=require("D:\\Projects\\IT training project\\node server\\urlgetter.js")
app.set('view engine','ejs')
/*const opcv=(req,res)=>{
    console.log(req.url)
}*/
app.use('/',geturl)
app.use('/routes',router)
app.get('/',(req,res)=>{
    var response=axios.post("http://127.0.0.1:5000",{"den":"gey"})
    console.log(response.data)
})
app.get("/addschema",async(req,res)=>{
    var created_schema=await Mymodel.create({name:"chandrahaas",age:20,username:"chan@1"})
    res.send(created_schema);
})

app.listen(3000)
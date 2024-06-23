const express=require("express")
const router=express.Router();
const process=require("D:\\Projects\\IT training project\\node server\\urlgetter.js")

router.use(process)

router.get('/',(req,res)=>{
    res.render("index")
})

router.get('/setind',(req,res)=>{
    res.send("<h1>HI</h1>")
})

module.exports=router;
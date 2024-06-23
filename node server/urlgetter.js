const url=(req,res,next)=>{
    console.log(req.url);
    next();
}
module.exports=url;
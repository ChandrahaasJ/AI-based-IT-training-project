const mongoose=require("mongoose")//requiring mongoose
mongoose.connect("mongodb://127.0.0.1:27012/1stDB");//setting up the data base 27012 is port:no and 127 is local host /1stDB is the name of the database
const userSchema=mongoose.Schema({username: String, name:String, age: Number});//creating user schema or documents
//making a collection for user with userschema
const dataschema=mongoose.Schema({data1:Number,data2:String})
module.exports={usermodel:mongoose.model("user",userSchema),datamodel:mongoose.model("data",dataschema)};//exporting the collection
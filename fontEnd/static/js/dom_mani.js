function fun()
{
    document.getElementById("papa").innerHTML="go coronas"
    //alert("this is a damage site")
    // var x = document.getElementById("papa").innerHTML;
    // alert(x)
}
function fun1()
{
    var x=document.getElementById("text1").value;
    alert("value"+x);

}
function fun2()
{
    var e="aakash@gmail.com"
    var p="12345"
    var temp=document.getElementById("mail").value;
    if(e==temp && p==document.getElementById("pwd").value){
        document.write("sucessfully login")
    }
    
    else{
        alert("sucessfully login")
        
    }
}
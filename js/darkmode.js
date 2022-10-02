var icon=document.getElementById("icon");

if(localStorage.getItem("theme")==null)
{
    localStorage.setItem("theme","light");
}
let localData=localStorage.getItem("theme");

if(localData=="light")
{
    icon.src="images/darkmoon.png";
    document.body.classList.remove("dark-theme");
}
else if(localData=="dark")
{
    icon.src="images/sun.png";
    document.body.classList.add("dark-theme");
}
var icon=document.getElementById("icon");
icon.onclick = function ()
{
    document.body.classList.toggle("dark-theme");
    if(document.body.classList.contains("dark-theme"))
    {
        icon.src="images/sun.png";
        localStorage.setItem("theme","dark");
    }
    else
    {
        icon.src="images/darkmoon.png";
        localStorage.setItem("theme","light");
    }
}
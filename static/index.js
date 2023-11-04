function input_value(){
    let input = document.getElementById("input").value
    let prioritet = document.getElementById("prioritet").value
    let q = {"input": input,"prioritet": prioritet}
    let link = "/input?"+new URLSearchParams(q)
    post_method(link)
    window.location.href = link
    console.log(link)
}
function post_method(link){
    fetch(link,{
        method:"POST"
    })

}
function deleteFile(e){
    console.log(e)
    fetch(`/input/${e}`, {
        method:"DELETE"
    }).then(()=>{
        window.location.href="/input"
    })
}
function filter(){
    let filter = document.getElementById("filter").value
    fetch(`/input/filter/${filter}`,{
        method:"GET"
    }).then(()=>{
        window.location.href=`/input/filter/${filter}`
    })
}
function sortiranje(){
    let sortiranje = document.getElementById("sortiranje").value
    fetch(`/input/sortiranje/${sortiranje}`,{
        method:"GET"
    }).then(()=>{
        window.location.href=`/input/sortiranje/${sortiranje}`
    })
}
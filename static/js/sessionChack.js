(async()=>{
    return checkSessionCode() 
})()
const getCookie = async() => {
    // Надійний спосіб зчитування куки за ім'ям "sessionID"
    let matches = document.cookie.match(new RegExp(
        "(?:^|; )" + "sessionID".replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}
const checkSessionCode= async()=>{
    let code = getCookie()
    let result = false
    await fetch(`/api/checksession/${code}`)
    .then(res=>res.json())
    .then(data=>{
        result = data.state
    })
    return result
}
const LogOut =  async () => {
    if(await deleteSession() === false){
        return false
    }
    deleteCookie()
    location.reload();
    return true

}
const deleteCookie = () => {
    document.cookie = "sessionID=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}
const deleteSession = async() =>{
    let code = await getCookie()
    return await DeleteRequest(code)
}
const getCookie = async() => {
    // Надійний спосіб зчитування куки за ім'ям "sessionID"
    let matches = document.cookie.match(new RegExp(
        "(?:^|; )" + "sessionID".replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}
const DeleteRequest = async(code)=>{
    let result = false
    await fetch(`/api/dellsession/${code}`)
    .then(res => res.json())
    .then(data => {
        result = data.state;
    });
    return result
}
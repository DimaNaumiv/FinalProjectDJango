const RegistrateUser = () =>{
    let name = document.getElementById('name')
    let password =document.getElementById('password')
    let con_password = document.getElementById('con_password')

    let name_text = name.value
    let pasword_text = password.value
    let con_password_text = con_password.value

    if(all_is(name_text,password_text,con_password_text)){
        if(password_text === con_password_text){
            saveUser(name_text,pasword_text)
        }
        return false
    }
}

const all_is = (name,password,con_password) =>{
    if(name !== "" && password !== "" && con_password !==""){
        return true
    }
    return false
}

const saveUser = () =>{

}
const hashPassword = (password) =>{
    let hesh = ""
    return hesh
}


const Authentication = async()=>{

    let name = document.getElementById('name')
    let password =document.getElementById('password')
    let con_password = document.getElementById('con_password')

    let name_text = name.value
    let password_text = password.value
    let con_password_text = con_password.value

    if(CheckData(name_text,password_text,con_password_text)===false){
        return false
    }

    let result = await UserInBase(name_text,password_text)

    if(result === null){
        await RegistrateUser(name_text,password_text)
        return true
    }

    addCodeCookie(result)
    location.reload();
    return true

}

const UserInBase =async(name_text,password_text)=>{
    let nameList = separateName(name_text)
    let firstName = nameList[0]
    let lastName = nameList[1]
    return GetRequest(firstName,lastName,password_text)
}

const GetRequest = async(firstName,lastName,password)=>{
    let result
    let code

    const userData = {
        first_name: firstName,
        last_name: lastName,
        password: password
    }

    await fetch('/api/checkuser/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData) // Перетворюємо об'єкт у рядок JSON
    })
    .then(res => res.json())
    .then(data => {
        result = data.state;
        code = data.session_code;
    });
    if(result === true){
        return code
    }
    return null
}

const RegistrateUser = async(name_t,password_t) =>{
    let code = await saveUser(name_t,password_t)
    addCodeCookie(code);
    return true
}

const CheckData = (name,password,con_password) =>{
    if(name !== "" && password !== "" && con_password !==""){
        if(password !== con_password){
            return false
        }
        return true
    }
    return false
}

const saveUser = async(name,password) =>{
    let nameList = separateName(name)
    let firstName = nameList[0]
    let lastName = nameList[1]


    return await saveRequest(firstName,lastName,password)
}

const separateName = (name) =>{
    return name.split(' ')
}
const saveRequest = async(first_name,last_name,password)=>{
    let result
    let code

    const userData = {
        first_name: first_name,
        last_name: last_name,
        password: password
    }

    await fetch('/api/registrate/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData) // Перетворюємо об'єкт у рядок JSON
    })
    .then(res => res.json())
    .then(data => {
        result = data.state;
        code = data.session_code;
    });
    if(result === true){
        return code
    }
    return 0
}



const addCodeCookie = (code) =>{
    const date = new Date
    date.setTime(date.getTime()+(1000*24*60*60*1000))
    let expres = "; expires="+date.toUTCString()
    document.cookie = "sessionID="+code+expres+"; path=/;"
}

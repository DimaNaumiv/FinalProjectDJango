const GetQuestion = (groupType,difficulty) =>{
    let question = document.getElementById("question");

    fetch(`/api/generate/${groupType}/${difficulty}/`)
    .then(res =>res.json())
    .then(data=>{
        if(data.status == "correct"){
            question.innerText = data.value
        }
    })
}

const CheckAnswer=()=>{
    let question = document.getElementById('question')
    let answer = document.getElementById('answer')


    fetch(`/api/check/${question.innerText}/${answer.value}/`)
    .then(res => res.json())
    .then(data=>{
        question.innerText = data.status
    })

}
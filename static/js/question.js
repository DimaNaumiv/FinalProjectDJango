(
    async()=>{
        let code = await getCookie();
        if(code){
            return
        }
        let modal = document.getElementById("ModalWarning")
        modal.showModal()
    }
)()

let startTime = 0;
let elapsedTime = 0;
let timerInterval = null;

let modalfail = document.getElementById("ModalFail")
let modalwin = document.getElementById("ModalWin")

let count = 0

const Generate = async(groupType)=>{
    const urlParams = new URLSearchParams(window.location.search);
    let min = urlParams.get('min');
    let max = urlParams.get('max');

    await GetQuestion(groupType,min,max)
    UseTimer()
}

const GetQuestion = async(groupType,min,max) =>{
    let question = document.getElementById("question");

    const generateData ={
        group_type:groupType,
        min:min,
        max:max
    }

    let result = await fetch('/api/generate/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(generateData) // Перетворюємо об'єкт у рядок JSON
    })

    let data = await result.json()
    question.innerText = data.value
}

const UseTimer = ()=>{
    if(TimerIsActive() == false){
        return
    }

    if (timerInterval) {
        clearInterval(timerInterval);
        elapsedTime = 0;
    }
    startTime = 0
    elapsedTime = 0
    timerInterval = null

    StartTimer()

}
const StartTimer = ()=>{
    // Оновлюємо таймер приблизно кожні 10-20 мілісекунд для плавності

    startTime = performance.now() - elapsedTime;

    timerInterval = setInterval(() => {
        elapsedTime = Math.floor(performance.now() - startTime);
        document.getElementById('timer').innerText = formatTime(elapsedTime);
    }, 10);

}
const StopTimer = () => {
    // Перевіряємо, чи таймер взагалі запущений
    if (timerInterval) {
        clearInterval(timerInterval); // Зупиняємо відлік
        timerInterval = null;         // Позначаємо, що таймер зупинено
    }
};
function formatTime(ms) {
    // Розрахунок годин, хвилин, секунд та мілісекунд
    let hours = Math.floor(ms / 3600000);
    let minutes = Math.floor((ms % 3600000) / 60000);
    let seconds = Math.floor((ms % 60000) / 1000);
    let milliseconds = ms % 1000;

    // Форматування з додаванням нулів попереду (01 замість 1)
    const pad = (num, size = 2) => String(num).padStart(size, '0');

    return `${pad(hours)}:${pad(minutes)}:${pad(seconds)}:${pad(milliseconds, 3)}`;
}
const TimerIsActive = ()=>{
    const urlParams = new URLSearchParams(window.location.search);
    let timer = urlParams.get('timerch');
    if(timer === "on"){
        return true
    }
    return false
}


const Answer = async(groupType)=>{
    let  time = "-"
    if(TimerIsActive()){
        StopTimer()
        time = document.getElementById('timer').innerText
    }
    let result = await CheckAnswer(groupType)

    if(result == "uncorrect"){
        modalfail.showModal()
        count = count+1
    }
    else{
        let answer = document.getElementById('answer').value
        let question = document.getElementById('question').innerText

        const urlParams = new URLSearchParams(window.location.search);
        let min = urlParams.get('min');
        let max = urlParams.get('max');

        document.getElementById('resolve_ansver').innerText = "your answer: "+ answer
        document.getElementById('resolve_question').innerText = "your question: " + question
        document.getElementById('resolve_time').innerText = "time wasted: " + time
        document.getElementById('resolve_fails').innerText = "fails: " + count
        document.getElementById('min_max').innerText = `min: ${min} max:${max}`

        modalwin.showModal()
    }

}

const CheckAnswer= async(groupType)=>{
    let question = document.getElementById('question')
    let answer = document.getElementById('answer')

    let status = ""

    let answerData = {
        group_type:groupType,
        question:question.innerText,
        answer:answer.value
    }

    let result = await fetch('/api/check/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(answerData) // Перетворюємо об'єкт у рядок JSON
    })
    let data = await result.json()
    return data.status
}

const CloseModal = ()=>{
    let modal = document.getElementById("ModalWarning")
    modal.close()
}

function validation(){
    let min = parseInt(document.getElementById("minInp").value)
    let max = parseInt(document.getElementById("maxInp").value)

    if(min>=max){
        document.getElementById("maxInp").value = min+1
        alert("min must be less then max")
    }
    return true
}

const Continue = () =>{
    modalfail.close()
    StartTimer()
}
const Restart = async(groupType) =>{
    modalfail.close()
    alert("Get ready!!!")
    await Generate(groupType)
    document.getElementById('answer').value =""
    count = 0
}
const Finish = () =>{
    modalfail.close()
    modalwin.close()
    
    document.getElementById('question').innerText = "..."
    document.getElementById('timer').innerText = "00:00:00:000"
    document.getElementById('answer').value =""

    count = 0
}
const Save = async(group_type) => {
    const urlParams = new URLSearchParams(window.location.search);
    let min = urlParams.get('min');
    let max = urlParams.get('max');
    let answer = document.getElementById('answer').value
    let question = document.getElementById('question').innerText
    let timer = document.getElementById('timer')
    let sessionID = await getCookie()

    let time = timer ? timer.innerText : "-"

    let saveData = {
        'group_type':group_type,
        'min_const':min,
        'max_const':max,
        'qustion':question,
        'answer':answer,
        'time':time,
        'fails':count,

        'sessionID':sessionID
    }

    let result = await fetch('/api/save/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(saveData) // Перетворюємо об'єкт у рядок JSON
    })
    let data = await result.json()
    if(!data.state){
        return
    }

    Finish()
}
from .methods.arthmetic import resolve_ar
def calculate(group_type,question):
    answer = 0.0
    
    if(group_type == "arithmetic"):
        answer = resolve_ar(question)

    return answer

def correct_or_no(answer,group_type,question):
    cor_answer = float(calculate(group_type,question))
    status = ""
    if(cor_answer == float(answer)):
        status = "correct"
    else:
        status = "uncorrect"
    
    return status
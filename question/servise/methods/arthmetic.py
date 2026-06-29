import re

def resolve_ar(question):
    clear_question = question.replace("=", "")

    if not re.match(r"^[0-9+\-*/().\s]+$", clear_question):
        return ""
    
    answer = eval(clear_question)
    return answer
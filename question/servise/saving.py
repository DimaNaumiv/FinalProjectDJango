from registration.models import Session,Result
def seve_result(group_type,min_const,max_const,qustion,answer,time,fails,sessionID):
    user_id = get_user_id(sessionID)
    Result.objects.create(
        group_type=group_type,
        min_const=min_const,
        max_const=max_const,
        qustion=qustion,
        answer=answer,
        time=time,
        fails=fails,
        user_id=user_id
    )
    return True

def get_user_id(sessionID):
    session = Session.objects.get(pk = sessionID)
    return session.user.pk
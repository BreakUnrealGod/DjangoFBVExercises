from libs.http import render_json
from social import logic
from social.models import Swiped


def recommend(request):
    """
    根据当前登录用户的 profile 筛选符合条件的用户
    :param request:
    :return:
    """
    recm_users = logic.recommend_users(request.user)

    users = [u.to_dict() for u in recm_users]

    return render_json(data=users)


def like(request):
    """
    喜欢
    :param request:
    :return:
    """
    sid = int(request.POST.get('sid'))
    user = request.user

    matched = logic.like_someone(user.id, sid)

    return render_json(data={'matched': matched})


def superlike(request):
    """
    超级喜欢
    :param request:
    :return:
    """
    sid = int(request.POST.get('sid'))
    user = request.user

    matched = logic.superlike_someone(user.id, sid)

    return render_json(data={'matched': matched})


def dislike(request):
    """
    不喜欢
    :param request:
    :return:
    """
    sid = int(request.POST.get('sid'))
    user = request.user

    Swiped.swipe(uid=user.id, sid=sid, mark='dislike')

    return render_json()


def rewind(request):
    """
    反悔
    不需要从客户端获取数据
    :param request:
    :return:
    """
    user = request.user
    logic.rewind(user)

    return render_json()


def liked_me(request):
    return None


def friends(request):
    return None

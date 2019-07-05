import datetime

from social.models import Swiped
from user.models import User


def recommend_users(user):
    """
    筛选符合 user.profile 条件的用户
    过滤掉已经被划过的用户
    :param user:
    :return:
    """
    today = datetime.date.today()

    # 1999 = 2019 - 20
    max_year = today.year - user.profile.min_dating_age
    # 2001 = 2019 - 18
    min_year = today.year - user.profile.max_dating_age

    swiped_users = Swiped.objects.filter(uid=user.id).only('sid')
    swiped_sid_list = [s.sid for s in swiped_users]

    users = User.objects.filter(
        sex=user.profile.dating_sex,
        location=user.profile.location,
        birth_year__gte=min_year,
        birth_year__lte=max_year,
    ).exclude(id__in=swiped_sid_list)[:20]

    return users

kalenjin_name_list = []


def get_last_id():
    if name_list:
        last_name = kalenjin_name_list[-1]
    else:
        return 1
    return last_name.id + 1


class KalenjinName:
    def __init__(self, boy_name, boy_name_trans, girl_name, girl_name_trans, girl_name_alternate,
                 nickname, english_meaning, kalenjin_meaning, related_name, time_of_birth,
                 event_at_birth, season_at_birth, pronunciation, comment):
        self.id = get_last_id()
        self.boy_name = boy_name
        self.boy_name_trans = boy_name_trans
        self.girl_name = girl_name
        self.girl_name_trans = girl_name_trans
        self.girl_name_alternate = girl_name_alternate
        self.nickname = nickname
        self.english_meaning = english_meaning
        self.kalenjin_meaning = kalenjin_meaning
        self.related_name = related_name
        self.time_of_birth = time_of_birth
        self.event_at_birth = event_at_birth
        self.season_at_birth = season_at_birth
        self.pronunciation = pronunciation
        self.comment = comment
        self.is_publish = False

    @property
    def data(self):
        return {
            'id': self.id,
            'boy_name': self.boy_name,
            'boy_name_trans': self.boy_name_trans,
            'girl_name': self.girl_name,
            'girl_name_trans': self.girl_name_trans,
            'girl_name_alternate': self.girl_name_alternate,
            'nickname': self.nickname,
            'english_meaning': self.english_meaning,
            'kalenjin_meaning': self.kalenjin_meaning,
            'related_name': self.related_name,
            'time_of_birth': self.time_of_birth,
            'event_at_birth': self.event_at_birth,
            'season_at_birth': self.season_at_birth,
            'pronunciation': self.pronunciation,
            'comment': self.comment
        }

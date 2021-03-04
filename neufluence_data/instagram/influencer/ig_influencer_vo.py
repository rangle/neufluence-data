

class IGInfluencerScrapedVO():


    def __init__(self, url, user_id, user_name, user_full_name, is_followed):
        self.url = url
        self.user_id = user_id
        self.user_name = user_name
        self.user_full_name = user_full_name
        self.is_followed = is_followed


    @staticmethod
    def from_dict(source):
        # ...
        return 0

    def to_dict(self):
        dest = {
            u'url': self.url,
            u'user_id': self.user_id,
            u'user_name': self.user_name,
            u'user_full_name': self.user_full_name,
            u'is_followed': self.is_followed
        }
        return dest


    def __repr__(self):
        return(
            f'ProfileFirestoreDAO(\
                url={self.url}, \
                user_id={self.user_id}, \
                user_name={self.user_name}, \
                user_full_name={self.user_full_name}, \
                is_followed = {self.is_followed}\
            )'
        )

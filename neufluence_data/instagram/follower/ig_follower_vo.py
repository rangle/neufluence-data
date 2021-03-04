

class IGFollowerSimpleVO():

    def __init__(self, user_name, user_full_name, user_picture_url):
        self.user_name = user_name
        self.user_full_name = user_full_name
        self.user_picture_url = user_picture_url


    def to_dict(self):
        dest = {
            u'user_name': self.user_name,
            u'user_full_name': self.user_full_name,
            u'user_picture_url': self.user_picture_url
        }
        return dest


    # Look on GCP documentation
    def from_dict(self):
        return 0


    # Look on GCP documentation for proper implementation
    def __repr__(self):
        return(
            f'ProfileFirestoreDAO(\
                user_name={self.user_name}, \
                user_full_name={self.user_full_name}\
                user_picture_url={self.user_picture_url}\
            )'
        )



class IGFollowerVO():


    def __init__(self, user_name, user_full_name, profile_pic_url,
                    number_of_followers, number_of_following, number_of_posts,
                    is_followed, ):

        self.user_name = user_name
        self.user_full_name = user_full_name
        self.profile_pic_url = profile_pic_url
        self.number_of_followers = number_of_followers
        self.number_of_following = number_of_following
        self.number_of_posts = number_of_posts
        self.is_followed = is_followed


""" COMPLEMENT PROPERLY


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
"""

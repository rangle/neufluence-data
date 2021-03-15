

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
    @staticmethod
    def from_dict(source):
        FollowerSimple=IGFollowerSimpleVO(source[u'user_name'],source[u'user_full_name'],source[u'user_picture_url'])
        return FollowerSimple

    # Look on GCP documentation for proper implementation
    def __repr__(self):
        return(
            f'IGFollowerSimpleVO(\
                user_name={self.user_name}, \
                user_full_name={self.user_full_name},\
                user_picture_url={self.user_picture_url}\
            )'
        )



class IGFollowerVO():


    def __init__(self, user_name, user_full_name, user_picture_url,
                    number_of_followers, number_of_following, number_of_posts ):

        self.user_name = user_name
        self.user_full_name = user_full_name
        self.user_picture_url = user_picture_url
        self.number_of_followers = number_of_followers
        self.number_of_following = number_of_following
        self.number_of_posts = number_of_posts


    def to_dict(self):
        dest = {
            u'user_name': self.user_name,
            u'user_full_name': self.user_full_name,
            u'user_picture_url': self.user_picture_url,
            u'number_of_followers':self.number_of_followers,
            u'number_of_following':self.number_of_following,
            u'number_of_posts':self.number_of_posts
        }
        return dest

    @staticmethod
    def from_dict(source):
        Follower=IGFollowerVO(source[u'user_name'],source[u'user_full_name'],source[u'user_picture_url'],\
        source[u'number_of_followers'],source[u'number_of_following'],source[u'number_of_posts'])
        return Follower

    def __repr__(self):
        return(
            f'IGFollowerVO(\
                user_name={self.user_name}, \
                user_full_name={self.user_full_name}, \
                user_picture_url={self.user_picture_url}, \
                number_of_followers={self.number_of_followers},\
                number_of_following={self.number_of_following},\
                number_of_posts={self.number_of_posts}\
            )'
        )

from instagram.follower.ig_follower_vo import IGFollowerVO

from instagram.influencer.ig_influencer_dao import IGInfluencerDAO

import neufluence_firebase


class IGFollowerDAO:


    def save_follower(followerVO):
        return 0


    # Using the influencer_user_name saves the list of followers
    def save_list_of_followers_simple(influencer_user_name, followers):
        db = firebase.get_firebase_db()
        print("got db")

        ig_influencer = IGInfluencerDAO.get_influencer_scraped_by_user_name(influencer_user_name)

        #for follower in followers:
            #array of map
            #influencer.collection(u'followers').add(follower.to_dict())
            #followers = ig_influencer(u'followers').document()
            #influencer.update({u'followers': firestore.ArrayUnion([u'map'])})

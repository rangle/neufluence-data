from instagram.follower.ig_follower_vo import IGFollowerVO

from instagram.influencer.ig_influencer_dao import IGInfluencerDAO

import neufluence_firebase as firebase
from google.cloud import firestore

class IGFollowerDAO:


    def save_follower(followerVO):
        return 0



    # Using the influencer_user_name saves the list of followers
    def save_list_of_followers_simple(influencer_user_name, followers):
        db = firebase.get_firebase_db()
        print("got db")

        ig_influencer = IGInfluencerDAO.get_influencer_scraped_by_user_name(influencer_user_name)
        ig_influencer_followers = ig_influencer.collection(u'follower').document()
        follower_map = [follower.to_dict() for follower in followers]
            #ig_influencer_followers.field(u'followers').add(follower.to_dict())
        ig_influencer_followers.set({
          u'followers':follower_map,
          u'scraped_timestamp': firestore.SERVER_TIMESTAMP
        })

        return
            #influencer.update({u'followers': firestore.ArrayUnion([u'map'])})


    def save_list_of_followers(influencer_user_name, followers):
        db = firebase.get_firebase_db()
        print("got db")

        ig_influencer = IGInfluencerDAO.get_influencer_scraped_by_user_name(influencer_user_name)
        ig_influencer_followers = ig_influencer.collection(u'follower').document()
        follower_map = [follower.to_dict() for follower in followers]
            #ig_influencer_followers.field(u'followers').add(follower.to_dict())
        ig_influencer_followers.set({
          u'followers':follower_map,
          u'scraped_timestamp': firestore.SERVER_TIMESTAMP
        })

        return

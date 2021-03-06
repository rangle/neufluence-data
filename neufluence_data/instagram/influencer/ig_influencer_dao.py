from instagram.follower.ig_follower_vo import IGFollowerSimpleVO
import neufluence_firebase as firebase


class IGInfluencerDAO():

    def get_influencer_by_user_name(user_name):
        #define
        db = firebase.get_firebase_db()
        print("got db")
        print("searching for user: " + user_name)

        influencers_ref = db.collection(u'social_media')
        query = influencers_ref.where(
                    u'user_name',u'==', user_name).limit(1)
        results = query.stream()
        print("results")
        print(results)

        for result in results:
            print("found 1 result")
            print(f'{result.id} => {result.to_dict()}')
            influencer_ref = db.collection(u'social_media').document(result.id)
        return influencer_ref
        # edge case to ahndle in case there's no influencer, throw an exception InfluencerScrapedNotFoundException


    def get_influencer_api_by_user_name(user_name):
        #define
        return 0


    # Gets the influencer scraped reference
    def get_influencer_scraped_by_user_name(user_name):

        db = firebase.get_firebase_db()
        print("got db")
        print("searching for user: " + user_name)

        influencers_ref = db.collection(u'influencers_scraped')
        query = influencers_ref.where(
                    u'user_name',u'==', user_name).limit(1)
        results = query.stream()
        print("results")
        print(results)

        for result in results:
            print("found 1 result")
            print(f'{result.id} => {result.to_dict()}')
            influencer_ref = db.collection(u'influencers_scraped').document(result.id)

        # edge case to ahndle in case there's no influencer, throw an exception InfluencerScrapedNotFoundException
        return influencer_ref

    def get_influencer_scraped_by_id(influencer_id):
        db = firebase.get_firebase_db()

        influencer = db.collection(u'influencers_scraped').document(influencer_id)

        return influencer

    def save_total_legit_followers(user_name,total_legit_followers):
        influencer_ref = IGInfluencerDAO.get_influencer_by_user_name(user_name)
        influencer_ref.update({
        u'total_legit_followers':total_legit_followers
        })
        print("save total legit followers")
        return

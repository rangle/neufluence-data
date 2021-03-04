import neufluence_firebase as firebase

from instagram.influencer.ig_influencer_dao import IGInfluencerDAO
from instagram.follower.ig_follower_dao import IGFollowerDAO
from instagram.follower.ig_follower_vo import IGFollowerSimpleVO


# create follower list from driver
f1 = IGFollowerSimpleVO("user_name_1", "user_full_name_1", "url")
f2 = IGFollowerSimpleVO("user_name_2", "user_full_name_2", "url")

# save list of followerVO
influencer_user_name = "bianca_test"

ig_influencer = IGInfluencerDAO.get_influencer_scraped_by_user_name(influencer_user_name)

#IGFollowerDAO.save_list_of_followers_simple(influencer_user_name, [f1, f2])

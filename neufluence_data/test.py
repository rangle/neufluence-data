import neufluence_firebase as firebase

from instagram.influencer.ig_influencer_dao import IGInfluencerDAO
from instagram.follower.ig_follower_dao import IGFollowerDAO
from instagram.follower.ig_follower_vo import IGFollowerSimpleVO
from instagram.follower.ig_follower_vo import IGFollowerVO

# create follower list from driver
#f1 = IGFollowerSimpleVO("user_name_1", "user_full_name_1", "url")
#f2 = IGFollowerSimpleVO("user_name_2", "user_full_name_2", "url")

#f3 = IGFollowerVO("user_name_1", "user_full_name_1", "profile_pic_url_1",200, 100, 50)
#f4 = IGFollowerVO("user_name_2", "user_full_name_2", "profile_pic_url_2",300, 200, 80)

# save list of followerVO
#influencer_user_name = "yaxin"
#ig_influencer = IGInfluencerDAO.get_influencer_scraped_by_user_name(influencer_user_name)
#IGFollowerDAO.save_list_of_followers_simple(influencer_user_name, [f1, f2])
#IGFollowerDAO.save_list_of_followers(influencer_user_name, [f3, f4])

influencer_user_name = "nadiamariesasso"
total_legit_followers = 200
#ig_influencer = IGInfluencerDAO.get_influencer_by_user_name(influencer_user_name)
IGInfluencerDAO.save_total_legit_followers(influencer_user_name,total_legit_followers)

import twitter

api = twitter.Api(consumer_key='PvyYvRKzcM8sQmtQS17SMuJJW',
                  consumer_secret='LP9Y85by1QgDWZnbxgDRtevpdWXLl38hJoN3JUB2ueHrpyRdVy',
                  access_token_key='2797388610-ObMaiSLpL4iMPn8WotIlwZPyeX2Fpz2O9kCS3m0',
                  access_token_secret='HzcWWScASzQUCUPvCbFqaPiJLvH0zIEWtb3v3WgIWYjZe')

users = api.GetFriends()
not_update_profile_image_users = [i for i in users \
                                  if api.GetUser(i.id).profile_image_url ==
                                  'http://abs.twimg.com/sticky/default_profile_images'\
                                  '/default_profile_normal.png']

print([u.name for u in not_update_profile_image_users])

for i in not_update_profile_image_users:
    api.PostDirectMessage(i, "You have not updated your profile picture")
    print(f"Informed {i}")

# coding: utf-8

# In[ ]:


def extractor_follows(id_):
    extractor= twitter_setup()
    ids = []
    try:
        u = extractor.get_user(id_)
        name = u.screen_name
        try:
            for page in tweepy.Cursor(extractor.followers_ids, id=id_).pages():
                ids.extend(page)
        except TweepError: 
               pass    
    except:
        print('exception ocurred')
        pass
    ids=pd.DataFrame(ids,columns=[name])
    return ids


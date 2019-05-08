
# coding: utf-8

# In[ ]:


def grid_of_follows(id_):
        
        extractor= twitter_setup()
        df = extractor_follows(id_)
        u = extractor.get_user(id_)
        name = u.screen_name
        df= pd.DataFrame(df,columns=[name],dtype=str)
        for i in df[name]:
            u = extractor.get_user(i)
            name = u.screen_name    
            follower= extractor_follows(i)
            follower= pd.DataFrame(follower,columns=[name],dtype=str, index= False,header= True)
            with open('followers_'+name+'.csv', 'a') as f:
             (follower).to_csv(f, header=True)
            print('work_in_progres')
            
        
        return 


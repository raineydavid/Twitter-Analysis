
# coding: utf-8

# In[1]:


def tweet_caller_csv(id_):
        #autentication
        #recollect tweet      ##01
        try: 
                extractor = twitter_setup() 
                u = extractor.get_user(id_)
                name = u.screen_name  
                tweets = extractor.user_timeline(id=id_, count=200,tweet_mode= 'extended')

        except:
                print('Error in try 01: caller')

        try:    #CREATE A DATAFRAME   ##02
                alltweet = []
                alltweet.extend(tweets)
                oldest = alltweet[-1].id - 1

                try:
                    while len(tweets) > 0:
                            tweets = extractor.user_timeline(id= id_,count=200,
                                           tweet_mode= 'extended',max_id=oldest)
                            alltweet.extend(tweets)
                            oldest = alltweet[-1].id - 1
                except ConnectionError:
                    print('ConnectionError')
                result = [[tweet.id, tweet.created_at, tweet.full_text, tweet.entities]
                          for tweet in alltweet]
                data= pd.DataFrame(result, columns=['id','date','text', 'entities'])
                
        except:
                print('Error in try: 02, dataframe')

        try:    #Extract hashtags     ##03
                hashtags=[]
                for key in data['entities']:
                    try:
                        hashtags.append(key['hashtags'][0]['text'])
                    except: 
                        hashtags.append('null')
                        pass
        except: 
                print('Error in try: 03, hashtags')


        try:    #Extract hashtags     ##04
                menciones = []
                menciones_id = []
                for key in data['entities']:
                    try:
                        menciones.append(key['user_mentions'][0]['name'])
                        menciones_id.append(key['user_mentions'][0]['id'])
                    except: 
                        menciones.append('null')
                        menciones_id.append('null')
                        pass
        except: 
                print('Error in try: 04, entities')   
                
                
        try:    #Extract hashtags     ##05

                retweet_count = [tweet.retweet_count for tweet in alltweet]
        except: 
                print('Error in try: 05, retweet_count')
                

        try:    #Extract hashtags     ##06

                like = [tweet.favorite_count for tweet in alltweet]
        except: 
                print('Error in try: 06, likes')

                
                
        try:    #unique data          ##07
                hashtags= pd.DataFrame(hashtags, columns= ['hashtags'])
                menciones = pd.DataFrame(menciones, columns= ['menciones'])
                menciones_id = pd.DataFrame(menciones_id, columns= ['menciones_id'])
                menciones_combinado = pd.concat([menciones, menciones_id], axis= 1)
                retweet_count = pd.DataFrame(retweet_count, columns= ['numero_retweet'])
                like_count = pd.DataFrame(like, columns=['numero_likes'])

        except:
                print('Error in try: 07, dataframes')
               
        try:    #unique data          ##08
                data=pd.concat([data,hashtags, menciones_combinado, retweet_count, like_count], axis= 1)

        except:
                print('Error in try: 08, concat')
                
                

        try:    #drop columna and RT  ##09
            data= data.drop(columns='entities')
            data = data.drop(data[data.text.str.contains("RT")].index)
            
        except:
                print('Error in try: 09, drop') 
        
        try:    # create a file       ##10
            data.to_csv(name+'.csv', line_terminator='\rn')
        
        except:
            print('error al crear fichero')
            
        return 


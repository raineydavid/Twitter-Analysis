
# coding: utf-8

# In[ ]:


def twitter_setup():
    """
    Función de utilidad para configurar la API de Twitter
    con nuestras claves de acceso.
    """
    # Autenticación y acceso usando claves:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    # Retornar API con autenticación:
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api


import codecs # support codecs.open encoding utf-8 in python2 
import pandas as pd # support csv reading
from collections import Counter
import string
def get_popularHashtags_unitedairlines():
    """Get the 10 most popular hashtags per day on tweets on
     United Airlines 10000 per day, 
    from 2017-04-04 to 2017-04-14 and save as .cvs files.
        :input: None
        :type: None
        :return: None
        :type: None
    """
    fields = ['hashtags'] # files to read
    # get any desird day as you want
    date_Day = ['04', '05', '06', '07', '08', '09', '10', '11', '12', '13']
    #
    popularity_cols=[[] for i in range(10)]
    dateCol=[]
    for date_DD in xrange(10):
        csv_input = pd.read_csv('United_Airlines_'+ "2017-04-" + 
          date_Day[date_DD] + '.csv', skipinitialspace=True, usecols=fields)
        dateCol.append("2017-04-" + date_Day[date_DD])
        print 'processing file: '+ 'United_Airlines_'+ "2017-04-" + date_Day[date_DD] + '.csv'
        
        # add all hashtags of all tweets from all files to list
        hashtags = []
        for htext in csv_input.hashtags:
          hstr = htext.translate(None, string.punctuation)
          for hashtag in hstr.split():
            hashtags.append(hashtag)
        
        c=Counter(hashtags)

        # take most popular 10 per day
        for i in range(10):
          popularity_cols[i].append(c.most_common(10)[i])

    # add dates
    popularity_cols.insert(0,dateCol)
    # headers
    headers=['date']
    for i in range(9,-1,-1):
      headers.append(i)
    
    # to dataframe and csv
    df = pd.DataFrame(popularity_cols)
    df=df.transpose()
    df.columns = headers

    df.to_csv('United_Airlines_Popular_Hashtags_'+ "2017-04-" + 
          date_Day[0] +"_to_2017-04-"+date_Day[len(date_Day)-1] + '.csv', index=False)

get_popularHashtags_unitedairlines()


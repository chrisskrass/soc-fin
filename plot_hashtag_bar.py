import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ast import literal_eval as make_tuple

def plotHashtags(filename, savePng=True):
    """Created a stacked bar plot for the given hashtag data csv
        :input: filename: path to file of csv
                savePng: if user wants the plot saved as a png
        :type: None
        :return: None
        :type: None
    """    
    # error checking
    assert isinstance(filename, basestring)
    try:
        df = pd.read_csv(filename)
    except:
        print "error reading file " + filename
        return
    col_number = df.shape[1]
    row_number = df.shape[0]

    #print hasthag counts to console
#     for i in df.ix[y]:
#         print i


    data = [[] for i in range(col_number)]
    col_number2=str(col_number-2)

    temp=[]
    for row in df.iterrows():
        index, data = row
        temp.append(data.tolist())
 
    
    xDates = df['date']
    data=[]
    data_numer=[]
    data_hashtag=[]
    # get data except dates
    for i in df.loc[:,col_number2:'0']:
        data.append( df[i].tolist())
    # extract tuple data
    for i in data:
        x=[]
        y=[]
        for j in i:
            x.append(make_tuple(j)[1])
            y.append(make_tuple(j)[0])
        data_numer.append(x)
        data_hashtag.append(y)
    df=pd.DataFrame(data_numer)
    df=df.transpose() 

    # plot counts
    ax = df.plot.bar(stacked=True,legend=False);

    #label totals at top of bar 
    for i in ax.patches[len(ax.patches)-row_number:]:
        plt.text(i.get_x(),i.get_y()+75, int(i.get_y()),fontsize=10)
        
    plt.gcf().subplots_adjust(bottom=0.15)
    plt.xticks(range(10),xDates)       
    plt.xticks(rotation=30)
    plt.ylabel('number of tweets')
    plt.xlabel('date')
 
    height = 2000
    for i in temp:
        plt.text(10,height,i)
        height = height-200

    

     # if set, save as png
    if savePng:
        plt.savefig(filename+'.png')
    plt.show();
    return

plotHashtags('United_Airlines_Popular_Hashtags_2017-04-04_to_2017-04-13.csv', True)


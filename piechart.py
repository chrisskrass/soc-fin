import pandas as pd
import matplotlib.pyplot as plt

def pie_chart(filepath):
    '''
    plot pie_chart about people opinions

    param: filepath: .csv file filepath
    type: basestring
    return: None
    type: None
    '''

    df = pd.read_csv(filepath)

    pos = df[:][df['compound']>0.5].shape[0]
    neutral = df[:][df['compound'].between(-.5, .5)].shape[0]
    neg = df[:][df['compound']<0.5].shape[0]

    # Data to plot
    labels = 'Positive', 'Neutral', 'Negative'
    sizes = [pos, neutral, neg]
    # colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0)

    # Plot
    plt.figure
    plt.title('Tesla 2018-01-29')
    plt.pie(sizes, explode=explode, labels=labels,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()

pie_chart('sentiment_data/TESLA_Sentiment/TESLA_Sentiment_2018-01-29.csv')

import pandas as pd
import numpy as np
from datetime import datetime # Used to convert strings (in sentiment analysis) to type Datetimeindex 
from matplotlib.pylab import subplots
import matplotlib.pyplot as plt

def plot_df(df_data, company_name):
    '''
    This function plots a single company's stocks and respective sentiment rating of tweets for given dates. 
    
    df_data: type DataFrame. Columns: Index(DateTime),Sentiments,Open,High,Low,Close,Volume
    company_name: type str
    high_lows: type boolean. Enable for additional text. 
    '''
    assert isinstance(df_data,pd.DataFrame)
    assert isinstance(company_name,str)    
    dates = df_data.index.values
    company_stocks = df_data.iloc[:,4] # At close
    sentiments = df_data.iloc[:,0]
    assert bool(len(dates)), "Does your df_data contain valid data?"
    assert bool(len(company_stocks))
    assert bool(len(sentiments))
    assert (company_stocks.all() > 0)
    
    #debug use
    debug_data = df_data.iloc[:,2] 

    fig,ax = subplots(nrows=2, sharex = True)
    fig.set_figheight(10)
    fig.set_figwidth(30)
    ax[0].plot(dates,company_stocks)
    ax[1].plot(dates,sentiments)
    ax[0].plot(dates,debug_data)
    ax[1].set_xlabel('Date')
    ax[0].set_ylabel('Stock Prices ($)')
    ax[1].set_ylabel('Sentiment Rating')
    title_text = company_name + ': Social Effects on Stock'
    ax[0].set_title(title_text)
#     ax[0].legend()
#     ax.set_xticks(np.arange(0, 10, 1))
#     ax.set_yticks(numpy.arange(0, 1., 0.1))
    ax[0].grid(b=True, which='both')
    ax[1].grid(b=True, which='both')
    ax[0].set_xticks(dates[1:-1:1],minor=True)
#     ax[0].tick_params('both', length=10, width=1, which='minor')
    plt.show()

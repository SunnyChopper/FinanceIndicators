# FinanceIndicators
This is a Python class that helps you get financial indicator data that can be used for machine learning. 

Most online free datasets (ex. Yahoo Finance) only give price data. That data by itself is usually not enough to extract some helpful information. So I decided to make a helper class that can derive more data from price data. 

I've been trading stocks and forex for since 2012, however, just now getting into computer science. I know that some of these indiciators can be very helpful to extract information. 

Currently, these are the indicators that I have programmed:
<ul>
<li>Stochastics</li>
<li>Simple Moving Average (SMA)</li>
<li>Bollinger Bands</li>
<li>Relative Strength Index (RSI)</li>
<li>Ichimoku Clouds</li>
</ul>

When there is more than one data point per price point, for example, a Bollinger Band returns an upper band, a middle band, and as a lower band, the function will return an array per price point. 

<b>Note: </b>I'm not a master in algorithm analysis and optimization. If someone can help me with algorithmic analysis, that'd be great!

from yahoo_fin import options
nflx_dates = options.get_expiration_dates("nflx")
chain = options.get_options_chain("nflx")
chain["calls"]
 
chain["puts"]
options.get_options_chain("nflx", "April 26, 2019")
 
options.get_options_chain("nflx", "05/03/19")
 
options.get_options_chain("nflx", "05/10/2019")
options.get_calls("nflx")
 
options.get_calls("nflx", "04/26/19")
 
 
options.get_puts("nflx")
 
options.get_puts("nflx", "04/26/19")

####################################################
#How to get options data for each expiration date

nflx_dates= options.get_expiration_dates("nflx")
 
info = {}
for date in nflx_dates:
    info[date] = options.get_options_chain("nflx")
    
info["October 18, 2019"]

##################################################

# How to get options data for every stock in the Dow
from yahoo_fin import stock_info as si
 
dow_tickers = si.tickers_dow()
 
# replace DOW with DWDP in ticker list
dow_tickers.remove("DOW")
dow_tickers.append("DWDP")
 
# scrape the options data for each Dow ticker
dow_data = {}
for ticker in dow_tickers:
    try:
        dow_data[ticker] = options.get_options_chain(ticker)
    except Exception:
        print(ticker + " failed")
        
        
dow_data["AAPL"]["calls"]
 
dow_data["WMT"]["calls"]

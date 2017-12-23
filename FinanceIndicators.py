# Import classes
import numpy as np

# These are helper functions to assist the main functions
def cl__(starting_index, end_index, prices):
	high = 0
	low = 10000
	for j in range(starting_index, end_index):
		price = prices[j]
		if price > high:
			high = price
		elif price < low:
			low = price
	cl = (high + low) / 2
	return cl

def bl__(starting_index, end_index, prices):
	high = 0
	low = 10000
	for j in range(starting_index, end_index):
		price = prices[j]
		if price > high:
			high = price
		elif price < low:
			low = price
	bl = (high + low) / 2
	return bl

def span_b__(starting_index, end_index, prices):
	high = 0
	low = 10000
	for j in range(starting_index, end_index):
		price = prices[j]
		if price > high:
			high = price
		elif price < low:
			low = price
	span_b = (high + low) / 2
	return span_b

def sma__(price_data, current_index, time_period):
	sum_of_price = 0
	for i in range(current_index - time_period, current_index):
		sum_of_price += price_data[i]
	return sum_of_price/time_period

def avg_gain__(price_data):
	sum_of_price = 0
	for i in range(0, len(price_data)):
		if i < (len(price_data) - 1):
			today_price = price_data[i]
			tomorrow_price = price_data[i+1]

			if tomorrow_price > today_price:
				sum_of_price += tomorrow_price - today_price
	return sum_of_price/len(price_data)

def avg_loss__(price_data):
	sum_of_price = 0
	for i in range(0, len(price_data)):
		if i < (len(price_data) - 1):
			today_price = price_data[i]
			tomorrow_price = price_data[i+1]

			if tomorrow_price < today_price:
				sum_of_price += today_price - tomorrow_price
	avg_loss = sum_of_price/len(price_data)
	if avg_loss == 0:
		avg_loss = 0.0001
	return avg_loss

# This function will return an array of stochastics values given price data
def getStochastics(price_data, k_value = 14):
	''' This function returns a numpy array with stocahstic inidicator values. '''
	# Create placeholder list
	stochastics = []

	for i in range(0, len(price_data)):
		if i < k_value:
			# This means this is before the calculation can be done
			stochastics.append(np.nan)
		else:
			# Find the lowest low, highest high, and current close to do calcualation
			lowest_low = 10000
			highest_high = 0
			current_close = price_data[i]

			# Look back 'k' days and get the highest high and lowest low
			for j in range(i - k_value, i):
				price = price_data[j]
				if price < lowest_low:
					lowest_low = price
				elif price > highest_high:
					highest_high = price

			# Calculate the k value
			k = ((current_close - lowest_low)/(highest_high - lowest_low)) * 100

			# Append the k value
			stochastics.append(k)

	# Return the numpy version
	return np.array(stochastics)

def getSMA(price_data, lookback = 10):
	''' This function returns a numpy array with simple moving average indicator values. '''
	# Create placeholder list
	sma = []

	# Loop through the dataset
	for i in range(0, len(price_data)):
		if i < lookback:
			# This means that we don't have enough data yet
			sma.append(np.nan)
		else:
			# Sum the 'n' previous days
			sum_of_price = 0
			for j in range(i - lookback, i):
				sum_of_price += price_data[j]

			# Find the average
			average_price = sum_of_price / lookback

			# Append to SMA list
			sma.append(average_price)


	# Return the numpy array version of the list
	return np.array(sma)

def getBollingerBands(price_data, k_value = 20):
	''' This function returns a numpy array with the Bollinger Bands indicator values. '''
	# Create placeholder list
	b_bands = []

	# Loop through dataset
	for i in range(0, len(price_data)):
		if i < k_value:
			# Not enough data to perform a calculation
			b_bands.append([np.nan, np.nan, np.nan])
		else:
			# Calculate the bands
			upper_band = sma__(price_data, i, k_value) + (np.std(price_data[i-k_value:i]) * 2)
			middle_band = sma__(price_data, i, k_value)
			lower_band = sma__(price_data, i, k_value) - (np.std(price_data[i-k_value:i]) * 2)

			# Append
			b_bands.append([lower_band, middle_band, upper_band])

	# Return the numpy array version of the list
	return np.array(b_bands)

def getRSI(price_data, k_value = 14):
	''' This function returns a numpy array with the RSI indicator values. '''
	# Create placeholder list
	rsi = []

	# Loop through dataset
	for i in range(0, len(price_data)):
		if i < k_value:
			# Not enough data to perform a calculation
			rsi.append(np.nan)
		else:
			rs = avg_gain__(price_data[i-k_value:i]) / avg_loss__(price_data[i-k_value:i])
			rsi_value = 100 - (100 / (1 + rs))
			rsi.append(rsi_value)

	# Return the numpy array version of the list
	return np.array(rsi)

def getIchimoku(price_data, conversion_line_period = 9, base_line_period = 26, leading_span_b_period = 52, lagging_span_value = 26):
	''' This function returns a numpy array with the Inchimoku inidicator values. 

		The values are in the order [conversion_line, base_line, leading_span_a, leading_span_b, lagging_span]
	'''
	# Create placeholder lists
	ichimoku = []

	# Loop through price data
	for i in range(0, len(price_data)):
		if i < conversion_line_period:
			# Not enough data for anything, append NaN to everything
			conversion_line = np.nan
			base_line = np.nan
			leading_span_a = np.nan
			leading_span_b = np.nan
			lagging_span = np.nan

			# Append
			ichimoku.append([conversion_line, base_line, leading_span_a, leading_span_b, lagging_span])
		elif i < base_line_period:
			# Somethings will still not have enough data...append NaN again
			base_line = np.nan
			leading_span_a = np.nan
			leading_span_b = np.nan
			lagging_span = np.nan

			# Conversion line can now be predicted
			conversion_line = cl__(i - conversion_line_period, i, price_data)

			# Append
			ichimoku.append([conversion_line, base_line, leading_span_a, leading_span_b, lagging_span])
		elif i < leading_span_b_period:
			# This time, the leading span B cannot be calculated, everything else can be though
			leading_span_b = np.nan 

			# Calculate the rest and append
			conversion_line = cl__(i - conversion_line_period, i, price_data)
			base_line = bl__(i - base_line_period, i, price_data)
			leading_span_a = (conversion_line + base_line) /2
			lagging_span = price_data[i-lagging_span_value]

			# Append
			ichimoku.append([conversion_line, base_line, leading_span_a, leading_span_b, lagging_span])
		else:
			# Everything can be calculated
			conversion_line = cl__(i - conversion_line_period, i, price_data)
			base_line = bl__(i - base_line_period, i, price_data)
			leading_span_a = (conversion_line + base_line) /2
			leading_span_b = span_b__(i - leading_span_b_period, i, price_data)
			lagging_span = price_data[i-lagging_span_value]

			# Append
			ichimoku.append([conversion_line, base_line, leading_span_a, leading_span_b, lagging_span])

	# Convert to numpy array and return
	return np.array(ichimoku)
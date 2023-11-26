# Problem description: u would have to exchange your money for various foreign currencies. 
# This problem deals with multiple currencies and their exchange rates. Your task is to 
# verify that some set of exchange rates is safe, namely detect a possibility of so-called arbitrage.

#My initial idea is to solve this problem using network flow with ford folkerson.
# Given some flow we can determine if we should output 'Arbitrage' or 'ok'
# There are max 200*200 exchange rates (edges)
# I think I will use adjacency lists to represent the graph
# as it is computationally more efficient for sparse graphs, as compared to 
# adjacency matrices.

# Upon further inspection this seems to be a DP problem about detecting negative cycles within the graoh. 
# A negative cycle is a directed cycle, such that the sum of edge weights are negative. 

# We can run Bellman-Ford algorithm V times to detect a negative cycle. If we detect a negative cycle, we can output 'Arbitrage'
# Need to figure out how to convert the decimal numbers to a negative number, possibly? It might not be necessary, as the ratios are still
# Stricly smaller ?? Otherwise we can say a positive number  1 > is > 1 and a negative number 0 < is < 1. 
# It is definitely necessary! To convert the problem we make the weights into their negative logarithm.
# Adding the logarithmic weights up during the bellman ford algorithm corresponds to multiplying currencies


# Some arbitrary number of test cases, need to use sys.stdinput to determine when input stream is over
#input for on test case:
number_of_currencies = int(input()) # between 1 and 200
currency_codes = input().split() # Three letter currency codes, all unique within test case
number_of_exchange_rates = int(input())
for exchange_rate in range(number_of_exchange_rates):
    firt_currency, second_currency, rate = input.split()


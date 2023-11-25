# Problem description: u would have to exchange your money for various foreign currencies. 
# This problem deals with multiple currencies and their exchange rates. Your task is to 
# verify that some set of exchange rates is safe, namely detect a possibility of so-called arbitrage.

#My initial idea is to solve this problem using network flow with ford folkerson.
# Given some flow we can determine if we should output 'Arbitrage' or 'ok'
# There are max 200*200 exchange rates (edges)
# I think I will use adjacency lists to represent the graph
# as it is computationally more efficient for sparse graphs, as compared to 
# adjacency matrices.

# Some arbitrary number of test cases, need to use sys.stdinput to determine when input stream is over
#input for on test case:
number_of_currencies = int(input()) # between 1 and 200
currency_codes = input().split() # Three letter currency codes, all unique within test case
number_of_exchange_rates = int(input())
for exchange_rate in range(number_of_exchange_rates):
    firt_currency, second_currency, rate = input.split()


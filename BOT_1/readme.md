#simple policy-gradient based agent


## network
#   NETWORK ARCHITECTURE
#   (input layer)                         (output layer)
#
#   stock_open
#   stock_close                             buy
#   stock_high      (fully_connected)       sell
#   stock_low                               hold
#   capital
#   stock_held


## assumptions
* Assume stocks are bought at closing rate.
* Buy defaults to max feasible vol of stocks if capital is lower than requested buy.
* Volume of sell defaults to max stock holding if requested sell volume is higher than holding volume.

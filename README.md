What is The Gateway?
===
The code samples here lets you trade futures, by using The Gateway.

Download The Gateway for free at http://thegateway.azurewebsites.net.

The Gateway simply extends CTS T4 (a futures trading platform) with a socket interface, allowing other programming languages such as Python to collect data and send orders.

- The *examples* folder contain Python scripts to test The Gateway.
- The *classes* folder contains required classes to run the examples.

All scripts tested with Python 2.7.

Requirements
===
1. A CTS-enabled futures trading account, or a simulator account. Sign up for a free simulator account at https://cts.sim.t4login.com/register?ref=CTS-footer.
2. The Gateway installed, with the indicated port opened.
3. Your scripts with socket connections to The Gateway using the port and IP address.

Getting started
===
- Open The Gateway and log in to your T4 account.
- Make a note of the IP address and port number displayed on The Gateway.
- Ensure that the port number is open and available when running over a network.
- When working with <code>contract_id</code>, use the *Search contract* tool in The Gateway and look for the desired *Alias ID*.

## Streaming market data ##

### 1. Importing the classes ###
In your Python script, import the required classes: 
```
from classes.socket_client import SocketClient
from classes.gateway_interface import GatewayInterface
```
Ensure your Python script lies in the same directory or in the *examples* directory within the source file directory. 

### 2. Set up the interface ###
Create an instance of *SocketClient* with your IP address and port number.

Then create an instance of *GatewayInterface*, which requires the instance of *SocketClient*. 

```
socket_client = SocketClient("localhost", 4000)
gateway = GatewayInterface(socket_client)
```

### 3. Request data ###
The list of public methods can be found at http://scctrader.azurewebsites.net/code-samples#methods.

For example, to stream market data, define a function to handle the event:
```
def on_market_data(market_data):
    print market_data
```

Then, tell The Gateway to use this function for market data updates:
```
gateway.set_data_handlers(market_data=on_market_data)
```

Now that our script can handle data updates, let's request for Emini Dow June 15 contract quotes:
```
gateway.request_market_data("XCME_E YM (M15)")
```

### 4. Keep the application active ###
Keep the socket connection running with an infinite loop:
```
socket_client.loop()
```
Press <kbd>Ctrl</kbd>+<kbd>Z</kbd> or similar to terminate the process.


## Sending a market order ##
First, import the required classes and set up the interface in the same manner.
```
from classes.socket_client import SocketClient
from classes.gateway_interface import GatewayInterface

socket_client = SocketClient("localhost", 4000)
gateway = GatewayInterface(socket_client)
```
To send a sell order of a Emini Nasdaq-100 June 15 contract at the market price:
```
gateway.send_market_order("XCME_Eq NQ (M15)", False, 1)
```

Documentation
===
Further information can be found at http://scctrader.azurewebsites.net/code-samples.

Disclaimer
===
Use The Gateway and all script files at your own risk! We at HFTStrat and all other third-party application providers are not responsible for losses or damages that may result from its use. 

The Gateway is not affliated with CTS in any circumstances. 

Futures and options trading involves substantial risk of loss and is not suitable for all investors. Clients may lose more than their initial investment. Past performance of actual trades or strategies cited herein is not necessarily indicative of future performance. 









What is The Gateway?
===
The code samples here lets you trade futures, by using The Gateway.
Download The Gateway for free at http://thegateway.azurewebsites.net.
The Gateway simply extends CTS T4 (a futures trading platform) with a socket interface, allowing other programming languages such as Python to collect data and send orders.

Requirements
===
1. A CTS-enabled futures trading account, or a simulator account. Sign up for a free simulator account at https://cts.sim.t4login.com/register?ref=CTS-footer.
2. The Gateway installed, with the indicated port opened.
3. Your scripts with socket connections to The Gataway using the port and IP address.

Getting started
===
## 1.Importing the classes ##
In your Python script, import the required classes: 
```
from classes.socket_client import SocketClient
from classes.gateway_interface import GatewayInterface
```
Ensure your Python script lies in the same directory or in the *examples* directory within the source file directory. 

## 2. Set up the interface ##
Create an instance of *SocketClient* with The Gateway's IP address and port number. Ensure that the port number is open and available when running over a network.

The IP address and port number can be obtained from The Gateway directly.

Then create an instance of *GatewayInterface*, which requires the instance of *SocketClient*. 

```
ip, port = "10.211.55.3", 4000
socket_client = SocketClient(ip, port)
gateway = GatewayInterface(socket_client)
```











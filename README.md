## A Routing table generator to use two networks at the same time for a specific services

> the ip list and routing tables that exists in this respository are created for discord streaming and voice channels it can be changed to any service by changing the ip list to the desired service and regenerate the route and unroute script with python.

by creating routes we are forcing the packets to be forwarded through the interface that we will select.

the "generateScripts.py" uses wmi package so you need to install it by :
> python3 -m pip install wmi

this script reads the ips from the ipList.txt file then he will create routing rules to route all the packets going to these ips through the secondary network selected when executing the python script.

after executing the generateScripts.py and selecting main interface and secondary interface you need to execute route.bat as admin to activate the routes.

Note: the IP lists can be changed through time which can affect the routing

## Resources

- [Discord IP ranges](https://github.com/DeadPackets/DiscordIPs/blob/main/dns_brute/latest_ranges.txt)

- [Windows Route Command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/route_ws2008)

- [Windows Management Instrumentation (WMI)](https://pypi.org/project/WMI/)
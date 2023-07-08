import wmi

# Connect to the WMI service
wmiService = wmi.WMI()

# Get all network interfaces
interfaces = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)

# Display the available interfaces
print("Available Network Interfaces:")
for i, interface in enumerate(interfaces):
    print(f"{i+1}. {interface.Description}")


# Prompt the user to choose two interfaces
interface_indices = []
while len(interface_indices) < 2:
    try:
        interfaceType = "Main Interface" if len(interface_indices) == 0 else "Streaming Interface"
        index = int(input(f"Choose Interface {interfaceType} (Enter corresponding number): "))
        if 1 <= index <= len(interfaces):
            if index not in interface_indices:
                interface_indices.append(index)
            else:
                print("Interface already selected. Choose a different interface.")
        else:
            print("Invalid input. Choose a valid interface number.")
    except ValueError:
        print("Invalid input. Enter a valid number.")


# Get the selected interfaces
interface_Main = interfaces[interface_indices[0]-1]
interface_Secondary = interfaces[interface_indices[1]-1]

# Display the chosen interfaces
print(f"Interface Main: {interface_Main.Description}")
print(f"Interface Streaming: {interface_Secondary.Description}")


routes = wmiService.Win32_IP4RouteTable()


ip_masks = []
with open("ipList.txt", 'r') as file:
    for line in file:
            line = line.strip().split()
            if("#" in line or line.strip() == ""):
                continue
                
            if len(line) == 2:
                ip_address = line[0]
                subnet_mask = line[1]
                ip_masks.append((ip_address, subnet_mask))
            else:
                print("Invalid line format:", line)

route_bat = open("route.bat", 'w')
unroute_bat = open("unroute.bat", 'w')
    
route_bat.write(f"netsh interface ip set interface {interface_Main.InterfaceIndex} metric=100\n")
route_bat.write(f"netsh interface ip set interface {interface_Secondary.InterfaceIndex} metric=200\n")
for range in ip_masks:
    route = f"route add {range[0]} MASK {range[1]} {interface_Secondary.DefaultIPGateway[0]} IF {interface_Secondary.InterfaceIndex}\n"
    unroute = f"route delete {range[0]}\n"
    route_bat.write(route)
    unroute_bat.write(unroute)
        

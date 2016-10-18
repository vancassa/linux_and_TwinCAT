This is an example of connecting Linux on a VM with TwinCAT on a Windows host, using pyads and TCP/IP.

![alt tag](https://puu.sh/rFf7K/dffe934e5d.png)

Ubuntu 14.04 in VMWare talking to Windows host through TCP/IP.
Python3 on Windows talking to TwinCAT through pyads.

## Notes
The better way is to use pyads in Linux on the VM to talk to TwinCAT directly.
However the route needs to be added in TwinCAT, and I've been getting error "Device is busy".
Please notify me if you find a way to do it.

Another better way is to set up a TCP/IP client or server in TwinCAT and let the Linux to talk to TwinCAT directly through TCP/IP.
However, running TCP/IP client or server in TwinCAT gave me error 6: target port not found.
The only help I could find is only this German forum: http://www.sps-forum.de/codesys-und-iec61131/60976-twincat3-tcpip-server-sample01-fb_socketlisten-system-error-6-a.html

EDIT: I managed to make my TCP/IP server working in TwinCAT. Error code 6 means that there is something wrong with the installation of TF6310 function. Go to Control Panel, uninstall the TF6310 TCP/IP Server function, and do a clean installation again. Go to your Task Manager - Processes, there should be TcpIpServer.exe running in the process.

This is an example of connecting Linux on VM with TwinCAT on a Windows host, using TCP/IP.

![alt tag](https://puu.sh/rMWjN/4b1f63343e.png)

The sample code and more info can be found here:
https://github.com/milk-coffee/TwinCAT_TCP_IP_Server


## Configuration
Network adapter settings for virtual machine: NAT or Host Only (DHCP)

My VMWare IP address on Windows: 192.168.52.1

IP address assigned to Ubuntu: 192.168.52.129

## Usage

1. Run the TwinCAT program
2. Run the Windows python program
3. Run the Linux python program. User will be prompted to send a command:
  * 'read' : read the 'test' variable in the TwinCAT
  * 'write 1' : write the 'test' variable in TwinCAT to be TRUE
  * 'write 0' : write the 'test' variable in TwinCAT to be FALSE
  * anything else will just be echoed back

### TwinCAT
Inside the TwinCAT program, there are only two variables, and I only use one of them in this example: 'test' which is a boolean, located in MAIN.POU

### Windows
The python program set up a TCP/IP server, and wait for any incoming data from the TCP/IP client.

If incoming data is 'read', pyads will read the value of 'test' variable in TwinCAT, and send it to the client.

If incoming data is 'write 1', pyads will set the value of 'test' variable to TRUE.

If incoming data is 'write 0', pyads will set the value of 'test' variable to FALSE.

```
python windows_tcp_server.py
> Connection address: ('192.168.52.129', 35866)
> received data: b'read'
> False
> received data: b'write 1'
> received data: b'read'
> True
> received data: b'write 0'
> received data: b'read'
> False
```

### Ubuntu
The python program connect a TCP/IP client to a server. User is prompted to send a command.

```
python3 linux_tcp_client.py
b'connected'
Send command: read
b'False'
Send command: write 1
b'write 1'
Send command: read
b'True'
Send command: write 0
b'write 0'
Send command: read
b'False'
Send command: close
```

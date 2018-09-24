# cmpe273-lab3

Code to send "Hello World" from client to server via UDP using Twisted Lib.

Files:
connected_udp_client.py
connected_udp_server.py
multicast_udp_client.py
multicast_udp_server.py

Question: What happened when you send message from client in Multicast UDP when server is not available?
Answer: When executed, the client itself joins the multicast group with the address "228.0.0.5". The client then sends a UDP message "Hello World" to this multicast address. Since no server is running and the client is the member of the multicast group, the client also receives the same message it sent earlier and prints "Datagram b'Hello World' received from ('<IP>', <Port>)" on screen.


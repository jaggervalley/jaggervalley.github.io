import socket


def scan():

  print "This is a port scanner"
  ipaddr = raw_input("Enter an IP address to check its ports: ")
  ports = [20,21,22,23,25,53,67,68,69,80,110,137,138,139,143,161,162,389,443]
  print "\nScanning ports on %s " %(ipaddr)
  
  for port in ports:
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if skt.connect_ex((ipaddr,port)) == 0:
      print "\tPort %d is open" %(port) 
    else:
      print "\tPort %d is closed" %(port)
  
  y = raw_input("...")
  
  
  
scan()

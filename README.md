# MPTCP

## Concept


- Wiki example: http://blog.multipath-tcp.org/blog/html/2018/12/18/advertising_addresses_with_multipath_tcp.html
- http://blog.multipath-tcp.org/blog/html/2018/12/18/advertising_addresses_with_multipath_tcp.html
  - Explanation on why `ADD_ADDR`

## Test


````shell
podman run --network host -v "$PWD":/WORKDIR -it  python:3-alpine python /WORKDIR/code/tcp_client.py 
````

Or use ubuntu with python, we can check MTCP via `sudo wireshark` and use `ip mtcp`

````
scoulomb@scoulomb-Precision-3540:~$ sudo ip mptcp monitor
[       CREATED] token=2275ffa6 remid=0 locid=0 saddr4=192.168.86.208 daddr4=5.196.67.207 sport=36918 dport=80
[   ESTABLISHED] token=2275ffa6 remid=0 locid=0 saddr4=192.168.86.208 daddr4=5.196.67.207 sport=36918 dport=80
[     ANNOUNCED] token=2275ffa6 remid=2 daddr6=2001:41d0:a:ffcf::1 dport=80
[       CREATED] token=52b5d054 remid=0 locid=0 saddr4=192.168.86.208 daddr4=5.196.67.207 sport=41114 dport=80
[   ESTABLISHED] token=52b5d054 remid=0 locid=0 saddr4=192.168.86.208 daddr4=5.196.67.207 sport=41114 dport=80
[     ANNOUNCED] token=52b5d054 remid=2 daddr6=2001:41d0:a:ffcf::1 dport=80
````
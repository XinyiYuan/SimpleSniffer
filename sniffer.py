#! /usr/bin/env py39env
#--*-- coding:utf-8 --*--

import struct,socket
import ctypes as ct
import libpcap as pcap

#pcap.config(LIBPCAP="wpcap")
errbuf = ct.create_string_buffer(pcap.PCAP_ERRBUF_SIZE + 1)

# 方法2 :使用lookupdev获取网卡接口名称
# if False:
device = pcap.lookupdev(errbuf)
if errbuf.value:
    print(errbuf.value)

# 方法3 ： 使用findalldevs获取网卡接口名称
if False:
    alldevs = ct.POINTER(pcap.pcap_if_t)()
    pcap.findalldevs(ct.byref(alldevs), errbuf)
    #print(alldevs[0].name)
    for dev in alldevs:
        print(dev.name)
        device = dev.name
        break # 使用第一个
    pcap.freealldevs(alldevs)

handle = pcap.open_live(device,4096,1,1000,errbuf)

if errbuf.value:
    print("hanle error :",errbuf.value)

fname = b"realtime1.cap"
fPcap = pcap.dump_open(handle,fname)
fPcapUbyte = ct.cast(fPcap,ct.POINTER(ct.c_ubyte))
pheader = pcap.pkthdr()
i = 0
print("live cap begin")
while True:
    packet = pcap.next(handle,pheader)
    if not packet :
        continue
    print(i,pheader.ts.tv_sec,pheader.len,pheader.caplen)
    p=ct.pointer(packet.contents)
    ipInfo = struct.unpack('<BBHHHBBH4s4s',bytes(p[14:34]))
    srcIp = socket.inet_ntoa(ipInfo[-2])
    dstIp = socket.inet_ntoa(ipInfo[-1])
    print(srcIp,"=>",dstIp)
    pcap.dump(fPcapUbyte,pheader,packet)

    i = i + 1
    if i > 2:
        break

print("i = ", i)
print("live cap end")
pcap.close(handle) # need close
pcap.dump_flush(fPcap)
pcap.dump_close(fPcap)
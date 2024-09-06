from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.node import OVSKernelSwitch, RemoteController
from time import sleep
from datetime import datetime
from random import randrange, choice

class MyTopo(Topo):

    def build(self):

        s1 = self.addSwitch('s1', cls=OVSKernelSwitch, protocols='OpenFlow13')

        h1 = self.addHost('h1', cpu=1.0/20, mac="00:00:00:00:00:01", ip="10.0.0.1/24")
        h2 = self.addHost('h2', cpu=1.0/20, mac="00:00:00:00:00:02", ip="10.0.0.2/24")
        h3 = self.addHost('h3', cpu=1.0/20, mac="00:00:00:00:00:03", ip="10.0.0.3/24")

        s2 = self.addSwitch('s2', cls=OVSKernelSwitch, protocols='OpenFlow13')

        h4 = self.addHost('h4', cpu=1.0/20, mac="00:00:00:00:00:04", ip="10.0.0.4/24")
        h5 = self.addHost('h5', cpu=1.0/20, mac="00:00:00:00:00:05", ip="10.0.0.5/24")
        h6 = self.addHost('h6', cpu=1.0/20, mac="00:00:00:00:00:06", ip="10.0.0.6/24")

        s3 = self.addSwitch('s3', cls=OVSKernelSwitch, protocols='OpenFlow13')

        h7 = self.addHost('h7', cpu=1.0/20, mac="00:00:00:00:00:07", ip="10.0.0.7/24")
        h8 = self.addHost('h8', cpu=1.0/20, mac="00:00:00:00:00:08", ip="10.0.0.8/24")
        h9 = self.addHost('h9', cpu=1.0/20, mac="00:00:00:00:00:09", ip="10.0.0.9/24")

        s4 = self.addSwitch('s4', cls=OVSKernelSwitch, protocols='OpenFlow13')

        h10 = self.addHost('h10', cpu=1.0/20, mac="00:00:00:00:00:10", ip="10.0.0.10/24")
        h11 = self.addHost('h11', cpu=1.0/20, mac="00:00:00:00:00:11", ip="10.0.0.11/24")
        h12 = self.addHost('h12', cpu=1.0/20, mac="00:00:00:00:00:12", ip="10.0.0.12/24")

        s5 = self.addSwitch('s5', cls=OVSKernelSwitch, protocols='OpenFlow13')

        h13 = self.addHost('h13', cpu=1.0/20, mac="00:00:00:00:00:13", ip="10.0.0.13/24")
        h14 = self.addHost('h14', cpu=1.0/20, mac="00:00:00:00:00:14", ip="10.0.0.14/24")
        h15 = self.addHost('h15', cpu=1.0/20, mac="00:00:00:00:00:15", ip="10.0.0.15/24")

        s6 = self.addSwitch('s6', cls=OVSKernelSwitch, protocols='OpenFlow13')

        h16 = self.addHost('h16', cpu=1.0/20, mac="00:00:00:00:00:16", ip="10.0.0.16/24")
        h17 = self.addHost('h17', cpu=1.0/20, mac="00:00:00:00:00:17", ip="10.0.0.17/24")
        h18 = self.addHost('h18', cpu=1.0/20, mac="00:00:00:00:00:18", ip="10.0.0.18/24")

        # Dodawanie połączeń
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)

        self.addLink(h4, s2)
        self.addLink(h5, s2)
        self.addLink(h6, s2)

        self.addLink(h7, s3)
        self.addLink(h8, s3)
        self.addLink(h9, s3)

        self.addLink(h10, s4)
        self.addLink(h11, s4)
        self.addLink(h12, s4)

        self.addLink(h13, s5)
        self.addLink(h14, s5)
        self.addLink(h15, s5)

        self.addLink(h16, s6)
        self.addLink(h17, s6)
        self.addLink(h18, s6)

        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s5, s6)

def ip_generator():
    ip = ".".join(["10", "0", "0", str(randrange(3, 19))])
    return ip

def startNetwork():

    topo = MyTopo()
    c0 = RemoteController('c0', ip='192.168.64.4', port=6653)
    net = Mininet(topo=topo, link=TCLink, controller=c0)
    net.start()

    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')
    h5 = net.get('h5')
    h6 = net.get('h6')
    h7 = net.get('h7')
    h8 = net.get('h8')
    h9 = net.get('h9')
    h10 = net.get('h10')
    h11 = net.get('h11')
    h12 = net.get('h12')
    h13 = net.get('h13')
    h14 = net.get('h14')
    h15 = net.get('h15')
    h16 = net.get('h16')
    h17 = net.get('h17')
    h18 = net.get('h18')

    hosts = [h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18]

    print("--------------------------------------------------------------------------------")
    print("Generating traffic ...")
    h1.cmd('cd /home/joanna/Downloads/5G_Anomaly_Detection/src/webserver')
    h1.cmd('python3 -m http.server 80 &')
    h1.cmd('iperf -s -p 5050 &')
    h1.cmd('iperf -s -u -p 5051 &')

    h2.cmd('service ssh start')
    h2.cmd('dnsmasq &')
    h2.cmd('mosquitto -d')
    sleep(10)

    for h in hosts:
        h.cmd('cd /home/joanna/Downloads/5G_Anomaly_Detection/src/mininet/Downloads')
    
    for i in range(5):
        print("--------------------------------------------------------------------------------")
        print("Iteration n {} ...".format(i+1))
        print("--------------------------------------------------------------------------------")

        for j in range(5):
            src = choice(hosts)
            dst = ip_generator()

            # Generowanie różnorodnego ruchu z anomaliami
            print("Generating anomalous traffic from %s to %s" % (src, dst))

            # Generowanie ICMP Flood (anomalna ilość pingów)
            print("Generating ICMP Flood traffic from %s to %s" % (src, dst))
            src.cmd("timeout 20s ping {} -c 1000 -i 0.001".format(dst))
            sleep(2)

            # Generowanie TCP SYN Flood (anomalny ruch TCP)
            print("Generating TCP SYN Flood traffic from %s to 10.0.0.1" % src)
            src.cmd("timeout 20s hping3 -S -p 5050 -i u1000 10.0.0.1")
            sleep(2)

            # Generowanie UDP Flood (anomalny ruch UDP)
            print("Generating UDP Flood traffic from %s to 10.0.0.1" % src)
            src.cmd("timeout 20s hping3 --udp -p 5051 --flood 10.0.0.1")
            sleep(2)

            # Generowanie nadmiernych żądań HTTP
            print("%s performing HTTP Flood attack on 10.0.0.1" % src)
            src.cmd("for i in {1..200}; do timeout 1s curl -s http://10.0.0.1/index.html; sleep 0.1; done")
            sleep(2)

            # Próba logowania SSH (Brute Force)
            print("Attempting SSH Brute Force attack from %s to 10.0.0.2" % src)
            src.cmd("timeout 30s hydra -l root -P /home/joanna/Downloads/5G_Anomaly_Detection/src/ssh/rockyou.txt 10.0.0.2 ssh")
            sleep(2)

            # Generowanie anomalnego ruchu strumieniowania wideo (wysoka przepustowość)
            print("Streaming high-bandwidth video from %s to 10.0.0.2 via UDP" % src)
            src.cmd("timeout 30s ffmpeg -re -i /home/joanna/Downloads/5G_Anomaly_Detection/src/videos/video.mp4 -vf scale=1920:1080 -b:v 5000k -f mpegts udp://10.0.0.2:1234")
            sleep(2)

            # Generowanie IoT złośliwych wiadomości (MQTT)
            print("Publishing anomalous MQTT messages from %s to topic 'sensor/temperature' on 10.0.0.2" % src)
            src.cmd("for i in {1..1000}; do mosquitto_pub -h 10.0.0.2 -t 'sensor/temperature' -m 'malicious'; sleep 0.05; done")
            sleep(2)

            # Generowanie anomalii VoIP (wysoki ruch)
            print("Generating high traffic VoIP from %s to 10.0.0.2 via SIP" % src)
            src.cmd("timeout 20s sipp -sn uac 10.0.0.2:5060 -r 1000 -m 1000")
            sleep(2)

            print("--------------------------------------------------------------------------------")  

            
            # Generowanie ruchu
            print("Generating normal traffic from %s to %s" % (src, dst))

            # Generowanie ruchu ICMP (ping)
            print("Generating ICMP traffic from %s to %s" % (src, dst))
            src.cmd("ping {} -c 5 -w 5".format(dst))
            sleep(0.1)

            # Generowanie ruchu TCP (iperf)
            print("Generating TCP traffic from %s to 10.0.0.1" % src)
            src.cmd("iperf -p 5050 -c 10.0.0.1 -b 10M")
            sleep(0.1)

            # Generowanie ruchu UDP (iperf)
            print("Generating UDP traffic from %s to 10.0.0.1" % src)
            src.cmd("iperf -p 5051 -u -c 10.0.0.1 -b 5M")
            sleep(0.1)

            # Generowanie ruchu HTTP (curl)
            print("%s downloading index.html from 10.0.0.1" % src)
            src.cmd("timeout 5s curl -O http://10.0.0.1/index.html")
            sleep(0.1)

            # Generowanie ruchu SCP (transfer pliku)
            print("Transferring test.zip from %s to 10.0.0.2 via SCP" % src)
            src.cmd("scp /home/joanna/Downloads/5G_Anomaly_Detection/src/mininet/Downloads/test.zip mininet@10.0.0.2:/home/joanna/Downloads/5G_Anomaly_Detection/src/mininet/Downloads/")
            sleep(0.1)

            # Generowanie ruchu strumieniowania wideo (ffmpeg)
            print("Streaming video from %s to 10.0.0.2 via UDP" % src)
            src.cmd("ffmpeg -re -i /home/joanna/Downloads/5G_Anomaly_Detection/src/videos/video.mp4 -vf scale=640:360 -b:v 500k -f mpegts udp://10.0.0.2:1234")
            sleep(0.1)

            # Generowanie ruchu IoT (MQTT)
            print("Publishing MQTT message from %s to topic 'sensor/temperature' on 10.0.0.2" % src)
            src.cmd("mosquitto_pub -h 10.0.0.2 -t 'sensor/temperature' -m '25.3'")
            sleep(0.1)

            # Generowanie ruchu VoIP (SIP)
            print("Generating VoIP traffic from %s to 10.0.0.2 via SIP" % src)
            src.cmd("sipp -sn uac 10.0.0.2:5060 -m 1")
            sleep(0.1)

            # Generowanie ruchu DNS (dig)
            print("Generating DNS query from %s to 10.0.0.2 for domain 'example.com'" % src)
            src.cmd("timeout 5s dig @10.0.0.2 example.com")
            sleep(0.1)

            print("--------------------------------------------------------------------------------")  

        # Czyszczenie pobranych plików
        h1.cmd("rm -f /home/joanna/Downloads/5G_Anomaly_Detection/src/mininet/Downloads/*")

    print("--------------------------------------------------------------------------------")  
    
    
    net.stop()

if __name__ == '__main__':
    
    start = datetime.now()
    
    setLogLevel('info')
    startNetwork()
    
    end = datetime.now()
    
    print(end-start)

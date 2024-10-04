# fglog_parser
Fortigate Disk Traffic Log Parser




# log entry sample;
date=2024-10-03 time=18:07:00 eventtime=1727950020698390194 tz="+0800" logid="0000000013" type="traffic" subtype="forward" level="notice" vd="root" srcip=79.100.100.100 srcport=50000 srcintf="port2" srcintfrole="wan" dstip=72.200.200.200 dstport=8000 dstintf="VLAN55" dstintfrole="lan" srcuuid="84c2c2c2-0567-5123-abcd-97ffabab10ab" dstuuid="84c2c2c2-0567-5123-abcd-86ffabab10ab" srccountry="Netherlands" dstcountry="Hong Kong" sessionid=170000001 proto=6 vrf=1 action="deny" policyid=88 policytype="policy" poluuid="e1646464-6012-5123-4901-b200112233ff" policyname="Mon-BraPolicy" service="8000" trandisp="noop" duration=0 sentbyte=0 rcvdbyte=0 sentpkt=0 rcvdpkt=0 appcat="unscanned" crscore=30 craction=131072 crlevel="high"

# log entry sample matching group() (internally)
date=2024-10-03
time=18:07:00
eventtime=1727950020698390194
tz="+0800"
logid="0000000013"
type="traffic"
subtype="forward"
level="notice"
vd="root"
srcip=79.100.100.100
srcport=50000
srcintf="port2"
srcintfrole="wan"
dstip=72.200.200.200
dstport=8000
dstintf="VLAN55"
dstintfrole="lan"
srcuuid="84c2c2c2-0567-5123-abcd-97ffabab10ab"
dstuuid="84c2c2c2-0567-5123-abcd-86ffabab10ab"
srccountry="Netherlands"
dstcountry="Hong Kong"
sessionid=170000001
proto=6
vrf=1
action="deny"
policyid=88
policytype="policy"
poluuid="e1646464-6012-5123-4901-b200112233ff"
policyname="Mon-BraPolicy"
service="8000"
trandisp="noop"
duration=0
sentbyte=0
rcvdbyte=0
sentpkt=0
rcvdpkt=0
appcat="unscanned"
crscore=30
craction=131072
crlevel="high"



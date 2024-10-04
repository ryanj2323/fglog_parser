#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Fortigate Log Parser
# 
# 
import re, argparse
from datetime import datetime

## VARs
fields=['eventtime','action','srccountry','srcip','srcport','dstport','dstip','dstcountry']
p='[a-z]+=[0-9]\S*|[a-z]+=["][a-zA-Z0-9+].[^"]+["]'


## FUNCs
def nanoutm2str(nano):
  fmt='%Y-%m-%d %H:%M:%S.%f'
  nt=datetime.fromtimestamp(int(nano)/1000000000).strftime(fmt)
  return nt

def onelinework(line):
  linedict={}
  m_iter=re.finditer(p, line)
  for m in m_iter:
    val=m.group().split('=')
    key=val[0]
    linedict[key]=val[-1].strip('"')
  #print(linedict)

  exp=''
  for fld in fields:
    if fld == 'eventtime':
      v=nanoutm2str(linedict.get(fld, ''))
    else:
      v=linedict.get(fld, '')
    exp+=v+'\t'
  exp=exp.rstrip()
  return exp+'\n'


## MAIN
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('arg1') 
  args=parser.parse_args()

  parsedfile=open(args.arg1+'_parsed.txt', "w", encoding='utf-8')
  parsedfile.write('\t'.join(fields)+'\n')
  with open(args.arg1) as f:
    for line in f:
      parsedfile.write(onelinework(line))










#! /usr/bin/env/ python

import socket

STX = "02"
ETX = "03"
LRC = ""

txRequestDelim = "20"
toIntStationNo= "00"
fromIntStationNo = "00"
pmsRequestNo = "001"
transactionCode = "001" 
password = "SAFLOK"
keyNum = ""
keyLevel =  "31"
encoderOne = "21"
encoderLED = "FF"
keyVolume "01"
projChkoutDate = "073016" #MMDDYY
projChkoutTime = "1305"   #HHMM
keyExpirDate = "073016"   #MMDDYY
keyExpirTime = "1305"     #HHMM
passNumOption = "0"

from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnection import CardConnection
from smartcard.util import toHexString, toBytes
from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.Exceptions import CardRequestTimeoutException

#-------------------------------------------------------Config-------------------------------------------------------------------
SELECT     = [0xA0, 0xA4, 0x00, 0x00, 0x02]
READ       = [0xA0, 0xB0, 0x00, 0x00, 0x00]
GET        = [0XA0, 0XC0, 0x00, 0x00]
DF_TELECOM = [0x7F, 0x10]
ADN        = [0x6F, 0x3A]
FDN        = [0x6F, 0x3B]
SMS        = [0x6F, 0x3C]


#Example ADN
#ADN        = [0xA0, 0xA4, 0x00, 0x00, 0x02, 0x6F, 0x3A]

#CLASS | INSTRUCTION | PARAMETER 1 | PARAMETER 2 | Length Request | File ID                | Length Response 
#0xA0       0xA4          0x00          0x00           0x02          0x6F0x3A ( 0x6F3A)        00 (Default)



#CLA | INS | P1 | P2 | Lc | Data | Le
#160   164    0    0   2    127    16

#CLA | INS | P1 | P2 | Lc | Data | Le
#160   178    0    0   10    127    16

#-------------------------------------------------------Connection-------------------------------------------------------------------
cardtype = AnyCardType()
cardrequest = CardRequest( timeout=10, cardType=cardtype )
cardservice = cardrequest.waitforcard()

cardservice.connection.connect( CardConnection.T0_protocol )

#print (' ATR             : ',toHexString( cardservice.connection.getATR() ))
#print ('Nama Card Reader : ',cardservice.connection.getReader())



#--------------------------------------------------DF TELECOM---------------------------------------------------------------------
SELECT_DF_TELECOM = SELECT + DF_TELECOM

#print ('sending DF_TELECOM : ' + toHexString(SELECT_DF_TELECOM))

response, sw1, sw2 = cardservice.connection.transmit( SELECT_DF_TELECOM )
#print ('response DF_TELECOM: ', response, ' status words: ', "%x %x" % (sw1, sw2))


if sw1 == 0x9F:
    DF_TELECOM = GET + [sw2]
    #print ('sending ' + toHexString(DF_TELECOM))
    response, sw1, sw2 = cardservice.connection.transmit( DF_TELECOM )
    #print ('response: ', toHexString(response), ' status words: ', "%x %x" % (sw1, sw2))


#--------------------------------------------------ADN-----------------------------------------------------------------------------
SELECT_ADN = SELECT + ADN

#print ('sending ADN :' + toHexString(SELECT_ADN))

response, sw1, sw2 = cardservice.connection.transmit(SELECT_ADN)
#print ('response: ', response, ' status words: ', "%x %x" % (sw1, sw2))

print ("")


if sw1 == 0x9F:
    ADN = GET + [sw2]
    #print ('sending ' + toHexString(ADN))
    R_ADN = response, sw1, sw2 = cardservice.connection.transmit( ADN )
    print ('ADN: ', toHexString(response), ' status words: ', "%x %x" % (sw1, sw2))
    print ('ADN', int(R_ADN[0][3]/R_ADN[0][14]),R_ADN[0][14])
print ("")


#--------------------------------------------------FDN-----------------------------------------------------------------------------
SELECT_FDN = SELECT + FDN

#print ('sending FDN :' + toHexString(SELECT_FDN))

response, sw1, sw2 = cardservice.connection.transmit(SELECT_FDN)
#print ('response: ', response, ' status words: ', "%x %x" % (sw1, sw2))

print ("")

if sw1 == 0x9F:
    FDN = GET + [sw2]
    #print ('sending ' + toHexString(FDN))
    R_FDN = response, sw1, sw2 = cardservice.connection.transmit( FDN )
    print ('FDN: ', toHexString(response), ' status words: ', "%x %x" % (sw1, sw2))
    print ('FDN', int(R_FDN[0][3]/R_FDN[0][14]),R_FDN[0][14])
    print ('xxx', R_FDN)
    print (response)

print("")


#--------------------------------------------------SMS-----------------------------------------------------------------------------
SELECT_SMS = SELECT + SMS

#print ('sending SMS :' + toHexString(SELECT_SMS))

response, sw1, sw2 = cardservice.connection.transmit(SELECT_SMS)
#print ('response: ', response, ' status words: ', "%x %x" % (sw1, sw2))

print ("")

if sw1 == 0x9F:
    SMS = GET + [sw2]
    print ('sending  SMS ' + toHexString(SMS))
    R_SMS = response, sw1, sw2 = cardservice.connection.transmit( SMS )
    #print ('SMS: ', toHexString(response), ' status words: ', "%x %x" % (sw1, sw2))
    print ('SMS_R: ', response, ' status words: ', "%x %x" % (sw1, sw2))
    print ('R_SMS_to_String: ', toHexString(response))
    print ('R_SMS_to_String_+:',(toHexString(response)[0]),(toHexString(response)[1]), (toHexString(response)[3]), (toHexString(response)[4]), (toHexString(response)[6]), (toHexString(response)[7]), (toHexString(response)[9]), (toHexString(response)[10]) )
    #print ('R_SMS[0][14]: ', R_SMS[0][14])
    #print ('yyy: ', toHexString(R_SMS[0][14]))
    #print ('SMS', int(R_SMS[0][3]/R_SMS[0][14]),R_SMS[0][14])

'''
#---------------------------------------------------Response------------------------------------------------------------------
#GET Response

30XA0 | 0XC0 | 00  | 00 | 17



ADN 5 x 28

00  |   00  |   00  |   8C  |   6F  |   3A  |   04  |   00  |   11  |   F0  |   22  |   01  |   02  |   01  |   1C  | 
 0       0      0      140     111      58       4       0      17     240      34       1       2       1      28                           
                     total 
                   file size



GET Response
0XA0 | 0XC0 | 00  | 00 | 0F


FDN 8 x 24

00  |   00  |   00  |   C0  |   6F  |   3B  |   04  |   00  |   12  |   F0  |   55  |   01  |   02  |   01  |   18  | 
 0       0      0      192     111      59       4       0      18      240    85       1       2       1       24
                       total 
                   file size


00  |   00  |   06  |   E0  |   6F  |   3C  |   04  |   00  |   11  |   F0 |    55  |   01  |   02  |   01  |   B0  | 

 '''
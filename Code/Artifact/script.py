from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnection import CardConnection
from smartcard.util import toHexString, toBytes
#from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
#from smartcard.Exceptions import CardRequestTimeoutException

#-------------------------------------------------------Config-------------------------------------------------------------------
#Apdu Command
SELECT     = [0xA0, 0xA4, 0x00, 0x00, 0x02]
READ       = [0xA0, 0xB0, 0x00, 0x00, 0x00]
GET        = [0XA0, 0XC0, 0x00, 0x00]

#MF
MF         = [0x3F, 0000]
DF_TELECOM = [0x7F, 0x10]
DF_GSM     = [0x7F, 0x20]
ADF_USIM   = [0x7F, 0xFF]
Level1PINs = [0x00, 0x00]
Level2PINs = [0x01, 0x00]
Level5PINs = [0x09, 0x00]
Level6PINs = [0x0A, 0x00]
DIR        = [0x2F, 0x00]
ICCID      = [0x2F, 0xE2]
PL         = [0x2F, 0x05]
ARR1       = [0x2F, 0x06]


#DF_Telecom
DF_PhoneBook = [0x5F, 0x3A]
DF_IMGDIR    = [0x5F, 0x50]
ARR2         = [0x6F, 0x05]
ADN          = [0x6F, 0x3A]
FDN          = [0x6F, 0x3B]
SMS          = [0x6F, 0x3C]
CCP          = [0x6F, 0x3D]
MSISDN       = [0x6F, 0x40]
SMSP         = [0x6F, 0x42]
SMSS         = [0x6F, 0x43]
LND          = [0x6F, 0x44]
SMSR         = [0x6F, 0x47]
SDN          = [0x6F, 0x49]
EXT1         = [0x6F, 0x4A]
EXT2         = [0x6F, 0x4B]
EXT3         = [0x6F, 0x4C]
BDN          = [0x6F, 0x4D]
EXT4_1       = [0x6F, 0x4E]

#DF_PhoneBook
PBR  = [0x4F, 0x30]
PSC  = [0x4F, 0x22]
CCP  = [0x4F, 0x23]
PUID = [0x4F, 0x24]

#DF_GSM
KeyMan          = [0x00, 0x11]
Ki              = [0x00, 0x50]
OPcKey          = [0x00, 0x51]
AUTHCNT         = [0x6F, 0x04]
LP              = [0x6F, 0x05]
IMSI            = [0x6F, 0x07]
Kc1             = [0x6F, 0x20]
PLMNsel         = [0x6F, 0x30]
HPLMN           = [0x6F, 0x31]
ACMmax          = [0x6F, 0x37]
SST             = [0x6F, 0x38]
ACM             = [0x6F, 0x39]
GID1            = [0x6F, 0x3E]
GID2            = [0x6F, 0x3F]
PUCT            = [0x6F, 0x41] 
CBMI            = [0x6F, 0x45] 
SPN             = [0x6F, 0x46] 
CBMID           = [0x6F, 0x48] 
BCCH            = [0x6F, 0x74] 
ACC             = [0x6F, 0x78] 
FPLMN           = [0x6F, 0x7B] 
LOCI            = [0x6F, 0x7E] 
AD              = [0x6F, 0xAD]        
PHASE           = [0x6F, 0xAE] 
VGCS            = [0x6F, 0xB1] 
VGCSS           = [0x6F, 0xB2] 
VBS             = [0x6F, 0xB3] 
VBSS            = [0x6F, 0xB4] 
eMLPP           = [0x6F, 0xB5] 
AAeM            = [0x6F, 0xB6] 
ECC             = [0x6F, 0xB7] 
CBMIR           = [0x6F, 0x50] 
NIA1            = [0x6F, 0x51] 
KcGPRS1         = [0x6F, 0x52] 
LOCIGPRS        = [0x6F, 0x53] 
SUME            = [0x6F, 0x54] 
PLMNwACT        = [0x6F, 0x60] 
OPLMNwACT       = [0x6F, 0x61] 
HPLMNACT        = [0x6F, 0x62] 
CPBCCH1         = [0x6F, 0x63] 
INVSCAN1        = [0x6F, 0x64] 
RFMRPH          = [0x6F, 0xF8] 
RFMPRO_SMS_NOK  = [0x6F, 0xF9] 
EF_RFMPRO_SMS   = [0x6F, 0xFA] 
RFMPRO_NOK      = [0x6F, 0xFB] 
RFMPRO          = [0x6F, 0xFC] 
RFMCNTR         = [0x6F, 0xFD] 
RFMData         = [0x6F, 0xFE] 
CSMS            = [0x6F, 0xFF] 
OTACLRAC        = [0xAC, 0x00] 
OTARFMAC        = [0xAC, 0x01] 


#DF_WIB
File_ID         = [0x27, 0x00]
TAR             = [0x6F, 0x01]  
ERRTEXT         = [0x6F, 0x02]   
BYTECODE        = [0x6F, 0x03]  
SMSHDR          = [0x6F, 0x04]  
#0348HDR         = [0x6F, 0x05] 
CNTR            = [0x6F, 0x06]  
VERINFO         = [0x6F, 0x07]   
WIBCFG          = [0x6F, 0x08]   
EVENTCFG        = [0x6F, 0x0B]   
CLNTBND1        = [0x6F, 0x0C]   
WIBVAR1         = [0x6F, 0x0D]   
TEXT1           = [0x6F, 0x0E]   
CSMSALPHA       = [0x6F, 0x50] 
SRVBND          = [0x6F, 0x51] 
CLNTBND2        = [0x6F, 0x52]  
WIBVAR2         = [0x6F, 0x53]   
TEXT2           = [0x6F, 0x54]  
EVENTQ          = [0x6F, 0x55]   
SCRIPTPREFIX    = [0x6F, 0x57]   
SECURITY        = [0x6F, 0x58] 


#[ADF_USIM]
File_ID       = [0x7F, 0xFF]
#Name         = $A0000000871002
DF_PhoneBook  = [0x5F, 0x3A]  
DF_GSMAccess  = [0x5F, 0x3B]  
DF_MExE       = [0x5F, 0x3C]  
DF_WLAN       = [0x5F, 0x40]  
DF_SoLSA      = [0x5F, 0x70]  
K             = [0x00, 0x50]    
MilenageConst = [0x00, 0x52]  
SQNMax        = [0x00, 0x56]  
SEQtable      = [0x00, 0x57]  
D             = [0x00, 0x58]  
L             = [0x00, 0x59]    
LI            = [0x6F, 0x05]  
ARR3          = [0x6F, 0x06]    
Keys          = [0x6F, 0x08]  
KeysPS        = [0x6F, 0x09]  
DCK           = [0x6F, 0x2C]  
HPPLMN        = [0x6F, 0x31]  
CNL           = [0x6F, 0x32]    
UST           = [0x6F, 0x38]                          
Ext5          = [0x6F, 0x4E]  
CCP2          = [0x6F, 0x4F]   
Ext4_2        = [0x6F, 0x55]  
EST           = [0x6F, 0x56]  
ACL           = [0x6F, 0x57]  
CMI           = [0x6F, 0x58]  
#START-HFN     = [0x6F, 0x5B]  
TRESHOLD      = [0x6F, 0x5C]    
HPLMNwAcT     = [0x6F, 0x62]  
PSLOCI        = [0x6F, 0x73]        
ICI           = [0x6F, 0x80]  
OCI           = [0x6F, 0x81]  
ICT           = [0x6F, 0x82]  
OCT           = [0x6F, 0x83]             
HiddenKey     = [0x6F, 0xC3]   
NETPAR        = [0x6F, 0xC4]  
PNN           = [0x6F, 0xC5]  
OPL           = [0x6F, 0xC6]  
MBDN          = [0x6F, 0xC7]   
Ext6          = [0x6F, 0xC8]  
MBI           = [0x6F, 0xC9]  
MWIS          = [0x6F, 0xCA]   
CFIS          = [0x6F, 0xCB]  
Ext7          = [0x6F, 0xCC]  
SPDI          = [0x6F, 0xCD]   
MMSN          = [0x6F, 0xCE]  
Ext8          = [0x6F, 0xCF]  
MMSICP        = [0x6F, 0xD0]  
MMSUP         = [0x6F, 0xD1]  
MMSUCP        = [0x6F, 0xD2]  
NIA2          = [0x6F, 0xD3]  
VGCSCA        = [0x6F, 0xD4]  
VBSCA         = [0x6F, 0xD5]  
GBABP         = [0x6F, 0xD6]  
MSK           = [0x6F, 0xD7]  
MUK           = [0x6F, 0xD8]  
EHPLMN        = [0x6F, 0xD9]  


#[DF_GSMAccess]
File_ID  = [0x5F, 0x3B]  
Kc2      = [0x4F, 0x20] 
KcGPRS2   = [0x4F, 0x52] 
CPBCCH2  = [0x4F, 0x63] 
invSCAN2 =[0x4F, 0x64] 


#-------------------------------------------------------Connection-------------------------------------------------------------------
cardtype = AnyCardType()
cardrequest = CardRequest( timeout=10, cardType=cardtype )
cardservice = cardrequest.waitforcard()

cardservice.connection.connect( CardConnection.T0_protocol )

#-------------------------------------Function Parsing response hexa to decimal-----------------------------------------------------


def search (input) :
    a= ((toHexString(input)[0]),(toHexString(input)[1]), (toHexString(input)[3]), (toHexString(input)[4]), (toHexString(
        input)[6]), (toHexString(input)[7]), (toHexString(input)[9]), (toHexString(input)[10]), (input)[14] )

    if ((a[0] != '0' or a[1] != '0') and (a[2] != '0' or a[3] != '0') and (a[4] != '0' or a[5] != '0') and (a[6] != '0' or a[7] != '0')):
        if input[14] != 0 :
            sum = ((a[0])+(a[1])),((a[2])+(a[3])),((a[4])+(a[5])),((a[6])+(a[7]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b/input[14]),input[14]

        else:
            sum = ((a[0])+(a[1])),((a[2])+(a[3])),((a[4])+(a[5])),((a[6])+(a[7]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b)

    elif ((a[0] != '0' or a[1] != '0') and (a[2] != '0' or a[3] != '0') and (a[4] != '0' or a[5] != '0')):
        if input[14] != 0 :
            sum = ((a[0])+(a[1])),((a[2])+(a[3])),((a[4])+(a[5]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b/input[14]),input[14]

        else:
            sum = ((a[0])+(a[1])),((a[2])+(a[3])),((a[4])+(a[5]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b)

    elif ((a[0] != '0' or a[1] != '0') and (a[2] != '0' or a[3] != '0') and (a[6] != '0' or a[7] != '0')):
        if input[14] != 0 :
            sum = ((a[0])+(a[1])),((a[2])+(a[3])),'00',((a[6])+(a[7]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b/input[14]),input[14]

        else:
            sum = ((a[0])+(a[1])),((a[2])+(a[3])),'00',((a[6])+(a[7]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b/input[14]),input[14]

    elif ((a[2] != '0' or a[3] != '0') and (a[4] != '0' or a[5] != '0') and (a[6] != '0' or a[7] != '0')):
        if input[14] != 0 :
            sum = ((a[2])+(a[3])),((a[4])+(a[5])),((a[6])+(a[7]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b/input[14]),input[14]

        else:
            sum = ((a[2])+(a[3])),((a[4])+(a[5])),((a[6])+(a[7]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b)

    elif ((a[0] != '0' or a[1] != '0' ) and (a[2] != '0' or a[3] != '0' )):
        if input[14] != 0 :
            sum = ((a[0])+(a[1])),((a[2])+(a[3]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b/input[14]),input[14]
        else:
            sum = ((a[0])+(a[1])),((a[2])+(a[3]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b)

    elif ((a[0] != '0' or a[1] != '0' ) and (a[4] != '0' or a[5] != '0' )):
        if input[14] != 0 :
            sum = ((a[0])+(a[1])),'00',((a[4])+(a[5]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b/input[14]),input[14]

        else:
            sum = ((a[0])+(a[1])),'00',((a[4])+(a[5]))
            #print ('if :',sum)
            join =  str(''. join(sum))
            b =  int(join,16)
            return int(b)

    elif ((a[0] != '0' or a[1] != '0' ) and (a[6] != '0' or a[7] != '0' )):
        if input[14] != 0 :
            sum = ((a[0])+(a[1])),'00','00'((a[6])+(a[7]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b/input[14]),input[14]

        else:
            sum = ((a[0])+(a[1])),'00','00'((a[6])+(a[7]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b)

    elif ((a[2] != '0' or a[3] != '0' ) and (a[4] != '0' or a[5] != '0' )):
        if input[14] != 0 :
            sum = ((a[2])+(a[3])),((a[4])+(a[5]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b/input[14]),input[14]

        else:
            sum = ((a[2])+(a[3])),((a[4])+(a[5]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b)

    elif ((a[2] != '0' or a[3] != '0' ) and (a[6] != '0' or a[7] != '0' )):
        if input[14] != 0 :
            sum = ((a[2])+(a[3])),'00',((a[6])+(a[7]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b/input[14]),input[14]

        else:
            sum = ((a[2])+(a[3])),'00',((a[6])+(a[7]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b)

    elif ((a[4] != '0' or a[5] != '0' ) and (a[6] != '0' or a[7] != '0' )):
        if input[14] != 0 :
            sum = ((a[4])+(a[5])),((a[6])+(a[7]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b/input[14]),input[14]

        else:
            sum = ((a[4])+(a[5])),((a[6])+(a[7]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b)

    elif (a[0] != '0' or a[1] != '0'):
        if input[14] != 0 :
            sum = ((a[0])+(a[1]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b/input[14]),input[14]

        else:
            sum = ((a[0])+(a[1]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b)


    elif (a[2] != '0' or a[3] != '0'):
        if input[14] != 0 :
            sum = ((a[2])+(a[3])),
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b/input[14]),input[14]

        else:
            sum = ((a[2])+(a[3])),
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b)

    elif (a[4] != '0' or a[5] != '0'):

        if input[14] != 0 :
            sum = ((a[4])+(a[5]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b/input[14]),input[14]

        else:
            sum = ((a[4])+(a[5]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b)

    elif (a[6] != '0' or a[7] != '0'):

        if input[14] != 0 :
            sum = ((a[6])+(a[7]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b/input[14]),input[14]

        else :
            sum = ((a[6])+(a[7]))
            #print ('if :',sum)
            join =  str(''.join(sum))
            b =  int(join,16)
            return int(b)

    else: 
        print ("huba")

#-------------------------------------Function Open Logical Channel-----------------------------------------------------------------

def open(input):
    SELECT_INPUT = SELECT + input
    response, sw1, sw2 = cardservice.connection.transmit( SELECT_INPUT )

    if sw1 == 0x9F:
        input = GET + [sw2]
        response, sw1, sw2 = cardservice.connection.transmit( input )

#-------------------------------------Function Open Logical Channel-----------------------------------------------------------------

def find (input1,input2):
    SELECT_FIND = SELECT + input1
    #print (SELECT_FIND)
    x = response, sw1, sw2 = cardservice.connection.transmit(SELECT_FIND)
    #print(x)

    if sw1 == 0x9F:
        SUM = GET + [sw2]
        R_FIND = response, sw1, sw2 = cardservice.connection.transmit( SUM )
        R1_FIND = response
        #print (R1_FIND)
        if R1_FIND[14] != 0 :
           print (input2,search(R1_FIND)[0],search(R1_FIND)[1])

        else :
            print (input2,search(R1_FIND))

#-----------------------------------------------Call Function----------------------------------------------------------------------

#MF Layer 1
print ("---MF---")

Result_Level1PINs = find(Level1PINs,'Level1PINs')
Result_Level2PINs = find(Level2PINs,'Level2PINs')
Result_Level2PINs = find(Level5PINs,'Level5PINs')
Result_Level6PINs = find(Level6PINs,'Level6PINs')
Result_DIR = find(DIR,'DIR')
Result_ICCID = find(ICCID,'ICCID')
Result_PL = find(PL,'PL')
Result_ARR1 = find(ARR1,'ARR')



#DF Layer 2
print("")
print ("---DF Telecom---")
open(DF_TELECOM)

Result_ARR2 = find(ARR2,'ARR')
Result_ADN = find(ADN,'ADN')
Result_FDN = find(FDN,'FDN')
Result_SMS = find(SMS,'SMS')
Result_CCP = find(CCP,'CCP')
Result_MSISDN = find(MSISDN,'MSISDN')
Result_SMSP = find(SMSP,'SMSP')
Result_SMSS = find(SMSS,'SMSS')
Result_LND = find(LND,'LND')
Result_SMSR = find(SMSR,'SMSR')
Result_SDN = find(SDN,'SDN')
Result_EXT1 = find(EXT1,'EXT1')
Result_EXT2 = find(EXT2,'EXT2')
Result_EXT3 = find(EXT3,'EXT3')
Result_BDN = find(BDN,'BDN')
Result_EXT4_1 = find(EXT4_1,'EXT4')
Result_SUME = find(SUME,'SUME')

print("")
print ("---DF GSM---")


open(DF_GSM)

Result_KeyMan = find(KeyMan,'KeyMan')
Result_Ki = find(Ki,'Ki')
Result_OPcKey = find(OPcKey,'OPcKey')
Result_AUTHCNT = find(AUTHCNT,'AUTHCNT')
Result_LP = find(LP,'LP')
Result_IMSI = find(IMSI,'IMSI')
Result_Kc1 = find(Kc1,'Kc')
Result_PLMNsel = find(PLMNsel,'PLMNsel')
Result_HPLMN = find(HPLMN,'HPLMN')
Result_ACMmax = find(ACMmax,'ACMmax')
Result_SST = find(SST,'SST')
Result_ACM = find(ACM,'ACM')
Result_GID1 = find(GID1,'GID1')
Result_GID2 = find(GID2,'GID2')
Result_PUCT = find(PUCT,'PUCT')
Result_CBMI = find(CBMI,'CBMI')
Result_SPN = find(SPN,'SPN')
Result_CBMID = find(CBMID,'CBMID')
Result_BCCH = find(BCCH,'BCCH')
Result_ACC = find(ACC,'ACC')
Result_FPLMN = find(FPLMN,'FPLMN')
Result_LOCI = find(LOCI,'LOCI')
Result_AD = find(AD,'AD')
Result_PHASE = find(PHASE,'PHASE')
Result_VGCS = find(VGCS,'VGCS')
Result_VGCSS = find(VGCSS,'VGCSS')
Result_VBS = find(VBS,'VBS')
Result_VBSS = find(VBSS,'VBSS')
Result_eMLPP = find(eMLPP,'eMLPP')
Result_AAeM = find(AAeM,'AAeM')
Result_ECC = find(ECC,'ECC')
Result_CBMIR = find(CBMIR,'CBMIR')
Result_NIA1 = find(NIA1,'NIA')
Result_KcGPRS1 = find(KcGPRS1,'KcGPRS')
Result_LOCIGPRS = find(LOCIGPRS,'LOCIGPRS')
Result_PLMNwACT = find(PLMNwACT,'PLMNwACT')
Result_OPLMNwACT = find(OPLMNwACT,'OPLMNwACT')
Result_HPLMNACT = find(HPLMNACT,'HPLMNACT')
Result_CPBCCH1 = find(CPBCCH1,'CPBCCH')
Result_INVSCAN1 = find(INVSCAN1,'INVSCAN')
Result_RFMRPH = find(RFMRPH,'RFMRPH')
Result_RFMPRO_SMS_NOK = find(RFMPRO_SMS_NOK,'RFMPRO_SMS_NOK')
Result_EF_RFMPRO_SMS = find(EF_RFMPRO_SMS,'EF_RFMPRO_SMS')
Result_RFMPRO_NOK = find(RFMPRO_NOK,'RFMPRO_NOK')
Result_RFMPRO = find(RFMPRO,'RFMPRO')
Result_RFMCNTR = find(RFMCNTR,'RFMCNTR')
Result_RFMData = find(RFMData,'RFMData')
Result_CSMS = find(CSMS,'CSMS')
Result_OTACLRAC = find(OTACLRAC,'OTACLRAC')
Result_OTARFMAC = find(OTARFMAC,'OTARFMAC')



print("")
print ("---ADF USIM---")

open(ADF_USIM)

print ("---Missing Part----")
#find(OPcKey,'OPcKey')
find(SQNMax,'SQNMax')
find(SEQtable,'SEQtable')
find(D,'D')
find(L,'L')
find(MilenageConst,'MilenageConst')
find(Keys,'Keys')
find(KeysPS,'KeysPS')
find(DCK,'DCK')
#find(Level2PINs,'Level2PINs')

 
Result_K =  find(K,'K')
Result_LI = find(LI,'LI')
Result_ARR3 = find(ARR3,'ARR')
Result_HPPLMN = find(HPPLMN,'HPPLMN')
find(CNL,'CNL')
Result_UST =  find(UST,'UST')
find(Ext5,'Ext5')
find(CCP2,'CCP2')
find(Ext4_2,'Ext4')
find(EST,'EST')
find(ACL,'ACL')
find(CMI,'CMI')
find(TRESHOLD,'TRESHOLD')
Result_HPLMNwAcT = find(HPLMNwAcT,'HPLMNwAcT')
find(PSLOCI,'PSLOCI')
find(ICI,'ICI')
find(OCI,'OCI')
find(ICT,'ICT')
find(OCT,'OCT')
find(HiddenKey,'HiddenKey')
find(NETPAR,'NETPAR')
Result_PNN =  find(PNN,'PNN')
Result_OPL =  find(OPL,'OPL')
find(MBDN,'MBDN')
find(Ext6,'Ext6')
find(MBI,'MBI')
find(MWIS,'MWIS')
find(CFIS,'CFIS')
find(Ext7,'Ext7')
Result_SPDI =  find(SPDI,'SPDI')
find(MMSN,'MMSN')
find(Ext8,'Ext8')
find(MMSICP,'MMSICP')
find(MMSUP,'MMSUP')
find(MMSUCP,'MMSUCP')
find(NIA2,'NIA')
find(VGCSCA,'VGCSCA')
find(VBSCA,'VBSCA')
find(GBABP,'GBABP')
find(MSK,'MSK')
find(MUK,'MUK')
find(EHPLMN,'EHPLMN')

'''
open(DF_PhoneBook)
find(PBR,'PBR')
find(PSC,'PSC')
find(CCP,'CCP')
find(PUID,'PUID')







find(File_ID,'File_ID')
find(TAR,'TAR')
find(ERRTEXT,'ERRTEXT')
find(BYTECODE,'BYTECODE')
find(SMSHDR,'SMSHDR')
find(CNTR,'CNTR')
find(VERINFO,'VERINFO')
find(WIBCFG,'WIBCFG')
find(EVENTCFG,'EVENTCFG')
find(CLNTBND1,'CLNTBND')
find(WIBVAR1,'WIBVAR')
find(TEXT1,'TEXT')
find(CSMSALPHA,'CSMSALPHA')
find(SRVBND,'SRVBND')
find(CLNTBND2,'CLNTBND')
find(WIBVAR2,'WIBVAR')
find(TEXT2,'TEXT')
find(EVENTQ,'EVENTQ')
find(SCRIPTPREFIX,'SCRIPTPREFIX')
find(SECURITY,'SECURITY')
find(File_ID,'File_ID')
find(DF_PhoneBook,'DF_PhoneBook')
find(DF_GSMAccess,'DF_GSMAccess')
find(DF_MExE,'DF_MExE')
find(DF_WLAN,'DF_WLAN')
find(DF_SoLSA,'DF_SoLSA')




find(File_ID,'File_ID')
find(Kc2,'Kc')
find(KcGPRS2,'KcGPRS')
find(CPBCCH2,'CPBCCH')
find(invSCAN2,'invSCAN')
'''



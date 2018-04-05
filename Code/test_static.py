from XL.ReadAndGetStatic import *
from XL.configuration import *



#Print All Paramaters on Simcard

#MF Layer 1
with open("Output.txt", "a") as text_file:
    print ("GROUP_MF", file=text_file)

find(Level1PINs,'Level1PINs'),read_chv(Level1PINs)
find(Level2PINs,'Level2PINs'),read_chv(Level2PINs)
find(Level5PINs,'Level5PINs'),read_chv(Level5PINs)
find(Level6PINs,'Level6PINs'),read_chv(Level6PINs)
find(DIR,'DIR'), read_chv(DIR)

find(ICCID,'ICCID'), read_chv(ICCID)
Result_read_iccid = read_iccid()

find(PL,'PL'),read_chv(PL)
find(ARR1,'ARR'),read_chv(ARR1)



#DF_GSM
with open("Output.txt", "a") as text_file:
    print ("GROUP_DFGSM", file=text_file)
open1(DF_GSM)

find(KeyMan,'KeyMan'),read_chv(KeyMan)
find(Ki,'Ki'),read_chv(Ki)
find(OPcKey,'OPcKey'),read_chv(OPcKey)
find(AUTHCNT,'AUTHCNT'),read_chv(AUTHCNT)
find(LP,'LP'),read_chv(LP)

find(IMSI,'IMSI'),read_chv(IMSI)
Result_read_imsi = read_imsi()


find(Kc1,'Kc'),read_chv(Kc1)
find(PLMNsel,'PLMNsel'),read_chv(PLMNsel)
find(HPLMN,'HPLMN'),read_chv(HPLMN)
find(ACMmax,'ACMmax'),read_chv(ACMmax)
find(SST,'SST'),read_chv(SST)
find(ACM,'ACM'),read_chv(ACM)
find(GID1,'GID1'),read_chv(GID1)
find(GID2,'GID2'),read_chv(GID2)
find(PUCT,'PUCT'),read_chv(PUCT)
find(CBMI,'CBMI'),read_chv(CBMI)
find(SPN,'SPN'),read_chv(SPN)
find(CBMID,'CBMID'),read_chv(CBMID)
find(BCCH,'BCCH'),read_chv(BCCH)
find(ACC,'ACC'),read_chv(ACC)
find(FPLMN,'FPLMN'),read_chv(FPLMN)
find(LOCI,'LOCI'),read_chv(LOCI)
find(AD,'AD'),read_chv(AD)
find(PHASE,'PHASE'),read_chv(PHASE)
find(VGCS,'VGCS'),read_chv(VGCS)
find(VGCSS,'VGCSS'),read_chv(VGCSS)
find(VBS,'VBS'),read_chv(VBS)
find(VBSS,'VBSS'),read_chv(VBSS)
find(eMLPP,'eMLPP'),read_chv(eMLPP)
find(AAeM,'AAeM'),read_chv(AAeM)
find(ECC,'ECC'),read_chv(ECC)
find(CBMIR,'CBMIR'),read_chv(CBMIR)
find(NIA1,'NIA'),read_chv(NIA1)
find(KcGPRS1,'KcGPRS'),read_chv(KcGPRS1)
find(LOCIGPRS,'LOCIGPRS'),read_chv(LOCIGPRS)
find(PLMNwACT,'PLMNwACT'),read_chv(PLMNwACT)
find(OPLMNwACT,'OPLMNwACT'),read_chv(OPLMNwACT)
find(HPLMNACT,'HPLMNACT'),read_chv(HPLMNACT)
find(CPBCCH1,'CPBCCH'),read_chv(CPBCCH1)
find(INVSCAN1,'INVSCAN'),read_chv(INVSCAN1)
find(RFMRPH,'RFMRPH'),read_chv(RFMRPH)
find(RFMPRO_SMS_NOK,'RFMPRO_SMS_NOK'),read_chv(RFMPRO_SMS_NOK)
find(EF_RFMPRO_SMS,'EF_RFMPRO_SMS'),read_chv(EF_RFMPRO_SMS)
find(RFMPRO_NOK,'RFMPRO_NOK'),read_chv(RFMPRO_NOK)
find(RFMPRO,'RFMPRO')
find(RFMCNTR,'RFMCNTR'),read_chv(RFMPRO)
find(RFMData,'RFMData'),read_chv(RFMData)
find(CSMS,'CSMS'),read_chv(CSMS)
find(OTACLRAC,'OTACLRAC'),read_chv(OTACLRAC)
find(OTARFMAC,'OTARFMAC'),read_chv(OTARFMAC)




#DF_Telecom
with open("Output.txt", "a") as text_file:
    print ("GROUP_DF Telecom", file=text_file)

open1(DF_TELECOM)

find(MSISDN,'MSISDN'),read_chv(MSISDN)
Result_read_msisdn = read_msisdn(MSISDN,'MSISDN')


find(ARR2,'ARR'),read_chv(ARR2)


find(ADN,'ADN'),read_chv(ADN)
find_detail(ADN,'RECORD_ADN')

find(FDN,'FDN'),read_chv(FDN)
find_detail(FDN,'RECORD_FDN')

find(SMS,'SMS'),read_chv(SMS)
find(CCP,'CCP'),read_chv(CCP)
#find(MSISDN,'MSISDN'),read_chv(MSISDN)


find(SMSP,'SMSP'),read_chv(SMSP)
find_detail_smsp(SMSP,'SMSP')


find(SMSS,'SMSS'),read_chv(SMSS)
find(LND,'LND'),read_chv(LND)
find(SMSR,'SMSR'),read_chv(SMSR)
find(SDN,'SDN'),read_chv(SDN)
find(EXT1,'EXT1'),read_chv(EXT1)
find(EXT2,'EXT2'),read_chv(EXT2)
find(EXT3,'EXT3'),read_chv(EXT3)
find(BDN,'BDN'),read_chv(BDN)
find(EXT4_1,'EXT4'),read_chv(EXT4_1)
find(SUME,'SUME'),read_chv(SUME)


#DF_PhoneBook
with open("Output.txt", "a") as text_file:
    print ('GROUP_DF_PhoneBook', file=text_file)
open1(DF_PhoneBook)
find(PBR,'PBR'),read_chv(PBR)
find(PSC,'PSC'),read_chv(PSC)
find(CCP2,'CC'),read_chv(CCP2)
find(PUID,'PUID'),read_chv(PUID)

with open("Output.txt", "a") as text_file:
    print ('GROUP_Other', file=text_file)

with open("Output.txt", "a") as text_file:
	print ('REF_MSISDN ',end='',file=text_file)
	for x in Result_read_msisdn:
		print (x, end=';',file=text_file)

with open("Output.txt", "a") as text_file:
    print ('', file=text_file)

with open("Output.txt", "a") as text_file:
    print ('REF_IMSI', Result_read_imsi, file=text_file)

with open("Output.txt", "a") as text_file:
    print ('REF_ICCID', Result_read_iccid, file=text_file)


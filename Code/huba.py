from XL.CardConnection import *
from XL.HexaToDecimal import search
from smartcard.util import toHexString, toBytes
from luhn import *


def read_msisdn (input1,input2) :

    #apdu command select + apa yang mau di select
    SELECT_FIND = SELECT + input1
    
    #get reponse,  sw1, s2
    #(     [],    159,  15)
    x = response, sw1, sw2 = cardservice.connection.transmit(SELECT_FIND)

    
    #if respon 0x9f it means success
    if sw1 == 0x9F:

        #Apdu Get Response, sw2 is length of data you can retrieve
        SUM = GET + [sw2]

        #send command to simcard, to retrive data
        R_FIND = response, sw1, sw2 = cardservice.connection.transmit( SUM )

        #response  list [0, 0, 0, 72, 111, 64, 4, 0, 17, 240, 85, 1, 2, 1, 24]
        R1_FIND    = response

        #reponse list[3]  = total size
        total_size = R1_FIND[3]

        #reponse list[14] = lenght
        lenght     = R1_FIND[14]

        #record           = total size / lenght
        record     = int (total_size / lenght)

        #print ('record :',record)


        if R1_FIND[14] != 0 :
           #print (input2,search(R1_FIND)[0],search(R1_FIND)[1])
           validate_element_store = []
           for x in range(0,record):

              #READ_MSISDN_1      = [0xA0, 0xB2, 0x01, 0x04, 0x18]
              #READ_MSISDN_2      = [0xA0, 0xB2, 0x02, 0x04, 0x18]
              #READ_MSISDN_3      = [0xA0, 0xB2, 0x03, 0x04, 0x18]

              #outputnya tupple: ([255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], 144, 0)
              x = response1, sw1, sw2 = cardservice.connection.transmit([0xA0, 0xB2, 0x01+x, 0x04, 0x18])

              #check value in reponse1 if all element == 255 then blank
              validate_element = all(item == 255 for item in response1)

              #store result validate element TRUE or False
              validate_element_store.append(validate_element)

              #if all element in validate_element_Store == True (means all element is 255), it will return blank
              if all(value == True for value in validate_element_store) :
                  return (' ') 

              #next enhancement, it should return the decimal response
              else :
                  with open("Output.txt", "a") as text_file:
                    print (x, file=text_file)
        else :
            with open("Output.txt", "a") as text_file:
              print (input2,search(R1_FIND), file=text_file)

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
          #R1_FIND[0] = Record | R1_FIND[1] = Lenght
           with open("Output.txt", "a") as text_file:
              print (input2,search(R1_FIND)[0],search(R1_FIND)[1], end="", file=text_file)

        else :
            with open("Output.txt", "a") as text_file:
              print (input2,search(R1_FIND), end="", file=text_file)


find(MSISDN,'MSISDN')
Result_read_msisdn = read_msisdn(MSISDN,'MSISDN')



print ('REF_MSISDN',Result_read_msisdn)

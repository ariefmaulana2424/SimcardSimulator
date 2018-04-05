from XL.CardConnection import *
from XL.HexaToDecimal import search
from smartcard.util import toHexString, toBytes
from luhn import *

#Apdu Command
SELECT             = [0xA0, 0xA4, 0x00, 0x00, 0x02]
READ               = [0xA0, 0xB0, 0x00, 0x00, 0x09]
GET                = [0XA0, 0XC0, 0x00, 0x00]


cardtype = AnyCardType()
cardrequest = CardRequest( timeout=10, cardType=cardtype )
cardservice = cardrequest.waitforcard()
cardservice.connection.connect( CardConnection.T0_protocol )


#Open Logical Channel ( EF , DF )
def open1(input):
    SELECT_INPUT = SELECT + input
    x = response, sw1, sw2 = cardservice.connection.transmit( SELECT_INPUT )
    #print(x)

    if sw1 == 0x9F:
        input = GET + [sw2]
        response, sw1, sw2 = cardservice.connection.transmit( input )



#Select File and Get Response, then send to Function search on HexaToDecimal.py
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


def read_iccid () :
      x = response, sw1, sw2 = cardservice.connection.transmit(READ)
      swap = response
      #print (swap)
      
      a= ((toHexString(swap)[9]),(toHexString(swap)[10]),(toHexString(swap)[12]),(toHexString(swap)[13]),(toHexString(swap)[15]),(toHexString(swap)[16]),(toHexString(swap)[18]),(toHexString(swap)[19]),(toHexString(swap)[21]),(toHexString(swap)[22]),(toHexString(swap)[24]),(toHexString(swap)[25]) )

      #print (a)
      sum = ((a[1])+(a[0])),((a[3])+(a[2])),((a[5])+(a[4])),((a[7])+(a[6])),((a[9])+(a[8])),((a[11])+(a[10]))
      join =  str(''.join(sum))
      luhn = (generate(join))
      ICCID_FINAL = '896211' + join + str(luhn)
      return (ICCID_FINAL)


def read_imsi () :
      x = response, sw1, sw2 = cardservice.connection.transmit(READ)
      swap = response
      #print (swap)
    
      a= ((toHexString(swap)[12]),(toHexString(swap)[13]),(toHexString(swap)[15]),(toHexString(swap)[16]),(toHexString(swap)[18]),(toHexString(swap)[19]),(toHexString(swap)[21]),(toHexString(swap)[22]),(toHexString(swap)[24]),(toHexString(swap)[25]) )

      #print (a)

      sum = ((a[1])+(a[0])),((a[3])+(a[2])),((a[5])+(a[4])),((a[7])+(a[6])),((a[9])+(a[8]))
      join =  str(''.join(sum))
      IMSI_FINAL = '51011' + join 
      return (IMSI_FINAL)      


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
                  return (response1)
        else :
            return (input2,search(R1_FIND))
      


def find_detail (input1,input2) :

    def intToChar(int_response):
        return chr(int_response)

    def intToHex(int_response):
        #0x81 0x18 0x0f jadi 81  18 0f
        hexa_without_0x  =  (hex(int_response))[2:]

        #swap poisition char 18 81 0f jadi 18 81 f0 
        reverse_position = ''.join(hexa_without_0x[::-1])

        replace_last_f = reverse_position.replace('f','')

        return replace_last_f

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
        lenght      = R1_FIND[14]   

        #record           = total size / lenght
        record      = int (total_size / lenght)

        #print ('record :',record)


        if R1_FIND[14] != 0 :
           #print (input2,search(R1_FIND)[0],search(R1_FIND)[1])
           
           first_digit = lenght - 15
           last_digit  = lenght - 15 + 2


           for x in range(0,record):

              #READ_ADN_1         = [0xA0, 0xB2, 0x01, 0x04, 0x1C]
              #READ_ADN_2         = [0xA0, 0xB2, 0x02, 0x04, 0x1C]
              #READ_ADN_3         = [0xA0, 0xB2, 0x03, 0x04, 0x1C]
              #READ_ADN_4         = [0xA0, 0xB2, 0x04, 0x04, 0x1C]
              #READ_ADN_5         = [0xA0, 0xB2, 0x05, 0x04, 0x1C]

              #outputnya x: ([67, 117, 115, 116, 46, 32, 83, 101, 114, 118, 105, 99, 101, 255, 3, 129, 24, 248, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], 144, 0)

              #outputnya response1: ([67, 117, 115, 116, 46, 32, 83, 101, 114, 118, 105, 99, 101, 255, 3, 129, 24, 248, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]

             
              

              x = response1, sw1, sw2 = cardservice.connection.transmit([0xA0, 0xB2, 0x01+x, 0x04, lenght])


              #print ('Response : ',response1)

              for index, val in enumerate(response1):

                  char_response = intToChar(val)
                  hexa_response = intToHex(val)

                  if index <= first_digit:

                      if index == 0  and val != 255:
                          with open("Output.txt", "a") as text_file:
                            print(input2, char_response, end ='', file=text_file)

                      elif index == 0 and val ==255:
                          with open("Output.txt", "a") as text_file:
                            print(input2, end ='', file=text_file)

                      else :
                          if val != 255:
                            with open("Output.txt", "a") as text_file:
                              print(char_response, end='', file=text_file)

                  elif index == 15 and response1[0] != 255:
                      with open("Output.txt", "a") as text_file:
                        print(';', end='', file=text_file)

                  elif index >= last_digit and val != 255:
                      with open("Output.txt", "a") as text_file:
                        print (hexa_response, end = '', file=text_file)



                  elif index >= last_digit and val == 255:
                      with open("Output.txt", "a") as text_file:
                        print ('', file=text_file)
                      break



        else :
            with open("Output.txt", "a") as text_file:
                print (input2,search(R1_FIND), file=text_file) 

                       
def find_detail_smsp (input1,input2) :

    def intToHex(int_response):
        #0x81 0x18 0x0f jadi 81  18 0f

        if int_response != 0:
          hexa_without_0x  =  (hex(int_response))[2:]

          #swap poisition char 18 81 0f jadi 18 81 f0 
          reverse_position = ''.join(hexa_without_0x[::-1])

          replace_last_f = reverse_position.replace('f','')

          return replace_last_f

        else :
          hexa_without_0x  =  (hex(int_response))[2:]

          #swap poisition char 18 81 0f jadi 18 81 f0 
          reverse_position = ''.join(hexa_without_0x[::-1])

          replace_last_f = reverse_position.replace('f','')

          return replace_last_f+'0'



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
        lenght      = R1_FIND[14]   

        #record           = total size / lenght
        record      = int (total_size / lenght)

        #print ('record :',record)


        if R1_FIND[14] != 0 :

           start_digit = lenght - 13
           last_digit  = 39 

           for x in range(0,record):

              #READ_SMSP_1         = [0xA0, 0xB2, 0x01, 0x04, 0x28]
              #READ_SMSP_2         = [0xA0, 0xB2, 0x02, 0x04, 0x28]
              #READ_SMSP_3         = [0xA0, 0xB2, 0x03, 0x04, 0x28]
              #READ_SMSP_4         = [0xA0, 0xB2, 0x04, 0x04, 0x28]

              #outputnya x: ([67, 117, 115, 116, 46, 32, 83, 101, 114, 118, 105, 99, 101, 255, 3, 129, 24, 248, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], 144, 0)

              #outputnya response1: ([67, 117, 115, 116, 46, 32, 83, 101, 114, 118, 105, 99, 101, 255, 3, 129, 24, 248, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]

             
              

              x = response1, sw1, sw2 = cardservice.connection.transmit([0xA0, 0xB2, 0x01+x, 0x04, lenght])


              #print ('Response : ',response1)

              for index, val in enumerate(response1):

                  hexa_response = intToHex(val)

                  if index >= start_digit:

                    if index == start_digit and val != 255:
                        with open("Output.txt", "a") as text_file:
                          print ('RECORD_SMSP',hexa_response,end='', file=text_file)

                    elif (index >= start_digit and index != last_digit) and val != 255:
                        with open("Output.txt", "a") as text_file:
                          print (hexa_response,end='', file=text_file)

                    elif index == start_digit and val == 255:
                        with open("Output.txt", "a") as text_file:
                          print('RECORD_SMSP',end='', file=text_file)

                    elif index >= start_digit and val == 255 :
                        with open("Output.txt", "a") as text_file:
                          print (' ', file=text_file)
                        break
        else :
            with open("Output.txt", "a") as text_file:
                print (input2,search(R1_FIND), file=text_file)


def read_chv (input1):

  SELECT_FIND = SELECT + input1
  #print (SELECT_FIND)
  x = response, sw1, sw2 = cardservice.connection.transmit(SELECT_FIND)
  #print(x)

  if sw1 == 0x9F:
      SUM = GET + [sw2]
      R_FIND = response, sw1, sw2 = cardservice.connection.transmit( SUM )

      #R1_FIND = [0, 0, 0, 96, 47, 0, 4, 0, 5, 240, 85, 1, 2, 1, 48]
      R1_FIND = response
      #print (R1_FIND)
               
      fil = {}
    
      cond = ('ALW', 'CHV1', 'CHV2', 'RFU', 'ADM', 'ADM', 
          'ADM', 'ADM', 'ADM', 'ADM', 'ADM',
          'ADM', 'ADM', 'ADM', 'ADM', 'NEW')
    
      fil['READ'] = cond[R1_FIND[8] >> 4]
      fil['UPDATE'] = cond[R1_FIND[8] & 0x0F]
      fil['INCREASE'] = cond[R1_FIND[9] >> 4]
      fil['INVALIDATE'] = cond[R1_FIND[10] & 0x0F]
      fil['REHABILITATE'] = cond[R1_FIND[10] >> 4]
    
      '''
      print ('READ: '+fil['READ'])
      print ('UPDATE: '+fil['UPDATE'])
      print ('INCREASE: '+fil['INCREASE'])
      print ('INVALIDATE: '+fil['INVALIDATE'])
      print ('REHABILITATE: '+fil['REHABILITATE'])
      '''
      with open("Output.txt", "a") as text_file:
        print  ('',fil['READ']+';'+fil['UPDATE']+';'+fil['INCREASE']+';'+fil['INVALIDATE']+';'+fil['REHABILITATE'], file=text_file) 

   

  



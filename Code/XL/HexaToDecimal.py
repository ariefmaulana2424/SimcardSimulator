from smartcard.util import toHexString, toBytes


#Convert response from function find (ReadAndGet.py), then translate into data which can be read.
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
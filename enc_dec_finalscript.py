import re
def main():
    oper= menu()
    if (oper[0]== 1 and oper[1]== 'Y'):
        print("enter key:")
        encrypt_key = key_extract(int(input()))
        print("enter your string:")
        str_send= input()
        b=(encryter(str_send,encrypt_key))
        write_file(b,'data.txt')
    elif(oper[0]== 1 and oper[1]== 'N'):
        print("enter key:")
        encrypt_key = key_extract(int(input()))
        print("enter your string:")
        str_send= input()
        b=(encryter(str_send,encrypt_key))
        print(b)
    elif(oper[0]== 2 and oper[1]== 'Y'):
        print("enter key:")
        encrypt_key = key_extract(int(input()))
        print(decrypter('PaSs',encrypt_key))
    elif(oper[0]== 2 and oper[1]== 'N'):
        print("enter key:")
        encrypt_key = key_extract(int(input()))
        print("enter your string:")
        str_send= input()
        encrypt_key = key_extract(int(input()))
        print(decrypter(str_send,encrypt_key))
    elif(oper[0]== 3):
        write_file('','data.txt')
        print('Done.')
    else:
        print("Please check your input.")






def write_file(to_wrt,opt):
    if (to_wrt!=''):
        f = open(str(opt), 'w', encoding='utf-8')
        for j in to_wrt:
            f.write(j)
        f.write('\n')
    else:
        f = open(str(opt),'w')
        f.truncate()
    f.close


def read_file():
    f = open('data.txt', 'r', encoding="utf-8")
    temp=f.read()
    return temp



def key_extract(key_In):
    k = key_In
    list_key = list()
    for i in range(6):
        mod = k % 10
        list_key.append(mod)
        k = k - mod
        k = k // 10
    return list_key


def enrule(lst_key):
    counter=0
    lst_encRULE= list()
    lst_encCHAR= list()
    for z in lst_key:
        if (counter % 2 == 0):
            if (z % 2 == 0):
                lst_encRULE.append(0)


            elif (z % 2 != 0):
                lst_encRULE.append(1)

        else:
            lst_encCHAR.append(z)

        counter = counter + 1

    return (lst_encCHAR,lst_encRULE)


def encryter(wrkng_str, enc_key):
    tpl_RULEset= enrule(enc_key)
    list_contn_str = wrkng_str.split()
    new_str= str()
    for k in list_contn_str:
        len_str = len(k)
        x = 0
        while (x < len_str):

            for y in range(3):
                if (y == 0):
                    if (tpl_RULEset[1][y] == 0):
                            new_str+=(chr(ord(k[x]) * tpl_RULEset[0][y]))
                    elif (tpl_RULEset[1][y] == 1):
                            new_str+=(chr(ord(k[x]) // tpl_RULEset[0][y]))


                if (y == 1):
                    if (tpl_RULEset[1][y] == 0):
                        new_str+=(chr(ord(k[x]) + tpl_RULEset[0][y]))
                    elif (tpl_RULEset[1][y] == 1):
                        new_str+=(chr(ord(k[x]) - tpl_RULEset[0][y]))

                if (y == 2):
                    if (tpl_RULEset[1][y] == 0):
                        new_str+=(chr(tpl_RULEset[0][y] + 33))
                    elif (tpl_RULEset[1][y] == 1):
                        new_str+=(chr(97 - (tpl_RULEset[0][y])))

            if (x == len_str-1):
                new_str +=' '




            x += 1

    return new_str

def decrypter(dec_str,dec_key):

    tpl_RULE=enrule(dec_key)
    new_str= str()
    if(dec_str=='PaSs'):
        temp=read_file()
    temp_2=re.split(' ',temp)
    temp_2=temp_2[:-1]
    for k in temp_2:
        x= str(k[2])
        list_opertional=(re.split(x,k))
        list_opertional=list_opertional[:-1]
        len_str=len(list_opertional)
        x=0
        while(x<len_str):
            if(tpl_RULE[1][1] == 0):
                new_str+=(chr(ord(list_opertional[x][1]) - tpl_RULE[0][1]))
            elif(tpl_RULE[1][1] == 1):
                new_str+=(chr(ord(list_opertional[x][1]) + tpl_RULE[0][1]))
            x+=1
        new_str+=' '
    return new_str









def menu():
    print("THIS IS ENCRYPTER/DECRYPTER SCRIPT. WELCOME")
    print('''enter option number from the following list:
           1> ENCRYPTER
           2> DECRYPTER
           3> Clear the default text file.

    ''')
    choice_1= int(input())
    if (choice_1==1):
        print("would you like to write the encrypted text to a text file?||ANSWER:Y/N||case sensitive")
        choice_2=str(input())
        if (choice_2.islower()):
            choice_2=choice_2.upper()
    elif(choice_1==2):
        print("should the text read from file?||ANSWER:Y/N||case sensitive")
        choice_2=str(input())
        if (choice_2.islower()):
            choice_2=choice_2.upper()
    elif(choice_1==3):
        choice_2=''


    return (choice_1,choice_2)


if __name__ == "__main__": main()

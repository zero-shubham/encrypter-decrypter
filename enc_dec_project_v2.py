def main():
    oper= menu()
    if (oper[0]== 1 and oper[1]== 'Y'):
        print("enter key:")
        encrypt_key = key_extract(int(input()))
        print("enter your string:")
        str_send= input()
        b=(encryter(str_send,encrypt_key))
        print(ord(b[0]))
        print(b)
        write_file(b)









def write_file(to_wrt):
    f = open('data.txt', 'w', encoding='utf-8')
    for j in to_wrt:
        f.write(j)
    f.close


def read_file():
    pass


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
    print(tpl_RULEset)
    for k in list_contn_str:
        len_str = len(k)
        x = 0
        while (x < len_str):

            for y in range(3):
                if (y == 0):
                    if (tpl_RULEset[1][y] == 0):
                        str_temp=(chr(ord(k[x]) * tpl_RULEset[0][y]))
                        if(ord(str_temp)>32):
                            new_str+=(chr(ord(k[x]) * tpl_RULEset[0][y]))
                        else:
                            while(ord(str_temp)<33):
                                str_temp= chr(ord(str_temp)+ tpl_RULEset[0][y])
                            new_str+=str_temp
                    elif (tpl_RULEset[1][y] == 1):
                        str_temp=(chr(ord(k[x]) // tpl_RULEset[0][y]))
                        if(ord(str_temp)>32):
                            new_str+=(chr(ord(k[x]) // tpl_RULEset[0][y]))
                        else:
                            while(ord(str_temp)<33):
                                str_temp= chr(ord(str_temp)+ tpl_RULEset[0][y])
                            new_str+=str_temp


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
    pass







def menu():
    print("THIS IS ENCRYPTER/DECRYPTER SCRIPT. WELCOME")
    print('''enter option number from the following list to tell us about your choice:
           1> ENCRYPTER
           2> DECRYPTER



    ''')
    choice_1= int(input())
    if (choice_1==1):
        print("would you like to write the encrypted text to a text file?||ANSWER:Y/N||case sensitive")
        choice_2=str(input())

    return (choice_1,choice_2)


if __name__ == "__main__": main()

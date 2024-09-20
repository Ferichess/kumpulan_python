# tutorial https://www.youtube.com/watch?v=n0tURC_xeyI
# 


# nama = "feri sandria"
# usia = 21

import random
from lib.libs import welcome_message

# welcome_message = "selamat datang di python"
# print(f"{welcome_message}")

# print(usia)
# print(10)
# print(f"{usia}")
# print(f'''
#       {nama} 
#       ''')

# nomor_saya = 10
# if (nomor_saya == 4):
#     print(f"benar nomor saya {nomor_saya}")
# else:
#     print(f"salah nomor saya {nomor_saya}")

# input("silahkan ketik apapun: ")

welcome_message("Selamat Datang Di Python")

goa_position = random.randint(1,4)
user_name = input("masukkan username: ")

while nama_user == "":
    user_name = input("masukkan username: ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4

goa = goa_kosong.copy()

goa[goa_position - 1]= "|0_0|"
goa_kosong = " ".join(goa_kosong)
goa = " ".join(goa)


while True :
    # print(f"username anda adalah {user_name}")
    print(f'''hallo {user_name} perhatikan goa di bawah ini
        {goa_kosong}
        
        ***
        ''')
    pilihan_user = int(input(f"di goa nomer berapa {user_name} berada ? [1/2/3/4] "))

    confirm_answer = input(f"apakah anda yakin {user_name} jawaban adalah {pilihan_user} ? (y/n) ")

    if (confirm_answer == "n"):
        print("program berhenti")
        exit()
    elif (confirm_answer == "y"):
        # print (f"{user_name} memilih {pilihan_user}")
        if (pilihan_user == goa_position):
            print(f"{goa} \n selamat {user_name} anda menang !!!")
        else:
            print(f"{goa} \n maaf {user_name} anda kalah !!!")
    else:
        print("ulangi kembali program")
        exit()
    play_again = input("\n \n apakah anda ingin bermain lagi ? (y/n) ")
    if (play_again == "n"):
        break
print("program selesai")


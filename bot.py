import requests, json, os
import time
from requests.exceptions import Timeout

banner =("""
ㅤㅤㅤㅤㅤㅤ\033[1;31m  ╔════════•ೋೋ•════════╗
\033[1;33m                WELLCOME TO SKYZONE
\033[1;31m             Tolong Gunakan Script ini
\033[1;31m                 sebijak mungkin
ㅤㅤㅤㅤㅤㅤ\033[1;31m  ╚════════•ೋೋ•════════╝
ㅤㅤㅤㅤㅤㅤㅤ\033[3;36mᵇʸ: sᴋʏʟᴀʀᴋ\033[0;37m
""")
os.system('clear')
print(banner)
txtid = input('\033[3;35mmasukkan link spoon: \033[3;34m')
params = {'username': txtid}
headers = {'User-Agent':'Mozilla/5.0',  'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'}
response = requests.get(txtid)
url = response.url
slink = url[34:-59]
print("\033[0;37m",slink)
print("\033[1;33mloading .")
time.sleep(.5)
print("\033[1;33mloading . .")
time.sleep(.5)
print("\033[1;33mloading . . .")
time.sleep(.5)
print("\033[1;33mloading . . . .")
time.sleep(.5)
print("\033[1;33mloading . . . . .")
time.sleep(2)
token = (
'39ba6f6957a80495ac80e638d7fb69be246b7afb',
'46b67351e331fe86331ab097d794cb1589a4a830',
'8b346293305e25699daebf95d14543600cfcbe05',
'a97b4fedec07580b1b3a9c1f9cc00e2e4b7ce4e8',
'cb92f75c76602dae7478fa7519022512deaae9d4',
'440b33dad96b0e7f1be7054076f2cb5179032686',
'7fdee01317e66764629b44627674074cd578d242',
'69e42c08f4995d9ccb539f8ec4bcbcb0da719e3b',
'6057322086bbcac056b1220abe2cba40c56aa611',
'35e09792313363e7da3e0a0d64c987ab81fc43c5',
'6aad3d237c2bb89d2421945afec76ebd1e45f951',
'fb259d300a1e0b4f414d78d571b3a4dfa8a7f1f5',
'c0e830cd6db1d67f83d62a54a675598af3d45591',
'667ea1931450552c34bcf40f9e5c3085bafab416',
'8921300150827e6b58aebb786e0d0f7fa1225f0e',
'f6fdf91cff0c63b909c45a0b3519c54f5fe3eb65',
'ca353f6ca3b9b4f1a5b12f4e875e61478682fca9',
'44eb50e19d565eff8cc9490a54269bfe2b2e35f5',
'1748ea2ed743bb30dabd3ad781ac43aa675c0070',
'3a23ba9f94eda441a41022923ae758f108b5b0cb',
'bfc497beafb62e5daa6f46e3fbbeec9b9a1932b1',
'23008ab0165eca0e22ac3edf2ef99f6c4c1673fe',
'234ff63cdc5db19a4d8c7ebc4fc1814918c2fe94',
'1a620e8563dc1c7b05d3d92a1b41daefb16a721b',
'0ca359d8f14fcec9a9fc1f6d9e5334706e260438',
'5b1665a5166c3e8151cb359be5b9e5f52d1c33ff',
'd2cad024e4efae0d62d3243c132044bb57efe38f',
'8a10ad00ac70cea5c403725c6376ab61e1c263da',
'4be632cefd894ef37a93605383389d1693648e76',
'ea6fce6d0d9d47573123d44ab2726b2bb661dccc', 
'e0a73368d1cfe253f5112c42518a197706d879f2', 
'a273d745616c65b33cbd48e2f40fbe9fa51a0193', 
'faf5e91f391565d0a96c5f8399ae04a97c7a2d90', 
'35504899a6a87d63de8410a416e9d6288c9ead60', 
'bfd7e29e08b8ca6628f0db6a90ecef5d8ccf3121', 
'339025ba95a7c75cd1a46015a891e4d939be041b', 
'1d5e3136981b32ecb2949d84a0f930a92a9f8891', 
'dcde4de30c7899321308defda0a70fe7d922921d', 
'1868c239787d73e3d2740899a45ce6f5a1450bf9', 
'582265366196ef856292ce52caa4403e53f1fa35', 
'f1455b00d12b5419a9b580fcfd028cce998056e4', 
'a0683f0f3fc91ebacb08c993b440392b2d225689', 
'9899ac8c90cf0e5bc9b3bb327160e438a6b6214f', 
'ee0db639f8b3e74ddea3e45c1bfa3bf7bfcaed24', 
'8898066bd789638d4bdfc5e3cbdb4bbaa0972104', 
'68e6f10a7ac0ce82e25007b3118a224ef6e4b4a1', 
'7c279d694095c68035f7f365f284d73923bade0e', 
'f50009bfc0ad907f6eda4aa52d96f737caf53be5', 
'fb9b218b2b72ff05f5bebad334a7f80b5cdfafa4', 
'752cba16e82b5a97822b81f72e3fc2b33fd9b99f', 
'b674226dfae89b236add16b2c7df259df380ccc7', 
'd467cc6b0bff0054b63b165b24f8af3d0af9602f', 
'dc9c9d6c9ed226e02b84115618ab99512bdc77ca', 
'90c5cc0880c7dd04a20c6a5e2a197f3a01a99d74', 
'1099c25fa3b5d607ea1c18165f4b64a72322c440', 
'840b720f7c3f3a0e41d04cf2b700bb891805c91d', 
'4c31294dc67b5d0669ce1df42fc01362b1b371ab', 
'a3297d55064ae46ed06892133c342e91df724cb5', 
'ee64427066f50170293ea1102fd37b4d035282fb', 
'1845ef553445aafe2fcee7bac5005b84044b9db7', 
'56cc8c8f42e17523d1baf6efb400b8e9d5e1a1c4', 
'4fe8d359aae539007b08888a47dd22e92aa46780', 
'4ce1e3cdcfd21ec5ca57148d1ccb3e90c7d51e54', 
'8aba4c81ad709b20944c4ee2363d13a7bd9dcebc', 
'7d55a161732b472aeb054807b091783654386009', 
'3e6065a767e9e8aa5d0b560fe5d6a4b8f3e3b7bb', 
'6d1a8a2fd2d154dc1eb97e61ba356635b8c4aac7', 
'3570107f623c545f6053acbc1479538f9518d652', 
'cf3231fb3dc2e1bfee17f0a48b333f99889692c6', 
'b9bd71ae4b6714cc9cfa2edd1ebf21077a9efc16', 
'2632f430e3313782b2174d61aae30c3b01e64d2a', 
'a28494e7770f062d8f641d8e3c13ecd68a43ade1', 
'8fe2d160c20bc3b782f84952e43ad9cc251dea87', 
'f2631bbdd75355ca9872ddad1119a2fc9738050a', 
'f96916bcc4d2b5b3d2ddf282f763a4908aa11cac', 
'1faf226217de0f5dd95dea38c951f46715167338', 
'122d0ea725c3456ac5f85ab6aa1db557402efb9c', 
'8177a12cc3e33b11d2d6ef8b1d4ddc01774feadc', 
'd3e4ec4b6befc2f02a418d00625823428ab56a7d', 
'bf144533c3a8029740fc05925e915c7c17378e2f', 
'2e8e6df7fa561e6d980afda686884e8fc131e30e', 
'8d2f2ab0dedd3ecf0b3029f3091f44dbf805536b', 
'bd8aefe8ac2c917d9a9c8698c866207880d9f43b', 
'ccad82f64aceb0a9ee3e7c10d4cac91c16d2a783', 
'4f1bc5d2d1981ef851d01697e64f10bec856eb78', 
'76e6cb6dcb37d353446c7af2c6afeef166955c30', 
'b7aa28549b64e4fb7f2ef0a8223aa2d229bcad21', 
'b2165143dd64c89447994589e175638566ea13c6', 
'517c3670342cf1934f6b9aac3e2be9e03274ad26', 
'ee582caf9185dbaa6ff9949cf1623dcaf5747730', 
'46ec82c62839dbb6b94f70e6203ded5f1ed0bb98',
'519cf393e74951f0abff577c4bc46997e22e0379',
'3b82a11a4f018e885ac3665e335ac920ef3368c4',
'f86bc2aa3c3a925941b8d5580e477e18e08a91e0',
'888045ddd9f385ce4e97704ac1d54aa4695a6c15',
'bdd49d8ca85511dfac337872d6ea8c927d7aaadf',
'5641780701f17b9d2ac81b1237636373e045e008',
'e3ef6ae25415817065427a42b637d3d79ada8e41',
'29017521e27da9b4bcda91a29528b2c0cbc31dbc',
'57b52fdda2574745c09b84f5ff92f121313bbb7e',
'5de52dba591a18af9e88964a216dc6c4f00f3814',
'e3b27ae637b530126c3da30f59fd4d9c19dabe07',
'ff8727cf1a2be016ee210d55c096246dac52528c',
'124a200f574cc13e80d6125216429ac411a443c8',
'f98b62594842f3f5e87a430ac79887b42646b7e8',
'cdafce1844a8848fb1eda3993b2e254faf747821',
'48d5345c90bc1a546d83e57beb0be1aa02d8a072',
'75721ea472cb941953ff853914c4a0db5a937c2a',
'08efa2ee29a96972627253dc2986ab440745c608',
'12a979c48972415d0f122ec820b8187e67688b99',
'0057504cf1cf33ea19d96e4692088b0c3f08ec4d',
'e60b70bbe36258ec70e2ae8c259c1aa0d226d28a',
'8f88d5136bb4ee007384e769d1911cf66f61d94f',
'0a2c96320271c17ab3c0428b31736031f318293e',
'4315524e4001afbafcb11d4011bf318718abc6dc',
'b4783ede2cce4840bec5285aff18c06fe728902a',
'1e61676955716ed566f83e84e1df137ec93d421a', 
'91e9a780310b6fe838bba6da8dcdffa2c4005af7',
'2613fba10ebac809aa397bd5f67567cc2bea1e28',
'fe4219960d2855663601c59b87198cef475d76cb',
'423b92a2c6102ed92acdac2b854dd1f1010d2457',
'7ab19aee7fcea47fea313f27cd9c4c847e39d1cb',
'09fd0fae27160e34eb475cfe97daa82adbf2e73a',
'2d7a424abac44053c48297ec467dfe5d10c76e7c',
'4972f0785012b536fc0ef520e410444af1026fad',
'd4a5e28158e446108ef3e25480ea433bfde1bf66',
'8d42611afae2c86ccb7ed30520320dcb3d8f3c79',
'2587244fa0f2a258a620c32d736f0b9cfa974881',
'f872407eeb6b56b0fab9581e1216521e43e3dabc',
'9f051fbb26cea8c7d7b3b840e58a49aee27a5ab6',
'c1783b498c3dedfe5a2a504edd84dc3ba9c76166',
'79d4b1236d38433a8e3fefaf3830eb50a84616de',
'7fe2779a34271366f692d214d312ff6989622eca',
'755e1d111e147ba62ee174c41209b2ea5e190fa2',
'c5ec4b36f216611f87e404f687a55d22bbc74077',
'e77724bcd24a3550a77ad9b1abf6e39b7d71818a',
'0c63c44a13e909912a35c3072881916b3985d595',
'0a718d11411a0b8efcc2b27df6632f457cf58ec4',
)
mode0 = ('report','join','like','leave')
os.system('clear')
print(banner)
print('\033[1;31m[1] \033[1;32mjoin')
print('\033[1;31m[2] \033[1;32mlike')
print('\033[1;31m[3] \033[1;32mout')
mode = mode0[int(input("\033[1;35mpilih mode bot: \033[1;34m"))]
os.system('clear')
print(banner)
bot = token[int(input("\033[1;35mtotal bot 127, masukkan jumlah bot: \033[1;34m"))]
i=0
for tokens in token:
    i+=1
    try:
        headers={'User-Agent':'Mozilla/5.0','Authorization':'Token ' + str(tokens)}
        response = requests.post('http://id-api.spooncast.net/lives/'+slink+'/'+mode+'/',headers=headers)
    except:
		    print('\033[1;31mgagal')
    if tokens == bot:
        print("\033[1;33m"+str(i)+" bot,selesai\033[0;37m")
        break
    if response.status_code == 200:
        print("\033[1;32m"+mode+" bot ke "+str(i)+" berhasil")
    elif response.status_code == 403:
        os.system('clear')
        print(banner)
        print("\033[1;33mserver sedang sibuk, tunggu 6 menit\033[0;37m")
        time.sleep(360)
    elif response.status_code == 401:
        print("\033[1;31mgagal token", str(tokens))
    else:
        print(response)
        print("\033[1;31m"+mode+" bot ke "+str(i)+" gagal")

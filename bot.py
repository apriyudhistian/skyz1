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
'd2cad024e4efae0d62d3243c132044bb57efe38f',
'a273d745616c65b33cbd48e2f40fbe9fa51a0193',
'7fdee01317e66764629b44627674074cd578d242',
'1099c25fa3b5d607ea1c18165f4b64a72322c440',
'ee0db639f8b3e74ddea3e45c1bfa3bf7bfcaed24',
'44eb50e19d565eff8cc9490a54269bfe2b2e35f5',
'f2631bbdd75355ca9872ddad1119a2fc9738050a',
'8aba4c81ad709b20944c4ee2363d13a7bd9dcebc',
'56cc8c8f42e17523d1baf6efb400b8e9d5e1a1c4',
'7c279d694095c68035f7f365f284d73923bade0e',
'dc9c9d6c9ed226e02b84115618ab99512bdc77ca',
'f1455b00d12b5419a9b580fcfd028cce998056e4',
'bfd7e29e08b8ca6628f0db6a90ecef5d8ccf3121',
'8fe2d160c20bc3b782f84952e43ad9cc251dea87',
'752cba16e82b5a97822b81f72e3fc2b33fd9b99f',
'35504899a6a87d63de8410a416e9d6288c9ead60',
'69e42c08f4995d9ccb539f8ec4bcbcb0da719e3b',
'd467cc6b0bff0054b63b165b24f8af3d0af9602f',
'dcde4de30c7899321308defda0a70fe7d922921d',
'f96916bcc4d2b5b3d2ddf282f763a4908aa11cac',
'582265366196ef856292ce52caa4403e53f1fa35',
'9899ac8c90cf0e5bc9b3bb327160e438a6b6214f',
'840b720f7c3f3a0e41d04cf2b700bb891805c91d',
'e0a73368d1cfe253f5112c42518a197706d879f2',
'6aad3d237c2bb89d2421945afec76ebd1e45f951',
'3570107f623c545f6053acbc1479538f9518d652',
'35e09792313363e7da3e0a0d64c987ab81fc43c5',
'b674226dfae89b236add16b2c7df259df380ccc7',
'1faf226217de0f5dd95dea38c951f46715167338',
'ee64427066f50170293ea1102fd37b4d035282fb',
'3e6065a767e9e8aa5d0b560fe5d6a4b8f3e3b7bb',
'6057322086bbcac056b1220abe2cba40c56aa611',
'fb259d300a1e0b4f414d78d571b3a4dfa8a7f1f5',
'ca353f6ca3b9b4f1a5b12f4e875e61478682fca9',
'8898066bd789638d4bdfc5e3cbdb4bbaa0972104',
'bfc497beafb62e5daa6f46e3fbbeec9b9a1932b1',
'39ba6f6957a80495ac80e638d7fb69be246b7afb',
'ccad82f64aceb0a9ee3e7c10d4cac91c16d2a783',
'faf5e91f391565d0a96c5f8399ae04a97c7a2d90',
'f6fdf91cff0c63b909c45a0b3519c54f5fe3eb65',
'4fe8d359aae539007b08888a47dd22e92aa46780',
'b9bd71ae4b6714cc9cfa2edd1ebf21077a9efc16',
'0ca359d8f14fcec9a9fc1f6d9e5334706e260438',
'1d5e3136981b32ecb2949d84a0f930a92a9f8891',
'1a620e8563dc1c7b05d3d92a1b41daefb16a721b',
'1748ea2ed743bb30dabd3ad781ac43aa675c0070',
'bd8aefe8ac2c917d9a9c8698c866207880d9f43b',
'8921300150827e6b58aebb786e0d0f7fa1225f0e',
'23008ab0165eca0e22ac3edf2ef99f6c4c1673fe',
'f86bc2aa3c3a925941b8d5580e477e18e08a91e0',
'122d0ea725c3456ac5f85ab6aa1db557402efb9c',
'4f1bc5d2d1981ef851d01697e64f10bec856eb78',
'440b33dad96b0e7f1be7054076f2cb5179032686',
'6d1a8a2fd2d154dc1eb97e61ba356635b8c4aac7',
'8a10ad00ac70cea5c403725c6376ab61e1c263da',
'888045ddd9f385ce4e97704ac1d54aa4695a6c15',
'8d2f2ab0dedd3ecf0b3029f3091f44dbf805536b',
'4c31294dc67b5d0669ce1df42fc01362b1b371ab',
'4be632cefd894ef37a93605383389d1693648e76',
'c0e830cd6db1d67f83d62a54a675598af3d45591',
'f50009bfc0ad907f6eda4aa52d96f737caf53be5',
'cf3231fb3dc2e1bfee17f0a48b333f99889692c6',
'4ce1e3cdcfd21ec5ca57148d1ccb3e90c7d51e54',
'a97b4fedec07580b1b3a9c1f9cc00e2e4b7ce4e8',
'8177a12cc3e33b11d2d6ef8b1d4ddc01774feadc',
'8b346293305e25699daebf95d14543600cfcbe05',
'a0683f0f3fc91ebacb08c993b440392b2d225689',
'46b67351e331fe86331ab097d794cb1589a4a830',
'bf144533c3a8029740fc05925e915c7c17378e2f',
'ea6fce6d0d9d47573123d44ab2726b2bb661dccc',
'3a23ba9f94eda441a41022923ae758f108b5b0cb',
'd3e4ec4b6befc2f02a418d00625823428ab56a7d',
'a28494e7770f062d8f641d8e3c13ecd68a43ade1',
'5b1665a5166c3e8151cb359be5b9e5f52d1c33ff',
'1868c239787d73e3d2740899a45ce6f5a1450bf9',
'3b82a11a4f018e885ac3665e335ac920ef3368c4',
'2632f430e3313782b2174d61aae30c3b01e64d2a',
'7d55a161732b472aeb054807b091783654386009',
'fb9b218b2b72ff05f5bebad334a7f80b5cdfafa4',
'68e6f10a7ac0ce82e25007b3118a224ef6e4b4a1',
'a3297d55064ae46ed06892133c342e91df724cb5',
'234ff63cdc5db19a4d8c7ebc4fc1814918c2fe94',
'667ea1931450552c34bcf40f9e5c3085bafab416',
'cb92f75c76602dae7478fa7519022512deaae9d4',
'90c5cc0880c7dd04a20c6a5e2a197f3a01a99d74',
'339025ba95a7c75cd1a46015a891e4d939be041b',
'1845ef553445aafe2fcee7bac5005b84044b9db7',
'2e8e6df7fa561e6d980afda686884e8fc131e30e',
'76e6cb6dcb37d353446c7af2c6afeef166955c3',
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

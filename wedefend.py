import os
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

#if you see this commend, that's mean I haven't finish yet this project
#by github.com/wishihab


print("Welcome to WeDefend by wishihab")
print("1. Network Activity")
print("2. Process Activity")
print("3. Scan File")
print("4. Folder Lock, Encryption")
fr = int(input("Please choose a number : "))

if fr ==1:
	print("1. Listing TCP and UDP connections")
	print("2. Listing TCP connections")
	print("3. Listing UDP connections")
	print("4. Listing TCP and UDP LISTENing connection")
	print("5. Listing TCP LISTENing connection")
	print("6. Listing UDP LISTENing connection")

	chs = int(input("NetworkAct: input a number : "))
	if chs == 1: os.system("clear") os.system("netstat -atu")
	if chs == 2: os.system("clear") os.system("netstat -at")
	if chs == 3: os.system("clear") os.system("netstat -au")
	if chs == 4: os.system("clear") os.system("netstat -ltu")
	if chs == 5: os.system("clear") os.system("netstat -lt")
	if chs == 6: os.system("clear") os.system("netstat -lu")
	if chs >= 7: print("-==========OOVVEERR NNUUMMBBEERR============-")
		
if fr == 2:
	print("1. Get list all application background")
	prs = int(input("ProcessAct: input a number : "))
	if prs == 1: os.system("ps -A")
	print("--=====How to kill? usage:pkill -u UID========--")
	if prs >= 2: print("---======= OOOVVVEEERRR ======---")

if fr == 3:
	print("Usage: scan namefile.ex")
	scn = raw_input("Usage here : ")
	if scn != null || scn != none:
	#do something here
		#read usage, check there is "scan" and "namefile.ex"
		#do next if correct, do repeat if notcorrect
	#scanning process by reading bytes and md5
	#if founded do this
	fnd = true;
	#if notfound do this
	fnd = false;
	
	#result here
	if fnd == true: print("-=Virus Detected=-")
	if fnd == false: print("-=No Virus Detected")
	
if fr == 4:
	print("1. Lock Windows or Linux Folder (Usage: lock )")
	print("2. Encrypt and Decrypt File")
	tls = int(input("input here : ")
	if tls == 1:
		print("Usage: lock /pathfolder/")
		#declare variable for pathfolder $varfolder
		lck = raw_input("Usage: ")
		if lck =='lock get$varfolder'
			#do locking folder with filter
			#if os.windows do locking cacls with echo
			#if os.linux do locking here
			#notify encryption
	if tls == 2:
		print("Usage: encrypt /pathfile/ or decrypt /pathfile/")
		#declare variable for pathfile $varfile
		enc = raw_input("Usage: ")
		if enc =='encrypt get$varfile'
			#do encrypting using aes pycrypt
			#notify if encrypting success
		if enc =='decrypt get$varfile'
			#ask password/privatekey if exist
			#do decryption using aes pycrypt
			#notify if decryption success
			
	


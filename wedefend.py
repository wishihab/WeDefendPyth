import os


print("Welcome to wedefend")
print("1. Network Activity")
print("2. Proccess Activity")
print("3. Scan File")
print("4. Tools : Lock, Encrypter")
fr = int(input("Please choose a number : "))

if fr ==1:
	print("1. Listing TCP and UDP connections") #netstat -atu
	print("2. Listing TCP connections") #netstat -at
	print("3. Listing UDP connections") #netstat -au
	print("4. Listing TCP and UDP LISTENing connection") #netstat -ltu
	print("5. Listing TCP LISTENing connection") #netstat -lt
	print("6. Listing UDP LISTENing connection") #netstat -lu

	chs = int(input("Please enter a number: "))
	if chs == 1:
		os.system("clear")
		os.system("netstat -atu")

	if chs == 2:
		os.system("clear")
		os.system("netstat -at")

	if chs == 3:
		os.system("clear")
		os.system("netstat -au")

	if chs == 4:
		os.system("clear")
		os.system("netstat -ltu")
	if chs == 5:
		os.system("clear")
		os.system("netstat -lt")

	if chs == 6:
		os.system("clear")
		os.system("netstat -lu")

	if chs >= 7:
		print("-==========OOVVEERR NNUUMMBBEERR============-")
	
		
if fr == 2:
	print("1. Get list all application background")
	
	
	prs = int(input("input a number : "))
	if prs == 1:
		os.system("ps -A")
		print("--=====How to kill? usage:pkill -u UID========--")
	if prs >=2:
		print("---======= OOOVVVEEERRR ======---")
if fr >= 3:
	print("-==========OOVVEERR NNUUMMBBEERR============-")

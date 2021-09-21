import os

install = input("\n>> Type [Y] for install or Type [R] for Remove/Exit: ")
run = os.system

if str(install) == "Y" or str(install) == 'y':

	run("chmod 777 pass_gen.py")
	run("sudo mkdir /usr/share/passgen")
	run("sudo cp pass_gen.py /usr/share/passgen/pass_gen.py")

	cmnd = (' #! /bin/sh \n exec python3 /usr/share/passgen/pass_gen.py "$@"')
	with open('/usr/bin/passgen','w')as file:
		file.write(cmnd)

	run("chmod +x /usr/bin/passgen & chmod +x /usr/share/passgen/pass_gen.py")
	print("Congrats! 'passgen' is install in your system, then type 'passgen' in anywhere :)")
	print("Happy privacy & Happy hacking")

if str(install) == "R" or str(install) == "r":
	run('sudo rm -rf /usr/share/passgen')
	run('sudo rm -rf /usr/bin/passgen')
	print("passgen remove successfully")

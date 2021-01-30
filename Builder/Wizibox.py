############################################################################
## Builder Wizibox framwork development UI/UX
## Engineer Aryia Behroziuan
## GitHub: https://github.com/Aryia-behroziuan
## Website: https://aryia-behroziuan.github.io/web/
## Wizibox from qitSource inc https://aryia-behroziuan.github.io/about/
############################################################################

### importing
import time
import os


## Title (Company)



## Development run
version = 'v1.0.0'

# login User
print('\nLogin in Wizibox')
print('----------------------------')
builder = input(' Email address: ')
time.sleep(1)
print('\nHi Welcome to Wizibox\n Develop your user interface with this framework')
time.sleep(2)
os.system('cls' or 'clear')


# Color
class color:
     blue = '\033[94m'
     yell = '\033[93m'
     end = '\033[0m'

# Program
for x in range(9000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    mainroot = str(input(color.blue+ 'Wizibox@Wizi.so/-$ ' + color.end))
    if mainroot == '-help':
          file = open('help.txt', encoding="utf-8")
          text = file.read()    
          print(text) 


    if  mainroot == 'cls':
          os.system('cls')


    if mainroot == 'clear':
          os.system('clear')    


    if mainroot == 'doc':
          file = open('Document.txt', encoding="utf-8")
          text = file.read()    
          print(text) 


    if mainroot == 'update':
          print('installed Wizibox '+version)
          print('Download the new update from the website'+color.yell+"'https://aryia-behroziuan.github.io/wizibox/'"+color.end)


    if mainroot == 'version':
          print('installed Wizibox '+version)
          print('Apply to update the software from the front'+color.yell+"'update'"+color.end)


    if mainroot == 'login -a':
          file = open('framwork/login-a.html', encoding="utf-8")
          text1 = file.read()   

          
          new_file = input('Enter url(new file):')

          Createindex = str(new_file+'\login-a.html')
          maindocument = open(str(Createindex), "a")
          maindocument.write(str(text))
          print('\nBuilding...')
          time.sleep(1)
          print(color.yell+'\nBuild Login Page in address: '+new_file+'\login-a.html'+color.end)
          print()

    if mainroot == 'login -b':
          file = open('framwork/login-b.html', encoding="utf-8")
          text = file.read()   
          
          new_file = input('Enter url(new file):')

          Createindex = str(new_file+'\login-b.html')
          maindocument = open(str(Createindex), "a")
          maindocument.write(str(text))
          print('\nBuilding...')
          time.sleep(1)
          print(color.yell+'\nBuild Login Page in address: '+new_file+'\login-b.html'+color.end)
          print()


    if mainroot == 'blog':
          file = open('framwork/blog.html', encoding="utf-8")
          text = file.read()   
          
          new_file = input('Enter url(new file):')

          Createindex = str(new_file+'/blog.html')
          maindocument = open(str(Createindex), "a")
          maindocument.write(str(text))
          print('\nBuilding...')
          time.sleep(1)
          print(color.yell+'\nBuild Login Page in address: '+new_file+'/blog.html'+color.end)
          print()
          

    if mainroot == 'blog':
          file = open('framwork/blog.html', encoding="utf-8")
          text = file.read()   
          
          new_file = input('Enter url(new file):')

          Createindex = str(new_file+'/blog.html')
          maindocument = open(str(Createindex), "a")
          maindocument.write(str(text))
          print('\nBuilding...')
          time.sleep(1)
          print(color.yell+'\nBuild Login Page in address: '+new_file+'/blog.html'+color.end)
          print()
          

    if mainroot == 'support':
          file = open('framwork/support.html', encoding="utf-8")
          text = file.read()   
          
          new_file = input('Enter url(new file):')

          Createindex = str(new_file+'/support.html')
          maindocument = open(str(Createindex), "a")
          maindocument.write(str(text))
          print('\nBuilding...')
          time.sleep(1)
          print(color.yell+'\nBuild Login Page in address: '+new_file+'/support.html'+color.end)
          print()



    if mainroot == 'profile':
          file = open('framwork/profile.html', encoding="utf-8")
          text = file.read()   
          
          new_file = input('Enter url(new file):')

          Createindex = str(new_file+'/profile.html')
          maindocument = open(str(Createindex), "a")
          maindocument.write(str(text))
          print('\nBuilding...')
          time.sleep(1)
          print(color.yell+'\nBuild Login Page in address: '+new_file+'/profile.html'+color.end)
          print()   



    if mainroot == 'about':
          file = open('framwork/about.html', encoding="utf-8")
          text = file.read() 
          
          new_file = input('Enter url(new file):')

          Createindex = str(new_file+'/about.html')
          maindocument = open(str(Createindex), "a")
          maindocument.write(str(text))
          print('\nBuilding...')
          time.sleep(1)
          print(color.yell+'\nBuild Login Page in address: '+new_file+'/about.html'+color.end)
          print()       

    if mainroot == "exit":
          break
          print(x)

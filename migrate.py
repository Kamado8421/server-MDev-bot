import os 
import time

os.system('cls')
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')

print('\n\n\033[1;32mMigração concluída!!\033[m\n\n')

time.sleep(2)
os.system('cls')
print('\033[1;32mIniciando servidor...\033[m\n')
os.system('python manage.py runserver')


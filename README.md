PS D:\OneDrive\Desktop\python game 2\CAPTON project> & C:/Users/navee/AppData/Local/Microsoft/WindowsApps/python3.12.exe "d:/OneDrive/Desktop/python game 2/CAPTON project/main.py"
pygame 2.6.0 (SDL 2.28.4, Python 3.12.10)
Hello from the pygame community. https://www.pygame.org/contribute.html
Traceback (most recent call last):
  File "d:\OneDrive\Desktop\python game 2\CAPTON project\main.py", line 156, in <module>
    if pygame.sprite.collide_rect(enemy.rect,spaceship.rect):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\navee\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\pygame\sprite.py", line 1484, in collide_rect
    return left.rect.colliderect(right.rect)
           ^^^^^^^^^
AttributeError: 'pygame.rect.Rect' object has no attribute 'rect'
PS D:\OneDrive\Desktop\python game 2\CAPTON project> 


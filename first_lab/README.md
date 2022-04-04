INSTRUCTIONS FOR WORKING WITH THIS CLI APPLICATION
===================================================

1. Go to the directory where this project is located (in my case ".../first_lab")

Example: `cd C:\User\pycharmProject\first_lab`

2. Run the file through the following command:

`python .\main.py command`

What commands can you use?
--------------------------
+ if you want to run the prepared preset and check the program operation

`preset`

+ if you want to read data from a previously prepared file (it must be in the same folder with the project)

`file 'filename'`

+ if you want to enter the starting data from the keyboard (the first two arguments are the size of the matrix, 
and then the number of living organisms in order of priority: rabbits, deer, squirrels, wolves, bears, plants)

`keyboard x y r d s w b p`

+ if you want to load a previously saved file

`load 'filename'`

3. After the appearance of 'Move #0', the following commands are valid:
+ next (next move)
+ save (save current state to file)
+ exit (finish the program)

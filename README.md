# SuperInstantiation
Automaes the task of copying component details from instantiation files in Vivado (I'm surprised it doesn't do this anwyay). Program copies all component declarations (from the .vho files) into main .vhd file. Some hard coded file paths are included as the more general solution was a good bit slower but if you find a fast way please commit it!

To setup: change the top_filename and base variables in the .pyw program to the appropriate ones for your project and change the file path in the SI.bat file to the absolute path of your .pyw program. Make sure the folder you have the SI.bat program in on your system path and if not add it. When complete the program can be simply run by pressing WIN+R, typing SI and hitting enter.

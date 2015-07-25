#! python3
import os, re

top_filename = 'NMSE'
base = 'C:\\Xilinx_Vivado_SDK_Win_2015.1_0428_1\\ug939-design-files\\lab_1\\'
filepath = os.path.join(base, top_filename, top_filename + '.srcs','sources_1\\ip')
os.chdir(filepath)
instantionaRegex = re.compile(r'COMPONENT Declaration ------ COMP_TAG\nCOMPONENT(.*)END COMPONENT;(.*)your_instance_name(.*)\);',re.DOTALL)
comp = ''
port = ''

for folderName, subfolders, filenames in os.walk(filepath):
    for filename in filenames:
        if(filename[-4:] == '.vho'):
            infile = open(filepath + '\\' + filename[:-4] + '\\'  + filename)
            contents = infile.read()
            mo = instantionaRegex.search(contents)
            comp += '\nCOMPONENT'+ mo.group(1) + 'END COMPONENT;\n'
            #port += 'your_instance_name'+ mo.group(3) + ');\n\n'
            infile.close()

VHDL_file = os.path.join(base, top_filename, top_filename + '.srcs','sources_1\\new\\', top_filename + '.vhd')
print(VHDL_file)
infile = open(VHDL_file)
contents = infile.read()
outputRegex = re.compile(r'(.*?)COMPONENT(.*)END COMPONENT;(.*)',re.DOTALL)
mo = outputRegex.search(contents)
infile.close()

outfile = open(VHDL_file,'w')
outfile.write(mo.group(1) + comp + mo.group(3))
outfile.close()

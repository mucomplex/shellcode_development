#!/usr/bin/python3
import os
import sys
import time
class general():
    def help(self):
        print('[*] Usage : '+ sys.argv[0] +' argv[1] argv[2]')
        print(' * argv[1] = asm files ex: test.asm')
        print(' * argv[2] = shell')
        print('[*] install missing program : '+sys.argv[0]+' install')
        print('[*] to compile shellcode : '+sys.argv[0]+' test.asm')
        print('[*] to view shellcode :'+sys.argv[0]+' test.asm shell')
        exit()

class compile():
    # initialize program
    def __init__(self,program):
        self.program = program
        program_name = self.program.split('.')[0]
    # compile program
    def nasm_compile(self):
        nasm_input = 'nasm -f elf ' + self.program
        os.system(nasm_input)
        program_name = self.program.split('.')[0]
        nasm_compile = 'ld -o '+ program_name +' '+ program_name +'.o -m elf_i386'
        os.system(nasm_compile)
        os.system('rm -rf %s.o' % program_name)
        print('[*] Complete compile')
    # disassemble program
    def disassemble(self):
        os.system('objdump -d %s -M intel' % self.program.split('.')[0])
    # check for extension
    def trace_extension(self):
        if self.program.find('.asm') == -1:
            print('please include the extension.')
            exit()
        else:
            return True
    # check file is exist
    def check_file(self):
        if os.path.isfile(self.program) == False:
            print('file does not exists')
        else:
            return True

# general argument
general_function = general()
if len(sys.argv) == 1:
    general_function.help()
# first argument settings
if len(sys.argv) == 2:
    if sys.argv[1] == 'install':
        os.system('sudo apt-get install nasm')
    elif sys.argv[1] == '-h':
        general_function.help()
    else:
        compile_program = compile(sys.argv[1])
        if compile_program.trace_extension() == True and compile_program.check_file() ==  True:
            compile_program.nasm_compile()
# 2nd argument settings
if len(sys.argv) == 3:
    if sys.argv[2] == 'shell':
        compile_program = compile(sys.argv[1])
        compile_program.disassemble()


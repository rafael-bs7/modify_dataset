import shutil, tempfile
import re
import os
import shutil


main_folder = '/home/rafael/Documentos/IC/ImgCUtwithParmider/Parminder/teste'

def file_loop(files):
    for file in files:
        
        file_name, file_extension = os.path.splitext(file)
        
        if file_extension == '.txt':

                
                with open(str(f"{file_name}{file_extension}"), 'r') as arquivo, \
                    tempfile.NamedTemporaryFile('w', delete=False) as out:
                    for linha in arquivo:
                        if linha[0] == '0':
                            linha = '2'+ linha[1:] # remontar a linha
                        elif linha[0] == '1':
                            linha = '0'+ linha[1:] # remontar a linha
                        elif linha[0] == '2':
                            linha = '1'+ linha[1:] # remontar a linha
                            
                        out.write(linha) # escreve no arquivo temporário

                # move o arquivo temporário para o original
                shutil.move(out.name, str(f"{file_name}{file_extension}") )
                # lê do arquivo e escreve em outro arquivo temporário
     
                

def main_loop():
    for root, dirs, files in os.walk(main_folder):
        file_loop(files)
    
    


if __name__ == '__main__':
    main_loop()
    
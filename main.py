from jumps.scm import Scm
from jumps.jump import Jump
from jumps.drop_jump import Drop_Jump
from jumps.lateral_jump import Lateral_Jump
from pathlib import Path
import numpy as np
import xlsxwriter
import os


def main():
    data_directoty = Path('/home/lenizio/biomechanics/jumps_project/data')
    output_directory = ('/home/lenizio/biomechanics/jumps_project/output/output.xlsx')
    workbook = xlsxwriter.Workbook(output_directory)
    worksheet1 = workbook.add_worksheet('Counter Movement Jump')
    worksheet2 = workbook.add_worksheet('Drop Jump')
    worksheet3= workbook.add_worksheet('Lateral Jump')
    
    headers1 = ['Voluntário', 'Tentativa', 'Peso(N)', 'Massa(kg)', 'Altura Salto(m)', 'IFR', 'Pico de Potência(W)','Pico de Potência(W/N)','Pico de Potência(W/kg)']
    headers2= ['Voluntário', 'Tentativa',"Altura Plataforma(m)", 'Peso(N)', 'Massa(kg)', 'Altura Salto(m)', 'IFR', 'Pico de Potência(W)','Pico de Potência(W/N)','Pico de Potência(W/kg)']
    headers3 = ['Voluntário', 'Tentativa', 'Altura Barreira(m)','Peso(N)', 'Massa(kg)', "Primeiro Pico","Segundo Pico","Terceiro Pico",'Quarto Pico',"Quinto Pico"] 
    
    for col_num, header in enumerate(headers1):
        worksheet1.write(0, col_num, header)

    for col_num, header in enumerate(headers2):
        worksheet2.write(0, col_num, header)
        
    for col_num, header in enumerate(headers3):
        worksheet3.write(0, col_num, header)


    row1 = 1  
    row2 = 1
    row3 = 1  
    
    
    for file in data_directoty.rglob("*"):
        if file.is_file():
            name,jump_type,attempt,weight = file.stem.strip().split('_')
            
            if jump_type=="scm":
                jump= Scm(name,jump_type,attempt,weight,filepath=file)
                worksheet1.write(row1, 0, name)
                worksheet1.write(row1, 1, attempt)
                worksheet1.write(row1, 2, weight)
                worksheet1.write(row1, 3, jump.mass)
                worksheet1.write(row1, 4, jump.jump_height)
                worksheet1.write(row1, 5, jump.reactive_strength_index)
                worksheet1.write(row1, 6, jump.peak_power)
                worksheet1.write(row1, 7, jump.peak_power/jump.weight)
                worksheet1.write(row1, 8, jump.peak_power/jump.mass)
                row1 += 1 
                jump.print_jump_data()               
            
            elif jump_type.startswith('sp'):
                drop_platform_height = jump_type.strip().split('.')[1]
                jump= Drop_Jump(name,jump_type,attempt,weight,drop_platform_height,filepath=file)
                worksheet2.write(row2, 0, name)
                worksheet2.write(row2, 1, attempt)
                worksheet2.write(row2, 2,jump.drop_platform_height)
                worksheet2.write(row2, 3, weight)
                worksheet2.write(row2, 4, jump.mass)
                worksheet2.write(row2, 5, jump.jump_height)
                worksheet2.write(row2, 6, jump.reactive_strength_index)
                worksheet2.write(row2, 7, jump.peak_power)
                worksheet2.write(row2, 8, jump.peak_power/jump.weight)
                worksheet2.write(row2, 9, jump.peak_power/jump.mass)
                row2 += 1
                jump.print_jump_data()               

            elif jump_type.startswith('sl'):
                hurdle_height = jump_type.strip().split('.')[1]
                jump=Lateral_Jump(name,jump_type,attempt,weight,hurdle_height,filepath=file)
                worksheet3.write(row3, 0, name)
                worksheet3.write(row3, 1, attempt)
                worksheet3.write(row3, 2, jump.hurdle_height)
                worksheet3.write(row3, 3, weight)
                worksheet3.write(row3, 4, jump.mass)
                column =5
                for i in range(len(jump.peak_force)):
                    worksheet3.write(row3, column,jump.peak_force[i])
                    column+=1
                row3 += 1
    
    workbook.close()


if __name__ =="__main__":
    main()
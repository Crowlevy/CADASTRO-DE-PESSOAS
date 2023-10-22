from openpyxl import Workbook

def exportarExcel(usuarios):
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(["NOME","IDADE","CPF","DATA DE NASCIMENTO","EMAIL"])
        
    for usuario in usuarios:
        sheet.append([usuario.nome,usuario.idade,usuario.cpf,usuario.data,usuario.email])
    workbook.save(filename="usuarios_cadastrados.xlsx")
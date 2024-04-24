from classes import *


lista_categoria = []
lista_desktop = []
lista_notebook = []

id = 1

cat = Categoria("Computador", 0)
lista_categoria.append(cat)

while True:
        try:
            num = int(input("Selecione:\n \n1) Cadastrar categoria \n2) Cadastrar Desktop \n3) Cadastrar Notebook \n4) Alterar Fonte Desktop\n5) Alterar Duração de Bateria Notebook \n6) Imprimir Desktop \n7) Imprimir Notebook \n\n\n"))

        
            if num == 1:
                aux = str(input("\nDigite o nome da categoria a cadastrar.\n"))
                cat = Categoria(aux, id)
                id = id+1
                lista_categoria.append(cat)
                print("Categoria " , aux , " criada e registrada.\n")

            if num == 2:
                aux = str(input("\nDigite o modelo do desktop ou digite 0 para valores padrão.\n"))
                if aux == "0":
                    desk = Desktop("HP", "Preto", 500, lista_categoria[0], "500w")
                    Desktop.cadastrar(desk, lista_desktop)
                    Desktop.getInformacao(desk)

                else:
                    aux2 = str(input("Digite a cor do computador.\n"))
                    aux3 = int(input("Digite o preço do computador.\n"))
                    for i in range(len(lista_categoria)):
                        print("Categoria: ", i,")",lista_categoria[i].id, lista_categoria[i].nome)
                    aux4 = int(input("Selecione a categoria do computador.\n"))
                    aux5 = str(input("Digite a potência da fonte do computador.\n"))
                    desk = Desktop(aux, aux2, aux3, lista_categoria[aux4], aux5)
                    Desktop.cadastrar(desk, lista_desktop)
                    Desktop.getInformacao(desk)


            if num == 3:
                aux = str(input("Digite o modelo do notebook ou digite 0 para valores padrão.\n"))
                if aux == "0":
                    note = Notebook("Dell", "Vermelho", 400, lista_categoria[0], "12h")
                    Notebook.cadastrar(note, lista_notebook)
                    Notebook.getInformacao(note)

                else:
                    aux2 = str(input("Digite a cor do notebook.\n"))
                    aux3 = int(input("Digite o preço do notebook.\n"))
                    for i in range(len(lista_categoria)):
                        print("Categoria: ", i,")", lista_categoria[i].id, lista_categoria[i].nome)
                    aux4 = int(input("Selecione a categoria do notebook.\n"))
                    aux5 = str(input("Digite a duração da bateria do notebook.\n"))
                    note = Notebook(aux, aux2, aux3, lista_categoria[aux4], aux5)
                    Notebook.cadastrar(note, lista_notebook)
                    Notebook.getInformacao(note)

            if num == 4:

                for i in range(len(lista_desktop)):
                    print("ID: ", i+1 , ")\n")
                    Desktop.getInformacao(lista_desktop[i])
                    print("-------------------------------------------------------")
                aux = int(input("\nSelecione o desktop para alterar a fonte, ou 0 para cancelar:\n"))
                if aux == 0:
                    pass
                else:
                    aux2 = str(input("Digite a nova fonte:\n"))
                    Desktop.setFonte(lista_desktop[aux-1], aux2)     

            if num == 5:

                for i in range(len(lista_notebook)):
                    print("ID: ", i+1 , ")\n")
                    Notebook.getInformacao(lista_notebook[i])
                    print("-------------------------------------------------------")
                aux = int(input("\nSelecione o notebook para alterar a bateria, ou 0 para cancelar:\n"))
                if aux == 0:
                    pass
                else:
                    aux2 = str(input("Digite a nova duração da bateria:\n"))
                    Notebook.setBateria(lista_notebook[aux-1], aux2)          

            if num == 7:

                for i in range(len(lista_notebook)):
                    print("ID: ", i+1 , ")\n")
                    Notebook.getInformacao(lista_notebook[i])
                    print("-------------------------------------------------------")

            if num == 6:

                for i in range(len(lista_desktop)):
                    print("ID: ", i+1 , ")\n")
                    Desktop.getInformacao(lista_desktop[i])
                    print("-------------------------------------------------------")

        except:
            print("Valor inválido digitado.")

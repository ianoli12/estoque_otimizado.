import pyodbc
import os
import tableprint as tp
import numpy as np
from prettytable import PrettyTable
from tabulate import tabulate
import pandas as pd
import sqlalchemy as sa
import numpy as np
import functools
from datetime import date


def modulo_est(conn):
    verficador = 2
    while(verficador == 2):
        print("\nMÓDULO DE ESTOQUE\n")

        print("1 - Consultar Produto do Estoque:\n")
        print("2 - Adicionar Produto ao Estoque:\n")
        print("3 - Alterar Produto do Estoque\n")
        print("4 - Excluir Produto\n")
        print("5 - Sair\n")
        op_moduloest = int(input("Digite a opção desejada\n"))

        #FAZ SELECT SIMPLES 
        #def select_tab(conn):
         #    cursor = conn.cursor()
          #   cursor.execute('select * from PRODUTOS')

        def modest_consprod(conn):
            pergunta = "s"
            
            while(pergunta == "s" and "S"):
                print("\nConsulta de Produtos:\n")
                #MOSTRA UM SIMPLES SELECT DA TABELA
                cursor = conn.cursor()
                #cursor.execute('SELECT TOP 10 PRODUCTID,NAME,PRODUCTNUMBER,COLOR,SAFETYSTOCKLEVEL,STANDARDCOST,LISTPRICE from Production.Product')
                #lista = list(cursor.execute('SELECT top 10 PRODUCTID,NAME from Production.Product'))
                df = pd.read_sql('SELECT PRODUCTID,NAME,PRODUCTNUMBER,Makeflag from Production.Product order by PRODUCTID',conn)
                print(df.to_string(index=False))

                #MOSTRA UM  SELECT APENAS DO CÓDIGO MENCIONADO
                CODPROD = int(input("Digite o código do produto: \n"))
                cursor.execute('select PRODUCTID from PRODUCTION.PRODUCT where PRODUCTID=?',CODPROD)
                
                prod_existe = 0
                
                #for x in df:
                #print(df.iloc[df[0],[0]].to_string(index=False))
                #if df['PRODUCTID'].values(CODPROD) == CODPROD:
                #print(np.where(df.index==CODPROD)[0])
                #df = productid.values[CODPROD]
                #print(df.values(1,[CODPROD])
                #if np.where(df.values([[1],[CODPROD]]):
                res = 0
                for x in cursor:
                    res = int(''.join(map(str,x)))
                    print(res)
               # c = df['PRODUCTID']
                #c[[0]]
                #print(int(c.iloc[CODPROD-1]))
                #d = df.convert_dtypes(d)
                #df = pd.DataFrame()
                #if c.iloc[CODPROD-1] == CODPROD:
                if res == CODPROD:
                    print("Dados do Produto:\n")
                    #cursor.execute('select PRODUCTID,NAME,PRODUCTNUMBER,Makeflag from Production.Product where PRODUCTID=?',CODPROD)
                    #d = cursor.fetchone()
                    #df.convert_dtypes(d)
                    print(df.loc[df['PRODUCTID']==res,['PRODUCTID','NAME','PRODUCTNUMBER','Makeflag']].to_string(index=False))
                else:
                    print("Produto não encontrado")
                    #print(df.iloc[CODPROD])
                pergunta = str(input("\nDeseja consultar novamente?(s/n)...\n"))


        

        def modest_addprod(conn):
            pergunta = "s"
            while(pergunta == "s"):
                PRODUCTID = int(input("\nDigite o código do produto a ser incluído: \n"))
                NAME = str(input("\n Novo nome: \n"))
                PRODUCTNUMBER = str(input("\nNova Identificação do Produto(ProductNumer): \n"))
                MAKEFLAG = bool(input("\nDigite a MakeFlag do Produto: \n"))
                FINISHEDGOODSFLAG = bool(input("\nDigite a FINISHEDGOODSFLAG do produto: \n"))
                COLOR = str(input("\n Cor do Produto: \n"))
                SAFETYSTOCKLEVEL = int(input("\nDigite a quantidade segura de estoque: \n"))
                REORDERPOINT = int(input("\nDigite o ponto de reordenação do produto: \n"))
                STANDARDCOST = float(input("\nDigite o preço padrão: \n"))
                LISTPRICE = float(input("\nDigite o valor na lista de preço desse produto: \n"))
                DAYSTOMANUFACTURE = int(input("\nQuantidade de dias para a manufatura do produto: \n"))
                SELLSTARTDATE = str(input("\n Digite a Data Inicial de venda do produto: (Ex:2008-04-30): \n"))

                cursor = conn.cursor()
                cursor.execute('SET IDENTITY_INSERT [Production].[Product] ON;INSERT INTO Production.Product(ProductID,Name,ProductNumber,MakeFlag,FinishedGoodsFlag,Color,SafetyStockLevel,ReorderPoint,StandardCost,ListPrice,DaysToManufacture,SellStartDate) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',PRODUCTID,NAME,PRODUCTNUMBER,MAKEFLAG,FINISHEDGOODSFLAG,COLOR,SAFETYSTOCKLEVEL,REORDERPOINT,STANDARDCOST,LISTPRICE,DAYSTOMANUFACTURE,SELLSTARTDATE)
                conn.commit()
                df2 = pd.read_sql('SELECT ProductID,Name,ProductNumber,MakeFlag,FinishedGoodsFlag,Color,SafetyStockLevel,ReorderPoint,StandardCost,ListPrice,DaysToManufacture,SellStartDate FROM PRODUCTION.PRODUCT ORDER BY PRODUCTID',conn)
                #Abaixo é necessário colocar o nome das colunas EXATAMENTE como está no banco de dados(usando mauísculo ou minusculo)
                print(df2.loc[df2['ProductID']==PRODUCTID,['ProductID','Name','ProductNumber','MakeFlag','FinishedGoodsFlag','Color','SafetyStockLevel','ReorderPoint','StandardCost','ListPrice','DaysToManufacture','SellStartDate']].to_string(index=False))

                pergunta = str(input("\nDeseja INCLUIR o produto novamente?...\n"))


        def modest_altprod(conn): 
            pergunta = "s"
            while(pergunta == "s"):
                PRODUCTID = str(input("\nDigite o código do produto a ser incluído: \n"))
                df2 = pd.read_sql('SELECT ProductID,Name,ProductNumber,MakeFlag,FinishedGoodsFlag,Color,SafetyStockLevel,ReorderPoint,StandardCost,ListPrice,DaysToManufacture,SellStartDate FROM PRODUCTION.PRODUCT ORDER BY PRODUCTID',conn)
                print(df2.loc[df2['ProductID']==PRODUCTID,['ProductID','Name','ProductNumber','MakeFlag','FinishedGoodsFlag','Color','SafetyStockLevel','ReorderPoint','StandardCost','ListPrice','DaysToManufacture','SellStartDate']].to_string(index=False))
                print("\n")

                NAME = str(input("\n Novo nome: \n"))
                PRODUCTNUMBER = str(input("\nNova Identificação do Produto(ProductNumer): \n"))
                MAKEFLAG = bool(input("\nNovo MakeFlag do Produto: \n"))
                FINISHEDGOODSFLAG = bool(input("\nNovo FINISHEDGOODSFLAG do produto: \n"))
                COLOR = str(input("\n Nova Cor do Produto: \n"))
                SAFETYSTOCKLEVEL = int(input("\nNova quantidade segura de estoque: \n"))
                REORDERPOINT = int(input("\nNovo ponto de reordenação do produto: \n"))
                STANDARDCOST = float(input("\nNovo preço padrão: \n"))
                LISTPRICE = float(input("\nNovo valor na lista de preço desse produto: \n"))
                DAYSTOMANUFACTURE = int(input("\nNova quantidade de dias para a manufatura do produto: \n"))
                SELLSTARTDATE = str(input("\n Nova Data Inicial de venda do produto: (Ex:2008-04-30): \n"))

                cursor = conn.cursor()
                #str(PRODUCTID)
                cursor.execute('SET IDENTITY_INSERT [Production].[Product] ON;UPDATE Production.Product SET ProductID=?,Name=?,ProductNumber=?,MakeFlag=?,FinishedGoodsFlag=?,Color=?,SafetyStockLevel=?,ReorderPoint=?,StandardCost=?,ListPrice=?,DaysToManufacture=?,SellStartDate=? WHERE ProductID = ? ',NAME,PRODUCTNUMBER,MAKEFLAG,FINISHEDGOODSFLAG,COLOR,SAFETYSTOCKLEVEL,REORDERPOINT,STANDARDCOST,LISTPRICE,DAYSTOMANUFACTURE,SELLSTARTDATE)
                conn.commit()
                #int(PRODUCTID)
                df2 = pd.read_sql('SELECT ProductID,Name,ProductNumber,MakeFlag,FinishedGoodsFlag,Color,SafetyStockLevel,ReorderPoint,StandardCost,ListPrice,DaysToManufacture,SellStartDate FROM PRODUCTION.PRODUCT ORDER BY PRODUCTID',conn)
                #Abaixo é necessário colocar o nome das colunas EXATAMENTE como está no banco de dados(usando mauísculo ou minusculo)
                print(df2.loc[df2['ProductID']==PRODUCTID,['ProductID','Name','ProductNumber','MakeFlag','FinishedGoodsFlag','Color','SafetyStockLevel','ReorderPoint','StandardCost','ListPrice','DaysToManufacture','SellStartDate']].to_string(index=False))

                pergunta = str(input("\nDeseja ALTERAR o produto novamente?...\n"))     




        def modest_delprod(conn):
            cursor = conn.cursor()
            cursor.execute(
            'delete from PRODUTOS where CODPROD = ?;',
            (2)
            )
            conn.commit()
            select_tab(conn)

        if op_moduloest == 1:
            modest_consprod(conn)
        elif op_moduloest == 2:
            modest_addprod(conn)
        elif op_moduloest == 3:
            modest_altprod(conn)
        elif op_moduloest == 4:
            modest_delprod(conn)
        else:
            print("A opção precisa ser numérica")


def sobre_software():
    print("Este software foi produzido por Ian Oliveira")

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-EK0ORPP;"
    "Database=AdventureWorks2017;"
    "Trusted_Connection=yes;"
)

print("BEM VINDO AO ESTOQUE BRASIL\n\n")

print("1 - Módulo de Estoque: \n")
print("2 - Sobre o software: \n")
op_menuprin = int(input('Digite a opção desejada:'))


if op_menuprin == 1:
    modulo_est(conn)
elif op_menuprin == 2:
    sobre_software()
else:
    print("Digite uma opção válida(numérica):")
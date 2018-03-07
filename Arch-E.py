#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from tkFileDialog import *
import ttk
import Tkinter as tk
import tkMessageBox
#import py2exe
from eppy import modeleditor
from eppy.modeleditor import IDF
from PIL import Image, ImageTk
from openpyxl import *
try:
    # python 2
    from tkFont import Font
except ImportError:
    # python 3
    from tkinter.font import Font
import tkFont

banco_de_dados = load_workbook('banco_de_dados.xlsx')
planilha_bd = banco_de_dados['resultados']


# Notas

nota_final_valor = 0

##################################################

nota_nivel3 = 0

nota_implantacao_ = 0
peso_implantacao_ = float(planilha_bd['B3'].value)
nota_forma_  = 0
peso_forma_ = float(planilha_bd['B8'].value)
nota_relacao_solo_ = 0
peso_relacao_solo_ = float(planilha_bd['B10'].value)

nota_afast_norte_ter_ = 0
nota_afast_norte_sup_ = 0
nota_afast_sul_ter_ = 0
nota_afast_sul_sup_ = 0
nota_afast_leste_ter_ = 0
nota_afast_leste_sup_ = 0
nota_afast_oeste_ter_ = 0
nota_afast_oeste_sup_ = 0

nota_afast_norte_ = 0
peso_afast_norte_ = float(planilha_bd['E34'].value)
nota_afast_sul_ = 0
peso_afast_sul_ = float(planilha_bd['E46'].value)
nota_afast_leste_ = 0
peso_afast_leste_ = float(planilha_bd['E58'].value)
nota_afast_oeste_ = 0
peso_afast_oeste_ = float(planilha_bd['E70'].value)
nota_afastamento_ = 0
peso_afastamento_ = float(planilha_bd['B34'].value)


##################################################

nota_nivel4 = 0

nota_estrutura_ = 0

nota_parede_ = 0
nota_u_parede_ = 0
nota_ct_parede_ = 0
nota_cor_parede_ = 0
nota_composicao_ = 0

nota_cobertura_ = 0
nota_u_cobertura_ = 0
nota_cor_cobertura_ = 0

nota_abertura_ = 0
nota_tipo_abertura_ = 0
nota_vidro_ = 0
nota_estanqueidade_ = 0

nota_iluminacao_ = 0
nota_iluminacao_norte_ = 0
nota_iluminacao_sul_ = 0
nota_iluminacao_leste_ = 0
nota_iluminacao_oeste_ = 0
nota_ventilacao_ = 0
nota_ventilacao_norte_ = 0
nota_ventilacao_sul_ = 0
nota_ventilacao_oeste_ = 0
nota_ventilacao_leste_ = 0

peso_estrutura_ = float(planilha_bd['B84'].value)

peso_parede_ = float(planilha_bd['B90'].value)
peso_composicao_ = float(planilha_bd['E90'].value)
peso_cor_parede_ = float(planilha_bd['E95'].value)

peso_cobertura_ = float(planilha_bd['B98'].value)
peso_u_cobertura_ = float(planilha_bd['E98'].value)
peso_cor_cobertura_ = float(planilha_bd['E101'].value)

peso_abertura_ = float(planilha_bd['B104'].value)
peso_tipo_abertura_ = float(planilha_bd['E104'].value)
peso_vidro_ = float(planilha_bd['E131'].value)
peso_estanqueidade_ = float(planilha_bd['E133'].value)

peso_iluminacao_ = float(planilha_bd['E107'].value)
peso_ventilacao_ = float(planilha_bd['E119'].value)


##################################################

amb_nome_ = ''
amb_contato_solo_ = ''
amb_u_solo_ = ''
amb_ct_solo_= ''
amb_cor_parede_ = ''
amb_orient_parede_ = ''
amb_u_parede_ = ''
amb_ct_parede_ = ''
amb_u_cobertura_ = ''
amb_cor_cobertura_ = ''
amb_tipo_abertura_ = ''
amb_vidro_ = ''
amb_estanqueidade_ = ''
amb_brise_ = ''
amb_iluminacao_norte_ = ''
amb_iluminacao_sul_ = ''
amb_iluminacao_leste_ = ''
amb_iluminacao_oeste_ = ''
amb_ventilacao_norte_ = ''
amb_ventilacao_sul_ = ''
amb_ventilacao_leste_ = ''
amb_iluminacao_oeste_ = '' 


nota_nivel5_amb1 = 0
nota_nivel5_amb2 = 0
nota_nivel5_amb3 = 0
nota_nivel5_amb4 = 0
nota_nivel5_amb5 = 0
nota_nivel5_amb6 = 0
nota_nivel5_amb7 = 0
nota_nivel5_amb8 = 0
nota_nivel5_amb9 = 0
nota_nivel5_amb10 = 0

nota_nivel5 = 0

nota_amb_u_solo_ = 0
nota_amb_ct_solo_ = 0
nota_amb_cor_parede_ = 0
peso_amb_cor_parede_ = planilha_bd['E152'].value
nota_amb_u_parede_ = 0
peso_amb_u_parede_ = planilha_bd['E147'].value
nota_amb_ct_parede_ = 0
peso_amb_ct_parede_ = planilha_bd['E150'].value
nota_amb_orient_parede_ = 0
peso_amb_orient_parede_ = planilha_bd['E155'].value
nota_amb_iluminacao_norte_ = 0
nota_amb_iluminacao_sul_ = 0
nota_amb_iluminacao_leste_ = 0
nota_amb_iluminacao_oeste_ = 0
nota_amb_ventilacao_norte_ = 0
nota_amb_ventilacao_sul_ = 0
nota_amb_ventilacao_leste_ = 0
nota_amb_ventilacao_oeste_ = 0
nota_amb_u_cobertura_ = 0
peso_amb_u_cobertura_ = planilha_bd['E163'].value
nota_amb_cor_cobertura_ = 0
peso_amb_cor_cobertura_ = planilha_bd['E166'].value
nota_amb_vidro_ = 0
peso_amb_vidro_ = planilha_bd['E206'].value
nota_amb_estanqueidade_ = 0
peso_amb_estanqueidade_ = planilha_bd['E208'].value
nota_amb_brise_ = 0
peso_amb_brise_ = planilha_bd['E201'].value
nota_amb_tipo_abertura_ = 0
peso_amb_tipo_abertura_ = planilha_bd['E203'].value

nota_amb_ventilacao_ = 0
peso_amb_ventilacao_ = planilha_bd['E185'].value
nota_amb_iluminacao_ = 0
peso_amb_iluminacao_ = planilha_bd['E169'].value
nota_amb_abertura_ = 0
peso_amb_abertura_ = planilha_bd['B169'].value
nota_amb_cobertura_ = 0
peso_amb_cobertura_ = planilha_bd['B163'].value
nota_amb_parede_ = 0
peso_amb_parede_ = planilha_bd['B147'].value
nota_amb_piso_ = 0
peso_amb_piso_ = planilha_bd['B137'].value

	

def calcula_nota_5():
	num = int(numero_ambientes_.get())
	print type(num)
	global num_atual, count_amb_preench,nota_nivel5, nota_final_valor,nota_nivel5_amb1,nota_nivel5_amb2,nota_nivel5_amb3,nota_nivel5_amb4,nota_nivel5_amb5,nota_nivel5_amb6,nota_nivel5_amb7,nota_nivel5_amb8,nota_nivel5_amb9,nota_nivel5_amb10,amb_nome_,amb_contato_solo_,amb_u_solo_,amb_ct_solo_,amb_cor_parede_,amb_orient_parede_,amb_u_parede_,amb_ct_parede_,amb_u_cobertura_,amb_cor_cobertura_,amb_tipo_abertura_,amb_vidro_,amb_estanqueidade_,amb_brise_,amb_iluminacao_norte_,amb_iluminacao_sul_,amb_iluminacao_leste_,amb_iluminacao_oeste_,amb_ventilacao_norte_,amb_ventilacao_sul_,amb_ventilacao_leste_,amb_iluminacao_oeste_,nota_amb_u_solo_,nota_amb_ct_solo_,nota_amb_cor_parede_,nota_amb_u_parede_,nota_amb_ct_parede_,nota_amb_orient_parede_,nota_amb_iluminacao_norte_,nota_amb_iluminacao_sul_,nota_amb_iluminacao_leste_,nota_amb_iluminacao_oeste_,nota_amb_ventilacao_norte_,nota_amb_ventilacao_sul_,nota_amb_ventilacao_leste_,nota_amb_ventilacao_oeste_,nota_amb_u_cobertura_,nota_amb_cor_cobertura_,nota_amb_vidro_,nota_amb_estanqueidade_,nota_amb_brise_,nota_amb_tipo_abertura_,nota_amb_ventilacao_,nota_amb_iluminacao_,nota_amb_abertura_,nota_amb_cobertura_,nota_amb_parede_,nota_amb_piso_

	if valor_do_ambiente == 1:

		nota_amb1_ventilacao_ = (nota_amb_ventilacao_norte_ * 0.25) + (nota_amb_ventilacao_sul_ * 0.25) + (nota_amb_ventilacao_leste_ * 0.25) + (nota_amb_ventilacao_oeste_ * 0.25)
		nota_amb1_iluminacao_ = (nota_amb_iluminacao_norte_ * 0.25) + (nota_amb_iluminacao_sul_ * 0.25) + (nota_amb_iluminacao_leste_ * 0.25) + (nota_amb_iluminacao_oeste_ * 0.25)

		nota_amb1_abertura_ = (nota_amb1_iluminacao_ * peso_amb_iluminacao_) + (nota_amb1_ventilacao_ * peso_amb_ventilacao_) + (nota_amb_brise_ * peso_amb_brise_) + (nota_amb_vidro_ * peso_amb_vidro_) + (nota_amb_estanqueidade_ * peso_amb_estanqueidade_) + (nota_amb_tipo_abertura_ * peso_amb_tipo_abertura_)

		nota_amb1_cobertura_ = (nota_amb_u_cobertura_ * peso_amb_u_cobertura_) + (nota_amb_cor_cobertura_ * peso_amb_cor_cobertura_)

		nota_amb1_parede_ = (nota_amb_u_parede_ * peso_amb_u_parede_) + (nota_amb_ct_parede_ * peso_amb_ct_parede_) + (nota_amb_cor_parede_ * peso_amb_cor_parede_) + (nota_amb_orient_parede_ * peso_amb_orient_parede_)

		nota_amb1_piso_ = (nota_amb_u_solo_ * 0.5) + (nota_amb_ct_solo_ * 0.5)

		nota_nivel5_amb1 = 0
		nota_nivel5_amb1 = (nota_amb1_piso_ * peso_amb_piso_) + (nota_amb1_parede_ * peso_amb_parede_) + (nota_amb1_cobertura_ * peso_amb_cobertura_) + (nota_amb1_abertura_ * peso_amb_abertura_)

		
		if nota_nivel5_amb1 <= 0.5:
			amb1_path_img1 = "grafico0.png"
			path_img2 = "grafico_p_0.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)
		
		elif nota_nivel5_amb1 > 0.5 and nota_nivel5_amb1 <= 1:
		 	amb1_path_img1 = "grafico1.png"
			path_img2 = "grafico_p_1.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)


		elif nota_nivel5_amb1 > 1 and nota_nivel5_amb1 <= 1.5:
		 	amb1_path_img1 = "grafico2.png"
			path_img2 = "grafico_p_2.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)


		elif nota_nivel5_amb1 > 1.5 and nota_nivel5_amb1 <= 2:
		 	amb1_path_img1 = "grafico3.png"
			path_img2 = "grafico_p_3.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)
	

		elif nota_nivel5_amb1 > 2 and nota_nivel5_amb1 <= 2.5:
		 	amb1_path_img1 = "grafico4.png"
			path_img2 = "grafico_p_4.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)


		elif nota_nivel5_amb1 > 2.5 and nota_nivel5_amb1 <= 3:
		 	amb1_path_img1 = "grafico5.png"
			path_img2 = "grafico_p_5.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)


		elif nota_nivel5_amb1 > 3 and nota_nivel5_amb1 <= 3.5:
		 	amb1_path_img1 = "grafico6.png"
			path_img2 = "grafico_p_6.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)


		elif nota_nivel5_amb1 > 3.5 and nota_nivel5_amb1 <= 4:
		 	amb1_path_img1 = "grafico7.png"
			path_img2 = "grafico_p_7.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)
	

		elif nota_nivel5_amb1 > 4 and nota_nivel5_amb1 <= 4.5:
		 	amb1_path_img1 = "grafico8.png"
			path_img2 = "grafico_p_8.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)


		elif nota_nivel5_amb1 > 4.5 and nota_nivel5_amb1 <= 5:
		 	amb1_path_img1 = "grafico9.png"
			path_img2 = "grafico_p_9.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)


		elif nota_nivel5_amb1 > 5 and nota_nivel5_amb1 <= 5.5:
		 	amb1_path_img1 = "grafico10.png"
			path_img2 = "grafico_p_10.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)


		elif nota_nivel5_amb1 > 5.5 and nota_nivel5_amb1 <= 6:
		 	amb1_path_img1 = "grafico11.png"
			path_img2 = "grafico_p_11.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)


		elif nota_nivel5_amb1 > 6 and nota_nivel5_amb1 <= 6.5:
		 	amb1_path_img1 = "grafico12.png"
			path_img2 = "grafico_p_12.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)
	

		elif nota_nivel5_amb1 > 6.5 and nota_nivel5_amb1 <= 7:
		 	amb1_path_img1 = "grafico13.png"
			path_img2 = "grafico_p_13.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)
						

		elif nota_nivel5_amb1 > 7 and nota_nivel5_amb1 <= 7.5:
		 	amb1_path_img1 = "grafico14.png"
			path_img2 = "grafico_p_14.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)


		elif nota_nivel5_amb1 > 7.5 and nota_nivel5_amb1 <= 8:
		 	amb1_path_img1 = "grafico15.png"
			path_img2 = "grafico_p_15.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)
	

		elif nota_nivel5_amb1 > 8 and nota_nivel5_amb1 <= 8.5:
		 	amb1_path_img1 = "grafico16.png"
			path_img2 = "grafico_p_16.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)

		elif nota_nivel5_amb1 > 8.5:
		 	amb1_path_img1 = "grafico17.png"
			path_img2 = "grafico_p_17.png"
			amb1_img1_nota = ImageTk.PhotoImage(file = amb1_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb1_label = tk.Label(top_amb5,image=amb1_img1_nota, background='white')
			amb1_label.image = amb1_img1_nota
			amb1_label.grid(row=3,sticky = E, padx = 40)
			amb1_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb1_nome_amb.grid(row=8,sticky = W, padx = 40)
			amb1_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb1_label.image = path_img2_nota
			amb1_label.grid(row=9,sticky = W, padx = 40)


	elif valor_do_ambiente == 2:

		nota_amb2_ventilacao_ = (nota_amb_ventilacao_norte_ * 0.25) + (nota_amb_ventilacao_sul_ * 0.25) + (nota_amb_ventilacao_leste_ * 0.25) + (nota_amb_ventilacao_oeste_ * 0.25)
		nota_amb2_iluminacao_ = (nota_amb_iluminacao_norte_ * 0.25) + (nota_amb_iluminacao_sul_ * 0.25) + (nota_amb_iluminacao_leste_ * 0.25) + (nota_amb_iluminacao_oeste_ * 0.25)

		nota_amb2_abertura_ = (nota_amb2_iluminacao_ * peso_amb_iluminacao_) + (nota_amb2_ventilacao_ * peso_amb_ventilacao_) + (nota_amb_brise_ * peso_amb_brise_) + (nota_amb_vidro_ * peso_amb_vidro_) + (nota_amb_estanqueidade_ * peso_amb_estanqueidade_) + (nota_amb_tipo_abertura_ * peso_amb_tipo_abertura_)

		nota_amb2_cobertura_ = (nota_amb_u_cobertura_ * peso_amb_u_cobertura_) + (nota_amb_cor_cobertura_ * peso_amb_cor_cobertura_)

		nota_amb2_parede_ = (nota_amb_u_parede_ * peso_amb_u_parede_) + (nota_amb_ct_parede_ * peso_amb_ct_parede_) + (nota_amb_cor_parede_ * peso_amb_cor_parede_) + (nota_amb_orient_parede_ * peso_amb_orient_parede_)

		nota_amb2_piso_ = (nota_amb_u_solo_ * 0.5) + (nota_amb_ct_solo_ * 0.5)

		nota_nivel5_amb2 = 0
		nota_nivel5_amb2 = (nota_amb2_piso_ * peso_amb_piso_) + (nota_amb2_parede_ * peso_amb_parede_) + (nota_amb2_cobertura_ * peso_amb_cobertura_) + (nota_amb2_abertura_ * peso_amb_abertura_)

		if nota_nivel5_amb2 <= 0.5:
			amb2_path_img1 = "grafico0.png"
			path_img2 = "grafico_p_0.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)

		elif nota_nivel5_amb2 > 0.5 and nota_nivel5_amb2 <= 1:
		 	amb2_path_img1 = "grafico1.png"
			path_img2 = "grafico_p_1.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)
		
		elif nota_nivel5_amb2 > 1 and nota_nivel5_amb2 <= 1.5:
		 	amb2_path_img1 = "grafico2.png"
			path_img2 = "grafico_p_2.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)

		elif nota_nivel5_amb2 > 1.5 and nota_nivel5_amb2 <= 2:
		 	amb2_path_img1 = "grafico3.png"
			path_img2 = "grafico_p_3.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)	

		elif nota_nivel5_amb2 > 2 and nota_nivel5_amb2 <= 2.5:
		 	amb2_path_img1 = "grafico4.png"
			path_img2 = "grafico_p_4.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)

		elif nota_nivel5_amb2 > 2.5 and nota_nivel5_amb2 <= 3:
		 	amb2_path_img1 = "grafico5.png"
			path_img2 = "grafico_p_5.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)

		elif nota_nivel5_amb2 > 3 and nota_nivel5_amb2 <= 3.5:
		 	amb2_path_img1 = "grafico6.png"
			path_img2 = "grafico_p_6.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)

		elif nota_nivel5_amb2 > 3.5 and nota_nivel5_amb2 <= 4:
		 	amb2_path_img1 = "grafico7.png"
			path_img2 = "grafico_p_7.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)

		elif nota_nivel5_amb2 > 4 and nota_nivel5_amb2 <= 4.5:
		 	amb2_path_img1 = "grafico8.png"
			path_img2 = "grafico_p_8.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)

		elif nota_nivel5_amb2 > 4.5 and nota_nivel5_amb2 <= 5:
		 	amb2_path_img1 = "grafico9.png"
			path_img2 = "grafico_p_9.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)

		elif nota_nivel5_amb2 > 5 and nota_nivel5_amb2 <= 5.5:
		 	amb2_path_img1 = "grafico10.png"
			path_img2 = "grafico_p_10.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)

		elif nota_nivel5_amb2 > 5.5 and nota_nivel5_amb2 <= 6:
		 	amb2_path_img1 = "grafico11.png"
			path_img2 = "grafico_p_11.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)

		elif nota_nivel5_amb2 > 6 and nota_nivel5_amb2 <= 6.5:
		 	amb2_path_img1 = "grafico12.png"
			path_img2 = "grafico_p_12.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)	

		elif nota_nivel5_amb2 > 6.5 and nota_nivel5_amb2 <= 7:
		 	amb2_path_img1 = "grafico13.png"
			path_img2 = "grafico_p_13.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)					

		elif nota_nivel5_amb2 > 7 and nota_nivel5_amb2 <= 7.5:
		 	amb2_path_img1 = "grafico14.png"
			path_img2 = "grafico_p_14.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)

		elif nota_nivel5_amb2 > 7.5 and nota_nivel5_amb2 <= 8:
		 	amb2_path_img1 = "grafico15.png"
			path_img2 = "grafico_p_15.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)	

		elif nota_nivel5_amb2 > 8 and nota_nivel5_amb2 <= 8.5:
		 	amb2_path_img1 = "grafico16.png"
			path_img2 = "grafico_p_16.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)	

		elif nota_nivel5_amb2 > 8.5:
		 	amb2_path_img1 = "grafico17.png"
			path_img2 = "grafico_p_17.png"
			amb2_img1_nota = ImageTk.PhotoImage(file = amb2_path_img1)
			path_img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			amb2_label = tk.Label(top_amb5,image=amb2_img1_nota, background='white')
			amb2_label.image = amb2_img1_nota
			amb2_label.grid(row=3,sticky = E, padx = 40)
			amb2_nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			amb2_nome_amb.grid(row=10,sticky = W, padx = 40)
			amb2_label = tk.Label(ambientes,image=path_img2_nota, background='white')
			amb2_label.image = path_img2_nota
			amb2_label.grid(row=11,sticky = W, padx = 40)

	elif valor_do_ambiente == 3:


		nota_amb3_ventilacao_ = (nota_amb_ventilacao_norte_ * 0.25) + (nota_amb_ventilacao_sul_ * 0.25) + (nota_amb_ventilacao_leste_ * 0.25) + (nota_amb_ventilacao_oeste_ * 0.25)
		nota_amb3_iluminacao_ = (nota_amb_iluminacao_norte_ * 0.25) + (nota_amb_iluminacao_sul_ * 0.25) + (nota_amb_iluminacao_leste_ * 0.25) + (nota_amb_iluminacao_oeste_ * 0.25)

		nota_amb3_abertura_ = (nota_amb3_iluminacao_ * peso_amb_iluminacao_) + (nota_amb3_ventilacao_ * peso_amb_ventilacao_) + (nota_amb_brise_ * peso_amb_brise_) + (nota_amb_vidro_ * peso_amb_vidro_) + (nota_amb_estanqueidade_ * peso_amb_estanqueidade_) + (nota_amb_tipo_abertura_ * peso_amb_tipo_abertura_)

		nota_amb3_cobertura_ = (nota_amb_u_cobertura_ * peso_amb_u_cobertura_) + (nota_amb_cor_cobertura_ * peso_amb_cor_cobertura_)

		nota_amb3_parede_ = (nota_amb_u_parede_ * peso_amb_u_parede_) + (nota_amb_ct_parede_ * peso_amb_ct_parede_) + (nota_amb_cor_parede_ * peso_amb_cor_parede_) + (nota_amb_orient_parede_ * peso_amb_orient_parede_)

		nota_amb3_piso_ = (nota_amb_u_solo_ * 0.5) + (nota_amb_ct_solo_ * 0.5)

		nota_nivel5_amb3 = 0
		nota_nivel5_amb3 = (nota_amb3_piso_ * peso_amb_piso_) + (nota_amb3_parede_ * peso_amb_parede_) + (nota_amb3_cobertura_ * peso_amb_cobertura_) + (nota_amb3_abertura_ * peso_amb_abertura_)

		#count_amb_preench = count_amb_preench + 1
		if nota_nivel5_amb3 <= 0.5:
			path_img1 = "grafico0.png"
			path_img2 = "grafico_p_0.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)

		elif nota_nivel5_amb3 > 0.5 and nota_nivel5_amb3 <= 1:
		 	path_img1 = "grafico1.png"
			path_img2 = "grafico_p_1.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)
		
		elif nota_nivel5_amb3 > 1 and nota_nivel5_amb3 <= 1.5:
		 	path_img1 = "grafico2.png"
			path_img2 = "grafico_p_2.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)

		elif nota_nivel5_amb3 > 1.5 and nota_nivel5_amb3 <= 2:
		 	path_img1 = "grafico3.png"
			path_img2 = "grafico_p_3.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)	

		elif nota_nivel5_amb3 > 2 and nota_nivel5_amb3 <= 2.5:
		 	path_img1 = "grafico4.png"
			path_img2 = "grafico_p_4.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)

		elif nota_nivel5_amb3 > 2.5 and nota_nivel5_amb3 <= 3:
		 	path_img1 = "grafico5.png"
			path_img2 = "grafico_p_5.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)

		elif nota_nivel5_amb3 > 3 and nota_nivel5_amb3 <= 3.5:
		 	path_img1 = "grafico6.png"
			path_img2 = "grafico_p_6.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)

		elif nota_nivel5_amb3 > 3.5 and nota_nivel5_amb3 <= 4:
		 	path_img1 = "grafico7.png"
			path_img2 = "grafico_p_7.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)

		elif nota_nivel5_amb3 > 4 and nota_nivel5_amb3 <= 4.5:
		 	path_img1 = "grafico8.png"
			path_img2 = "grafico_p_8.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)

		elif nota_nivel5_amb3 > 4.5 and nota_nivel5_amb3 <= 5:
		 	path_img1 = "grafico9.png"
			path_img2 = "grafico_p_9.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)

		elif nota_nivel5_amb3 > 5 and nota_nivel5_amb3 <= 5.5:
		 	path_img1 = "grafico10.png"
			path_img2 = "grafico_p_10.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)

		elif nota_nivel5_amb3 > 5.5 and nota_nivel5_amb3 <= 6:
		 	path_img1 = "grafico11.png"
			path_img2 = "grafico_p_11.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)

		elif nota_nivel5_amb3 > 6 and nota_nivel5_amb3 <= 6.5:
		 	path_img1 = "grafico12.png"
			path_img2 = "grafico_p_12.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)

		elif nota_nivel5_amb3 > 6.5 and nota_nivel5_amb3 <= 7:
		 	path_img1 = "grafico13.png"
			path_img2 = "grafico_p_13.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)						

		elif nota_nivel5_amb3 > 7 and nota_nivel5_amb3 <= 7.5:
		 	path_img1 = "grafico14.png"
			path_img2 = "grafico_p_14.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)

		elif nota_nivel5_amb3 > 7.5 and nota_nivel5_amb3 <= 8:
		 	path_img1 = "grafico15.png"
			path_img2 = "grafico_p_15.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)

		elif nota_nivel5_amb3 > 8 and nota_nivel5_amb3 <= 8.5:
		 	path_img1 = "grafico16.png"
			path_img2 = "grafico_p_16.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)	

		elif nota_nivel5_amb3 > 8.5:
		 	path_img1 = "grafico17.png"
			path_img2 = "grafico_p_17.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=12,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=13,sticky = W, padx = 40)

	elif valor_do_ambiente == 4:

		nota_amb4_ventilacao_ = (nota_amb_ventilacao_norte_ * 0.25) + (nota_amb_ventilacao_sul_ * 0.25) + (nota_amb_ventilacao_leste_ * 0.25) + (nota_amb_ventilacao_oeste_ * 0.25)
		nota_amb4_iluminacao_ = (nota_amb_iluminacao_norte_ * 0.25) + (nota_amb_iluminacao_sul_ * 0.25) + (nota_amb_iluminacao_leste_ * 0.25) + (nota_amb_iluminacao_oeste_ * 0.25)

		nota_amb4_abertura_ = (nota_amb4_iluminacao_ * peso_amb_iluminacao_) + (nota_amb4_ventilacao_ * peso_amb_ventilacao_) + (nota_amb_brise_ * peso_amb_brise_) + (nota_amb_vidro_ * peso_amb_vidro_) + (nota_amb_estanqueidade_ * peso_amb_estanqueidade_) + (nota_amb_tipo_abertura_ * peso_amb_tipo_abertura_)

		nota_amb4_cobertura_ = (nota_amb_u_cobertura_ * peso_amb_u_cobertura_) + (nota_amb_cor_cobertura_ * peso_amb_cor_cobertura_)

		nota_amb4_parede_ = (nota_amb_u_parede_ * peso_amb_u_parede_) + (nota_amb_ct_parede_ * peso_amb_ct_parede_) + (nota_amb_cor_parede_ * peso_amb_cor_parede_) + (nota_amb_orient_parede_ * peso_amb_orient_parede_)

		nota_amb4_piso_ = (nota_amb_u_solo_ * 0.5) + (nota_amb_ct_solo_ * 0.5)

		nota_nivel5_amb4 = 0
		nota_nivel5_amb4 = (nota_amb4_piso_ * peso_amb_piso_) + (nota_amb4_parede_ * peso_amb_parede_) + (nota_amb4_cobertura_ * peso_amb_cobertura_) + (nota_amb4_abertura_ * peso_amb_abertura_)

		#count_amb_preench = count_amb_preench + 1
		if nota_nivel5_amb4 <= 0.5:
			path_img1 = "grafico0.png"
			path_img2 = "grafico_p_0.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)

		elif nota_nivel5_amb4 > 0.5 and nota_nivel5_amb4 <= 1:
		 	path_img1 = "grafico1.png"
			path_img2 = "grafico_p_1.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)
		
		elif nota_nivel5_amb4 > 1 and nota_nivel5_amb4 <= 1.5:
		 	path_img1 = "grafico2.png"
			path_img2 = "grafico_p_2.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)

		elif nota_nivel5_amb4 > 1.5 and nota_nivel5_amb4 <= 2:
		 	path_img1 = "grafico3.png"
			path_img2 = "grafico_p_3.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)

		elif nota_nivel5_amb4 > 2 and nota_nivel5_amb4 <= 2.5:
		 	path_img1 = "grafico4.png"
			path_img2 = "grafico_p_4.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)

		elif nota_nivel5_amb4 > 2.5 and nota_nivel5_amb4 <= 3:
		 	path_img1 = "grafico5.png"
			path_img2 = "grafico_p_5.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)

		elif nota_nivel5_amb4 > 3 and nota_nivel5_amb4 <= 3.5:
		 	path_img1 = "grafico6.png"
			path_img2 = "grafico_p_6.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)

		elif nota_nivel5_amb4 > 3.5 and nota_nivel5_amb4 <= 4:
		 	path_img1 = "grafico7.png"
			path_img2 = "grafico_p_7.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)	

		elif nota_nivel5_amb4 > 4 and nota_nivel5_amb4 <= 4.5:
		 	path_img1 = "grafico8.png"
			path_img2 = "grafico_p_8.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)

		elif nota_nivel5_amb4 > 4.5 and nota_nivel5_amb4 <= 5:
		 	path_img1 = "grafico9.png"
			path_img2 = "grafico_p_9.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)

		elif nota_nivel5_amb4 > 5 and nota_nivel5_amb4 <= 5.5:
		 	path_img1 = "grafico10.png"
			path_img2 = "grafico_p_10.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)

		elif nota_nivel5_amb4 > 5.5 and nota_nivel5_amb4 <= 6:
		 	path_img1 = "grafico11.png"
			path_img2 = "grafico_p_11.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)

		elif nota_nivel5_amb4 > 6 and nota_nivel5_amb4 <= 6.5:
		 	path_img1 = "grafico12.png"
			path_img2 = "grafico_p_12.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)	

		elif nota_nivel5_amb4 > 6.5 and nota_nivel5_amb4 <= 7:
		 	path_img1 = "grafico13.png"
			path_img2 = "grafico_p_13.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)					

		elif nota_nivel5_amb4 > 7 and nota_nivel5_amb4 <= 7.5:
		 	path_img1 = "grafico14.png"
			path_img2 = "grafico_p_14.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)

		elif nota_nivel5_amb4 > 7.5 and nota_nivel5_amb4 <= 8:
		 	path_img1 = "grafico15.png"
			path_img2 = "grafico_p_15.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)	

		elif nota_nivel5_amb4 > 8 and nota_nivel5_amb4 <= 8.5:
		 	path_img1 = "grafico16.png"
			path_img2 = "grafico_p_16.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)

		elif nota_nivel5_amb4 > 8.5:
		 	path_img1 = "grafico17.png"
			path_img2 = "grafico_p_17.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=14,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=15,sticky = W, padx = 40)

	elif valor_do_ambiente == 5:

		nota_amb5_ventilacao_ = (nota_amb_ventilacao_norte_ * 0.25) + (nota_amb_ventilacao_sul_ * 0.25) + (nota_amb_ventilacao_leste_ * 0.25) + (nota_amb_ventilacao_oeste_ * 0.25)
		nota_amb5_iluminacao_ = (nota_amb_iluminacao_norte_ * 0.25) + (nota_amb_iluminacao_sul_ * 0.25) + (nota_amb_iluminacao_leste_ * 0.25) + (nota_amb_iluminacao_oeste_ * 0.25)

		nota_amb5_abertura_ = (nota_amb5_iluminacao_ * peso_amb_iluminacao_) + (nota_amb5_ventilacao_ * peso_amb_ventilacao_) + (nota_amb_brise_ * peso_amb_brise_) + (nota_amb_vidro_ * peso_amb_vidro_) + (nota_amb_estanqueidade_ * peso_amb_estanqueidade_) + (nota_amb_tipo_abertura_ * peso_amb_tipo_abertura_)

		nota_amb5_cobertura_ = (nota_amb_u_cobertura_ * peso_amb_u_cobertura_) + (nota_amb_cor_cobertura_ * peso_amb_cor_cobertura_)

		nota_amb5_parede_ = (nota_amb_u_parede_ * peso_amb_u_parede_) + (nota_amb_ct_parede_ * peso_amb_ct_parede_) + (nota_amb_cor_parede_ * peso_amb_cor_parede_) + (nota_amb_orient_parede_ * peso_amb_orient_parede_)

		nota_amb5_piso_ = (nota_amb_u_solo_ * 0.5) + (nota_amb_ct_solo_ * 0.5)

		nota_nivel5_amb5 = 0
		nota_nivel5_amb5 = (nota_amb5_piso_ * peso_amb_piso_) + (nota_amb5_parede_ * peso_amb_parede_) + (nota_amb5_cobertura_ * peso_amb_cobertura_) + (nota_amb5_abertura_ * peso_amb_abertura_)

		#count_amb_preench = count_amb_preench + 1
		if nota_nivel5_amb5 <= 0.5:
			path_img1 = "grafico0.png"
			path_img2 = "grafico_p_0.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)

		elif nota_nivel5_amb5 > 0.5 and nota_nivel5_amb5 <= 1:
		 	path_img1 = "grafico1.png"
			path_img2 = "grafico_p_1.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)
		
		elif nota_nivel5_amb5 > 1 and nota_nivel5_amb5 <= 1.5:
		 	path_img1 = "grafico2.png"
			path_img2 = "grafico_p_2.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)

		elif nota_nivel5_amb5 > 1.5 and nota_nivel5_amb5 <= 2:
		 	path_img1 = "grafico3.png"
			path_img2 = "grafico_p_3.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)	

		elif nota_nivel5_amb5 > 2 and nota_nivel5_amb5 <= 2.5:
		 	path_img1 = "grafico4.png"
			path_img2 = "grafico_p_4.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)

		elif nota_nivel5_amb5 > 2.5 and nota_nivel5_amb5 <= 3:
		 	path_img1 = "grafico5.png"
			path_img2 = "grafico_p_5.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)

		elif nota_nivel5_amb5 > 3 and nota_nivel5_amb5 <= 3.5:
		 	path_img1 = "grafico6.png"
			path_img2 = "grafico_p_6.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)

		elif nota_nivel5_amb5 > 3.5 and nota_nivel5_amb5 <= 4:
		 	path_img1 = "grafico7.png"
			path_img2 = "grafico_p_7.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)	

		elif nota_nivel5_amb5 > 4 and nota_nivel5_amb5 <= 4.5:
		 	path_img1 = "grafico8.png"
			path_img2 = "grafico_p_8.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)

		elif nota_nivel5_amb5 > 4.5 and nota_nivel5_amb5 <= 5:
		 	path_img1 = "grafico9.png"
			path_img2 = "grafico_p_9.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)

		elif nota_nivel5_amb5 > 5 and nota_nivel5_amb5 <= 5.5:
		 	path_img1 = "grafico10.png"
			path_img2 = "grafico_p_10.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)

		elif nota_nivel5_amb5 > 5.5 and nota_nivel5_amb5 <= 6:
		 	path_img1 = "grafico11.png"
			path_img2 = "grafico_p_11.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)

		elif nota_nivel5_amb5 > 6 and nota_nivel5_amb5 <= 6.5:
		 	path_img1 = "grafico12.png"
			path_img2 = "grafico_p_12.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)	

		elif nota_nivel5_amb5 > 6.5 and nota_nivel5_amb5 <= 7:
		 	path_img1 = "grafico13.png"
			path_img2 = "grafico_p_13.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)						

		elif nota_nivel5_amb5 > 7 and nota_nivel5_amb5 <= 7.5:
		 	path_img1 = "grafico14.png"
			path_img2 = "grafico_p_14.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)

		elif nota_nivel5_amb5 > 7.5 and nota_nivel5_amb5 <= 8:
		 	path_img1 = "grafico15.png"
			path_img2 = "grafico_p_15.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)	

		elif nota_nivel5_amb5 > 8 and nota_nivel5_amb5 <= 8.5:
		 	path_img1 = "grafico16.png"
			path_img2 = "grafico_p_16.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)	

		elif nota_nivel5_amb5 > 8.5:
		 	path_img1 = "grafico17.png"
			path_img2 = "grafico_p_17.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=16,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=17,sticky = W, padx = 40)

	elif valor_do_ambiente == 6:

		nota_amb6_ventilacao_ = (nota_amb_ventilacao_norte_ * 0.25) + (nota_amb_ventilacao_sul_ * 0.25) + (nota_amb_ventilacao_leste_ * 0.25) + (nota_amb_ventilacao_oeste_ * 0.25)
		nota_amb6_iluminacao_ = (nota_amb_iluminacao_norte_ * 0.25) + (nota_amb_iluminacao_sul_ * 0.25) + (nota_amb_iluminacao_leste_ * 0.25) + (nota_amb_iluminacao_oeste_ * 0.25)

		nota_amb6_abertura_ = (nota_amb6_iluminacao_ * peso_amb_iluminacao_) + (nota_amb6_ventilacao_ * peso_amb_ventilacao_) + (nota_amb_brise_ * peso_amb_brise_) + (nota_amb_vidro_ * peso_amb_vidro_) + (nota_amb_estanqueidade_ * peso_amb_estanqueidade_) + (nota_amb_tipo_abertura_ * peso_amb_tipo_abertura_)

		nota_amb6_cobertura_ = (nota_amb_u_cobertura_ * peso_amb_u_cobertura_) + (nota_amb_cor_cobertura_ * peso_amb_cor_cobertura_)

		nota_amb6_parede_ = (nota_amb_u_parede_ * peso_amb_u_parede_) + (nota_amb_ct_parede_ * peso_amb_ct_parede_) + (nota_amb_cor_parede_ * peso_amb_cor_parede_) + (nota_amb_orient_parede_ * peso_amb_orient_parede_)

		nota_amb6_piso_ = (nota_amb_u_solo_ * 0.5) + (nota_amb_ct_solo_ * 0.5)

		nota_nivel5_amb6 = 0
		nota_nivel5_amb6 = (nota_amb6_piso_ * peso_amb_piso_) + (nota_amb6_parede_ * peso_amb_parede_) + (nota_amb6_cobertura_ * peso_amb_cobertura_) + (nota_amb6_abertura_ * peso_amb_abertura_)

		#count_amb_preench = count_amb_preench + 1
		if nota_nivel5_amb6 <= 0.5:
			path_img1 = "grafico0.png"
			path_img2 = "grafico_p_0.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

		elif nota_nivel5_amb6 > 0.5 and nota_nivel5_amb6 <= 1:
		 	path_img1 = "grafico1.png"
			path_img2 = "grafico_p_1.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)
		
		elif nota_nivel5_amb6 > 1 and nota_nivel5_amb6 <= 1.5:
		 	path_img1 = "grafico2.png"
			path_img2 = "grafico_p_2.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

		elif nota_nivel5_amb6 > 1.5 and nota_nivel5_amb6 <= 2:
		 	path_img1 = "grafico3.png"
			path_img2 = "grafico_p_3.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

		elif nota_nivel5_amb6 > 2 and nota_nivel5_amb6 <= 2.5:
		 	path_img1 = "grafico4.png"
			path_img2 = "grafico_p_4.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

		elif nota_nivel5_amb6 > 2.5 and nota_nivel5_amb6 <= 3:
		 	path_img1 = "grafico5.png"
			path_img2 = "grafico_p_5.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

		elif nota_nivel5_amb6 > 3 and nota_nivel5_amb6 <= 3.5:
		 	path_img1 = "grafico6.png"
			path_img2 = "grafico_p_6.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

		elif nota_nivel5_amb6 > 3.5 and nota_nivel5_amb6 <= 4:
		 	path_img1 = "grafico7.png"
			path_img2 = "grafico_p_7.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

		elif nota_nivel5_amb6 > 4 and nota_nivel5_amb6 <= 4.5:
		 	path_img1 = "grafico8.png"
			path_img2 = "grafico_p_8.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

		elif nota_nivel5_amb6 > 4.5 and nota_nivel5_amb6 <= 5:
		 	path_img1 = "grafico9.png"
			path_img2 = "grafico_p_9.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

		elif nota_nivel5_amb6 > 5 and nota_nivel5_amb6 <= 5.5:
		 	path_img1 = "grafico10.png"
			path_img2 = "grafico_p_10.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

		elif nota_nivel5_amb6 > 5.5 and nota_nivel5_amb6 <= 6:
		 	path_img1 = "grafico11.png"
			path_img2 = "grafico_p_11.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

		elif nota_nivel5_amb6 > 6 and nota_nivel5_amb6 <= 6.5:
		 	path_img1 = "grafico12.png"
			path_img2 = "grafico_p_12.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

		elif nota_nivel5_amb6 > 6.5 and nota_nivel5_amb6 <= 7:
		 	path_img1 = "grafico13.png"
			path_img2 = "grafico_p_13.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)			

		elif nota_nivel5_amb6 > 7 and nota_nivel5_amb6 <= 7.5:
		 	path_img1 = "grafico14.png"
			path_img2 = "grafico_p_14.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

		elif nota_nivel5_amb6 > 7.5 and nota_nivel5_amb6 <= 8:
		 	path_img1 = "grafico15.png"
			path_img2 = "grafico_p_15.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

		elif nota_nivel5_amb6 > 8 and nota_nivel5_amb6 <= 8.5:
		 	path_img1 = "grafico16.png"
			path_img2 = "grafico_p_16.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

		elif nota_nivel5_amb6 > 8.5:
		 	path_img1 = "grafico17.png"
			path_img2 = "grafico_p_17.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=18,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=19,sticky = W, padx = 40)

	elif valor_do_ambiente == 7:

		nota_amb7_ventilacao_ = (nota_amb_ventilacao_norte_ * 0.25) + (nota_amb_ventilacao_sul_ * 0.25) + (nota_amb_ventilacao_leste_ * 0.25) + (nota_amb_ventilacao_oeste_ * 0.25)
		nota_amb7_iluminacao_ = (nota_amb_iluminacao_norte_ * 0.25) + (nota_amb_iluminacao_sul_ * 0.25) + (nota_amb_iluminacao_leste_ * 0.25) + (nota_amb_iluminacao_oeste_ * 0.25)

		nota_amb7_abertura_ = (nota_amb7_iluminacao_ * peso_amb_iluminacao_) + (nota_amb7_ventilacao_ * peso_amb_ventilacao_) + (nota_amb_brise_ * peso_amb_brise_) + (nota_amb_vidro_ * peso_amb_vidro_) + (nota_amb_estanqueidade_ * peso_amb_estanqueidade_) + (nota_amb_tipo_abertura_ * peso_amb_tipo_abertura_)

		nota_amb7_cobertura_ = (nota_amb_u_cobertura_ * peso_amb_u_cobertura_) + (nota_amb_cor_cobertura_ * peso_amb_cor_cobertura_)

		nota_amb7_parede_ = (nota_amb_u_parede_ * peso_amb_u_parede_) + (nota_amb_ct_parede_ * peso_amb_ct_parede_) + (nota_amb_cor_parede_ * peso_amb_cor_parede_) + (nota_amb_orient_parede_ * peso_amb_orient_parede_)

		nota_amb7_piso_ = (nota_amb_u_solo_ * 0.5) + (nota_amb_ct_solo_ * 0.5)

		nota_nivel5_amb7 = 0
		nota_nivel5_amb7 = (nota_amb7_piso_ * peso_amb_piso_) + (nota_amb7_parede_ * peso_amb_parede_) + (nota_amb7_cobertura_ * peso_amb_cobertura_) + (nota_amb7_abertura_ * peso_amb_abertura_)

		#count_amb_preench = count_amb_preench + 1
		if nota_nivel5_amb7 <= 0.5:
			path_img1 = "grafico0.png"
			path_img2 = "grafico_p_0.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)

		elif nota_nivel5_amb7 > 0.5 and nota_nivel5_amb7 <= 1:
		 	path_img1 = "grafico1.png"
			path_img2 = "grafico_p_1.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)
		
		elif nota_nivel5_amb7 > 1 and nota_nivel5_amb7 <= 1.5:
		 	path_img1 = "grafico2.png"
			path_img2 = "grafico_p_2.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)

		elif nota_nivel5_amb7 > 1.5 and nota_nivel5_amb7 <= 2:
		 	path_img1 = "grafico3.png"
			path_img2 = "grafico_p_3.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)

		elif nota_nivel5_amb7 > 2 and nota_nivel5_amb7 <= 2.5:
		 	path_img1 = "grafico4.png"
			path_img2 = "grafico_p_4.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)

		elif nota_nivel5_amb7 > 2.5 and nota_nivel5_amb7 <= 3:
		 	path_img1 = "grafico5.png"
			path_img2 = "grafico_p_5.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)

		elif nota_nivel5_amb7 > 3 and nota_nivel5_amb7 <= 3.5:
		 	path_img1 = "grafico6.png"
			path_img2 = "grafico_p_6.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)

		elif nota_nivel5_amb7 > 3.5 and nota_nivel5_amb7 <= 4:
		 	path_img1 = "grafico7.png"
			path_img2 = "grafico_p_7.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)

		elif nota_nivel5_amb7 > 4 and nota_nivel5_amb7 <= 4.5:
		 	path_img1 = "grafico8.png"
			path_img2 = "grafico_p_8.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)

		elif nota_nivel5_amb7 > 4.5 and nota_nivel5_amb7 <= 5:
		 	path_img1 = "grafico9.png"
			path_img2 = "grafico_p_9.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)

		elif nota_nivel5_amb7 > 5 and nota_nivel5_amb7 <= 5.5:
		 	path_img1 = "grafico10.png"
			path_img2 = "grafico_p_10.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)

		elif nota_nivel5_amb7 > 5.5 and nota_nivel5_amb7 <= 6:
		 	path_img1 = "grafico11.png"
			path_img2 = "grafico_p_11.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)

		elif nota_nivel5_amb7 > 6 and nota_nivel5_amb7 <= 6.5:
		 	path_img1 = "grafico12.png"
			path_img2 = "grafico_p_12.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)

		elif nota_nivel5_amb7 > 6.5 and nota_nivel5_amb7 <= 7:
		 	path_img1 = "grafico13.png"
			path_img2 = "grafico_p_13.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)
		elif nota_nivel5_amb7 > 7 and nota_nivel5_amb7 <= 7.5:
		 	path_img1 = "grafico14.png"
			path_img2 = "grafico_p_14.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)

		elif nota_nivel5_amb7 > 7.5 and nota_nivel5_amb7 <= 8:
		 	path_img1 = "grafico15.png"
			path_img2 = "grafico_p_15.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)

		elif nota_nivel5_amb7 > 8 and nota_nivel5_amb7 <= 8.5:
		 	path_img1 = "grafico16.png"
			path_img2 = "grafico_p_16.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)	

		elif nota_nivel5_amb7 > 8.5:
		 	path_img1 = "grafico17.png"
			path_img2 = "grafico_p_17.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=20,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=21,sticky = W, padx = 40)

	elif valor_do_ambiente == 8:

		nota_amb8_ventilacao_ = (nota_amb_ventilacao_norte_ * 0.25) + (nota_amb_ventilacao_sul_ * 0.25) + (nota_amb_ventilacao_leste_ * 0.25) + (nota_amb_ventilacao_oeste_ * 0.25)
		nota_amb8_iluminacao_ = (nota_amb_iluminacao_norte_ * 0.25) + (nota_amb_iluminacao_sul_ * 0.25) + (nota_amb_iluminacao_leste_ * 0.25) + (nota_amb_iluminacao_oeste_ * 0.25)

		nota_amb8_abertura_ = (nota_amb8_iluminacao_ * peso_amb_iluminacao_) + (nota_amb8_ventilacao_ * peso_amb_ventilacao_) + (nota_amb_brise_ * peso_amb_brise_) + (nota_amb_vidro_ * peso_amb_vidro_) + (nota_amb_estanqueidade_ * peso_amb_estanqueidade_) + (nota_amb_tipo_abertura_ * peso_amb_tipo_abertura_)

		nota_amb8_cobertura_ = (nota_amb_u_cobertura_ * peso_amb_u_cobertura_) + (nota_amb_cor_cobertura_ * peso_amb_cor_cobertura_)

		nota_amb8_parede_ = (nota_amb_u_parede_ * peso_amb_u_parede_) + (nota_amb_ct_parede_ * peso_amb_ct_parede_) + (nota_amb_cor_parede_ * peso_amb_cor_parede_) + (nota_amb_orient_parede_ * peso_amb_orient_parede_)

		nota_amb8_piso_ = (nota_amb_u_solo_ * 0.5) + (nota_amb_ct_solo_ * 0.5)

		nota_nivel5_amb8 = 0
		nota_nivel5_amb8 = (nota_amb8_piso_ * peso_amb_piso_) + (nota_amb8_parede_ * peso_amb_parede_) + (nota_amb8_cobertura_ * peso_amb_cobertura_) + (nota_amb8_abertura_ * peso_amb_abertura_)

		if nota_nivel5_amb8 <= 0.5:
			path_img1 = "grafico0.png"
			path_img2 = "grafico_p_0.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)

		elif nota_nivel5_amb8 > 0.5 and nota_nivel5_amb8 <= 1:
		 	path_img1 = "grafico1.png"
			path_img2 = "grafico_p_1.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)

		elif nota_nivel5_amb8 > 1 and nota_nivel5_amb8 <= 1.5:
		 	path_img1 = "grafico2.png"
			path_img2 = "grafico_p_2.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)

		elif nota_nivel5_amb8 > 1.5 and nota_nivel5_amb8 <= 2:
		 	path_img1 = "grafico3.png"
			path_img2 = "grafico_p_3.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)

		elif nota_nivel5_amb8 > 2 and nota_nivel5_amb8 <= 2.5:
		 	path_img1 = "grafico4.png"
			path_img2 = "grafico_p_4.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)

		elif nota_nivel5_amb8 > 2.5 and nota_nivel5_amb8 <= 3:
		 	path_img1 = "grafico5.png"
			path_img2 = "grafico_p_5.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)

		elif nota_nivel5_amb8 > 3 and nota_nivel5_amb8 <= 3.5:
		 	path_img1 = "grafico6.png"
			path_img2 = "grafico_p_6.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)

		elif nota_nivel5_amb8 > 3.5 and nota_nivel5_amb8 <= 4:
		 	path_img1 = "grafico7.png"
			path_img2 = "grafico_p_7.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)

		elif nota_nivel5_amb8 > 4 and nota_nivel5_amb8 <= 4.5:
		 	path_img1 = "grafico8.png"
			path_img2 = "grafico_p_8.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)

		elif nota_nivel5_amb8 > 4.5 and nota_nivel5_amb8 <= 5:
		 	path_img1 = "grafico9.png"
			path_img2 = "grafico_p_9.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)

		elif nota_nivel5_amb8 > 5 and nota_nivel5_amb8 <= 5.5:
		 	path_img1 = "grafico10.png"
			path_img2 = "grafico_p_10.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)

		elif nota_nivel5_amb8 > 5.5 and nota_nivel5_amb8 <= 6:
		 	path_img1 = "grafico11.png"
			path_img2 = "grafico_p_11.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)

		elif nota_nivel5_amb8 > 6 and nota_nivel5_amb8 <= 6.5:
		 	path_img1 = "grafico12.png"
			path_img2 = "grafico_p_12.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)	

		elif nota_nivel5_amb8 > 6.5 and nota_nivel5_amb8 <= 7:
		 	path_img1 = "grafico13.png"
			path_img2 = "grafico_p_13.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)				

		elif nota_nivel5_amb8 > 7 and nota_nivel5_amb8 <= 7.5:
		 	path_img1 = "grafico14.png"
			path_img2 = "grafico_p_14.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)

		elif nota_nivel5_amb8 > 7.5 and nota_nivel5_amb8 <= 8:
		 	path_img1 = "grafico15.png"
			path_img2 = "grafico_p_15.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)

		elif nota_nivel5_amb8 > 8 and nota_nivel5_amb8 <= 8.5:
		 	path_img1 = "grafico16.png"
			path_img2 = "grafico_p_16.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)	

		elif nota_nivel5_amb8 > 8.5:
		 	path_img1 = "grafico17.png"
			path_img2 = "grafico_p_17.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=22,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=23,sticky = W, padx = 40)

	elif valor_do_ambiente == 9:

		nota_amb9_ventilacao_ = (nota_amb_ventilacao_norte_ * 0.25) + (nota_amb_ventilacao_sul_ * 0.25) + (nota_amb_ventilacao_leste_ * 0.25) + (nota_amb_ventilacao_oeste_ * 0.25)
		nota_amb9_iluminacao_ = (nota_amb_iluminacao_norte_ * 0.25) + (nota_amb_iluminacao_sul_ * 0.25) + (nota_amb_iluminacao_leste_ * 0.25) + (nota_amb_iluminacao_oeste_ * 0.25)

		nota_amb9_abertura_ = (nota_amb9_iluminacao_ * peso_amb_iluminacao_) + (nota_amb9_ventilacao_ * peso_amb_ventilacao_) + (nota_amb_brise_ * peso_amb_brise_) + (nota_amb_vidro_ * peso_amb_vidro_) + (nota_amb_estanqueidade_ * peso_amb_estanqueidade_) + (nota_amb_tipo_abertura_ * peso_amb_tipo_abertura_)

		nota_amb9_cobertura_ = (nota_amb_u_cobertura_ * peso_amb_u_cobertura_) + (nota_amb_cor_cobertura_ * peso_amb_cor_cobertura_)

		nota_amb9_parede_ = (nota_amb_u_parede_ * peso_amb_u_parede_) + (nota_amb_ct_parede_ * peso_amb_ct_parede_) + (nota_amb_cor_parede_ * peso_amb_cor_parede_) + (nota_amb_orient_parede_ * peso_amb_orient_parede_)

		nota_amb9_piso_ = (nota_amb_u_solo_ * 0.5) + (nota_amb_ct_solo_ * 0.5)

		nota_nivel5_amb9 = 0
		nota_nivel5_amb9 = (nota_amb9_piso_ * peso_amb_piso_) + (nota_amb9_parede_ * peso_amb_parede_) + (nota_amb9_cobertura_ * peso_amb_cobertura_) + (nota_amb9_abertura_ * peso_amb_abertura_)

		if nota_nivel5_amb9 <= 0.5:
			path_img1 = "grafico0.png"
			path_img2 = "grafico_p_0.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)

		elif nota_nivel5_amb9 > 0.5 and nota_nivel5_amb9 <= 1:
		 	path_img1 = "grafico1.png"
			path_img2 = "grafico_p_1.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)

		elif nota_nivel5_amb9 > 1 and nota_nivel5_amb9 <= 1.5:
		 	path_img1 = "grafico2.png"
			path_img2 = "grafico_p_2.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)


		elif nota_nivel5_amb9 > 1.5 and nota_nivel5_amb9 <= 2:
		 	path_img1 = "grafico3.png"
			path_img2 = "grafico_p_3.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)

		elif nota_nivel5_amb9 > 2 and nota_nivel5_amb9 <= 2.5:
		 	path_img1 = "grafico4.png"
			path_img2 = "grafico_p_4.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)

		elif nota_nivel5_amb9 > 2.5 and nota_nivel5_amb9 <= 3:
		 	path_img1 = "grafico5.png"
			path_img2 = "grafico_p_5.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)


		elif nota_nivel5_amb9 > 3 and nota_nivel5_amb9 <= 3.5:
		 	path_img1 = "grafico6.png"
			path_img2 = "grafico_p_6.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)


		elif nota_nivel5_amb9 > 3.5 and nota_nivel5_amb9 <= 4:
		 	path_img1 = "grafico7.png"
			path_img2 = "grafico_p_7.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)
	

		elif nota_nivel5_amb9 > 4 and nota_nivel5_amb9 <= 4.5:
		 	path_img1 = "grafico8.png"
			path_img2 = "grafico_p_8.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)


		elif nota_nivel5_amb9 > 4.5 and nota_nivel5_amb9 <= 5:
		 	path_img1 = "grafico9.png"
			path_img2 = "grafico_p_9.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)


		elif nota_nivel5_amb9 > 5 and nota_nivel5_amb9 <= 5.5:
		 	path_img1 = "grafico10.png"
			path_img2 = "grafico_p_10.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)


		elif nota_nivel5_amb9 > 5.5 and nota_nivel5_amb9 <= 6:
		 	path_img1 = "grafico11.png"
			path_img2 = "grafico_p_11.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)

		elif nota_nivel5_amb9 > 6 and nota_nivel5_amb9 <= 6.5:
		 	path_img1 = "grafico12.png"
			path_img2 = "grafico_p_12.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)
	

		elif nota_nivel5_amb9 > 6.5 and nota_nivel5_amb9 <= 7:
		 	path_img1 = "grafico13.png"
			path_img2 = "grafico_p_13.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)
						

		elif nota_nivel5_amb9 > 7 and nota_nivel5_amb9 <= 7.5:
		 	path_img1 = "grafico14.png"
			path_img2 = "grafico_p_14.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)


		elif nota_nivel5_amb9 > 7.5 and nota_nivel5_amb9 <= 8:
		 	path_img1 = "grafico15.png"
			path_img2 = "grafico_p_15.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)
	

		elif nota_nivel5_amb9 > 8 and nota_nivel5_amb9 <= 8.5:
		 	path_img1 = "grafico16.png"
			path_img2 = "grafico_p_16.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)
	

		elif nota_nivel5_amb9 > 8.5:
		 	path_img1 = "grafico17.png"
			path_img2 = "grafico_p_17.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=24,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=25,sticky = W, padx = 40)


	elif valor_do_ambiente == 10:

		nota_amb10_ventilacao_ = (nota_amb_ventilacao_norte_ * 0.25) + (nota_amb_ventilacao_sul_ * 0.25) + (nota_amb_ventilacao_leste_ * 0.25) + (nota_amb_ventilacao_oeste_ * 0.25)
		nota_amb10_iluminacao_ = (nota_amb_iluminacao_norte_ * 0.25) + (nota_amb_iluminacao_sul_ * 0.25) + (nota_amb_iluminacao_leste_ * 0.25) + (nota_amb_iluminacao_oeste_ * 0.25)

		nota_amb10_abertura_ = (nota_amb10_iluminacao_ * peso_amb_iluminacao_) + (nota_amb10_ventilacao_ * peso_amb_ventilacao_) + (nota_amb_brise_ * peso_amb_brise_) + (nota_amb_vidro_ * peso_amb_vidro_) + (nota_amb_estanqueidade_ * peso_amb_estanqueidade_) + (nota_amb_tipo_abertura_ * peso_amb_tipo_abertura_)

		nota_amb10_cobertura_ = (nota_amb_u_cobertura_ * peso_amb_u_cobertura_) + (nota_amb_cor_cobertura_ * peso_amb_cor_cobertura_)

		nota_amb10_parede_ = (nota_amb_u_parede_ * peso_amb_u_parede_) + (nota_amb_ct_parede_ * peso_amb_ct_parede_) + (nota_amb_cor_parede_ * peso_amb_cor_parede_) + (nota_amb_orient_parede_ * peso_amb_orient_parede_)

		nota_amb10_piso_ = (nota_amb_u_solo_ * 0.5) + (nota_amb_ct_solo_ * 0.5)

		nota_nivel5_amb10 = 0
		nota_nivel5_amb10 = (nota_amb10_piso_ * peso_amb_piso_) + (nota_amb10_parede_ * peso_amb_parede_) + (nota_amb10_cobertura_ * peso_amb_cobertura_) + (nota_amb10_abertura_ * peso_amb_abertura_)

		if nota_nivel5_amb10 <= 0.5:
			path_img1 = "grafico0.png"
			path_img2 = "grafico_p_0.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)

		elif nota_nivel5_amb10 > 0.5 and nota_nivel5_amb10 <= 1:
		 	path_img1 = "grafico1.png"
			path_img2 = "grafico_p_1.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)
		
		elif nota_nivel5_amb10 > 1 and nota_nivel5_amb10 <= 1.5:
		 	path_img1 = "grafico2.png"
			path_img2 = "grafico_p_2.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)

		elif nota_nivel5_amb10 > 1.5 and nota_nivel5_amb10 <= 2:
		 	path_img1 = "grafico3.png"
			path_img2 = "grafico_p_3.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)

		elif nota_nivel5_amb10 > 2 and nota_nivel5_amb10 <= 2.5:
		 	path_img1 = "grafico4.png"
			path_img2 = "grafico_p_4.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)

		elif nota_nivel5_amb10 > 2.5 and nota_nivel5_amb10 <= 3:
		 	path_img1 = "grafico5.png"
			path_img2 = "grafico_p_5.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)
		elif nota_nivel5_amb10 > 3 and nota_nivel5_amb10 <= 3.5:
		 	path_img1 = "grafico6.png"
			path_img2 = "grafico_p_6.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)

		elif nota_nivel5_amb10 > 3.5 and nota_nivel5_amb10 <= 4:
		 	path_img1 = "grafico7.png"
			path_img2 = "grafico_p_7.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)

		elif nota_nivel5_amb10 > 4 and nota_nivel5_amb10 <= 4.5:
		 	path_img1 = "grafico8.png"
			path_img2 = "grafico_p_8.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)

		elif nota_nivel5_amb10 > 4.5 and nota_nivel5_amb10 <= 5:
		 	path_img1 = "grafico9.png"
			path_img2 = "grafico_p_9.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)

		elif nota_nivel5_amb10 > 5 and nota_nivel5_amb10 <= 5.5:
		 	path_img1 = "grafico10.png"
			path_img2 = "grafico_p_10.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)

		elif nota_nivel5_amb10 > 5.5 and nota_nivel5_amb10 <= 6:
		 	path_img1 = "grafico11.png"
			path_img2 = "grafico_p_11.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)

		elif nota_nivel5_amb10 > 6 and nota_nivel5_amb10 <= 6.5:
		 	path_img1 = "grafico12.png"
			path_img2 = "grafico_p_12.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)	

		elif nota_nivel5_amb10 > 6.5 and nota_nivel5_amb10 <= 7:
		 	path_img1 = "grafico13.png"
			path_img2 = "grafico_p_13.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)
		elif nota_nivel5_amb10 > 7 and nota_nivel5_amb10 <= 7.5:
		 	path_img1 = "grafico14.png"
			path_img2 = "grafico_p_14.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)

		elif nota_nivel5_amb10 > 7.5 and nota_nivel5_amb10 <= 8:
		 	path_img1 = "grafico15.png"
			path_img2 = "grafico_p_15.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)

		elif nota_nivel5_amb10 > 8 and nota_nivel5_amb10 <= 8.5:
		 	path_img1 = "grafico16.png"
			path_img2 = "grafico_p_16.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)

		elif nota_nivel5_amb10 > 8.5:
		 	path_img1 = "grafico17.png"
			path_img2 = "grafico_p_17.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img2_nota = ImageTk.PhotoImage(file = path_img2)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(top_amb5,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=3,sticky = E, padx = 40)
			nome_amb = tk.Label(ambientes,text=amb_nome_, background='white',font="Arial 8 bold",fg='#545454')
			nome_amb.grid(row=26,sticky = W, padx = 40)
			label = tk.Label(ambientes,image=img2_nota, background='white')
			label.image = img2_nota
			label.grid(row=27,sticky = W, padx = 40)

	if num == 1:
		nota_nivel5 = nota_nivel5_amb1
		nota_final_valor = (nota_nivel3+nota_nivel4+nota_nivel5)/(num+2)
	elif num == 2:
		nota_nivel5 = (nota_nivel5_amb1 + nota_nivel5_amb2)/2
		nota_final_valor = (nota_nivel3+nota_nivel4+nota_nivel5_amb1+nota_nivel5_amb2)/(num+2)
	elif num == 3:
		nota_nivel5 = (nota_nivel5_amb1 + nota_nivel5_amb2 + nota_nivel5_amb3)/3
		nota_final_valor = (nota_nivel3+nota_nivel4+nota_nivel5_amb1+nota_nivel5_amb2+ nota_nivel5_amb3)/(num+2)
	elif num == 4:
		nota_nivel5 = (nota_nivel5_amb1 + nota_nivel5_amb2 + nota_nivel5_amb3 + nota_nivel5_amb4)/4
		nota_final_valor = (nota_nivel3+nota_nivel4+nota_nivel5_amb1+nota_nivel5_amb2 + nota_nivel5_amb3+ nota_nivel5_amb4)/(num+2)
	elif num == 5:
		nota_nivel5 = (nota_nivel5_amb1 + nota_nivel5_amb2 + nota_nivel5_amb3 + nota_nivel5_amb4 + nota_nivel5_amb5)/5		
		nota_final_valor = (nota_nivel3+nota_nivel4+nota_nivel5_amb1+nota_nivel5_amb2 + nota_nivel5_amb3+ nota_nivel5_amb4+ nota_nivel5_amb5)/(num+2)
	elif num == 6:
		nota_nivel5 = (nota_nivel5_amb1 + nota_nivel5_amb2 + nota_nivel5_amb3 + nota_nivel5_amb4 + nota_nivel5_amb5 + nota_nivel5_amb6)/6
		nota_final_valor = (nota_nivel3+nota_nivel4+nota_nivel5_amb1+nota_nivel5_amb2 + nota_nivel5_amb3+ nota_nivel5_amb4 + nota_nivel5_amb5 + nota_nivel5_amb6)/(num+2)
	elif num == 7:
		nota_nivel5 = (nota_nivel5_amb1 + nota_nivel5_amb2 + nota_nivel5_amb3 + nota_nivel5_amb4 + nota_nivel5_amb5 + nota_nivel5_amb6 + nota_nivel5_amb7)/7
		nota_final_valor = (nota_nivel3+nota_nivel4+nota_nivel5_amb1+nota_nivel5_amb2 + nota_nivel5_amb3+ nota_nivel5_amb4 + nota_nivel5_amb5 + nota_nivel5_amb6 + nota_nivel5_amb7)/(num+2)
	elif num == 8:
		nota_nivel5 = (nota_nivel5_amb1 + nota_nivel5_amb2 + nota_nivel5_amb3 + nota_nivel5_amb4 + nota_nivel5_amb5 + nota_nivel5_amb6 + nota_nivel5_amb7 + nota_nivel5_amb8)/8
		nota_final_valor = (nota_nivel3+nota_nivel4+nota_nivel5_amb1+nota_nivel5_amb2 + nota_nivel5_amb3+ nota_nivel5_amb4 + nota_nivel5_amb5 + nota_nivel5_amb6 + nota_nivel5_amb7 + nota_nivel5_amb8)/(num+2)
	elif num == 9:
		nota_nivel5 = (nota_nivel5_amb1 + nota_nivel5_amb2 + nota_nivel5_amb3 + nota_nivel5_amb4 + nota_nivel5_amb5 + nota_nivel5_amb6 + nota_nivel5_amb7 + nota_nivel5_amb8 + nota_nivel5_amb9)/9		
		nota_final_valor = (nota_nivel3+nota_nivel4+nota_nivel5_amb1+nota_nivel5_amb2 + nota_nivel5_amb3+ nota_nivel5_amb4 + nota_nivel5_amb5 + nota_nivel5_amb6 + nota_nivel5_amb7 + nota_nivel5_amb8 + nota_nivel5_amb9)/(num+2)
	elif num == 10:	
		nota_nivel5 = (nota_nivel5_amb1 + nota_nivel5_amb2 + nota_nivel5_amb3 + nota_nivel5_amb4 + nota_nivel5_amb5 + nota_nivel5_amb6 + nota_nivel5_amb7 + nota_nivel5_amb8 + nota_nivel5_amb9 + nota_nivel5_amb10)/10		
		nota_final_valor = (nota_nivel3+nota_nivel4+nota_nivel5_amb1+nota_nivel5_amb2 + nota_nivel5_amb3+ nota_nivel5_amb4 + nota_nivel5_amb5 + nota_nivel5_amb6 + nota_nivel5_amb7 + nota_nivel5_amb8 + nota_nivel5_amb9 + nota_nivel5_amb10)/(num+2)
	
	if nota_nivel5 <= 0.5:
			path_img1 = "grafico0.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)
	elif nota_nivel5 > 0.5 and nota_nivel5 <= 1:
		 	path_img1 = "grafico1.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)
		
	elif nota_nivel5 > 1 and nota_nivel5 <= 1.5:
		 	path_img1 = "grafico2.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)

	elif nota_nivel5 > 1.5 and nota_nivel5 <= 2:
		 	path_img1 = "grafico3.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)

	elif nota_nivel5 > 2 and nota_nivel5 <= 2.5:
		 	path_img1 = "grafico4.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)

	elif nota_nivel5 > 2.5 and nota_nivel5 <= 3:
			path_img1 = "grafico5.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)

	elif nota_nivel5 > 3 and nota_nivel5 <= 3.5:
			path_img1 = "grafico6.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)


	elif nota_nivel5 > 3.5 and nota_nivel5 <= 4:
			path_img1 = "grafico7.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)

	elif nota_nivel5 > 4 and nota_nivel5 <= 4.5:
			path_img1 = "grafico8.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)


	elif nota_nivel5 > 4.5 and nota_nivel5 <= 5:
			path_img1 = "grafico9.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)

	elif nota_nivel5 > 5 and nota_nivel5 <= 5.5:
			path_img1 = "grafico10.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)

	elif nota_nivel5 > 5.5 and nota_nivel5 <= 6:
			path_img1 = "grafico11.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)


	elif nota_nivel5 > 6 and nota_nivel5 <= 6.5:
			path_img1 = "grafico12.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)

	elif nota_nivel5 > 6.5 and nota_nivel5 <= 7:
			path_img1 = "grafico13.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)
				

	elif nota_nivel5 > 7 and nota_nivel5 <= 7.5:
			path_img1 = "grafico14.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)


	elif nota_nivel5 > 7.5 and nota_nivel5 <= 8:
			path_img1 = "grafico15.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)


	elif nota_nivel5 > 8 and nota_nivel5 <= 8.5:
			path_img1 = "grafico16.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)


	elif nota_nivel5 > 8.5:
			path_img1 = "grafico17.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			label = tk.Label(ambientes,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=2,  sticky=E,padx=40)

# NOTA FINAL

	if nota_final_valor <= 0.5:
			path_img1 = "grafico_g_0.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 0.5 and nota_final_valor <= 1:
		 	path_img1 = "grafico_g_1.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)
		
	elif nota_final_valor > 1 and nota_final_valor <= 1.5:
		 	path_img1 = "grafico_g_2.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 1.5 and nota_final_valor <= 2:
		 	path_img1 = "grafico_g_3.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 2 and nota_final_valor <= 2.5:
		 	path_img1 = "grafico_g_4.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 2.5 and nota_final_valor <= 3:
			path_img1 = "grafico_g_5.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 3 and nota_final_valor <= 3.5:
			path_img1 = "grafico_g_6.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 3.5 and nota_final_valor <= 4:
			path_img1 = "grafico_g_7.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 4 and nota_final_valor <= 4.5:
			path_img1 = "grafico_g_8.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 4.5 and nota_final_valor <= 5:
			path_img1 = "grafico_g_9.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 5 and nota_final_valor <= 5.5:
			path_img1 = "grafico_g_10.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 5.5 and nota_final_valor <= 6:
			path_img1 = "grafico_g_11.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 6 and nota_final_valor <= 6.5:
			path_img1 = "grafico_g_12.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 6.5 and nota_final_valor <= 7:
			path_img1 = "grafico_g_13.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 7 and nota_final_valor <= 7.5:
			path_img1 = "grafico_g_14.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 7.5 and nota_final_valor <= 8:
			path_img1 = "grafico_g_15.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 8 and nota_final_valor <= 8.5:
			path_img1 = "grafico_g_16.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	elif nota_final_valor > 8.5:
			path_img1 = "grafico_g_17.png"
			img1_nota = ImageTk.PhotoImage(file = path_img1)
			#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
			label = tk.Label(nota_final,image=img1_nota, background='white')
			label.image = img1_nota
			label.grid(row=7,sticky=S,padx=80)

	print "nota amb u solo: %f" % nota_amb_u_solo_
	print "nota amb ct solo: %f" % nota_amb_ct_solo_
	print  "Nota amb u parede: %f" % nota_amb_u_parede_
	print "Nota amb ct parede: %f" % nota_amb_ct_parede_
	print "Nota amb cor parede: %f" % nota_amb_cor_parede_
	print "Nota amb orient parede: %f" % nota_amb_orient_parede_
	print "Nota amb u cobertura: %f" % nota_amb_u_cobertura_
	print "Nota amb cor cobertura: %f" % nota_amb_cor_cobertura_

	print "Tipo amb abertura: %f" % nota_amb_tipo_abertura_
	print "amb Vidro: %f"% nota_amb_vidro_
	print "amb Estanqueidade: %f"% nota_amb_estanqueidade_
	print "amb brise: %f"% nota_amb_brise_
	
	print "Nota amb_iluminacao norte: %f" % nota_amb_iluminacao_norte_
	print "Nota amb_iluminacao sul: %f" % nota_amb_iluminacao_sul_
	print "Nota amb_iluminacao leste: %f" % nota_amb_iluminacao_leste_
	print "Nota amb_iluminacao oeste: %f" % nota_amb_iluminacao_oeste_

	print "Nota amb_ventilacao norte: %f" % nota_amb_ventilacao_norte_
	print "Nota amb_ventilacao sul: %f" % nota_amb_ventilacao_sul_
	print "Nota amb_ventilacao leste: %f" % nota_amb_ventilacao_leste_
	print "Nota amb_ventilacao oeste: %f" % nota_amb_ventilacao_oeste_

	print "\n\n"

	print  "peso amb u parede: %f" % peso_amb_u_parede_
	print "peso amb ct parede: %f" % peso_amb_ct_parede_
	print "peso amb cor parede: %f" % peso_amb_cor_parede_
	print "peso amb orient parede: %f" % peso_amb_orient_parede_
	print "peso amb u cobertura: %f" % peso_amb_u_cobertura_
	print "peso amb cor cobertura: %f" % peso_amb_cor_cobertura_

	print "peso Tipo amb abertura: %f" % peso_amb_tipo_abertura_
	print "peso amb Vidro: %f"% peso_amb_vidro_
	print "peso amb Estanqueidade: %f"% peso_amb_estanqueidade_
	print "peso amb brise: %f"% peso_amb_brise_
	

	print "\n\n"

	print "nota amb ventilacao: %f" % nota_amb_ventilacao_
	print "peso ventilacao: %f" % peso_amb_ventilacao_
	print "nota amb iluminacao %f" % nota_amb_iluminacao_
	print "peso iluminacao: %f" % peso_amb_iluminacao_
	print "nota amb abertura: %f" % nota_amb_abertura_
	print "peso amb abertura: %f" % peso_amb_abertura_
	print "nota amb cobertura: %f" % nota_amb_cobertura_
	print "peso amb cobertura: %f" % peso_amb_cobertura_
	print "nota amb parede: %f" % nota_amb_parede_
	print "peso amb parede: %f" % peso_amb_parede_
	print "nota amb piso: %f" % nota_amb_piso_
	print "peso amb piso: %f" % peso_amb_piso_

	print "Nota nivel 5 amb1: %f\n" % nota_nivel5_amb1
	print "Nota Nivel 5 amb2: %f\n" % nota_nivel5_amb2
	print "Nota nivel 5 amb3: %f\n" % nota_nivel5_amb3
	print "Nota nivel 5 amb4: %f\n" % nota_nivel5_amb4
	print "Nota Nivel 5 amb5: %f\n" % nota_nivel5_amb5
	print "Nota nivel 5 amb6: %f\n" % nota_nivel5_amb6
	print "Nota nivel 5 amb7: %f\n" % nota_nivel5_amb7
	print "Nota nivel 5 amb8: %f\n" % nota_nivel5_amb8
	print "Nota Nivel 5 amb9: %f\n" % nota_nivel5_amb9
	print "Nota nivel 5 amb10: %f\n" % nota_nivel5_amb10
	print "Nota nível 5: %f\n" %nota_nivel5
	print "Nota final: %f\n"%nota_final_valor
	print "\n\n"		
	return		
	#top_amb5.quit()
ok_cont = 0
top_relacao_solo = ''
top_afastamento = ''
top_forma_geral = ''
top_implantacao = ''

def ok_top_amb5():
	top_amb5.destroy()
	return
def ok_top_relacao_solo():
	top_relacao_solo.destroy()
	return
def ok_top_implantacao():
	top_implantacao.destroy()
	return
def ok_top_afastamento():
	top_afastamento.destroy()
	return
def ok_top_forma_geral():
	top_forma_geral.destroy()
	return			

def nota_amb_u_solo(event):
	global nota_amb_u_solo_
	valor_amb_u_solo = amb_u_solo_.get()
	valor_amb_contato_solo = amb_contato_solo_.get()
	if 'Sim' == valor_amb_contato_solo.encode('utf-8') and 'U < 1,5' == valor_amb_u_solo.encode('utf-8'):
		nota_amb_u_solo_ = planilha_bd['J137'].value
		calcula_nota_5()
		return
	if 'Sim' == valor_amb_contato_solo.encode('utf-8') and '1,5 < U < 2,0' == valor_amb_u_solo.encode('utf-8'):
		nota_amb_u_solo_ = planilha_bd['J138'].value
		calcula_nota_5()
		return
	if 'Sim' == valor_amb_contato_solo.encode('utf-8') and 'U > 2,0' == valor_amb_u_solo.encode('utf-8'):
		nota_amb_u_solo_ = planilha_bd['J139'].value
		calcula_nota_5()
		return	
	if 'Não' == valor_amb_contato_solo.encode('utf-8') and 'U < 1,5' == valor_amb_u_solo.encode('utf-8'):
		nota_amb_u_solo_ = planilha_bd['J142'].value
		calcula_nota_5()
		return
	if 'Não' == valor_amb_contato_solo.encode('utf-8') and '1,5 < U < 2,0' == valor_amb_u_solo.encode('utf-8'):
		nota_amb_u_solo_ = planilha_bd['J143'].value
		calcula_nota_5()
		return	
	if 'Não' == valor_amb_contato_solo.encode('utf-8') and 'U > 2,0' == valor_amb_u_solo.encode('utf-8'):
		nota_amb_u_solo_ = planilha_bd['J144'].value
		calcula_nota_5()
		return

def nota_amb_ct_solo(event):
	global nota_amb_ct_solo_
	valor_amb_ct_solo = amb_ct_solo_.get()
	valor_amb_contato_solo = amb_contato_solo_.get()
	if 'Sim' == valor_amb_contato_solo.encode('utf-8') and 'CT < 130' == valor_amb_ct_solo.encode('utf-8'):
		nota_amb_ct_solo_ = planilha_bd['J140'].value
		calcula_nota_5()
		return
	if 'Sim' == valor_amb_contato_solo.encode('utf-8') and 'CT > 130' == valor_amb_ct_solo.encode('utf-8'):
		nota_amb_ct_solo_ = planilha_bd['J141'].value
		calcula_nota_5()
		return		
	if 'Não' == valor_amb_contato_solo.encode('utf-8') and 'CT < 130' == valor_amb_ct_solo.encode('utf-8'):
		nota_amb_ct_solo_ = planilha_bd['J145'].value
		calcula_nota_5()
		return
	if 'Não' == valor_amb_contato_solo.encode('utf-8') and 'CT > 130' == valor_amb_ct_solo.encode('utf-8'):
		nota_amb_ct_solo_ = planilha_bd['J146'].value
		calcula_nota_5()
		return		

def nota_amb_u_parede(event):
	global nota_amb_u_parede_
	valor_nota_amb_u_parede = amb_u_parede_.get()
	if 'U < 1,5' in valor_nota_amb_u_parede.encode('utf-8'):
		nota_amb_u_parede_ = planilha_bd['J147'].value
		calcula_nota_5()
		return
	if '1,5 < U < 2,0' in valor_nota_amb_u_parede.encode('utf-8'):
		nota_amb_u_parede_ = planilha_bd['J148'].value
		calcula_nota_5()
		return
	if 'U > 2,0' in valor_nota_amb_u_parede.encode('utf-8'):
		nota_amb_u_parede_ = planilha_bd['J149'].value
		calcula_nota_5()
		return

def nota_amb_ct_parede(event):
	global nota_amb_ct_parede_
	valor_nota_amb_ct_parede = amb_ct_parede_.get()
	if 'CT < 130' in valor_nota_amb_ct_parede.encode('utf-8'):
		nota_amb_ct_parede_ = planilha_bd['J150'].value
		calcula_nota_5()
		return
	if 'CT > 130' in valor_nota_amb_ct_parede.encode('utf-8'):
		nota_amb_ct_parede_ = planilha_bd['J151'].value
		calcula_nota_5()
		return					


def nota_amb_cor_parede(event):
	global nota_amb_cor_parede_
	valor_nota_amb_cor_parede = amb_cor_parede_.get()
	if 'Tons claros (α<0,4)' in valor_nota_amb_cor_parede.encode('utf-8'):
		nota_amb_cor_parede_ = planilha_bd['J152'].value
		calcula_nota_5()
		return
	if 'Tons médios (0,4<α<0,7)' in valor_nota_amb_cor_parede.encode('utf-8'):
		nota_amb_cor_parede_ = planilha_bd['J153'].value
		calcula_nota_5()
		return
	if 'Tons escuros (α>0,7)' in valor_nota_amb_cor_parede.encode('utf-8'):
		nota_amb_cor_parede_ = planilha_bd['J154'].value	
		calcula_nota_5()
		return

def nota_amb_orient_parede(event):
	global nota_amb_orient_parede_
	valor_nota_amb_orient_parede = amb_orient_parede_.get()
	if 'Norte' in valor_nota_amb_orient_parede.encode('utf-8'):
		nota_amb_orient_parede_ = planilha_bd['J155'].value
		calcula_nota_5()
		return
	if 'Nordeste' in valor_nota_amb_orient_parede.encode('utf-8'):
		nota_amb_orient_parede_ = planilha_bd['J156'].value
		calcula_nota_5()
		return
	if 'Leste' in valor_nota_amb_orient_parede.encode('utf-8'):
		nota_amb_orient_parede_ = planilha_bd['J157'].value
		calcula_nota_5()
		return
	if 'Sudeste' in valor_nota_amb_orient_parede.encode('utf-8'):
		nota_amb_orient_parede_ = planilha_bd['J158'].value
		calcula_nota_5()
		return
	if 'Sul' in valor_nota_amb_orient_parede.encode('utf-8'):
		nota_amb_orient_parede_ = planilha_bd['J159'].value
		calcula_nota_5()
		return
	if 'Sudoeste' in valor_nota_amb_orient_parede.encode('utf-8'):
		nota_amb_orient_parede_ = planilha_bd['J160'].value
		calcula_nota_5()
		return
	if 'Oeste' in valor_nota_amb_orient_parede.encode('utf-8'):
		nota_amb_orient_parede_ = planilha_bd['J161'].value
		calcula_nota_5()
		return
	if 'Noroeste' in valor_nota_amb_orient_parede.encode('utf-8'):
		nota_amb_orient_parede_ = planilha_bd['J162'].value
		calcula_nota_5()
		return		


def nota_amb_u_cobertura(event):
	global nota_amb_u_cobertura_
	valor_nota_amb_u_cobertura = amb_u_cobertura_.get()
	if 'U < 1,5' in valor_nota_amb_u_cobertura.encode('utf-8'):
		nota_amb_u_cobertura_ = planilha_bd['J163'].value
		calcula_nota_5()
		return	
	if '1,5 < U < 2,0' in valor_nota_amb_u_cobertura.encode('utf-8'):
		nota_amb_u_cobertura_ = planilha_bd['J164'].value
		calcula_nota_5()
		return	
	if 'U > 2,0' in valor_nota_amb_u_cobertura.encode('utf-8'):
		nota_amb_u_cobertura_ = planilha_bd['J165'].value
		calcula_nota_5()
		return	
def nota_amb_cor_cobertura(event):
	global nota_amb_cor_cobertura_
	valor_nota_amb_cor_cobertura = amb_cor_cobertura_.get()
	if 'Tons claros (α<0,4)' in valor_nota_amb_cor_cobertura.encode('utf-8'):
		nota_amb_cor_cobertura_ = planilha_bd['J166'].value
		calcula_nota_5()
		return	
	if 'Tons médios (0,4<α<0,7)' in valor_nota_amb_cor_cobertura.encode('utf-8'):
		nota_amb_cor_cobertura_ = planilha_bd['J167'].value
		calcula_nota_5()
		return	
	if 'Tons escuros (α>0,7)' in valor_nota_amb_cor_cobertura.encode('utf-8'):
		nota_amb_cor_cobertura_ = planilha_bd['J168'].value
		calcula_nota_5()
		return

def nota_amb_iluminacao_norte(event):
	global nota_amb_iluminacao_norte_
	valor_amb_iluminacao_norte = amb_iluminacao_norte_.get()
	if '< 20%' in valor_amb_iluminacao_norte.encode('utf-8'):
		nota_amb_iluminacao_norte_ = planilha_bd['J169'].value
		calcula_nota_5()
		return	
	if '20 - 50%' in valor_amb_iluminacao_norte.encode('utf-8'):
		nota_amb_iluminacao_norte_ = planilha_bd['J170'].value
		calcula_nota_5()
		return	
	if '50 - 80%' in valor_amb_iluminacao_norte.encode('utf-8'):
		nota_amb_iluminacao_norte_ = planilha_bd['J171'].value
		calcula_nota_5()
		return	
	if '> 80%' in valor_amb_iluminacao_norte.encode('utf-8'):
		nota_amb_iluminacao_norte_ = planilha_bd['J172'].value
		calcula_nota_5()
		return	

def nota_amb_iluminacao_sul(event):
	global nota_amb_iluminacao_sul_
	valor_amb_iluminacao_sul = amb_iluminacao_sul_.get()
	if '< 20%' in valor_amb_iluminacao_sul.encode('utf-8'):
		nota_amb_iluminacao_sul_ = planilha_bd['J173'].value
		calcula_nota_5()
		return	
	if '20 - 50%' in valor_amb_iluminacao_sul.encode('utf-8'):
		nota_amb_iluminacao_sul_ = planilha_bd['J174'].value
		calcula_nota_5()
		return	
	if '50 - 80%' in valor_amb_iluminacao_sul.encode('utf-8'):
		nota_amb_iluminacao_sul_ = planilha_bd['J175'].value
		calcula_nota_5()
		return	
	if '> 80%' in valor_amb_iluminacao_sul.encode('utf-8'):
		nota_amb_iluminacao_sul_ = planilha_bd['J176'].value	
		calcula_nota_5()
		return	

def nota_amb_iluminacao_leste(event):
	global nota_amb_iluminacao_leste_
	valor_amb_iluminacao_leste = amb_iluminacao_leste_.get()
	if '< 20%' in valor_amb_iluminacao_leste.encode('utf-8'):
		nota_amb_iluminacao_leste_ = planilha_bd['J177'].value
		calcula_nota_5()
		return	
	if '20 - 50%' in valor_amb_iluminacao_leste.encode('utf-8'):
		nota_amb_iluminacao_leste_ = planilha_bd['J178'].value
		calcula_nota_5()
		return	
	if '50 - 80%' in valor_amb_iluminacao_leste.encode('utf-8'):
		nota_amb_iluminacao_leste_ = planilha_bd['J179'].value
		calcula_nota_5()
		return	
	if '> 80%' in valor_amb_iluminacao_leste.encode('utf-8'):
		nota_amb_iluminacao_leste_ = planilha_bd['J180'].value
		calcula_nota_5()
		return		

def nota_amb_iluminacao_oeste(event):
	global nota_amb_iluminacao_oeste_
	valor_amb_iluminacao_oeste = amb_iluminacao_oeste_.get()
	if '< 20%' in valor_amb_iluminacao_oeste.encode('utf-8'):
		nota_amb_iluminacao_oeste_ = planilha_bd['J181'].value
		calcula_nota_5()
		return	
	if '20 - 50%' in valor_amb_iluminacao_oeste.encode('utf-8'):
		nota_amb_iluminacao_oeste_ = planilha_bd['J182'].value
		calcula_nota_5()
		return	
	if '50 - 80%' in valor_amb_iluminacao_oeste.encode('utf-8'):
		nota_amb_iluminacao_oeste_ = planilha_bd['J183'].value
		calcula_nota_5()
		return	
	if '> 80%' in valor_amb_iluminacao_oeste.encode('utf-8'):
		nota_amb_iluminacao_oeste_ = planilha_bd['J184'].value
		calcula_nota_5()
		return	

def nota_amb_ventilacao_norte(event):
	global nota_amb_ventilacao_norte_
	valor_amb_ventilacao_norte = amb_ventilacao_norte_.get()
	if '< 20%' in valor_amb_ventilacao_norte.encode('utf-8'):
		nota_amb_ventilacao_norte_ = planilha_bd['J185'].value
		calcula_nota_5()
		return	
	if '20 - 50%' in valor_amb_ventilacao_norte.encode('utf-8'):
		nota_amb_ventilacao_norte_ = planilha_bd['J186'].value
		calcula_nota_5()
		return	
	if '50 - 80%' in valor_amb_ventilacao_norte.encode('utf-8'):
		nota_amb_ventilacao_norte_ = planilha_bd['J187'].value
		calcula_nota_5()
		return	
	if '> 80%' in valor_amb_ventilacao_norte.encode('utf-8'):
		nota_amb_ventilacao_norte_ = planilha_bd['J188'].value
		calcula_nota_5()
		return	

def nota_amb_ventilacao_sul(event):
	global nota_amb_ventilacao_sul_
	valor_amb_ventilacao_sul = amb_ventilacao_sul_.get()
	if '< 20%' in valor_amb_ventilacao_sul.encode('utf-8'):
		nota_amb_ventilacao_sul_ = planilha_bd['J189'].value
		calcula_nota_5()
		return	
	if '20 - 50%' in valor_amb_ventilacao_sul.encode('utf-8'):
		nota_amb_ventilacao_sul_ = planilha_bd['J190'].value
		calcula_nota_5()
		return	
	if '50 - 80%' in valor_amb_ventilacao_sul.encode('utf-8'):
		nota_amb_ventilacao_sul_ = planilha_bd['J191'].value
		calcula_nota_5()
		return	
	if '> 80%' in valor_amb_ventilacao_sul.encode('utf-8'):
		nota_amb_ventilacao_sul_ = planilha_bd['J192'].value	
		calcula_nota_5()
		return	

def nota_amb_ventilacao_leste(event):
	global nota_amb_ventilacao_leste_
	valor_amb_ventilacao_leste = amb_ventilacao_leste_.get()
	if '< 20%' in valor_amb_ventilacao_leste.encode('utf-8'):
		nota_amb_ventilacao_leste_ = planilha_bd['J193'].value
		calcula_nota_5()
		return	
	if '20 - 50%' in valor_amb_ventilacao_leste.encode('utf-8'):
		nota_amb_ventilacao_leste_ = planilha_bd['J194'].value
		calcula_nota_5()
		return	
	if '50 - 80%' in valor_amb_ventilacao_leste.encode('utf-8'):
		nota_amb_ventilacao_leste_ = planilha_bd['J195'].value
		calcula_nota_5()
		return	
	if '> 80%' in valor_amb_ventilacao_leste.encode('utf-8'):
		nota_amb_ventilacao_leste_ = planilha_bd['J196'].value
		calcula_nota_5()
		return		

def nota_amb_ventilacao_oeste(event):
	global nota_amb_ventilacao_oeste_
	valor_amb_ventilacao_oeste = amb_ventilacao_oeste_.get()
	if '< 20%' in valor_amb_ventilacao_oeste.encode('utf-8'):
		nota_amb_ventilacao_oeste_ = planilha_bd['J197'].value
		calcula_nota_5()
		return	
	if '20 - 50%' in valor_amb_ventilacao_oeste.encode('utf-8'):
		nota_amb_ventilacao_oeste_ = planilha_bd['J198'].value
		calcula_nota_5()
		return	
	if '50 - 80%' in valor_amb_ventilacao_oeste.encode('utf-8'):
		nota_amb_ventilacao_oeste_ = planilha_bd['J199'].value
		calcula_nota_5()
		return	
	if '> 80%' in valor_amb_ventilacao_oeste.encode('utf-8'):
		nota_amb_ventilacao_oeste_ = planilha_bd['J200'].value	
		calcula_nota_5()
		return				
								
def nota_amb_brise(event):
	global nota_amb_brise_
	valor_amb_brise = amb_brise_.get()
	if 'Período mais quente do verão' in valor_amb_brise.encode('utf-8'):
		nota_amb_brise_ = planilha_bd['J201'].value
		calcula_nota_5()
		return	
	if 'Todo o ano' in valor_amb_brise.encode('utf-8'):
		nota_amb_brise_ = planilha_bd['J202'].value
		calcula_nota_5()
		return	

def nota_amb_tipo_abertura(event):
	global nota_amb_tipo_abertura_
	valor_amb_tipo_abertura = amb_tipo_abertura_.get()
	if 'PVC' in valor_amb_tipo_abertura.encode('utf-8'):
		nota_amb_tipo_abertura_ = planilha_bd['J203'].value
		calcula_nota_5()
		return	
	if 'Madeira' in valor_amb_tipo_abertura.encode('utf-8'):
		nota_amb_tipo_abertura_ = planilha_bd['J204'].value
		calcula_nota_5()
		return	
	if 'Metálica' in valor_amb_tipo_abertura.encode('utf-8'):
		nota_amb_tipo_abertura_ = planilha_bd['J205'].value	
		calcula_nota_5()
		return	

def nota_amb_vidro(event):
	global nota_amb_vidro_
	valor_amb_vidro = amb_vidro_.get()
	if 'Simples' in valor_amb_vidro.encode('utf-8'):
		nota_amb_vidro_ = planilha_bd['J206'].value
		calcula_nota_5()
		return	
	if 'Duplo' in valor_amb_vidro.encode('utf-8'):
		nota_amb_vidro_ = planilha_bd['J207'].value
		calcula_nota_5()
		return	

def nota_amb_estanqueidade(event):
	global nota_amb_estanqueidade_
	valor_amb_estanqueidade = amb_estanqueidade_.get()
	if 'Muito estanque' in valor_amb_estanqueidade.encode('utf-8'):
		nota_amb_estanqueidade_ = planilha_bd['J208'].value
		calcula_nota_5()
		return	
	if 'Pouco estanque' in valor_amb_estanqueidade.encode('utf-8'):
		nota_amb_estanqueidade_ = planilha_bd['J209'].value	
		calcula_nota_5()
		return		


top_amb5 = ''
valor_do_ambiente = 0
def seleciona_ambiente(event):
	
	global top_amb5, amb_nome_, amb_contato_solo_,valor_do_ambiente, amb_u_solo_,amb_ct_solo_,amb_cor_parede_ ,amb_orient_parede_ ,amb_u_parede_ ,amb_ct_parede_ ,amb_u_cobertura_ ,amb_cor_cobertura_ ,amb_tipo_abertura_ ,amb_vidro_ ,amb_estanqueidade_ ,amb_brise_ ,amb_iluminacao_norte_ ,amb_iluminacao_sul_ ,amb_iluminacao_leste_ ,amb_iluminacao_oeste_ ,amb_ventilacao_norte_ ,amb_ventilacao_sul_ ,amb_ventilacao_leste_ ,amb_ventilacao_oeste_
	
	global nota_amb_u_solo_, nota_amb_ct_solo_, nota_amb_cor_parede_, nota_amb_u_parede_, nota_amb_ct_parede_, nota_amb_orient_parede_, nota_amb_iluminacao_norte_, nota_amb_iluminacao_sul_,nota_amb_iluminacao_leste_,nota_amb_iluminacao_oeste_,nota_amb_ventilacao_norte_,nota_amb_ventilacao_sul_,nota_amb_ventilacao_leste_,nota_amb_ventilacao_oeste_,nota_amb_u_cobertura_,nota_amb_cor_cobertura_,nota_amb_vidro_,nota_amb_estanqueidade_,nota_amb_brise_,nota_amb_tipo_abertura_,nota_amb_ventilacao_,nota_amb_iluminacao_,nota_amb_abertura_,nota_amb_cobertura_,nota_amb_parede_,nota_amb_piso_   

	nota_amb_u_solo_ = 0
	nota_amb_ct_solo_ = 0
	nota_amb_cor_parede_ = 0
	nota_amb_u_parede_ = 0

	nota_amb_ct_parede_ = 0
	nota_amb_orient_parede_ = 0
	nota_amb_iluminacao_norte_ = 0
	nota_amb_iluminacao_sul_ = 0
	nota_amb_iluminacao_leste_ = 0
	nota_amb_iluminacao_oeste_ = 0
	nota_amb_ventilacao_norte_ = 0
	nota_amb_ventilacao_sul_ = 0
	nota_amb_ventilacao_leste_ = 0
	nota_amb_ventilacao_oeste_ = 0
	nota_amb_u_cobertura_ = 0
	nota_amb_cor_cobertura_ = 0
	nota_amb_vidro_ = 0
	nota_amb_estanqueidade_ = 0
	nota_amb_brise_ = 0
	nota_amb_tipo_abertura_ = 0
	nota_amb_ventilacao_ = 0
	nota_amb_iluminacao_ = 0
	nota_amb_abertura_ = 0
	nota_amb_cobertura_ = 0
	nota_amb_parede_ = 0
	nota_amb_piso_ = 0


	for i in range(10):
		if n_ambientes_[i].get() == amb_ambiente_.get():
			valor_do_ambiente = i
			valor_do_ambiente = valor_do_ambiente + 1
			amb_nome_ = amb_ambiente_.get()
			break

	print valor_do_ambiente

	#nome_a = n_ambientes_.get()
	#print valor_ambiente
	
	top_amb5 = Toplevel()
	top_amb5.resizable(0,0)
	top_amb5.geometry('480x700')
	top_amb5.configure(background='white')
	top_amb5.tk.call('wm', 'iconphoto', top_amb5._w, img)

	em_branco = tk.Label(top_amb5, text="",background='white') 
	em_branco.grid(row=2, sticky=W,padx=40)

	amb = tk.Label(top_amb5, text="%s" % amb_ambiente_.get(),font="Arial 12 bold",background='white',fg='#545454') 
	amb.grid(  row=3, sticky=W, padx = 40)

	path_img1 = "grafico0.png"
	img1_nota = ImageTk.PhotoImage(file = path_img1)
	#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
	label = tk.Label(top_amb5,image=img1_nota, background='white')
	label.image = img1_nota
	label.grid(row=3,sticky = E, padx = 40)

	amb_piso = tk.Label(top_amb5, text="Piso",font="Arial 10 bold",background='white',fg='#545454') 
	amb_piso.grid(  row=6, sticky=W, padx = 40)

	amb_contato_solo = tk.Label(top_amb5, text="Contato com o solo",font="Arial 8",background='white',fg='#545454') 
	amb_contato_solo.grid(  row=7, sticky=W, padx = 40)


	amb_contato_solo_ = ttk.Combobox(top_amb5, width=63,font="Arial 8",background='white')
	amb_contato_solo_['values'] = "Sim","Não"
	amb_contato_solo_.grid(  row=8,stick=W, padx = 40)
	#amb_contato_solo_.bind("<<ComboboxSelected>>", nota_amb_contato_solo)

	amb_u_solo = tk.Label(top_amb5, text="Transmitância",font="Arial 8",background='white',fg='#545454') 
	amb_u_solo.grid(  row=9, sticky=W, padx = 40)


	amb_u_solo_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_u_solo_['values'] = "U < 1,5", "1,5 < U < 2,0", "U > 2,0"
	amb_u_solo_.grid(  row=10,stick=W, padx = 40)
	amb_u_solo_.bind("<<ComboboxSelected>>", nota_amb_u_solo)

	amb_ct_solo = tk.Label(top_amb5, text="Capacidade Térmica",font="Arial 8",background='white',fg='#545454') 
	amb_ct_solo.grid(row=9, sticky=E, padx = 138)


	amb_ct_solo_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_ct_solo_['values'] = "CT < 130","CT > 130"
	amb_ct_solo_.grid(  row=10,stick=E, padx = 40)
	amb_ct_solo_.bind("<<ComboboxSelected>>", nota_amb_ct_solo)

	amb_parede = tk.Label(top_amb5, text="Paredes",font="Arial 10 bold",background='white',fg='#545454') 
	amb_parede.grid(  row=12, sticky=W, padx = 40)

	amb_cor_parede = tk.Label(top_amb5, text="Cor",font="Arial 8",background='white',fg='#545454') 
	amb_cor_parede.grid(  row=13, sticky=W, padx = 40)

	amb_cor_parede_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_cor_parede_['values'] = "Tons claros (α<0,4)","Tons médios (0,4<α<0,7)","Tons escuros (α>0,7)"
	amb_cor_parede_.grid(  row=14,stick=W, padx = 40)
	amb_cor_parede_.bind("<<ComboboxSelected>>", nota_amb_cor_parede)

	amb_orient_parede = tk.Label(top_amb5, text="Orientação",font="Arial 8",background='white',fg='#545454') 
	amb_orient_parede.grid(  row=13, sticky=E, padx = 171)


	amb_orient_parede_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_orient_parede_['values'] = "Norte","Nordeste","Sul","Sudoeste","Leste","Sudeste","Oeste","Noroeste"
	amb_orient_parede_.grid(  row=14,stick=E, padx = 40)
	amb_orient_parede_.bind("<<ComboboxSelected>>", nota_amb_orient_parede)

	amb_u_parede = tk.Label(top_amb5, text="Transmitância",font="Arial 8",background='white',fg='#545454') 
	amb_u_parede.grid(  row=15, sticky=W, padx = 40)


	amb_u_parede_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_u_parede_['values'] = "U < 1,5", "1,5 < U < 2,0", "U > 2,0"
	amb_u_parede_.grid(  row=16,stick=W, padx = 40)
	amb_u_parede_.bind("<<ComboboxSelected>>", nota_amb_u_parede)

	amb_ct_parede = tk.Label(top_amb5, text="Capacidade Térmica",font="Arial 8",background='white',fg='#545454') 
	amb_ct_parede.grid(  row=15, sticky=E, padx = 138)

	amb_ct_parede_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_ct_parede_['values'] = "CT < 130","CT > 130"
	amb_ct_parede_.grid(  row=16,stick=E, padx = 40)
	amb_ct_parede_.bind("<<ComboboxSelected>>", nota_amb_ct_parede)

	amb_cobertura = tk.Label(top_amb5, text="Cobertura",font="Arial 10 bold",background='white',fg='#545454') 
	amb_cobertura.grid(  row=18, sticky=W, padx = 40)

	amb_u_cobertura = tk.Label(top_amb5, text="Transmitância",font="Arial 8",background='white',fg='#545454') 
	amb_u_cobertura.grid(  row=19, sticky=W, padx = 40)


	amb_u_cobertura_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_u_cobertura_['values'] = "U < 1,5", "1,5 < U < 2,0", "U > 2,0"
	amb_u_cobertura_.grid(  row=20,stick=W, padx = 40)
	amb_u_cobertura_.bind("<<ComboboxSelected>>", nota_amb_u_cobertura)

	amb_cor_cobertura = tk.Label(top_amb5, text="Cor",font="Arial 8",background='white',fg='#545454') 
	amb_cor_cobertura.grid(  row=19, sticky=E, padx = 208)


	amb_cor_cobertura_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_cor_cobertura_['values'] = "Tons claros (α<0,4)","Tons médios (0,4<α<0,7)","Tons escuros (α>0,7)"
	amb_cor_cobertura_.grid(  row=20,stick=E, padx = 40)
	amb_cor_cobertura_.bind("<<ComboboxSelected>>", nota_amb_cor_cobertura)

	amb_abertura = tk.Label(top_amb5, text="Aberturas",font="Arial 10 bold",background='white',fg='#545454') 
	amb_abertura.grid(  row=22, sticky=W, padx = 40)

	amb_tipo_abertura = tk.Label(top_amb5, text="Tipo de abertura",font="Arial 8 ",background='white',fg='#545454') 
	amb_tipo_abertura.grid(  row=23, sticky=W, padx = 40)

	amb_tipo_abertura_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_tipo_abertura_['values'] = "PVC","Madeira","Metálica"
	amb_tipo_abertura_.grid(  row=24,stick=W, padx = 40)
	amb_tipo_abertura_.bind("<<ComboboxSelected>>", nota_amb_tipo_abertura)

	amb_vidro = tk.Label(top_amb5, text="Tipo de vidro",font="Arial 8 ",background='white',fg='#545454') 
	amb_vidro.grid(  row=23, sticky=E, padx = 165)


	amb_vidro_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_vidro_['values'] = "Simples","Duplo"
	amb_vidro_.grid(  row=24,stick=E, padx = 40)
	amb_vidro_.bind("<<ComboboxSelected>>", nota_amb_vidro)

	amb_estanqueidade = tk.Label(top_amb5, text="Estanqueidade",font="Arial 8 ",background='white',fg='#545454') 
	amb_estanqueidade.grid(  row=25, sticky=W, padx = 40)


	amb_estanqueidade_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_estanqueidade_['values'] = "Muito estanque","Pouco estanque"
	amb_estanqueidade_.grid(  row=26,stick=W, padx = 40)
	amb_estanqueidade_.bind("<<ComboboxSelected>>", nota_amb_estanqueidade)

	amb_brise = tk.Label(top_amb5, text="Proteção solar",font="Arial 8 ",background='white',fg='#545454') 
	amb_brise.grid(  row=25, sticky=E, padx = 158)


	amb_brise_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_brise_['values'] = "Período mais quente do verão", "Todo o ano"
	amb_brise_.grid(  row=26,stick=E, padx = 40)
	amb_brise_.bind("<<ComboboxSelected>>", nota_amb_brise)


	area_de_ilumina_area_parede = tk.Label(top_amb5, text="Área de iluminação\npor área de parede",font="Arial 8",background='white',fg='#545454') 
	area_de_ilumina_area_parede.grid(  row=28, sticky=W, padx = 40)

	amb_iluminacao_norte = tk.Label(top_amb5, text="Norte",font="Arial 8 ",background='white',fg='#9e9e9e') 
	amb_iluminacao_norte.grid(  row=29, sticky=W, padx = 40)

	amb_iluminacao_norte_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_iluminacao_norte_['values'] = "< 20%","20 - 50%", "50 - 80%", "> 80%"
	amb_iluminacao_norte_.grid(  row=30,stick=W, padx = 40)
	amb_iluminacao_norte_.bind("<<ComboboxSelected>>", nota_amb_iluminacao_norte)

	amb_iluminacao_sul = tk.Label(top_amb5, text="Sul",font="Arial 8 ",background='white',fg='#9e9e9e') 
	amb_iluminacao_sul.grid(  row=31, sticky=W, padx = 40)


	amb_iluminacao_sul_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_iluminacao_sul_['values'] = "< 20%","20 - 50%", "50 - 80%", "> 80%"
	amb_iluminacao_sul_.grid(  row=32,stick=W, padx = 40)
	amb_iluminacao_sul_.bind("<<ComboboxSelected>>", nota_amb_iluminacao_sul)

	amb_iluminacao_leste = tk.Label(top_amb5, text="Leste",font="Arial 8 ",background='white',fg='#9e9e9e') 
	amb_iluminacao_leste.grid(  row=33, sticky=W, padx = 40)



	amb_iluminacao_leste_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_iluminacao_leste_['values'] = "< 20%","20 - 50%", "50 - 80%", "> 80%"
	amb_iluminacao_leste_.grid(  row=34,stick=W, padx = 40)
	amb_iluminacao_leste_.bind("<<ComboboxSelected>>", nota_amb_iluminacao_leste)

	amb_iluminacao_oeste = tk.Label(top_amb5, text="Oeste",font="Arial 8 ",background='white',fg='#9e9e9e') 
	amb_iluminacao_oeste.grid(  row=35, sticky=W, padx = 40)
	amb_iluminacao_oeste_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_iluminacao_oeste_['values'] = "< 20%","20 - 50%", "50 - 80%", "> 80%"
	amb_iluminacao_oeste_.grid(  row=36,stick=W, padx = 40)
	amb_iluminacao_oeste_.bind("<<ComboboxSelected>>", nota_amb_iluminacao_oeste)


	area_de_ventila_area_parede = tk.Label(top_amb5, text="Área de ventilação\npor área de parede",font="Arial 8",background='white',fg='#545454') 
	area_de_ventila_area_parede.grid(  row=28, sticky=E, padx = 134)

			#area_de_ventila_area_fachada = tk.Label(envoltoria, text="Area de ventilação por área de fachada:",font="Arial 8",background='white',fg='#545454') 
			#area_de_ventila_area_fachada.grid(  row=20, sticky=E)

	amb_ventilacao_norte = tk.Label(top_amb5, text="Norte",font="Arial 8 ",background='white',fg='#9e9e9e')

	amb_ventilacao_norte.grid(  row=29, sticky=E, padx = 198)


	amb_ventilacao_norte_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_ventilacao_norte_['values'] = "< 20%","20 - 50%", "50 - 80%", "> 80%"
	amb_ventilacao_norte_.grid(  row=30,stick=E, padx = 40)
	amb_ventilacao_norte_.bind("<<ComboboxSelected>>", nota_amb_ventilacao_norte)

	amb_ventilacao_sul = tk.Label(top_amb5, text="Sul",font="Arial 8 ",background='white',fg='#9e9e9e') 
	amb_ventilacao_sul.grid(  row=31, sticky=E, padx = 208)


	amb_ventilacao_sul_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_ventilacao_sul_['values'] = "< 20%","20 - 50%", "50 - 80%", "> 80%"
	amb_ventilacao_sul_.grid(  row=32,stick=E, padx = 40)
	amb_ventilacao_sul_.bind("<<ComboboxSelected>>", nota_amb_ventilacao_sul)

	amb_ventilacao_leste = tk.Label(top_amb5, text="Leste",font="Arial 8 ",background='white',fg='#9e9e9e') 
	amb_ventilacao_leste.grid(  row=33, sticky=E, padx = 198)



	amb_ventilacao_leste_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_ventilacao_leste_['values'] = "< 20%","20 - 50%", "50 - 80%", "> 80%"
	amb_ventilacao_leste_.grid(  row=34,stick=E, padx = 40)
	amb_ventilacao_leste_.bind("<<ComboboxSelected>>", nota_amb_ventilacao_leste)

	amb_ventilacao_oeste = tk.Label(top_amb5, text="Oeste",font="Arial 8 ",background='white',fg='#9e9e9e') 
	amb_ventilacao_oeste.grid(row=35, sticky=E, padx = 198)  


	amb_ventilacao_oeste_ = ttk.Combobox(top_amb5, width=28,font="Arial 8",background='white')
	amb_ventilacao_oeste_['values'] = "< 20%","20 - 50%", "50 - 80%", "> 80%"
	amb_ventilacao_oeste_.grid(row=36,stick=E, padx = 40)
	amb_ventilacao_oeste_.bind("<<ComboboxSelected>>", nota_amb_ventilacao_oeste)
	
	em_branco = tk.Label(top_amb5, text="",background='white') 
	em_branco.grid(row=37, sticky=W,padx=40)

	bt_ok = ttk.Button(top_amb5, text="OK",command=ok_top_amb5,style='TButton')
	bt_ok.grid(row=38,sticky=E,padx=40)

	top_amb5.mainloop()
	

def seleciona_num_area(event):
	num_amb = []
	valor_ambientes = numero_ambientes_.get()
	for i in range(int(valor_ambientes)):
		num_amb.append(i+1)
		n_ambientes_[i].configure(state='normal')
	
	

def seleciona_desenho_urbano(event):
	valor_desenho_urbano = desenho_urbano_.get()
	if 'Traçado regular, edificações no alinhamento predial' in valor_desenho_urbano.encode('utf-8'):
		print "valor desenho urbano é 0,25"  


def calcula_nota_4():
	global nota_nivel4, nota_composicao_, nota_parede_, nota_cobertura_, nota_iluminacao_, nota_ventilacao_, nota_abertura_

	nota_composicao_ = (nota_u_parede_ * 0.5) + (nota_ct_parede_ * 0.5)
	nota_parede_ = (nota_composicao_ * peso_composicao_) + (nota_cor_parede_ * peso_cor_parede_)

	nota_cobertura_ = (nota_u_cobertura_ * peso_u_cobertura_) + (nota_cor_cobertura_ * peso_cor_cobertura_)

	nota_iluminacao_ = (nota_iluminacao_norte_ * 0.25) + (nota_iluminacao_sul_ * 0.25) + (nota_iluminacao_leste_ * 0.25) + (nota_iluminacao_oeste_ * 0.25)
	nota_ventilacao_ = (nota_ventilacao_norte_ * 0.25) + (nota_ventilacao_sul_ * 0.25) + (nota_ventilacao_leste_ * 0.25) + (nota_ventilacao_oeste_ * 0.25)
	nota_abertura_ = (nota_tipo_abertura_ * peso_tipo_abertura_) + (nota_iluminacao_ * peso_iluminacao_) + (nota_ventilacao_ * peso_ventilacao_) + (nota_vidro_ * peso_vidro_) + (nota_estanqueidade_ * peso_estanqueidade_)
	
	nota_nivel4 = (nota_estrutura_ * peso_estrutura_) + (nota_parede_ * peso_parede_) + (nota_cobertura_ * peso_cobertura_) + (nota_abertura_ * peso_abertura_)

	if nota_nivel4 <= 0.5:
		path_img1 = "grafico0.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel4 > 0.5 and nota_nivel4 <= 1:
	 	path_img1 = "grafico1.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel4 > 1 and nota_nivel4 <= 1.5:
	 	path_img1 = "grafico2.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel4 > 1.5 and nota_nivel4 <= 2:
	 	path_img1 = "grafico3.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)	

	elif nota_nivel4 > 2 and nota_nivel4 <= 2.5:
	 	path_img1 = "grafico4.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel4 > 2.5 and nota_nivel4 <= 3:
	 	path_img1 = "grafico5.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel4 > 3 and nota_nivel4 <= 3.5:
	 	path_img1 = "grafico6.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel4 > 3.5 and nota_nivel4 <= 4:
	 	path_img1 = "grafico7.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)	

	elif nota_nivel4 > 4 and nota_nivel4 <= 4.5:
	 	path_img1 = "grafico8.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel4 > 4.5 and nota_nivel4 <= 5:
	 	path_img1 = "grafico9.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel4 > 5 and nota_nivel4 <= 5.5:
	 	path_img1 = "grafico10.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel4 > 5.5 and nota_nivel4 <= 6:
	 	path_img1 = "grafico11.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel4 > 6 and nota_nivel4 <= 6.5:
	 	path_img1 = "grafico12.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)	

	elif nota_nivel4 > 6.5 and nota_nivel4 <= 7:
	 	path_img1 = "grafico13.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)						

	elif nota_nivel4 > 7 and nota_nivel4 <= 7.5:
	 	path_img1 = "grafico14.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel4 > 7.5 and nota_nivel4 <= 8:
	 	path_img1 = "grafico15.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)	

	elif nota_nivel4 > 8 and nota_nivel4 <= 8.5:
	 	path_img1 = "grafico16.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)	

	elif nota_nivel4 <8.5:
	 	path_img1 = "grafico17.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(envoltoria,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	print "nota estrutura: %f\n" % nota_estrutura_
	print  "Nota u parede: %f\n" % nota_u_parede_
	print "Nota ct parede: %f\n" % nota_ct_parede_
	print "Nota cor parede: %f\n" % nota_cor_parede_
	print "Nota parede: %f\n" % nota_parede_
	print "Nota u cobertura: %f\n" % nota_u_cobertura_
	print "Nota cor cobertura: %f\n" % nota_cor_cobertura_
	print "Nota cobertura: %f\n" % nota_cobertura_


	print "Tipo abertura: %f\n" % nota_tipo_abertura_
	print "Vidro: %f\n"% nota_vidro_
	print "Estanqueidade: %f\n"% nota_estanqueidade_
	
	print "Nota iluminacao norte: %f\n" % nota_iluminacao_norte_
	print "Nota iluminacao sul: %f\n" % nota_iluminacao_sul_
	print "Nota iluminacao leste: %f\n" % nota_iluminacao_leste_
	print "Nota iluminacao oeste: %f\n" % nota_iluminacao_oeste_
	print "Nota iluminacao: %f\n" % nota_iluminacao_

	print "Nota ventilacao norte: %f\n" % nota_ventilacao_norte_
	print "Nota ventilacao sul: %f\n" % nota_ventilacao_sul_
	print "Nota ventilacao leste: %f\n" % nota_ventilacao_leste_
	print "Nota ventilacao oeste: %f\n" % nota_ventilacao_oeste_
	print "Nota ventilacao: %f\n" % nota_ventilacao_

	print "peso Tipo abertura: %f\n" % peso_tipo_abertura_
	print "peso Vidro: %f\n"% peso_vidro_
	print "peso Estanqueidade: %f\n"% peso_estanqueidade_
	print "peso iluminacao: %f\n" % peso_iluminacao_
	print "peso ventilacao: %f\n" % peso_ventilacao_

	print "\nNota abertura %f\n" % nota_abertura_
	print "Nota Nivel 4: %f\n" % nota_nivel4
	print "\n\n"

def calcula_nota_3():

	global nota_nivel3, nota_afastamento_
	nota_afast_norte_ = (nota_afast_norte_sup_ * 0.5) + (nota_afast_norte_ter_ * 0.5)
	nota_afast_sul_ = (nota_afast_sul_sup_ * 0.5) + (nota_afast_sul_ter_ * 0.5)
	nota_afast_leste_ = (nota_afast_leste_sup_ * 0.5) + (nota_afast_leste_ter_ * 0.5)
	nota_afast_oeste_ = (nota_afast_oeste_sup_ * 0.5) + (nota_afast_oeste_ter_ * 0.5)

	nota_afastamento_ = (nota_afast_norte_ * peso_afast_norte_) + (nota_afast_sul_ * peso_afast_sul_) + (nota_afast_leste_ * peso_afast_leste_) + (nota_afast_oeste_ * peso_afast_oeste_)

	nota_nivel3 = (nota_implantacao_* peso_implantacao_) + (nota_forma_ * peso_forma_) + (nota_relacao_solo_ * peso_relacao_solo_) + (nota_afastamento_ * peso_afastamento_)
	


	if nota_nivel3 <= 0.5:
		path_img1 = "grafico1.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel3 > 0.5 and nota_nivel3 <= 1:
	 	path_img1 = "grafico2.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel3 > 1 and nota_nivel3 <= 1.5:
	 	path_img1 = "grafico3.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel3 > 1.5 and nota_nivel3 <= 2:
	 	path_img1 = "grafico4.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)	

	elif nota_nivel3 > 2 and nota_nivel3 <= 2.5:
	 	path_img1 = "grafico5.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel3 > 2.5 and nota_nivel3 <= 3:
	 	path_img1 = "grafico6.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel3 > 3 and nota_nivel3 <= 3.5:
	 	path_img1 = "grafico7.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel3 > 3.5 and nota_nivel3 <= 4:
	 	path_img1 = "grafico8.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)	

	elif nota_nivel3 > 4 and nota_nivel3 <= 4.5:
	 	path_img1 = "grafico9.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel3 > 4.5 and nota_nivel3 <= 5:
	 	path_img1 = "grafico10.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel3 > 5 and nota_nivel3 <= 5.5:
	 	path_img1 = "grafico11.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel3 > 5.5 and nota_nivel3 <= 6:
	 	path_img1 = "grafico12.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel3 > 6 and nota_nivel3 <= 6.5:
	 	path_img1 = "grafico13.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)	

	elif nota_nivel3 > 6.5 and nota_nivel3 <= 7:
	 	path_img1 = "grafico14.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)						

	elif nota_nivel3 > 7 and nota_nivel3 <= 7.5:
	 	path_img1 = "grafico15.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)

	elif nota_nivel3 > 7.5 and nota_nivel3 <= 8:
	 	path_img1 = "grafico16.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)	

	elif nota_nivel3 > 8 and nota_nivel3 <= 8.5:
	 	path_img1 = "grafico17.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)	

	elif nota_nivel3 <8.5:
	 	path_img1 = "grafico17.png"
		img1_nota = ImageTk.PhotoImage(file = path_img1)
		#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
		label = tk.Label(implantacao,image=img1_nota, background='white')
		label.image = img1_nota
		label.grid(row=3,sticky = E, padx = 40)	
			
	print  "Nota implantacao: %f\n" % nota_implantacao_
	print "Nota Forma: %f\n" % nota_forma_
	print "Nota Relacao com o solo: %f\n" % nota_relacao_solo_
	print "Nota afastamento norte ter: %f\n" % nota_afast_norte_ter_
	print "Nota afastamento norte sup: %f\n" % nota_afast_norte_sup_
	print "Nota afastamento sul ter: %f\n" % nota_afast_sul_ter_
	print "Nota afastamento sul sup: %f\n" % nota_afast_sul_sup_
	print "Nota afastamento leste ter: %f\n" % nota_afast_leste_ter_
	print "Nota afastamento leste sup: %f\n" % nota_afast_leste_sup_
	print "Nota afastamento oeste ter: %f\n" % nota_afast_oeste_ter_
	print "Nota afastamento oest sup: %f\n" % nota_afast_oeste_sup_
	print "Nota afastamento: %f\n" % nota_afastamento_
	print "Nota Nivel 3: %f\n" % nota_nivel3
	print "\n\n"

### CONJUNTO DE REGRAS #####


#### NÍVEL 3 ####

def nota_implantacao(event):
	global nota_implantacao_
	valor_implantacao = implantacao_item_.get()
	if 'Em linha, maiores fachadas norte-sul' == valor_implantacao.encode('utf-8'):
		nota_implantacao_ = planilha_bd['J3'].value
		calcula_nota_3()
		return

	if 'Em linha, maiores fachadas leste-oeste' == valor_implantacao.encode('utf-8'):
		nota_implantacao_ = planilha_bd['J4'].value
		calcula_nota_3()
		return

	if 'Em linha, outras orientações' == valor_implantacao.encode('utf-8'):
		nota_implantacao_ = planilha_bd['J5'].value
		calcula_nota_3()
		return

	if 'Compacta' == valor_implantacao.encode('utf-8'):
		nota_implantacao_ = planilha_bd['J6'].value
		calcula_nota_3()
		return

	if 'Compacta, com pátio(s) interno(s)' == valor_implantacao.encode('utf-8'):
		nota_implantacao_ = planilha_bd['J7'].value
		calcula_nota_3()
		return
	

def nota_forma(event):
	global nota_forma_
	valor_forma = forma_geral_.get()
	if 'Forma compacta (prismática)' == valor_forma.encode('utf-8'):
		nota_forma_ = planilha_bd['J8'].value
		calcula_nota_3()
		return
	if 'Forma complexa' == valor_forma.encode('utf-8'):
		nota_forma_ = planilha_bd['J9'].value
		calcula_nota_3()
		return

def nota_relacao_solo(event):
	global nota_relacao_solo_

	valor_relacao_solo = relacao_solo_.get()
	valor_tipo_de_solo = tipo_de_solo_.get()

	if 'Edificação semi-enterrada' == valor_relacao_solo.encode('utf-8') and 'Argila' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J10'].value
		calcula_nota_3()
		return
	if 'Edificação semi-enterrada' == valor_relacao_solo.encode('utf-8') and 'Areia' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J11'].value
		calcula_nota_3()
		return
	if 'Edificação semi-enterrada' == valor_relacao_solo.encode('utf-8') and 'Saibro' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J12'].value
		calcula_nota_3()
		return
	if 'Edificação semi-enterrada' == valor_relacao_solo.encode('utf-8') and 'Rocha' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J13'].value
		calcula_nota_3()
		return		
			

	if 'Edificação em contato com o solo' == valor_relacao_solo.encode('utf-8') and 'Argila' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J14'].value
		calcula_nota_3()
		return

	if 'Edificação em contato com o solo' == valor_relacao_solo.encode('utf-8') and 'Areia' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J15'].value
		calcula_nota_3()
		return

	if 'Edificação em contato com o solo' == valor_relacao_solo.encode('utf-8') and 'Saibro' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J16'].value
		calcula_nota_3()
		return

	if 'Edificação em contato com o solo' == valor_relacao_solo.encode('utf-8') and 'Rocha' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J17'].value
		calcula_nota_3()
		return


	if 'Edificação elevada do solo' == valor_relacao_solo.encode('utf-8') and 'Argila' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J18'].value
		calcula_nota_3()
		return
	if 'Edificação elevada do solo' == valor_relacao_solo.encode('utf-8') and 'Areia' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J19'].value
		calcula_nota_3()
		return
	if 'Edificação elevada do solo' == valor_relacao_solo.encode('utf-8') and 'Saibro' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J20'].value
		calcula_nota_3()
		return
	if 'Edificação elevada do solo' == valor_relacao_solo.encode('utf-8') and 'Rocha' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J21'].value
		calcula_nota_3()
		return		



	if 'Edificação elevada do solo com isolamento' == valor_relacao_solo.encode('utf-8') and 'Argila' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J22'].value
		print nota_relacao_solo_
		calcula_nota_3()
		return
	if 'Edificação elevada do solo com isolamento' == valor_relacao_solo.encode('utf-8') and 'Areia' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J23'].value
		calcula_nota_3()
		return
	if 'Edificação elevada do solo com isolamento' == valor_relacao_solo.encode('utf-8') and 'Saibro' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J24'].value
		calcula_nota_3()
		return
	if 'Edificação elevada do solo com isolamento' == valor_relacao_solo.encode('utf-8') and 'Rocha' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J25'].value
		calcula_nota_3()
		return
		
	if 'Edificação elevada do solo com porão ventilado' == valor_relacao_solo.encode('utf-8') and 'Argila' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J26'].value
		calcula_nota_3()
		return			 
	if 'Edificação elevada do solo com porão ventilado' == valor_relacao_solo.encode('utf-8') and 'Areia' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J27'].value
		calcula_nota_3()
		return		

	if 'Edificação elevada do solo com porão ventilado' == valor_relacao_solo.encode('utf-8') and 'Saibro' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J28'].value
		calcula_nota_3()
		return		
	if 'Edificação elevada do solo com porão ventilado' == valor_relacao_solo.encode('utf-8') and 'Rocha' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J29'].value
		calcula_nota_3()
		return		


	if 'Edificação elevada do solo com isolamento e porão ventilado' == valor_relacao_solo.encode('utf-8') and 'Argila' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J30'].value
		calcula_nota_3()
		return			
	if 'Edificação elevada do solo com isolamento e porão ventilado' == valor_relacao_solo.encode('utf-8') and 'Areia' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J31'].value
		calcula_nota_3()
		return			 
	if 'Edificação elevada do solo com isolamento e porão ventilado' == valor_relacao_solo.encode('utf-8') and 'Saibro' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J32'].value
		calcula_nota_3()
		return	
	if 'Edificação elevada do solo com isolamento e porão ventilado' == valor_relacao_solo.encode('utf-8') and 'Rocha' == valor_tipo_de_solo.encode('utf-8'):
		nota_relacao_solo_ = planilha_bd['J33'].value
		calcula_nota_3()
		return

def nota_afast_norte_ter(event):
	global nota_afast_norte_ter_
	valor_nota_afast_norte_ter = afastamento_norte_terreo_.get()
	if '0 < α < 30' == valor_nota_afast_norte_ter.encode('utf-8'):
		nota_afast_norte_ter_ = planilha_bd['J34'].value
		calcula_nota_3()
		return 
	if '30 < α < 45' == valor_nota_afast_norte_ter.encode('utf-8'):
		nota_afast_norte_ter_ = planilha_bd['J35'].value
		calcula_nota_3()
		return
	if '45 < α < 60' == valor_nota_afast_norte_ter.encode('utf-8'):
		nota_afast_norte_ter_ = planilha_bd['J36'].value
		calcula_nota_3()
		return		
	if '60 < α < 75' == valor_nota_afast_norte_ter.encode('utf-8'):
		nota_afast_norte_ter_ = planilha_bd['J37'].value
		calcula_nota_3()
		return
	if '75 < α < 90' == valor_nota_afast_norte_ter.encode('utf-8'):
		nota_afast_norte_ter_ = planilha_bd['J38'].value
		calcula_nota_3()
		return
	if 'α = 90' == valor_nota_afast_norte_ter.encode('utf-8'):
		nota_afast_norte_ter_ = planilha_bd['J39'].value
		calcula_nota_3()
		return

def nota_afast_norte_sup(event):
	global nota_afast_norte_sup_
	valor_nota_afast_norte_sup = afastamento_norte_sup_.get()
	if '0 < α < 30' == valor_nota_afast_norte_sup.encode('utf-8'):
		nota_afast_norte_sup_ = planilha_bd['J40'].value
		calcula_nota_3()
		return 
	if '30 < α < 45' == valor_nota_afast_norte_sup.encode('utf-8'):
		nota_afast_norte_sup_ = planilha_bd['J41'].value
		calcula_nota_3()
		return
	if '45 < α < 60' == valor_nota_afast_norte_sup.encode('utf-8'):
		nota_afast_norte_sup_ = planilha_bd['J42'].value
		calcula_nota_3()
		return		
	if '60 < α < 75' == valor_nota_afast_norte_sup.encode('utf-8'):
		nota_afast_norte_sup_ = planilha_bd['J43'].value
		calcula_nota_3()
		return
	if '75 < α < 90' == valor_nota_afast_norte_sup.encode('utf-8'):
		nota_afast_norte_sup_ = planilha_bd['J44'].value
		calcula_nota_3()
		return
	if 'α = 90' == valor_nota_afast_norte_sup.encode('utf-8'):
		nota_afast_norte_sup_ = planilha_bd['J45'].value
		calcula_nota_3()
		return		


def nota_afast_sul_ter(event):
	global nota_afast_sul_ter_
	valor_nota_afast_sul_ter = afastamento_sul_terreo_.get()
	if '0 < α < 30' == valor_nota_afast_sul_ter.encode('utf-8'):
		nota_afast_sul_ter_ = planilha_bd['J46'].value
		calcula_nota_3()
		return 
	if '30 < α < 45' == valor_nota_afast_sul_ter.encode('utf-8'):
		nota_afast_sul_ter_ = planilha_bd['J47'].value
		calcula_nota_3()
		return
	if '45 < α < 60' == valor_nota_afast_sul_ter.encode('utf-8'):
		nota_afast_sul_ter_ = planilha_bd['J48'].value
		calcula_nota_3()
		return		
	if '60 < α < 75' == valor_nota_afast_sul_ter.encode('utf-8'):
		nota_afast_sul_ter_ = planilha_bd['J49'].value
		calcula_nota_3()
		return
	if '75 < α < 90' == valor_nota_afast_sul_ter.encode('utf-8'):
		nota_afast_sul_ter_ = planilha_bd['J50'].value
		calcula_nota_3()
		return
	if 'α = 90' == valor_nota_afast_sul_ter.encode('utf-8'):
		nota_afast_sul_ter_ = planilha_bd['J51'].value
		calcula_nota_3()
		return

def nota_afast_sul_sup(event):
	global nota_afast_sul_sup_
	valor_nota_afast_sul_sup = afastamento_sul_sup_.get()
	if '0 < α < 30' == valor_nota_afast_sul_sup.encode('utf-8'):
		nota_afast_sul_sup_ = planilha_bd['J52'].value
		calcula_nota_3()
		return 
	if '30 < α < 45' == valor_nota_afast_sul_sup.encode('utf-8'):
		nota_afast_sul_sup_ = planilha_bd['J53'].value
		calcula_nota_3()
		return
	if '45 < α < 60' == valor_nota_afast_sul_sup.encode('utf-8'):
		nota_afast_sul_sup_= planilha_bd['J54'].value
		calcula_nota_3()
		return		
	if '60 < α < 75' == valor_nota_afast_sul_sup.encode('utf-8'):
		nota_afast_sul_sup_ = planilha_bd['J55'].value
		calcula_nota_3()
		return
	if '75 < α < 90' == valor_nota_afast_sul_sup.encode('utf-8'):
		nota_afast_sul_sup_ = planilha_bd['J56'].value
		calcula_nota_3()
		return
	if 'α = 90' == valor_nota_afast_sul_sup.encode('utf-8'):
		nota_afast_sul_sup_ = planilha_bd['J57'].value
		calcula_nota_3()
		return


def nota_afast_leste_ter(event):
	global nota_afast_leste_ter_
	valor_nota_afast_leste_ter = afastamento_leste_terreo_.get()
	if '0 < α < 30' == valor_nota_afast_leste_ter.encode('utf-8'):
		nota_afast_leste_ter_ = planilha_bd['J58'].value
		calcula_nota_3()
		return 
	if '30 < α < 45' == valor_nota_afast_leste_ter.encode('utf-8'):
		nota_afast_leste_ter_ = planilha_bd['J59'].value
		calcula_nota_3()
		return
	if '45 < α < 60' == valor_nota_afast_leste_ter.encode('utf-8'):
		nota_afast_leste_ter_ = planilha_bd['J60'].value
		calcula_nota_3()
		return		
	if '60 < α < 75' == valor_nota_afast_leste_ter.encode('utf-8'):
		nota_afast_leste_ter_ = planilha_bd['J61'].value
		calcula_nota_3()
		return
	if '75 < α < 90' == valor_nota_afast_leste_ter.encode('utf-8'):
		nota_afast_leste_ter_ = planilha_bd['J62'].value
		calcula_nota_3()
		return
	if 'α = 90' == valor_nota_afast_leste_ter.encode('utf-8'):
		nota_afast_leste_ter_ = planilha_bd['J63'].value
		calcula_nota_3()
		return

def nota_afast_leste_sup(event):
	global nota_afast_leste_sup_
	valor_nota_afast_leste_sup = afastamento_leste_sup_.get()
	if '0 < α < 30' == valor_nota_afast_leste_sup.encode('utf-8'):
		nota_afast_leste_sup_ = planilha_bd['J64'].value
		calcula_nota_3()
		return 
	if '30 < α < 45' == valor_nota_afast_leste_sup.encode('utf-8'):
		nota_afast_leste_sup_ = planilha_bd['J65'].value
		calcula_nota_3()
		return
	if '45 < α < 60' == valor_nota_afast_leste_sup.encode('utf-8'):
		nota_afast_leste_sup_ = planilha_bd['J66'].value
		calcula_nota_3()
		return		
	if '60 < α < 75' == valor_nota_afast_leste_sup.encode('utf-8'):
		nota_afast_leste_sup_ = planilha_bd['J67'].value
		calcula_nota_3()
		return
	if '75 < α < 90' == valor_nota_afast_leste_sup.encode('utf-8'):
		nota_afast_leste_sup_ = planilha_bd['J68'].value
		calcula_nota_3()
		return
	if 'α = 90' == valor_nota_afast_leste_sup.encode('utf-8'):
		nota_afast_leste_sup_ = planilha_bd['J69'].value
		calcula_nota_3()
		return		


def nota_afast_oeste_ter(event):
	global nota_afast_oeste_ter_
	valor_nota_afast_oeste_ter = afastamento_oeste_terreo_.get()
	if '0 < α < 30' == valor_nota_afast_oeste_ter.encode('utf-8'):
		nota_afast_oeste_ter_ = planilha_bd['J70'].value
		calcula_nota_3()
		return 
	if '30 < α < 45' == valor_nota_afast_oeste_ter.encode('utf-8'):
		nota_afast_oeste_ter_ = planilha_bd['J71'].value
		calcula_nota_3()
		return
	if '45 < α < 60' == valor_nota_afast_oeste_ter.encode('utf-8'):
		nota_afast_oeste_ter_ = planilha_bd['J72'].value
		calcula_nota_3()
		return		
	if '60 < α < 75' == valor_nota_afast_oeste_ter.encode('utf-8'):
		nota_afast_oeste_ter_ = planilha_bd['J73'].value
		calcula_nota_3()
		return
	if '75 < α < 90' == valor_nota_afast_oeste_ter.encode('utf-8'):
		nota_afast_oeste_ter_ = planilha_bd['J74'].value
		calcula_nota_3()
		return
	if 'α = 90' == valor_nota_afast_oeste_ter.encode('utf-8'):
		nota_afast_oeste_ter_ = planilha_bd['J75'].value
		calcula_nota_3()
		return

def nota_afast_oeste_sup(event):
	global nota_afast_oeste_sup_
	valor_nota_afast_oeste_sup = afastamento_oeste_sup_.get()
	if '0 < α < 30' == valor_nota_afast_oeste_sup.encode('utf-8'):
		nota_afast_oeste_sup_ = planilha_bd['J76'].value
		calcula_nota_3()
		return 
	if '30 < α < 45' == valor_nota_afast_oeste_sup.encode('utf-8'):
		nota_afast_oeste_sup_ = planilha_bd['J77'].value
		calcula_nota_3()
		return
	if '45 < α < 60' == valor_nota_afast_oeste_sup.encode('utf-8'):
		nota_afast_oeste_sup_ = planilha_bd['J78'].value
		calcula_nota_3()
		return		
	if '60 < α < 75' == valor_nota_afast_oeste_sup.encode('utf-8'):
		nota_afast_oeste_sup_ = planilha_bd['J79'].value
		calcula_nota_3()
		return
	if '75 < α < 90' == valor_nota_afast_oeste_sup.encode('utf-8'):
		nota_afast_oeste_sup_ = planilha_bd['J80'].value
		calcula_nota_3()
		return
	if 'α = 90' == valor_nota_afast_oeste_sup.encode('utf-8'):
		nota_afast_oeste_sup_ = planilha_bd['J81'].value
		calcula_nota_3()
		return

#### NÍVEL 4 ####

def nota_estrutura(event):
	global nota_estrutura_
	valor_nota_estrutura = estrutura_.get()
	if 'Concreto armado, sem pontes térmicas' == valor_nota_estrutura.encode('utf-8'):
		nota_estrutura_ = planilha_bd['J84'].value
		calcula_nota_4()
		return
	if 'Concreto armado, com pontes térmicas' == valor_nota_estrutura.encode('utf-8'):
		nota_estrutura_ = planilha_bd['J85'].value
		calcula_nota_4()
		return
	if 'Blocos cerâmicos auto-portantes' == valor_nota_estrutura.encode('utf-8'):
		nota_estrutura_ = planilha_bd['J86'].value
		calcula_nota_4()
		return
	if 'Metálica, sem pontes térmicas' == valor_nota_estrutura.encode('utf-8'):
		nota_estrutura_ = planilha_bd['J87'].value
		calcula_nota_4()
		return
	if 'Metálica, com pontes térmicas' == valor_nota_estrutura.encode('utf-8'):
		nota_estrutura_ = planilha_bd['J88'].value
		calcula_nota_4()
		return
	if 'Madeira' == valor_nota_estrutura.encode('utf-8'):
		nota_estrutura_ = planilha_bd['J89'].value
		calcula_nota_4()
		return		
			
def nota_u_parede(event):
	global nota_u_parede_
	valor_nota_u_parede = u_parede_.get()
	if 'U < 1,5' == valor_nota_u_parede.encode('utf-8'):
		nota_u_parede_ = planilha_bd['J90'].value
		calcula_nota_4()
		return
 	if '1,5 < U < 2,0' == valor_nota_u_parede.encode('utf-8'):
		nota_u_parede_ = planilha_bd['J91'].value
		calcula_nota_4()
		return
	if 'U > 2,0' == valor_nota_u_parede.encode('utf-8'):
		nota_u_parede_ = planilha_bd['J92'].value
		calcula_nota_4()
		return

def nota_ct_parede(event):
	global nota_ct_parede_
	valor_nota_ct_parede = ct_parede_.get()
	if 'CT < 130' == valor_nota_ct_parede.encode('utf-8'):
		nota_ct_parede_ = planilha_bd['J93'].value
		calcula_nota_4()
		return
 	if 'CT > 130' == valor_nota_ct_parede.encode('utf-8'):
		nota_ct_parede_ = planilha_bd['J94'].value
		calcula_nota_4()
		return

def nota_cor_parede(event):
	global nota_cor_parede_
	valor_nota_cor_parede = cor_parede_.get()
	if 'Tons claros (α<0,4)' == valor_nota_cor_parede.encode('utf-8'):
		nota_cor_parede_ = planilha_bd['J95'].value
		calcula_nota_4()
		return
 	if 'Tons médios (0,4<α<0,7)' == valor_nota_cor_parede.encode('utf-8'):
		nota_cor_parede_ = planilha_bd['J96'].value
		calcula_nota_4()
		return
	if 'Tons escuros (α>0,7)' == valor_nota_cor_parede.encode('utf-8'):
		nota_cor_parede_ = planilha_bd['J97'].value
		calcula_nota_4()
		return

def nota_u_cobertura(event):
	global nota_u_cobertura_
	valor_nota_u_cobertura = u_cobertura_.get()
	if 'U < 1,5' == valor_nota_u_cobertura.encode('utf-8'):
		nota_u_cobertura_ = planilha_bd['J98'].value
		calcula_nota_4()
		return
 	if '1,5 < U < 2,0' == valor_nota_u_cobertura.encode('utf-8'):
		nota_u_cobertura_ = planilha_bd['J99'].value
		calcula_nota_4()
		return
	if 'U > 2,0' == valor_nota_u_cobertura.encode('utf-8'):
		nota_u_cobertura_ = planilha_bd['J100'].value
		calcula_nota_4()
		return		

def nota_cor_cobertura(event):
	global nota_cor_cobertura_
	valor_nota_cor_cobertura = cor_cobertura_.get()
	if 'Tons claros (α<0,4)' == valor_nota_cor_cobertura.encode('utf-8'):
		nota_cor_cobertura_ = planilha_bd['J101'].value
		calcula_nota_4()
		return
 	if 'Tons médios (0,4<α<0,7)' == valor_nota_cor_cobertura.encode('utf-8'):
		nota_cor_cobertura_ = planilha_bd['J102'].value
		calcula_nota_4()
		return
	if 'Tons escuros (α>0,7)' == valor_nota_cor_cobertura.encode('utf-8'):
		nota_cor_cobertura_ = planilha_bd['J103'].value
		calcula_nota_4()
		return

def nota_tipo_abertura(event):
	global nota_tipo_abertura_
	valor_nota_tipo_abertura = tipo_abertura_.get()
	if 'PVC' == valor_nota_tipo_abertura.encode('utf-8'):
		nota_tipo_abertura_ = planilha_bd['J104'].value
		calcula_nota_4()
		return		
	if 'Madeira' == valor_nota_tipo_abertura.encode('utf-8'):
		nota_tipo_abertura_ = planilha_bd['J105'].value
		calcula_nota_4()
		return				
	if 'Metálica' == valor_nota_tipo_abertura.encode('utf-8'):
		nota_tipo_abertura_ = planilha_bd['J106'].value		
		calcula_nota_4()
		return

def nota_iluminacao_norte(event):
	global nota_iluminacao_norte_
	valor_nota_iluminacao_norte = iluminacao_norte_.get()
	if '< 20%' == valor_nota_iluminacao_norte.encode('utf-8'):
		nota_iluminacao_norte_ = planilha_bd['J107'].value
		calcula_nota_4()
		return
	if '20% - 40%' == valor_nota_iluminacao_norte.encode('utf-8'):
		nota_iluminacao_norte_ = planilha_bd['J108'].value
		calcula_nota_4()
		return
	if '> 40%' == valor_nota_iluminacao_norte.encode('utf-8'):
		nota_iluminacao_norte_ = planilha_bd['J109'].value
		calcula_nota_4()
		return

def nota_iluminacao_sul(event):
	global nota_iluminacao_sul_
	valor_nota_iluminacao_sul = iluminacao_sul_.get()
	if '< 20%' == valor_nota_iluminacao_sul.encode('utf-8'):
		nota_iluminacao_sul_ = planilha_bd['J110'].value
		calcula_nota_4()
		return
	if '20% - 40%' == valor_nota_iluminacao_sul.encode('utf-8'):
		nota_iluminacao_sul_ = planilha_bd['J111'].value
		calcula_nota_4()
		return
	if '> 40%' == valor_nota_iluminacao_sul.encode('utf-8'):
		nota_iluminacao_sul_ = planilha_bd['J112'].value
		calcula_nota_4()
		return

def nota_iluminacao_leste(event):
	global nota_iluminacao_leste_
	valor_nota_iluminacao_leste = iluminacao_leste_.get()
	if '< 20%' == valor_nota_iluminacao_leste.encode('utf-8'):
		nota_iluminacao_leste_ = planilha_bd['J113'].value
		calcula_nota_4()
		return
	if '20% - 40%' == valor_nota_iluminacao_leste.encode('utf-8'):
		nota_iluminacao_leste_ = planilha_bd['J114'].value
		calcula_nota_4()
		return
	if '> 40%' == valor_nota_iluminacao_leste.encode('utf-8'):
		nota_iluminacao_leste_ = planilha_bd['J115'].value
		calcula_nota_4()
		return		

def nota_iluminacao_oeste(event):
	global nota_iluminacao_oeste_
	valor_nota_iluminacao_oeste = iluminacao_oeste_.get()
	if '< 20%' == valor_nota_iluminacao_oeste.encode('utf-8'):
		nota_iluminacao_oeste_ = planilha_bd['J116'].value
		calcula_nota_4()
		return
	if '20% - 40%' == valor_nota_iluminacao_oeste.encode('utf-8'):
		nota_iluminacao_oeste_ = planilha_bd['J117'].value
		calcula_nota_4()
		return
	if '> 40%' == valor_nota_iluminacao_oeste.encode('utf-8'):
		nota_iluminacao_oeste_ = planilha_bd['J118'].value
		calcula_nota_4()
		return

def nota_ventilacao_norte(event):
	global nota_ventilacao_norte_
	valor_nota_ventilacao_norte = ventilacao_norte_.get()
	if '< 10%' == valor_nota_ventilacao_norte.encode('utf-8'):
		nota_ventilacao_norte_ = planilha_bd['J119'].value
		calcula_nota_4()
		return
	if '10% - 20%' == valor_nota_ventilacao_norte.encode('utf-8'):
		nota_ventilacao_norte_ = planilha_bd['J120'].value
		calcula_nota_4()
		return
	if '> 20%' == valor_nota_ventilacao_norte.encode('utf-8'):
		nota_ventilacao_norte_ = planilha_bd['J121'].value
		calcula_nota_4()
		return

def nota_ventilacao_sul(event):
	global nota_ventilacao_sul_
	valor_nota_ventilacao_sul = ventilacao_sul_.get()
	if '< 10%' == valor_nota_ventilacao_sul.encode('utf-8'):
		nota_ventilacao_sul_ = planilha_bd['J122'].value
		calcula_nota_4()
		return
	if '10% - 20%' == valor_nota_ventilacao_sul.encode('utf-8'):
		nota_ventilacao_sul_ = planilha_bd['J123'].value
		calcula_nota_4()
		return
	if '> 20%' == valor_nota_ventilacao_sul.encode('utf-8'):
		nota_ventilacao_sul_ = planilha_bd['J124'].value
		calcula_nota_4()
		return

def nota_ventilacao_leste(event):
	global nota_ventilacao_leste_
	valor_nota_ventilacao_leste = ventilacao_leste_.get()
	if '< 10%' == valor_nota_ventilacao_leste.encode('utf-8'):
		nota_ventilacao_leste_ = planilha_bd['J125'].value
		calcula_nota_4()
		return
	if '10% - 20%' == valor_nota_ventilacao_leste.encode('utf-8'):
		nota_ventilacao_leste_ = planilha_bd['J126'].value
		calcula_nota_4()
		return
	if '> 20%' == valor_nota_ventilacao_leste.encode('utf-8'):
		nota_ventilacao_leste_ = planilha_bd['J127'].value	
		calcula_nota_4()
		return	

def nota_ventilacao_oeste(event):
	global nota_ventilacao_oeste_
	valor_nota_ventilacao_oeste = ventilacao_oeste_.get()
	if '< 10%' == valor_nota_ventilacao_oeste.encode('utf-8'):
		nota_ventilacao_oeste_ = planilha_bd['J128'].value
		calcula_nota_4()
		return
	if '10% - 20%' == valor_nota_ventilacao_oeste.encode('utf-8'):
		nota_ventilacao_oeste_ = planilha_bd['J129'].value
		calcula_nota_4()
		return
	if '> 20%' == valor_nota_ventilacao_oeste.encode('utf-8'):
		nota_ventilacao_oeste_ = planilha_bd['J130'].value	
		calcula_nota_4()
		return				

def nota_vidro(event):
	global nota_vidro_
	valor_nota_vidro = vidro_.get()
	if 'Simples' == valor_nota_vidro.encode('utf-8'):
		nota_vidro_ = planilha_bd['J131'].value		
		calcula_nota_4()
		return
	if 'Duplo' == valor_nota_vidro.encode('utf-8'):
		nota_vidro_ = planilha_bd['J132'].value			
		calcula_nota_4()
		return	

def nota_estanqueidade(event):
	global nota_estanqueidade_
	valor_nota_estanqueidade = estanqueidade_.get()
	if 'Muito estanque' == valor_nota_estanqueidade.encode('utf-8'):
		nota_estanqueidade_ = planilha_bd['J133'].value
		calcula_nota_4()
		return		
	if 'Pouco estanque' == valor_nota_estanqueidade.encode('utf-8'):
		nota_estanqueidade_ = planilha_bd['J134'].value
		calcula_nota_4()
		return




tkTop = Tk()	
tkTop.title("ARCH - E (Beta)")
tkTop.geometry('480x650')
tkTop.resizable(0,0)
tkTop.configure(background='white')
img = ImageTk.PhotoImage(file='logo_p.png')
tkTop.tk.call('wm', 'iconphoto', tkTop._w, img)

#stylelogo_p_3

noteStyler = ttk.Style()
noteStyler.theme_use('vista')
noteStyler.configure("TFrame", background="white", foreground="green", borderwidth=0)
noteStyler.configure("TNotebook", background='white',darkcolor='#3A8FD7',lightcolor='#3A8FD7', borderwidth=0)
noteStyler.map("TNotebook.Tab", background=[("selected", 'gray')], foreground=[("selected", '#3A8FD7')]);
noteStyler.configure("TNotebook.Tab", background='#9e9e9e', foreground='#9e9e9e',bordercolor='#3A8FD7',  borderwidth=0,font='Arial 8 bold')
noteStyler.configure("TButton",background='gray',foreground='#3A8FD7', borderwidth=0,font='Arial 10 bold')


notebook = ttk.Notebook(tkTop,style='TNotebook')
inicio = ttk.Frame(notebook,style='TFrame')
informacoes = ttk.Frame(notebook,style='TFrame')
entorno = ttk.Frame(notebook,style='TFrame')
implantacao = ttk.Frame(notebook,style='TFrame')
envoltoria = ttk.Frame(notebook,style='TFrame')
ambientes = ttk.Frame(notebook,style='TFrame')
nota_final = ttk.Frame(notebook,style='TFrame')

notebook.add(inicio,text='Início',compound = tk.TOP)
notebook.add(informacoes, text='1 - Info')
notebook.add(entorno, text='2 - Entorno')
notebook.add(implantacao, text='3 - Implantação')
notebook.add(envoltoria, text='4 - Envoltória')
notebook.add(ambientes, text='5 - Ambientes')
notebook.add(nota_final, text='Nota Final')
notebook.grid()

lista_nomes = []
def salvar():
	global lista_nomes
	amb_ambiente_.set('')
	#amb_ambiente_.current(0)
	for i in range(int(numero_ambientes_.get())):
		lista_nomes.append(n_ambientes_[i].get())
	amb_ambiente_['values'] = lista_nomes
	#numero_ambientes_.configure(state='disable')
	for i in range(int(numero_ambientes_.get())):
		lista_nomes.remove(n_ambientes_[i].get())
	#amb_ambiente_.current(0)

def iniciar():
	notebook.select(informacoes)

def gerar_relatorio():
	sucesso = tk.Label(nota_final, text="Relatório gerado com sucesso!",background='white',font='hero 10 italic bold',fg='#545454') 
	sucesso.grid( row=11, sticky=S,padx=80)
	log = open('Relatorio do projeto \'%s\'.txt' % nome_projeto_.get().encode('utf-8'),'w')
	#log.write("##### RELATÓRIO DAS NOTAS OBTIDAS DURANTE A AVALIAÇÃO ARCH-E: #####\nNome do projeto: %s\nDesrição: %s\nUso: %s\nCidade (Zona Bioclimática): %s\nNúmero de ambientes de permanência prolongada: %s\nNome Ambiente 1: %s\nNome Ambiente 2: %s\nNome Ambiente 3: %s\nNome Ambiente 4: %s\nNome Ambiente 5: %s\nNome Ambiente 6: %s\nNome Ambiente 7: %s\nNome Ambiente 8: %s\nNome Ambiente 9: %s\nNome Ambiente 10: %s\n" % nome_projeto_.get(),descricao_.get(),uso_.get(),cidade_.get(),numero_ambientes_.get(),nome_amb[0].get())
	log.write("##### RELATÓRIO DAS NOTAS OBTIDAS DURANTE A AVALIAÇÃO DO SISTEMA ESPECIALISTA ARCH-E: #####\n\n")
	log.write("1 - Informações:\n\n")
	log.write("Nome do projeto: %s\n" % nome_projeto_.get().encode('utf-8'))
	log.write("Desrição: %s\n" % descricao_.get().encode('utf-8'))
	log.write("Uso: %s\n" % uso_.get().encode('utf-8'))
	log.write("Cidade (Zona Bioclimática): %s\n" % cidade_.get().encode('utf-8'))
	log.write("Número de ambientes de permanência prolongada: %s\n" % numero_ambientes_.get().encode('utf-8'))
	log.write("Nome Ambiente 1: %s\n" % n_ambientes_[0].get().encode('utf-8'))
	log.write("Nome Ambiente 2: %s\n" % n_ambientes_[1].get().encode('utf-8'))
	log.write("Nome Ambiente 3: %s\n" % n_ambientes_[2].get().encode('utf-8'))
	log.write("Nome Ambiente 4: %s\n" % n_ambientes_[3].get().encode('utf-8'))
	log.write("Nome Ambiente 5: %s\n" % n_ambientes_[4].get().encode('utf-8'))
	log.write("Nome Ambiente 6: %s\n" % n_ambientes_[5].get().encode('utf-8'))
	log.write("Nome Ambiente 7: %s\n" % n_ambientes_[6].get().encode('utf-8'))
	log.write("Nome Ambiente 8: %s\n" % n_ambientes_[7].get().encode('utf-8'))
	log.write("Nome Ambiente 9: %s\n" % n_ambientes_[8].get().encode('utf-8'))
	log.write("Nome Ambiente 10: %s\n" % n_ambientes_[9].get().encode('utf-8'))


	log.write("\n\n2 - Entorno:\n\n")
	log.write("Desenho Urbano: %s\n" % desenho_urbano_.get().encode('utf-8'))
	log.write("Topografia (sentido da inclinação): %s\n" % topografia_.get().encode('utf-8'))
	log.write("Tipo de solo: %s\n" % tipo_de_solo_.get().encode('utf-8'))

	log.write("\n\n3 - Implantação:\n\n")
	log.write("Nota Implamentação: %.2f\n" % nota_implantacao_)
	log.write("Nota Forma Geral (Volumetria): %.2f\n" % nota_forma_)
	log.write("Nota Relação com o solo: %.2f\n" % nota_relacao_solo_)
	print nota_afastamento_
	log.write("Nota Afastamento das edificações vizinhas: %.2f\n" % nota_afastamento_)
	log.write("\n\nNOTA NÍVEL 3: %.2f\n\n" % nota_nivel3)


	log.write("\n\n4 - Envoltória:\n\n")
	log.write("Nota da Composição: %.2f\n" % nota_composicao_)
	log.write("Nota das Paredes: %.2f\n" % nota_parede_)
	log.write("Nota da Cobertura: %.2f\n" % nota_cobertura_)
	log.write("Nota da Iluminação %.2f\n" % nota_iluminacao_)
	log.write("Nota da Ventilação %.2f\n" % nota_ventilacao_)
	log.write("Nota das Aberturas %.2f\n" % nota_abertura_)
	log.write("\n\nNOTA NÍVEL 4: %.2f\n\n" % nota_nivel4)


	log.write("\n\n5 - Ambientes:\n\n")
	log.write("Nota do Ambiente 1 (%s): %.2f\n" % (n_ambientes_[0].get().encode('utf-8'), nota_nivel5_amb1))
	log.write("Nota do Ambiente 2 (%s): %.2f\n" % (n_ambientes_[1].get().encode('utf-8'), nota_nivel5_amb2))
	log.write("Nota do Ambiente 3 (%s): %.2f\n" % (n_ambientes_[2].get().encode('utf-8'), nota_nivel5_amb3))
	log.write("Nota do Ambiente 4 (%s): %.2f\n" % (n_ambientes_[3].get().encode('utf-8'), nota_nivel5_amb4))
	log.write("Nota do Ambiente 5 (%s): %.2f\n" % (n_ambientes_[4].get().encode('utf-8'), nota_nivel5_amb5))
	log.write("Nota do Ambiente 6 (%s): %.2f\n" % (n_ambientes_[5].get().encode('utf-8'), nota_nivel5_amb6))
	log.write("Nota do Ambiente 7 (%s): %.2f\n" % (n_ambientes_[6].get().encode('utf-8'), nota_nivel5_amb7))
	log.write("Nota do Ambiente 8 (%s): %.2f\n" % (n_ambientes_[7].get().encode('utf-8'), nota_nivel5_amb8))
	log.write("Nota do Ambiente 9 (%s): %.2f\n" % (n_ambientes_[8].get().encode('utf-8'), nota_nivel5_amb9))
	log.write("Nota do Ambiente 10 (%s): %.2f\n" % (n_ambientes_[9].get().encode('utf-8'), nota_nivel5_amb10))
	log.write("\n\nNOTA NÍVEL 5 (Média do(s) %d ambiente(s)): %.2f\n\n" % (int(numero_ambientes_.get()), nota_nivel5))

	log.write("\n\nNOTA FINAL: %.2f\n\n" % nota_final_valor)

	log.close()

imagem_info = ImageTk.PhotoImage(file="info.png")

sobre = ''
def ok_sobre():
	sobre.destroy()
def sobre():
	#tkTop.option_add('*Dialog.msg.font', 'Arial 20')
	#tkMessageBox.showinfo("Afastamento das edificações vizinhas", "Relação entre o afastamento e a altura das edificações vizinhas, caracterizada pelo ângulo (α) em cada orientação. Ângulos menores que 30° significam que a edificação vizinha não influencia na insolação e ventilação. Quando o ângulo é igual a 90°, a edificação está em contato direto com a edificação vizinha.")		
	global sobre
	sobre = Toplevel()
	sobre.resizable(0,0)
	sobre.configure(background='white')
	sobre.tk.call('wm', 'iconphoto', sobre._w, img)
	sobre.title('Sobre')

	em_branco = tk.Label(sobre, text="",background='white') 
	em_branco.grid( row=0, sticky=W)

	j = Image.open("sobre.png") 
	photo = ImageTk.PhotoImage(j)
	label = tk.Label(sobre,image=photo, background='white')
	label.image = photo
	label.grid(row=1,sticky=S)
	
	em_branco = tk.Label(sobre, text="",background='white') 
	em_branco.grid( row=2, sticky=W)

	bt_ok_sobre = ttk.Button(sobre, text="Ok",command=ok_sobre,style='TButton')
	bt_ok_sobre.grid(row=3,sticky=E,padx=20)

	i = Image.open("logo_p2.png") 
	photo = ImageTk.PhotoImage(i)
	label = tk.Label(sobre,image=photo, background='white')
	label.image = photo
	label.grid(row=3,sticky=W,padx=20)

	em_branco = tk.Label(sobre, text="",background='white') 
	em_branco.grid( row=4, sticky=W)

	#tkTop.option_add('*Dialog.msg.font', 'Arial 20')
	#tkMessageBox.showinfo("Implantação", "Disposição, em planta, da edificação no terreno, determinante na exposição das fachadas ao sol e aos ventos.")
	sobre.mainloop()

#### TELA INICIAL ####

em_branco = tk.Label(inicio, text="",background='white') 
em_branco.grid( row=0, sticky=W,padx=40)

i = Image.open("_logo.png") 
i = i.resize((300,80),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(i)
label = tk.Label(inicio,image=photo, background='white')
label.image = photo
label.grid(row=1,sticky=S,padx=80,pady=30)

em_branco = tk.Label(inicio, text="",background='white') 
em_branco.grid( row=2, sticky=W,padx=40)
em_branco = tk.Label(inicio, text="",background='white') 
em_branco.grid( row=3, sticky=W,padx=40)


em_branco = tk.Label(inicio, text="",background='white') 
em_branco.grid( row=8, sticky=W,padx=40)

bt_iniciar = ttk.Button(inicio, text="       Iniciar       ",command = iniciar,style='TButton')
bt_iniciar.grid(row=9,sticky=S, padx=80)

em_branco = tk.Label(inicio, text="",background='white') 
em_branco.grid( row=10, sticky=W,padx=40)

em_branco = tk.Label(inicio, text="",background='white') 
em_branco.grid( row=14, sticky=W,padx=40)
em_branco = tk.Label(inicio, text="",background='white') 
em_branco.grid( row=15, sticky=W,padx=40)
em_branco = tk.Label(inicio, text="",background='white') 
em_branco.grid( row=16, sticky=W,padx=40)

bt_sobre = ttk.Button(inicio, text="        Sobre        ",style='TButton',command=sobre)
bt_sobre.grid(row=19,sticky=S)

i = Image.open("_logos.png") 
#i = i.resize((200,60),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(i)
label = tk.Label(inicio,image=photo, background='white')
label.image = photo
label.grid(row=18,sticky=S,padx=80)

clima = ''
estrategias = ''
def ok_clima():
	clima.destroy()
def clima():
	#tkTop.option_add('*Dialog.msg.font', 'Arial 20')
	#tkMessageBox.showinfo("Afastamento das edificações vizinhas", "Relação entre o afastamento e a altura das edificações vizinhas, caracterizada pelo ângulo (α) em cada orientação. Ângulos menores que 30° significam que a edificação vizinha não influencia na insolação e ventilação. Quando o ângulo é igual a 90°, a edificação está em contato direto com a edificação vizinha.")		
	global clima
	clima = Toplevel()
	clima.resizable(0,0)
	clima.configure(background='white')
	clima.tk.call('wm', 'iconphoto', clima._w, img)
	clima.title('Clima')

	em_branco = tk.Label(clima, text="",background='white') 
	em_branco.grid( row=0, sticky=W)

	j = Image.open("clima.png") 
	photo = ImageTk.PhotoImage(j)
	label = tk.Label(clima,image=photo, background='white')
	label.image = photo
	label.grid(row=1,sticky=S)
	
	em_branco = tk.Label(clima, text="",background='white') 
	em_branco.grid( row=2, sticky=W)

	bt_ok_clima = ttk.Button(clima, text="Ok",command=ok_clima,style='TButton')
	bt_ok_clima.grid(row=3,sticky=E,padx=20)

	i = Image.open("logo_p2.png") 
	photo = ImageTk.PhotoImage(i)
	label = tk.Label(clima,image=photo, background='white')
	label.image = photo
	label.grid(row=3,sticky=W,padx=20)

	em_branco = tk.Label(clima, text="",background='white') 
	em_branco.grid( row=4, sticky=W)

	#tkTop.option_add('*Dialog.msg.font', 'Arial 20')
	#tkMessageBox.showinfo("Implantação", "Disposição, em planta, da edificação no terreno, determinante na exposição das fachadas ao sol e aos ventos.")
	clima.mainloop()

def ok_estrategia():
	estrategia.destroy()
def estrategia():
	#tkTop.option_add('*Dialog.msg.font', 'Arial 20')
	#tkMessageBox.showinfo("Afastamento das edificações vizinhas", "Relação entre o afastamento e a altura das edificações vizinhas, caracterizada pelo ângulo (α) em cada orientação. Ângulos menores que 30° significam que a edificação vizinha não influencia na insolação e ventilação. Quando o ângulo é igual a 90°, a edificação está em contato direto com a edificação vizinha.")		
	global estrategia
	estrategia = Toplevel()
	estrategia.resizable(0,0)
	estrategia.configure(background='white')
	estrategia.tk.call('wm', 'iconphoto', estrategia._w, img)
	estrategia.title('Estratégias')

	em_branco = tk.Label(estrategia, text="",background='white') 
	em_branco.grid( row=0, sticky=W)

	j = Image.open("estrategia.png") 
	photo = ImageTk.PhotoImage(j)
	label = tk.Label(estrategia,image=photo, background='white')
	label.image = photo
	label.grid(row=1,sticky=S)
	
	em_branco = tk.Label(estrategia, text="",background='white') 
	em_branco.grid( row=2, sticky=W)

	bt_ok_estrategia = ttk.Button(estrategia, text="Ok",command=ok_estrategia,style='TButton')
	bt_ok_estrategia.grid(row=3,sticky=E,padx=20)

	i = Image.open("logo_p2.png") 
	photo = ImageTk.PhotoImage(i)
	label = tk.Label(estrategia,image=photo, background='white')
	label.image = photo
	label.grid(row=3,sticky=W,padx=20)

	em_branco = tk.Label(estrategia, text="",background='white') 
	em_branco.grid( row=4, sticky=W)

	#tkTop.option_add('*Dialog.msg.font', 'Arial 20')
	#tkMessageBox.showinfo("Implantação", "Disposição, em planta, da edificação no terreno, determinante na exposição das fachadas ao sol e aos ventos.")
	estrategia.mainloop()



##### NÍVEL 1 - INFORMAÇÕES #####

#print font.families()

em_branco = tk.Label(informacoes, text="",background='white') 
em_branco.grid(row=2, sticky=W,padx=40)

texto_info = tk.Label(informacoes,text="Nível 1 - Informações",font=("Arial", "12", "bold"),background='white',fg='#545454')
texto_info.grid(row=3,sticky=W,padx=40)

em_branco = tk.Label(informacoes, text="",background='white') 
em_branco.grid(row=4, sticky=W,padx=40)

nome_projeto = tk.Label(informacoes, text="Nome do projeto",font="Arial 10 bold",background='white',fg='#545454') 
nome_projeto.grid(row=5, sticky=W,padx=40)
nome_projeto_ = Entry(informacoes, width=65,font="Arial 8",background='white',fg='black',borderwidth=0.5)
nome_projeto_.grid(row=6,sticky=W,padx=40)

em_branco = tk.Label(informacoes, text="",background='white',fg='gray') 
em_branco.grid(row=7, sticky=W,padx=40)

descricao = tk.Label(informacoes, text="Descrição",font="Arial 10 bold",background='white',fg='#545454') 
descricao.grid(row=8, sticky=W,padx=40)
descricao_ = Entry(informacoes, width=65,font="Arial 8",background='white',fg='black')
descricao_.grid(row=9,sticky=W,padx=40)

em_branco = tk.Label(informacoes, text="",background='white',fg='gray') 
em_branco.grid(row=10, sticky=W,padx=40)

uso = tk.Label(informacoes, text="Uso ",font="Arial 10 bold",background='white',fg='#545454') 
uso.grid(row=11, sticky=W,padx=40)
us = StringVar()
uso_ = ttk.Combobox(informacoes, textvariable=us, width=63,font="Arial 8",background='white')
uso_['values'] = "Residencial"
#uso_.current(0)
uso_.grid(row=12, sticky=W,padx=40)
em_branco = tk.Label(informacoes, text="",background='white',fg='gray') 
em_branco.grid( row=13, sticky=W,padx=40)

cidade = tk.Label(informacoes, text="Cidade (Zona Bioclimática)",font="Arial 10 bold",background='white',fg='#545454') 
cidade.grid( row=14,sticky=W,padx=40 )
cid = StringVar()
cidade_ = ttk.Combobox(informacoes, textvariable=cid, width=63,font="Arial 8",background='white')
cidade_['values'] = "Zona Bioclimática 2",
#cidade_.current(0)
cidade_.grid( row=15,sticky=W,padx=40)

em_branco = tk.Label(informacoes, text="",background='white',fg='gray') 
em_branco.grid( row=16,sticky=W,padx=40 )

num_ambientes = tk.Label(informacoes, text="Nº de ambientes de permanência prolongada",font="Arial 10 bold",background='white',fg='#545454') 
num_ambientes.grid( row=19,sticky=W,padx=40 )
num_amb = StringVar()
numero_ambientes_ = ttk.Combobox(informacoes, textvariable=num_amb, width=63,font="Arial 8",background='white')
numero_ambientes_['values'] = '1','2','3','4','5','6','7','8','9','10'
#numero_ambientes_.current(0)
numero_ambientes_.grid( row=20,sticky=W,padx=40)
numero_ambientes_.bind("<<ComboboxSelected>>", seleciona_num_area)

#bt_num_ambientes = ttk.Button(informacoes, text="Ok", command=area_dos_ambientes,style='TButton')
#bt_num_ambientes.grid(column=2, row=20,sticky=E)

pos_final = 21
para_printar = 0
n_ambientes = []
n_ambientes_ = []

em_branco = tk.Label(informacoes, text="",background='white') 
em_branco.grid(  row=pos_final, sticky=W)


for i in range(10):
	para_printar = para_printar+1
	pos_final = pos_final+1
	n_ambientes.append(tk.Label(informacoes, text="Nome do ambiente %d" % para_printar,font="Arial 8",background='white',fg='gray'))
	n_ambientes[i].grid( row=pos_final, sticky = W,padx=40)
	n_ambientes_.append(tk.Entry(informacoes, width=44,state='disable',borderwidth=0.5))
	n_ambientes_[i].grid(row=pos_final, sticky = E, padx = 40)

pos_final = pos_final+1

#print para_printar

em_branco = tk.Label(informacoes, text="",background='white') 
em_branco.grid(  row=pos_final, sticky=W)

pos_final = pos_final+1


bt_resultado_1 = ttk.Button(informacoes, text="Clima",command=clima,style='TButton')
bt_resultado_1.grid(row=pos_final,sticky=W, padx=40)
bt_resultado_2 = ttk.Button(informacoes, text="Estratégias",command=estrategia,style='TButton')
bt_resultado_2.grid(row=pos_final,sticky=W, padx=140)
bt_resultado_3 = ttk.Button(informacoes, text="Salvar",style='TButton', command=salvar)
bt_resultado_3.grid(row=pos_final,sticky=E, padx=40)




##### NÍVEL 2 - ENTORNO #####



em_branco = tk.Label(entorno, text="",background='white') 
em_branco.grid(  row=2, sticky=W)

texto_info = tk.Label(entorno,text="Nível 2 - Entorno Imediato",font="Arial 12 bold",background='white',fg='#545454')
texto_info.grid(row=3,sticky=W,padx=40)

em_branco = tk.Label(entorno, text="",background='white') 
em_branco.grid(row=4, sticky=W,padx=40)

desenho_urbano = tk.Label(entorno, text="Desenho urbano",font="Arial 10 bold",background='white',fg='#545454') 
desenho_urbano.grid( row=5, sticky=W,padx=40)
#bt_desenho_info = ttk.Button(entorno,style='TButton',image=imagem_info)
#bt_desenho_info.image = imagem_info
#bt_desenho_info.grid(row=5,sticky=W, padx=150)
desenho_urbano_ = ttk.Combobox(entorno, width=63,font="Arial 8",background='white')
desenho_urbano_['values'] = "Traçado regular, edificações no alinhamento predial","Traçado regular, edificações recuadas","Superquadras com recuos laterais","Torres","Outro"
desenho_urbano_.grid( row=6,stick=W,padx=40)
#desenho_urbano_.bind("<<ComboboxSelected>>", seleciona_desenho_urbano)

em_branco = tk.Label(entorno, text="",background='white') 
em_branco.grid(row=7, sticky=W,padx=40)

topografia = tk.Label(entorno, text="Topografia (sentido da inclinação)",font="Arial 10 bold",background='white',fg='#545454') 
topografia.grid( row=8, sticky=W,padx=40)
#bt_topografia_info = ttk.Button(entorno,style='TButton',image=imagem_info)
#bt_topografia_info.image = imagem_info
#bt_topografia_info.grid(row=8,sticky=W, padx=265)
topografia_ = ttk.Combobox(entorno, width=63,font="Arial 8",background='white')
topografia_['values'] = "Não","Norte","Sul","Leste","Oeste"
topografia_.grid( row=9,stick=W,padx=40)
#topografia_.bind("<<ComboboxSelected>>", seleciona_desenho_urbano)

em_branco = tk.Label(entorno, text="",background='white') 
em_branco.grid( row=10, sticky=W,padx=40)

tipo_de_solo = tk.Label(entorno, text="Tipo de solo",font="Arial 10 bold",background='white',fg='#545454') 
tipo_de_solo.grid( row=11, sticky=W,padx=40)
#bt_solo_info = ttk.Button(entorno,style='TButton',image=imagem_info)
#bt_solo_info.image = imagem_info
#bt_solo_info.grid(row=11,sticky=W, padx=125)
tipo_de_solo_ = ttk.Combobox(entorno, width=63,font="Arial 8",background='white')
tipo_de_solo_['values'] = "Areia","Argila","Saibro","Rocha"
tipo_de_solo_.grid( row=12,stick=W,padx=40)
#tipo_de_solo_.bind("<<ComboboxSelected>>", seleciona_desenho_urbano)

em_branco = tk.Label(entorno, text="",background='white') 
em_branco.grid(  row=13, sticky=W)



##### NÍVEL 3 - IMPLANTAÇÃO #####

def info_implantacao():
	global top_implantacao
	top_implantacao = Toplevel()
	top_implantacao.resizable(0,0)
	top_implantacao.configure(background='white')
	top_implantacao.tk.call('wm', 'iconphoto', top_implantacao._w, img)
	top_implantacao.title('Implantação')

	em_branco = tk.Label(top_implantacao, text="",background='white') 
	em_branco.grid( row=0, sticky=W)

	j = Image.open("implantacao.png") 
	photo = ImageTk.PhotoImage(j)
	label = tk.Label(top_implantacao,image=photo, background='white')
	label.image = photo
	label.grid(row=1,sticky=S)

	bt_ok_implatacao = ttk.Button(top_implantacao, text="Ok",command=ok_top_implantacao,style='TButton')
	bt_ok_implatacao.grid(row=3,sticky=E,padx=20)

	i = Image.open("logo_p2.png") 
	photo = ImageTk.PhotoImage(i)
	label = tk.Label(top_implantacao,image=photo, background='white')
	label.image = photo
	label.grid(row=3,sticky=W,padx=20)

	em_branco = tk.Label(top_implantacao, text="",background='white') 
	em_branco.grid( row=4, sticky=W)

	#tkTop.option_add('*Dialog.msg.font', 'Arial 20')
	#tkMessageBox.showinfo("Implantação", "Disposição, em planta, da edificação no terreno, determinante na exposição das fachadas ao sol e aos ventos.")
	top_implantacao.mainloop()

def info_forma_geral():
	#tkTop.option_add('*Dialog.msg.font', 'Arial 20')
	#tkMessageBox.showinfo("Forma geral", "Disposição espacial da edificação, determinante na área da envoltória, diretamente responsável pelas trocas térmicas entre o edifício e o meio")
	
	global top_forma_geral
	top_forma_geral = Toplevel()
	top_forma_geral.resizable(0,0)
	top_forma_geral.configure(background='white')
	top_forma_geral.tk.call('wm', 'iconphoto', top_forma_geral._w, img)
	top_forma_geral.title('Forma geral')

	em_branco = tk.Label(top_forma_geral, text="",background='white') 
	em_branco.grid( row=0, sticky=W)

	j = Image.open("forma_geral.png") 
	photo = ImageTk.PhotoImage(j)
	label = tk.Label(top_forma_geral,image=photo, background='white')
	label.image = photo
	label.grid(row=1,sticky=S)

	bt_ok_implatacao = ttk.Button(top_forma_geral, text="Ok",command=ok_top_forma_geral,style='TButton')
	bt_ok_implatacao.grid(row=3,sticky=E,padx=20)

	i = Image.open("logo_p2.png") 
	photo = ImageTk.PhotoImage(i)
	label = tk.Label(top_forma_geral,image=photo, background='white')
	label.image = photo
	label.grid(row=3,sticky=W,padx=20)

	em_branco = tk.Label(top_forma_geral, text="",background='white') 
	em_branco.grid( row=4, sticky=W)

	#tkTop.option_add('*Dialog.msg.font', 'Arial 20')
	#tkMessageBox.showinfo("Implantação", "Disposição, em planta, da edificação no terreno, determinante na exposição das fachadas ao sol e aos ventos.")
	top_forma_geral.mainloop()

def info_relacao_solo():
	#tkTop.option_add('*Dialog.msg.font', 'Arial 20')
	#tkMessageBox.showinfo("Relação com o solo", "Caracteriza o contato da edificação com o terreno. Quanto maior o contato com o solo, mais estável termicamente será o edifício e maior a umidade, reduzindo-se as possibilidades de trocas térmicas com o exterior.")
	global top_relacao_solo
	top_relacao_solo = Toplevel()
	top_relacao_solo.resizable(0,0)
	top_relacao_solo.configure(background='white')
	top_relacao_solo.tk.call('wm', 'iconphoto', top_relacao_solo._w, img)
	top_relacao_solo.title('Relação com o solo')

	em_branco = tk.Label(top_relacao_solo, text="",background='white') 
	em_branco.grid( row=0, sticky=W)

	j = Image.open("relacao_solo.png") 
	photo = ImageTk.PhotoImage(j)
	label = tk.Label(top_relacao_solo,image=photo, background='white')
	label.image = photo
	label.grid(row=1,sticky=S)

	bt_ok_implatacao = ttk.Button(top_relacao_solo, text="Ok",command=ok_top_relacao_solo,style='TButton')
	bt_ok_implatacao.grid(row=3,sticky=E,padx=20)

	i = Image.open("logo_p2.png") 
	photo = ImageTk.PhotoImage(i)
	label = tk.Label(top_relacao_solo,image=photo, background='white')
	label.image = photo
	label.grid(row=3,sticky=W,padx=20)

	em_branco = tk.Label(top_relacao_solo, text="",background='white') 
	em_branco.grid( row=4, sticky=W)

	#tkTop.option_add('*Dialog.msg.font', 'Arial 20')
	#tkMessageBox.showinfo("Implantação", "Disposição, em planta, da edificação no terreno, determinante na exposição das fachadas ao sol e aos ventos.")
	top_relacao_solo.mainloop()

def info_afastamento():
	#tkTop.option_add('*Dialog.msg.font', 'Arial 20')
	#tkMessageBox.showinfo("Afastamento das edificações vizinhas", "Relação entre o afastamento e a altura das edificações vizinhas, caracterizada pelo ângulo (α) em cada orientação. Ângulos menores que 30° significam que a edificação vizinha não influencia na insolação e ventilação. Quando o ângulo é igual a 90°, a edificação está em contato direto com a edificação vizinha.")		
	global top_afastamento
	top_afastamento = Toplevel()
	top_afastamento.resizable(0,0)
	top_afastamento.configure(background='white')
	top_afastamento.tk.call('wm', 'iconphoto', top_afastamento._w, img)
	top_afastamento.title('Afastamento das edificações vizinhas')

	em_branco = tk.Label(top_afastamento, text="",background='white') 
	em_branco.grid( row=0, sticky=W)

	j = Image.open("afastamento.png") 
	photo = ImageTk.PhotoImage(j)
	label = tk.Label(top_afastamento,image=photo, background='white')
	label.image = photo
	label.grid(row=1,sticky=S)

	bt_ok_implatacao = ttk.Button(top_afastamento, text="Ok",command=ok_top_afastamento,style='TButton')
	bt_ok_implatacao.grid(row=3,sticky=E,padx=20)

	i = Image.open("logo_p2.png") 
	photo = ImageTk.PhotoImage(i)
	label = tk.Label(top_afastamento,image=photo, background='white')
	label.image = photo
	label.grid(row=3,sticky=W,padx=20)

	em_branco = tk.Label(top_afastamento, text="",background='white') 
	em_branco.grid( row=4, sticky=W)

	#tkTop.option_add('*Dialog.msg.font', 'Arial 20')
	#tkMessageBox.showinfo("Implantação", "Disposição, em planta, da edificação no terreno, determinante na exposição das fachadas ao sol e aos ventos.")
	top_afastamento.mainloop()


path_img1 = "grafico0.png"
img1_nota = ImageTk.PhotoImage(file = path_img1)
#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
label = tk.Label(implantacao,image=img1_nota, background='white')
label.image = img1_nota
label.grid(row=3,sticky = E,padx=40)

em_branco = tk.Label(implantacao, text="",background='white') 
em_branco.grid( row=2, sticky=W,padx=40)

texto_info1 = tk.Label(implantacao,text="Nível 3 - Implantação,\n Traçado e Volumetria",font="Arial 12 bold",background='white',fg='#545454')
texto_info1.grid(row=3,sticky=W,padx=40)

#texto_info2 = tk.Label(implantacao,text="Traçado e Volumetria",font="Arial 12 bold",background='white',fg='#545454')
#texto_info2.grid(row=4,sticky=W)
 
em_branco = tk.Label(implantacao, text="",background='white') 
em_branco.grid( row=5, sticky=W,padx=40)

implantacao_item = tk.Label(implantacao, text="Implantação",font="Arial 10 bold",background='white',fg='#545454') 
implantacao_item.grid( row=6, sticky=W,padx=40)
#noteStyler.configure("TButton",background='white',foreground='white', borderwidth=0,font='Arial 10 bold')
bt_implantacao_info = tk.Button(implantacao,command=info_implantacao,image=imagem_info,borderwidth=0,background='white')
bt_implantacao_info.image = imagem_info
bt_implantacao_info.grid(row=6,sticky=W, padx=125)
implantacao_item_ = ttk.Combobox(implantacao, width=63,font="Arial 8",background='white')
implantacao_item_['values'] = "Em linha, maiores fachadas norte-sul","Em linha, maiores fachadas leste-oeste","Em linha, outras orientações","Compacta","Compacta, com pátio(s) interno(s)"
implantacao_item_.grid( row=7,stick=W,padx=40)
implantacao_item_.bind("<<ComboboxSelected>>", nota_implantacao)

em_branco = tk.Label(implantacao, text="",background='white') 
em_branco.grid( row=8, sticky=W,padx=40)

forma_geral = tk.Label(implantacao, text="Forma geral (volumetria)",font="Arial 10 bold",background='white',fg='#545454') 
forma_geral.grid( row=9, sticky=W,padx=40)
bt_forma_geral_info = tk.Button(implantacao,command=info_forma_geral,image=imagem_info,borderwidth=0,background='white')
bt_forma_geral_info.image = imagem_info
#bt_forma_geral.info.background = 'white'
bt_forma_geral_info.grid(row=9,sticky=W, padx=205)
forma_geral_ = ttk.Combobox(implantacao, width=63,font="Arial 8",background='white')
forma_geral_['values'] = "Forma compacta (prismática)","Forma complexa"
forma_geral_.grid( row=10,stick=W,padx=40)
forma_geral_.bind("<<ComboboxSelected>>", nota_forma)

em_branco = tk.Label(implantacao, text="",background='white') 
em_branco.grid( row=11, sticky=W,padx=40)

relacao_solo = tk.Label(implantacao, text="Relação com o solo",font="Arial 10 bold",background='white',fg='#545454') 
relacao_solo.grid( row=12, sticky=W,padx=40)
bt_relacao_solo_info = tk.Button(implantacao,command=info_relacao_solo,image=imagem_info,borderwidth=0,background='white')
#noteStyler.configure("TButton",background='gray',foreground='#3A8FD7', borderwidth=0,font='Arial 10 bold')
bt_relacao_solo_info.image = imagem_info
bt_relacao_solo_info.grid(row=12,sticky=W, padx=171)
relacao_solo_ = ttk.Combobox(implantacao, width=63,font="Arial 8",background='white')
relacao_solo_['values'] = "Edificação semi-enterrada","Edificação em contato com o solo","Edificação elevada do solo","Edificação elevada do solo com isolamento","Edificação elevada do solo com porão ventilado","Edificação elevada do solo com isolamento e porão ventilado"
relacao_solo_.grid( row=13,stick=W,padx=40)
relacao_solo_.bind("<<ComboboxSelected>>", nota_relacao_solo)

em_branco = tk.Label(implantacao, text="",background='white') 
em_branco.grid( row=14, sticky=W,padx=40)

afastamento = tk.Label(implantacao, text="Afastamento das edificações vizinhas",font="Arial 10 bold",background='white',fg='#545454') 
afastamento.grid( row=15, sticky=W,padx=40)
bt_afastamento_info = tk.Button(implantacao,command=info_afastamento,image=imagem_info,borderwidth=0,background='white')
bt_afastamento_info.image = imagem_info
bt_afastamento_info.grid(row=15,sticky=E, padx=186)

afastamento_norte = tk.Label(implantacao, text="Norte",font="Arial 8",background='white',fg='#545454') 
afastamento_norte.grid( row=17, sticky=W,padx=40)

afastamento_norte_terreo = tk.Label(implantacao, text="Térreo",font="Arial 8",background='white',fg='#9e9e9e') 
afastamento_norte_terreo.grid( row=18, sticky=W,padx=40)
afastamento_norte_terreo_ = ttk.Combobox(implantacao, width=28,font="Arial 8",background='white')
afastamento_norte_terreo_['values'] = "0 < α < 30","30 < α < 45","45 < α < 60","60 < α < 75","75 < α < 90","α = 90"
afastamento_norte_terreo_.grid(  row=19,stick=W,padx=40)
afastamento_norte_terreo_.bind("<<ComboboxSelected>>", nota_afast_norte_ter)

afastamento_norte_sup = tk.Label(implantacao, text="Superior                                                ",font="Arial 8",background='white',fg='#9e9e9e') 
afastamento_norte_sup.grid( row=18, sticky=E,padx=40)
afastamento_norte_sup_ = ttk.Combobox(implantacao, width=28,font="Arial 8",background='white')
afastamento_norte_sup_['values'] = "0 < α < 30","30 < α < 45","45 < α < 60","60 < α < 75","75 < α < 90","α = 90"
afastamento_norte_sup_.grid( row=19,stick=E,padx=40)
afastamento_norte_sup_.bind("<<ComboboxSelected>>", nota_afast_norte_sup)

afastamento_sul = tk.Label(implantacao, text="Sul",font="Arial 8",background='white',fg='#545454') 
afastamento_sul.grid( row=21, sticky=W,padx=40)

afastamento_sul_terreo = tk.Label(implantacao, text="Térreo",font="Arial 8",background='white',fg='#9e9e9e') 
afastamento_sul_terreo.grid( row=22, sticky=W,padx=40)
afastamento_sul_terreo_ = ttk.Combobox(implantacao, width=28,font="Arial 8",background='white')
afastamento_sul_terreo_['values'] = "0 < α < 30","30 < α < 45","45 < α < 60","60 < α < 75","75 < α < 90","α = 90"
afastamento_sul_terreo_.grid( row=23,stick=W,padx=40)
afastamento_sul_terreo_.bind("<<ComboboxSelected>>", nota_afast_sul_ter)

afastamento_sul_sup = tk.Label(implantacao, text="Superior                                                ",font="Arial 8",background='white',fg='#9e9e9e') 
afastamento_sul_sup.grid( row=22, sticky=E,padx=40)
afastamento_sul_sup_ = ttk.Combobox(implantacao, width=28,font="Arial 8",background='white')
afastamento_sul_sup_['values'] = "0 < α < 30","30 < α < 45","45 < α < 60","60 < α < 75","75 < α < 90","α = 90"
afastamento_sul_sup_.grid( row=23,stick=E,padx=40)
afastamento_sul_sup_.bind("<<ComboboxSelected>>", nota_afast_sul_sup)

afastamento_leste = tk.Label(implantacao, text="Leste",font="Arial 8",background='white',fg='#545454') 
afastamento_leste.grid( row=25, sticky=W,padx=40)

afastamento_leste_terreo = tk.Label(implantacao, text="Térreo",font="Arial 8",background='white',fg='#9e9e9e') 
afastamento_leste_terreo.grid( row=26, sticky=W,padx=40)
afastamento_leste_terreo_ = ttk.Combobox(implantacao, width=28,font="Arial 8",background='white')
afastamento_leste_terreo_['values'] = "0 < α < 30","30 < α < 45","45 < α < 60","60 < α < 75","75 < α < 90","α = 90"
afastamento_leste_terreo_.grid( row=27,stick=W,padx=40)
afastamento_leste_terreo_.bind("<<ComboboxSelected>>", nota_afast_leste_ter)

afastamento_leste_sup = tk.Label(implantacao, text="Superior                                                ",font="Arial 8",background='white',fg='#9e9e9e') 
afastamento_leste_sup.grid( row=26, sticky=E,padx=40)
afastamento_leste_sup_ = ttk.Combobox(implantacao, width=28,font="Arial 8",background='white')
afastamento_leste_sup_['values'] = "0 < α < 30","30 < α < 45","45 < α < 60","60 < α < 75","75 < α < 90","α = 90"
afastamento_leste_sup_.grid( row=27,stick=E,padx=40)
afastamento_leste_sup_.bind("<<ComboboxSelected>>", nota_afast_leste_sup)

afastamento_oeste = tk.Label(implantacao, text="Oeste",font="Arial 8",background='white',fg='#545454') 
afastamento_oeste.grid( row=28, sticky=W,padx=40)

afastamento_oeste_terreo = tk.Label(implantacao, text="Térreo",font="Arial 8",background='white',fg='#9e9e9e') 
afastamento_oeste_terreo.grid( row=29, sticky=W,padx=40)
afastamento_oeste_terreo_ = ttk.Combobox(implantacao, width=28,font="Arial 8",background='white')
afastamento_oeste_terreo_['values'] = "0 < α < 30","30 < α < 45","45 < α < 60","60 < α < 75","75 < α < 90","α = 90"
afastamento_oeste_terreo_.grid( row=30,stick=W,padx=40)
afastamento_oeste_terreo_.bind("<<ComboboxSelected>>", nota_afast_oeste_ter)

afastamento_oeste_sup = tk.Label(implantacao, text="Superior                                                ",font="Arial 8",background='white',fg='#9e9e9e') 
afastamento_oeste_sup.grid( row=29, sticky=E,padx=40)
afastamento_oeste_sup_ = ttk.Combobox(implantacao, width=28,font="Arial 8",background='white')
afastamento_oeste_sup_['values'] = "0 < α < 30","30 < α < 45","45 < α < 60","60 < α < 75","75 < α < 90","α = 90"
afastamento_oeste_sup_.grid( row=30,stick=E,padx=40)
afastamento_oeste_sup_.bind("<<ComboboxSelected>>", nota_afast_oeste_sup)

em_branco = tk.Label(implantacao, text="",background='white') 
em_branco.grid(row=31, sticky=W,padx=40)
	


##### NÍVEL 4 - ENVOLTÓRIA #####


em_branco = tk.Label(envoltoria, text="",background='white') 
em_branco.grid( row=2, sticky=W,padx=40)

path_img1 = "grafico0.png"
img1_nota = ImageTk.PhotoImage(file = path_img1)
#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
label = tk.Label(envoltoria,image=img1_nota, background='white')
label.image = img1_nota
label.grid(row=3,  sticky=E,padx=40)


texto_info = tk.Label(envoltoria,text="Nível 4 - Envoltória",font="Arial 12 bold",background='white',fg='#545454')
texto_info.grid(row=3,sticky=W,padx=40)

em_branco = tk.Label(envoltoria, text="",background='white') 
em_branco.grid( row=4, sticky=W,padx=40)

estrutura = tk.Label(envoltoria, text="Estrutura",font="Arial 10 bold",background='white',fg='#545454') 
estrutura.grid( row=5, sticky=W,padx=40)
estrutura_ = ttk.Combobox(envoltoria, width=63,font="Arial 8",background='white')
estrutura_['values'] = "Concreto armado, sem pontes térmicas", "Concreto armado, com pontes térmicas", "Blocos cerâmicos auto-portantes", "Metálica, sem pontes térmicas", "Metálica, com pontes térmicas", "Madeira"
estrutura_.grid( row=6,stick=W,padx=40)
estrutura_.bind("<<ComboboxSelected>>", nota_estrutura)

em_branco = tk.Label(envoltoria, text="",background='white') 
em_branco.grid( row=7, sticky=W,padx=40)

parede = tk.Label(envoltoria, text="Paredes",font="Arial 10 bold",background='white',fg='#545454') 
parede.grid( row=8, sticky=W,padx=40)

u_parede = tk.Label(envoltoria, text="Transmitância térmica ",font="Arial 8 ",background='white',fg='#545454') 
u_parede.grid( row=9, sticky=W,padx=40)
u_parede_ = ttk.Combobox(envoltoria, width=18,font="Arial 8",background='white')
u_parede_['values'] = "U < 1,5", "1,5 < U < 2,0", "U > 2,0"
u_parede_.grid( row=10,stick=W,padx=40)
u_parede_.bind("<<ComboboxSelected>>", nota_u_parede)

ct_parede = tk.Label(envoltoria, text="Capacidade térmica         ",font="Arial 8 ",background='white',fg='#545454') 
ct_parede.grid( row=9, sticky=S,padx=40)
ct_parede_ = ttk.Combobox(envoltoria, width=18,font="Arial 8",background='white')
ct_parede_['values'] = "CT < 130", "CT > 130"
ct_parede_.grid( row=10,stick=S,padx=40)
ct_parede_.bind("<<ComboboxSelected>>", nota_ct_parede)

cor_parede = tk.Label(envoltoria, text="Cor                                   ",font="Arial 8 ",background='white',fg='#545454') 
cor_parede.grid( row=9, sticky=E,padx=40)
cor_parede_ = ttk.Combobox(envoltoria, width=18,font="Arial 8",background='white')
cor_parede_['values'] = "Tons claros (α<0,4)","Tons médios (0,4<α<0,7)","Tons escuros (α>0,7)"
cor_parede_.grid( row=10,stick=E,padx=40)
cor_parede_.bind("<<ComboboxSelected>>", nota_cor_parede)

em_branco = tk.Label(envoltoria, text="",background='white') 
em_branco.grid( row=11, sticky=W,padx=40)

cobertura = tk.Label(envoltoria, text="Cobertura",font="Arial 10 bold",background='white',fg='#545454') 
cobertura.grid( row=12, sticky=W,padx=40)

u_cobertura = tk.Label(envoltoria, text="Transmitância térmica",font="Arial 8 ",background='white',fg='#545454') 
u_cobertura.grid( row=13, sticky=W,padx=40)
u_cobertura_ = ttk.Combobox(envoltoria, width=28,font="Arial 8",background='white')
u_cobertura_['values'] = "U < 1,5", "1,5 < U < 2,0", "U > 2,0"
u_cobertura_.grid( row=14,stick=W,padx=40)
u_cobertura_.bind("<<ComboboxSelected>>", nota_u_cobertura)

#ct_cobertura = tk.Label(envoltoria, text="Capacidade térmica:        ",font="Arial 8 ",background='white',fg='#545454') 
#ct_cobertura.grid(  row=13, sticky=S)
#ct_cobertura_ = ttk.Combobox(envoltoria, width=18,font="Arial 8",background='white')
#ct_cobertura_['values'] = "CT < 130", "CT > 130"
#ct_cobertura_.grid(  row=14,stick=S)
#ct_cobertura_.bind("<<ComboboxSelected>>", seleciona_desenho_urbano)

cor_cobertura = tk.Label(envoltoria, text="Cor                                                       ",font="Arial 8 ",background='white',fg='#545454') 
cor_cobertura.grid( row=13, sticky=E,padx=40)
cor_cobertura_ = ttk.Combobox(envoltoria, width=28,font="Arial 8",background='white')
cor_cobertura_['values'] = "Tons claros (α<0,4)","Tons médios (0,4<α<0,7)","Tons escuros (α>0,7)"
cor_cobertura_.grid( row=14,stick=E,padx=40)
cor_cobertura_.bind("<<ComboboxSelected>>", nota_cor_cobertura)

em_branco = tk.Label(envoltoria, text="",background='white') 
em_branco.grid( row=15, sticky=W,padx=40)

abertura = tk.Label(envoltoria, text="Aberturas",font="Arial 10 bold",background='white',fg='#545454') 
abertura.grid( row=16, sticky=W,padx=40)

tipo_abertura = tk.Label(envoltoria, text="Tipo de abertura",font="Arial 8 ",background='white',fg='#545454') 
tipo_abertura.grid( row=17, sticky=W,padx=40)
tipo_abertura_ = ttk.Combobox(envoltoria, width=18,font="Arial 8",background='white')
tipo_abertura_['values'] = "PVC","Madeira","Metálica"
tipo_abertura_.grid( row=18,stick=W,padx=40)
tipo_abertura_.bind("<<ComboboxSelected>>", nota_tipo_abertura)

vidro = tk.Label(envoltoria, text="Tipo de vidro                   ",font="Arial 8 ",background='white',fg='#545454') 
vidro.grid( row=17, sticky=S,padx=40)
vidro_ = ttk.Combobox(envoltoria, width=18,font="Arial 8",background='white')
vidro_['values'] = "Simples","Duplo"
vidro_.grid( row=18,stick=S,padx=40)
vidro_.bind("<<ComboboxSelected>>", nota_vidro)

estanqueidade = tk.Label(envoltoria, text="Estanqueidade                 ",font="Arial 8 ",background='white',fg='#545454') 
estanqueidade.grid( row=17, sticky=E,padx=40)
estanqueidade_ = ttk.Combobox(envoltoria, width=18,font="Arial 8",background='white')
estanqueidade_['values'] = "Muito estanque","Pouco estanque"
estanqueidade_.grid( row=18,stick=E,padx=40)
estanqueidade_.bind("<<ComboboxSelected>>", nota_estanqueidade)

em_branco = tk.Label(envoltoria, text="",background='white') 
em_branco.grid( row=19, sticky=W,padx=40)

area_de_ilumina_area_fachada = tk.Label(envoltoria, text="Área de iluminação\npor área de fachada",font="Arial 8",background='white',fg='#545454') 
area_de_ilumina_area_fachada.grid(row=20, sticky=W,padx=40)

#area_de_ventila_area_fachada = tk.Label(envoltoria, text="Area de ventilação por área de fachada:",font="Arial 8",background='white',fg='#545454') 
#area_de_ventila_area_fachada.grid(  row=20, sticky=E)

iluminacao_norte = tk.Label(envoltoria, text="Norte",font="Arial 8 ",background='white',fg='#9e9e9e') 
iluminacao_norte.grid( row=21, sticky=W,padx=40)
iluminacao_norte_ = ttk.Combobox(envoltoria, width=28,font="Arial 8",background='white')
iluminacao_norte_['values'] = "< 20%", "20% - 40%", "> 40%"
iluminacao_norte_.grid( row=22,stick=W,padx=40)
iluminacao_norte_.bind("<<ComboboxSelected>>", nota_iluminacao_norte)

iluminacao_sul = tk.Label(envoltoria, text="Sul",font="Arial 8 ",background='white',fg='#9e9e9e') 
iluminacao_sul.grid( row=23, sticky=W,padx=40)
iluminacao_sul_ = ttk.Combobox(envoltoria, width=28,font="Arial 8",background='white')
iluminacao_sul_['values'] = "< 20%", "20% - 40%", "> 40%"
iluminacao_sul_.grid( row=24,stick=W,padx=40)
iluminacao_sul_.bind("<<ComboboxSelected>>", nota_iluminacao_sul)

iluminacao_leste = tk.Label(envoltoria, text="Leste",font="Arial 8 ",background='white',fg='#9e9e9e') 
iluminacao_leste.grid( row=25, sticky=W,padx=40)
iluminacao_leste_ = ttk.Combobox(envoltoria, width=28,font="Arial 8",background='white')
iluminacao_leste_['values'] = "< 20%", "20% - 40%", "> 40%"
iluminacao_leste_.grid( row=26,stick=W,padx=40)
iluminacao_leste_.bind("<<ComboboxSelected>>", nota_iluminacao_leste)

iluminacao_oeste = tk.Label(envoltoria, text="Oeste",font="Arial 8 ",background='white',fg='#9e9e9e') 
iluminacao_oeste.grid( row=27, sticky=W,padx=40)
iluminacao_oeste_ = ttk.Combobox(envoltoria, width=28,font="Arial 8",background='white')
iluminacao_oeste_['values'] = "< 20%", "20% - 40%", "> 40%"
iluminacao_oeste_.grid( row=28,stick=W,padx=40)
iluminacao_oeste_.bind("<<ComboboxSelected>>", nota_iluminacao_oeste)


area_de_ventila_area_parede = tk.Label(envoltoria, text=" Área de ventilação                            \npor área de fachada                             ",font="Arial 8",background='white',fg='#545454') 
area_de_ventila_area_parede.grid(  row=20, sticky=E,padx=40)

#area_de_ventila_area_fachada = tk.Label(envoltoria, text="Area de ventilação por área de fachada:",font="Arial 8",background='white',fg='#545454') 
#area_de_ventila_area_fachada.grid(  row=20, sticky=E)

ventilacao_norte = tk.Label(envoltoria, text="Norte                                                    ",font="Arial 8 ",background='white',fg='#9e9e9e') 
ventilacao_norte.grid( row=21, sticky=E,padx=40)
ventilacao_norte_ = ttk.Combobox(envoltoria, width=28,font="Arial 8",background='white')
ventilacao_norte_['values'] = "< 10%", "10% - 20%", "> 20%"
ventilacao_norte_.grid( row=22,stick=E,padx=40)
ventilacao_norte_.bind("<<ComboboxSelected>>", nota_ventilacao_norte)

ventilacao_sul = tk.Label(envoltoria, text="Sul                                                        ",font="Arial 8 ",background='white',fg='#9e9e9e') 
ventilacao_sul.grid( row=23, sticky=E,padx=40)
ventilacao_sul_ = ttk.Combobox(envoltoria, width=28,font="Arial 8",background='white')
ventilacao_sul_['values'] = "< 10%", "10% - 20%", "> 20%"
ventilacao_sul_.grid( row=24,stick=E,padx=40)
ventilacao_sul_.bind("<<ComboboxSelected>>", nota_ventilacao_sul)

ventilacao_leste = tk.Label(envoltoria, text="Leste                                                    ",font="Arial 8 ",background='white',fg='#9e9e9e') 
ventilacao_leste.grid( row=25, sticky=E,padx=40)
ventilacao_leste_ = ttk.Combobox(envoltoria, width=28,font="Arial 8",background='white')
ventilacao_leste_['values'] = "< 10%", "10% - 20%", "> 20%"
ventilacao_leste_.grid( row=26,stick=E,padx=40)
ventilacao_leste_.bind("<<ComboboxSelected>>", nota_ventilacao_leste)

ventilacao_oeste = tk.Label(envoltoria, text="Oeste                                                    ",font="Arial 8 ",background='white',fg='#9e9e9e') 
ventilacao_oeste.grid( row=27, sticky=E,padx=40)  
ventilacao_oeste_ = ttk.Combobox(envoltoria, width=28,font="Arial 8",background='white')
ventilacao_oeste_['values'] = "< 10%", "10% - 20%", "> 20%"
ventilacao_oeste_.grid( row=28,stick=E,padx=40)
ventilacao_oeste_.bind("<<ComboboxSelected>>", nota_ventilacao_oeste)

em_branco = tk.Label(envoltoria, text="",background='white') 
em_branco.grid( row=37, sticky=W,padx=40)


##### NÍVEL 5 - AMBIENTES INTERNOS #####

em_branco = tk.Label(ambientes, text="",background='white') 
em_branco.grid( row=1, sticky=W,padx=40)

path_img1 = "grafico0.png"
img1_nota = ImageTk.PhotoImage(file = path_img1)
#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
label = tk.Label(ambientes,image=img1_nota, background='white')
label.image = img1_nota
label.grid(row=2,  sticky=E,padx=40)

texto_info1 = tk.Label(ambientes,text="Nível 5 - Ambientes Internos",font="Arial 12 bold",background='white',fg='#545454')
texto_info1.grid(row=2,sticky=W,padx=40)

#print font.families()
em_branco = tk.Label(ambientes, text="",background='white') 
em_branco.grid( row=3, sticky=W,padx=40)

amb_ambiente = tk.Label(ambientes, text="Selecione um ambiente",font="Arial 10 bold",background='white',fg='#545454') 
amb_ambiente.grid( row=4, sticky=W,padx=40)

amb_ambiente_ = ttk.Combobox(ambientes, width=63,font="Arial 8",background='white')
amb_ambiente_['values'] = ''
amb_ambiente_.grid( row=5,stick=W,padx=40)
amb_ambiente_.bind("<<ComboboxSelected>>", seleciona_ambiente)

'''
path_img2 = "grafico1.png"
img2_nota = ImageTk.PhotoImage(file = path_img2)
#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
label = tk.Label(nota_final,image=img2_nota, background='white')
label.image = img2_nota
label.grid(column=2,row=3,sticky = S, padx = 40, pady =200)
'''

##### NOTA FINAL #####

em_branco = tk.Label(nota_final, text="",background='white') 
em_branco.grid( row=0, sticky=W,padx=40)

i = Image.open("_logo.png") 
i = i.resize((160,45),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(i)
label = tk.Label(nota_final,image=photo, background='white')
label.image = photo
label.grid(row=1,sticky=S,padx=130,pady=30)

em_branco = tk.Label(nota_final, text="",background='white') 
em_branco.grid( row=2, sticky=W,padx=40)
em_branco = tk.Label(nota_final, text="",background='white') 
em_branco.grid( row=3, sticky=W,padx=40)
em_branco = tk.Label(nota_final, text="",background='white') 
em_branco.grid( row=4, sticky=W,padx=40)

texto_final = tk.Label(nota_final,text="Avaliação Final",font='Arial 12 bold',background='white',fg='#545454')
texto_final.grid(row=6,sticky=S,padx=80)

path_img1 = "grafico_g_0.png"
img1_nota = ImageTk.PhotoImage(file = path_img1)
#img1_nota = img1_nota.resize((20, 20),Image.ANTIALIAS)
label = tk.Label(nota_final,image=img1_nota, background='white')
label.image = img1_nota
label.grid(row=7,sticky=S,padx=80)

em_branco = tk.Label(nota_final, text="",background='white') 
em_branco.grid( row=8, sticky=W,padx=40)

bt_log = ttk.Button(nota_final, text="      Gerar Relatório       ",command= gerar_relatorio,style='TButton')
bt_log.grid(row=9,sticky=S, padx=80)

em_branco = tk.Label(nota_final, text="",background='white') 
em_branco.grid( row=10, sticky=W,padx=40)
em_branco = tk.Label(nota_final, text="",background='white') 
em_branco.grid( row=11, sticky=W,padx=40)
em_branco = tk.Label(nota_final, text="",background='white') 
em_branco.grid( row=12, sticky=W,padx=40)
em_branco = tk.Label(nota_final, text="",background='white') 
em_branco.grid( row=13, sticky=W,padx=40)

i = Image.open("_logos.png") 
#i = i.resize((200,60),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(i)
label = tk.Label(nota_final,image=photo, background='white')
label.image = photo
label.grid(row=14,sticky=S,padx=80)

#Tktop.report_callback_extension
tk.mainloop()
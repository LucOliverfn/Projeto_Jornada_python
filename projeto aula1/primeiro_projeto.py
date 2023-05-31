from fpdf import FPDF

projeto = str(input ("Digite o nome do projeto :"))
horas_estimadas = float(input ("Digite o total de horas estimadas :"))
valor_hora = float(input ("Digite o valor da hora :"))
prazo = str(input ("Digite em meses quanto sera o prazo para a entrega :"))
nome = str(input("Qual o nome do arquivo? :"))
total = valor_hora * horas_estimadas
# falando que a variavel pdf é o objeto do FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")
pdf.image ("template.png",x=0, y=0)

# adicionando textos ao pdf (primeiro numero é x e y é o segundo )
# sendo que x é coluna e y é linha
pdf.text(115,145,projeto)
pdf.text(115,160,str(horas_estimadas))
pdf.text(115,175,str(valor_hora))
pdf.text(115,190,prazo)
pdf.text(115,205, str(total))

pdf.output(f'{nome}.pdf')
print("Orçamento Gerado com sucesso!!!!!!!!!")

from fpdf import FPDF

projeto = input("Digite a descrição do projeto: ")
horas_trabalhadas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digie o valor de horas trabalhadas: ")
prazo = input("Digite o prazo estimado: ")

valor_total = int(horas_trabalhadas) * int(valor_hora)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png", x=0, y=0)

pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_trabalhadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output("Orçamento.pdf")
print ("Orçamento gerado com sucesso!")
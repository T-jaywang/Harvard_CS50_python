from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", style="B", size=30)
        pdf.set_xy(0, 10)
        self.cell(0, 20, "CS50 Shirtificate",align= "C")
    
name = input("Name: ")

pdf = PDF()
pdf.add_page()

page_width = pdf.w
img_width = 180
x = (page_width - img_width) / 2
y = 90

pdf.image("shirtificate.png", x=x, y=y, w=img_width)

pdf.set_font("Helvetica", style="B", size=20)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(0, y+60)
pdf.cell(page_width, 15, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")


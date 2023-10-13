from fpdf import FPDF
#########################################################
A4_HEIGHT = 297
A4_WIDTH = 210
#########################################################
list_gesucht={'Vorname':"",
            'Nachname':"",
            'Wohnort': "",
            'Alter': "",
            'Größe': "",
            'Gestalt': "",
            'Haar':"",
            'Augenfarbe': "",
            'ZuletztgesehenWann':"",
            'ZuletztgesehenWo':"",
            'Zustand':"",
            'Bekleidung':"",
            'Fortbewegung':"",
            'Sonstiges':"",}

list_sonst={'Dateiname':"Steckbrief",
            'Abschnittleiter':"",
            'Funk1':"",
            'Funk2':"",
            'Funk3': "",
            'Ansprechpartner': "",
            'Mobil1': "",
            'Mobil2': "",
             'StandortEL':"",}
####################################################################
# class PDF(FPDF)
# Define Header and Footer of the PDF
#
####################################################################
class PDF(FPDF):
    def header(self):
        # Select Arial bold 15
        self.set_font('Arial', 'B', 15)

        #self.cell(0, 15, 'Title', 1, 0, 'C')
        pdf.cell(0, 10,link=pdf.image('Header.png',None,10,190))
        # Line break
        self.ln(40)


pdf = PDF(format="A4")
pdf.add_page()
pdf.set_font('helvetica', size=12)            
pdf.cell(0,20, txt="hello world", ln=True, border=True)

pdf.add_page()
pdf.output(list_sonst["Dateiname"] + ".pdf")
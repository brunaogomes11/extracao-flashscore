
paises_campeonatos = [
    {
        "País":"Europa",
        "Campeonatos":[
            {"Nome":"Liga dos Campeões", "inicio":1989, "fim": 2024, "label":'liga-dos-campeoes'},
            {"Nome":"Liga Europa", "inicio":1989, "fim": 2024, "label":'liga-europa'},
            {"Nome":"Liga da Conferência Europeia", "inicio":2021, "fim": 2024, "label":'liga-da-conferencia-europei'},
        ]
    },
    {
        "País":"Alemanha",
        "Campeonatos":[
            {"Nome":"Bundesliga", "inicio":1989, "fim": 2024, "label":'bundesliga'},
            {"Nome":"Bundesliga 2", "inicio":1989, "fim": 2024, "label":'2-bundesliga'},
        ]
    },
    {
        "País":"Espanha",
        "Campeonatos":[
            {"Nome":"LaLiga", "inicio":1989, "fim": 2024, "label":'laliga'},
            {"Nome":"LaLiga 2", "inicio":1989, "fim": 2024, "label":'laliga2'},
        ]
    },
    {
        "País":"França",
        "Campeonatos":[
            {"Nome":"Ligue 1", "inicio":1989, "fim": 2024, "label":'ligue-1'},
            {"Nome":"Ligue 2", "inicio":1989, "fim": 2024, "label":'ligue-2'},
        ]
    },
    {
        "País":"Inglaterra",
        "Campeonatos":[
            {"Nome":"Premier League", "inicio":1989, "fim": 2024, "label":'campeonato-ingles'},
            {"Nome":"Championship", "inicio":1989, "fim": 2024, "label":'2-divisao'},
        ]
    },
    {
        "País":"Italia",
        "Campeonatos":[
            {"Nome":"Série A", "inicio":1989, "fim": 2024, "label":'serie-a'},
            {"Nome":"Série B", "inicio":1989, "fim": 2024, "label":'serie-b'},
        ]
    },
    # {
    #     "País":"Brasil",
    #     "Campeonatos":[
    #         {"Nome":"Série A", "inicio":1998, "fim": 2024, "label":'serie-a'},
    #         {"Nome":"Série B", "inicio":1989, "fim": 2024, "label":'serie-b'},
    #     ]
    # },
]
from everyRounds import get_data_from_tournament
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QPushButton, QSplitter,
    QTextEdit, QWidget, QVBoxLayout)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(806, 614)
        font = QFont()
        font.setFamilies([u"Leelawadee UI"])
        Main.setFont(font)
        Main.setMinimumSize(QSize(806, 614))
        Main.setMaximumSize(QSize(806, 614))
        self.gridLayout = QGridLayout(Main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tituloLabel = QLabel(Main)
        self.tituloLabel.setObjectName(u"tituloLabel")
        self.tituloLabel.setMinimumSize(QSize(200, 30))
        self.tituloLabel.setMaximumSize(QSize(200, 30))
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(12)
        self.tituloLabel.setFont(font1)
        self.tituloLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.tituloLabel, 0, 0, 1, 1, Qt.AlignHCenter)

        self.logo = QLabel(Main)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(200, 30))
        self.logo.setStyleSheet(u"")
        self.logo.setPixmap(QPixmap("./image/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.logo, 1, 0, 1, 1, Qt.AlignHCenter)

        self.paisLabel = QLabel(Main)
        self.paisLabel.setObjectName(u"paisLabel")
        self.paisLabel.setMinimumSize(QSize(49, 16))
        self.paisLabel.setMaximumSize(QSize(300, 25))
        font2 = QFont()
        font2.setFamilies([u"Leelawadee UI"])
        font2.setPointSize(12)
        self.paisLabel.setFont(font2)
        self.paisLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.paisLabel, 2, 0, 1, 1)

        self.paisCB = QComboBox(Main)
        for i in range(0, len(paises_campeonatos)+1):
            self.paisCB.addItem("")
        self.paisCB.setObjectName(u"paisCB")
        self.paisCB.activated.connect(self.mudarCampeonatos)
        self.paisCB.setMaximumSize(QSize(300, 30))

        self.gridLayout.addWidget(self.paisCB, 3, 0, 1, 1)

        self.campeonatoLabel = QLabel(Main)
        self.campeonatoLabel.setObjectName(u"campeonatoLabel")
        self.campeonatoLabel.setMinimumSize(QSize(49, 16))
        self.campeonatoLabel.setMaximumSize(QSize(300, 25))
        self.campeonatoLabel.setFont(font2)
        self.campeonatoLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.campeonatoLabel, 4, 0, 1, 1)

        self.campeonatoCB = QComboBox(Main)
        self.campeonatoCB.addItem("")
        self.campeonatoCB.addItem("")
        self.campeonatoCB.setObjectName(u"campeonatoCB")
        self.campeonatoCB.activated.connect(self.mudarTemporadas)
        self.campeonatoCB.setEnabled(False)
        self.campeonatoCB.setMaximumSize(QSize(300, 30))

        self.gridLayout.addWidget(self.campeonatoCB, 5, 0, 1, 1)

        self.temporadaLabel = QLabel(Main)
        self.temporadaLabel.setObjectName(u"temporadaLabel")
        self.temporadaLabel.setMinimumSize(QSize(49, 16))
        self.temporadaLabel.setMaximumSize(QSize(300, 25))
        self.temporadaLabel.setFont(font2)
        self.temporadaLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.temporadaLabel, 6, 0, 1, 1)

        self.tempCB = QComboBox(Main)
        self.tempCB.addItem("")
        self.tempCB.setObjectName(u"tempCB")
        self.tempCB.setEnabled(False)
        self.tempCB.setMaximumSize(QSize(300, 30))

        self.gridLayout.addWidget(self.tempCB, 7, 0, 1, 1)

        self.nomeDSLabel = QLabel(Main)
        self.nomeDSLabel.setObjectName(u"nomeDSLabel")
        self.nomeDSLabel.setMinimumSize(QSize(49, 16))
        self.nomeDSLabel.setMaximumSize(QSize(300, 25))
        self.nomeDSLabel.setFont(font2)
        self.nomeDSLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.nomeDSLabel, 8, 0, 1, 1)

        self.textEdit = QTextEdit(Main)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(300, 30))

        self.gridLayout.addWidget(self.textEdit, 9, 0, 1, 1)

        self.temposLabel = QLabel(Main)
        self.temposLabel.setObjectName(u"temposLabel")
        self.temposLabel.setMinimumSize(QSize(49, 16))
        self.temposLabel.setMaximumSize(QSize(300, 25))
        self.temposLabel.setFont(font2)
        self.temposLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.temposLabel, 10, 0, 1, 1)

        self.splitter = QSplitter(Main)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.full_timeCB = QCheckBox(self.splitter)
        self.full_timeCB.setObjectName(u"full_timeCB")
        self.full_timeCB.setMaximumSize(QSize(16777215, 30))
        self.splitter.addWidget(self.full_timeCB)
        self.first_timeCB = QCheckBox(self.splitter)
        self.first_timeCB.setObjectName(u"first_timeCB")
        self.first_timeCB.setMaximumSize(QSize(16777215, 30))
        self.splitter.addWidget(self.first_timeCB)
        self.second_timeCB = QCheckBox(self.splitter)
        self.second_timeCB.setObjectName(u"second_timeCB")
        self.second_timeCB.setMaximumSize(QSize(16777215, 30))
        self.full_timeCB.stateChanged.connect(self.ativarGerar)
        self.first_timeCB.stateChanged.connect(self.ativarGerar)
        self.second_timeCB.stateChanged.connect(self.ativarGerar)
        
        self.splitter.addWidget(self.second_timeCB)

        self.gridLayout.addWidget(self.splitter, 11, 0, 1, 1)

        self.gerarButton = QPushButton(Main)
        self.gerarButton.setObjectName(u"gerarButton")
        self.gerarButton.setEnabled(False)
        self.gerarButton.setMinimumSize(QSize(200, 50))
        self.gerarButton.setMaximumSize(QSize(200, 50))
        self.gerarButton.setFont(font2)
        self.gerarButton.clicked.connect(self.verificarInput)

        self.gridLayout.addWidget(self.gerarButton, 12, 0, 1, 1, Qt.AlignHCenter)
        # self.progressBar = QProgressBar(Main)
        # self.progressBar.setObjectName(u"progressBar")
        # self.gerarButton.clicked.connect(self.verificarInput)
        # self.progressBar.setValue(0)

        # self.gridLayout.addWidget(self.progressBar, 13, 0, 1, 1)
        
        self.Estatisticas = QVBoxLayout()
        self.Estatisticas.setObjectName(u"Estatisticas")
        self.est1 = QCheckBox(Main)
        self.est1.setObjectName(u"est1")
        self.est1.setChecked(True)

        self.Estatisticas.addWidget(self.est1)

        self.est2 = QCheckBox(Main)
        self.est2.setObjectName(u"est2")
        self.est2.setChecked(True)

        self.Estatisticas.addWidget(self.est2)

        self.est3 = QCheckBox(Main)
        self.est3.setObjectName(u"est3")
        self.est3.setChecked(True)

        self.Estatisticas.addWidget(self.est3)

        self.est4 = QCheckBox(Main)
        self.est4.setObjectName(u"est4")
        self.est4.setChecked(True)

        self.Estatisticas.addWidget(self.est4)

        self.est5 = QCheckBox(Main)
        self.est5.setObjectName(u"est5")
        self.est5.setChecked(True)

        self.Estatisticas.addWidget(self.est5)

        self.est6 = QCheckBox(Main)
        self.est6.setObjectName(u"est6")
        self.est6.setChecked(True)

        self.Estatisticas.addWidget(self.est6)

        self.estt7 = QCheckBox(Main)
        self.estt7.setObjectName(u"estt7")
        self.estt7.setChecked(True)

        self.Estatisticas.addWidget(self.estt7)

        self.est8 = QCheckBox(Main)
        self.est8.setObjectName(u"est8")
        self.est8.setChecked(True)

        self.Estatisticas.addWidget(self.est8)

        self.est9 = QCheckBox(Main)
        self.est9.setObjectName(u"est9")
        self.est9.setChecked(True)

        self.Estatisticas.addWidget(self.est9)

        self.est10 = QCheckBox(Main)
        self.est10.setObjectName(u"est10")
        self.est10.setChecked(True)

        self.Estatisticas.addWidget(self.est10)

        self.est11 = QCheckBox(Main)
        self.est11.setObjectName(u"est11")
        self.est11.setChecked(True)

        self.Estatisticas.addWidget(self.est11)

        self.est12 = QCheckBox(Main)
        self.est12.setObjectName(u"est12")
        self.est12.setChecked(True)

        self.Estatisticas.addWidget(self.est12)

        self.est13 = QCheckBox(Main)
        self.est13.setObjectName(u"est13")
        self.est13.setChecked(True)

        self.Estatisticas.addWidget(self.est13)

        self.est14 = QCheckBox(Main)
        self.est14.setObjectName(u"est14")
        self.est14.setChecked(True)

        self.Estatisticas.addWidget(self.est14)

        self.est15 = QCheckBox(Main)
        self.est15.setObjectName(u"est15")
        self.est15.setChecked(True)

        self.Estatisticas.addWidget(self.est15)

        self.est16 = QCheckBox(Main)
        self.est16.setObjectName(u"est16")
        self.est16.setChecked(True)

        self.Estatisticas.addWidget(self.est16)

        self.est17 = QCheckBox(Main)
        self.est17.setObjectName(u"est17")
        self.est17.setChecked(True)

        self.Estatisticas.addWidget(self.est17)


        self.gridLayout.addLayout(self.Estatisticas, 1, 1, 11, 1)

        self.label = QLabel(Main)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)
        self.retranslateUi(Main)
        QMetaObject.connectSlotsByName(Main)
    # setupUi
    def mudarCampeonatos(self):
        index_pais = self.paisCB.currentIndex()
        if (self.paisCB.currentIndex() != 0):
            for i in range(0, len(paises_campeonatos[index_pais-1]["Campeonatos"])):
                
                self.campeonatoCB.setItemText(i, paises_campeonatos[index_pais-1]["Campeonatos"][i]["Nome"])
            self.campeonatoCB.setEnabled(True)
        else:
            self.campeonatoCB.setEnabled(False)
            
    def mudarTemporadas(self):
        index_pais = self.paisCB.currentIndex()
        index_campeonato = self.campeonatoCB.currentIndex()
        if (paises_campeonatos[index_pais-1]["Campeonatos"][index_campeonato]["Nome"] == "Brasil"):
            for i in range(paises_campeonatos[index_pais-1]["Campeonatos"][index_campeonato]["inicio"]):
                self.campeonatoCB.setItemText(i, paises_campeonatos[index_pais-1]["Campeonatos"][i]["Nome"])
        # else:
            
        self.campeonatoCB.setEnabled(True)
    def ativarGerar(self):
        index_pais = self.paisCB.currentIndex()
        index_campeonato = self.campeonatoCB.isEnabled()
        nomeDataset = self.textEdit.toPlainText()
        if (index_pais != 0 and index_campeonato != False and nomeDataset !='' and (self.full_timeCB.isChecked or self.first_timeCB.isChecked or self.second_timeCB.isChecked)):
            self.gerarButton.setEnabled(True)
        elif (self.full_timeCB.isChecked == False or self.first_timeCB.isChecked == False  or self.second_timeCB.isChecked == False):
            self.gerarButton.setEnabled(False)
        else:
            self.gerarButton.setEnabled(False)

    def verificarInput(self):
        index_pais = self.paisCB.currentIndex()
        index_campeonato = self.campeonatoCB.isEnabled()
        nomeDataset = self.textEdit.toPlainText()
        pais = paises_campeonatos[index_pais-1]["País"].lower() 
        if pais == "França": 
            pais = "franca"
        elif pais ==  "Itália":
            pais = 'italia'
        if (index_pais != 0 and index_campeonato != False and nomeDataset !='' and (self.full_timeCB.isChecked or self.first_timeCB.isChecked or self.second_timeCB.isChecked)):
            listaTempos = []
            if (self.full_timeCB.isChecked): listaTempos.append(0)
            if(self.first_timeCB.isChecked): listaTempos.append(1)
            if(self.second_timeCB.isChecked): listaTempos.append(2)
            get_data_from_tournament(nomeDataset, pais, paises_campeonatos[index_pais-1]["Campeonatos"][index_campeonato-1]["label"], listaTempos)
    
    # def atualizarBarraProgresso(self, valor_atual, total_passos):
    #     progresso_atual = (valor_atual + 1) * 100 // total_passos
    #     self.progressBar.setValue(progresso_atual)
    
    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.tituloLabel.setText(QCoreApplication.translate("Main", u"EXTRA\u00c7\u00c3O DE DADOS", None))
        self.logo.setText("")
        self.paisLabel.setText(QCoreApplication.translate("Main", u"Regi\u00e3o", None))
        self.paisCB.setItemText(0, QCoreApplication.translate("Main", u"Selecione uma regi\u00e3o", None))
        for i in range(0, len(paises_campeonatos)):
            self.paisCB.setItemText(i+1, QCoreApplication.translate("Main", paises_campeonatos[i]["País"], None))

        self.campeonatoLabel.setText(QCoreApplication.translate("Main", u"Campeonato", None))

        self.temporadaLabel.setText(QCoreApplication.translate("Main", u"Temporada", None))
        self.tempCB.setItemText(0, QCoreApplication.translate("Main", u"EM BREVE", None))

        self.nomeDSLabel.setText(QCoreApplication.translate("Main", u"Nome do dataset", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Main", u"Digite o nome para o dataset", None))
        self.temposLabel.setText(QCoreApplication.translate("Main", u"Tempo(s) ", None))
        self.full_timeCB.setText(QCoreApplication.translate("Main", u"Tempo regulamentar (1\u00b0 e 2\u00b0 tempo)", None))
        self.first_timeCB.setText(QCoreApplication.translate("Main", u"1\u00b0 Tempo", None))
        self.second_timeCB.setText(QCoreApplication.translate("Main", u"2\u00b0 Tempo", None))
        self.gerarButton.setText(QCoreApplication.translate("Main", u"Gerar", None))
        self.est1.setText(QCoreApplication.translate("Main", u"Gols do 1\u00b0 Tempo", None))
        self.est2.setText(QCoreApplication.translate("Main", u"Gols do 2\u00b0 Tempo", None))
        self.est3.setText(QCoreApplication.translate("Main", u"Gols Esperados", None))
        self.est4.setText(QCoreApplication.translate("Main", u"Posse de bola", None))
        self.est5.setText(QCoreApplication.translate("Main", u"Tentativas de gols", None))
        self.est6.setText(QCoreApplication.translate("Main", u"Chutes no gol", None))
        self.estt7.setText(QCoreApplication.translate("Main", u"Chutes para fora", None))
        self.est8.setText(QCoreApplication.translate("Main", u"Faltas Cobradas", None))
        self.est9.setText(QCoreApplication.translate("Main", u"Escanteios", None))
        self.est10.setText(QCoreApplication.translate("Main", u"Impedimentos", None))
        self.est11.setText(QCoreApplication.translate("Main", u"Laterais cobrados", None))
        self.est12.setText(QCoreApplication.translate("Main", u"Defesas do goleiro", None))
        self.est13.setText(QCoreApplication.translate("Main", u"Cart\u00f5es Amarelos", None))
        self.est14.setText(QCoreApplication.translate("Main", u"Cart\u00f5es Vermelhos", None))
        self.est15.setText(QCoreApplication.translate("Main", u"Passes Totais", None))
        self.est16.setText(QCoreApplication.translate("Main", u"Ataques Perigosos", None))
        self.est17.setText(QCoreApplication.translate("Main", u"Bolas Afastadas", None))
        self.label.setText(QCoreApplication.translate("Main", u"Estat\u00edsticas", None))
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
if __name__ == '__main__':
    import sys
    print("Iniciando o aplicativo")
    app = QApplication(sys.argv)
    mywidget = MyWidget()
    mywidget.show()
    sys.exit(app.exec())

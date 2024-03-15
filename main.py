
paises_campeonatos = [
    {
        "País":"Inglaterra",
        "Campeonatos":[
            {"Nome":"Premier League", "inicio":1989, "fim": 2024},
            {"Nome":"Championship", "inicio":1989, "fim": 2024},
        ]
    },
    {
        "País":"Brasil",
        "Campeonatos":[
            {"Nome":"Série A", "inicio":1989, "fim": 2024},
            {"Nome":"Série B", "inicio":1989, "fim": 2024},
        ]
    },
    {
        "País":"Alemanha",
        "Campeonatos":[
            {"Nome":"Bundesliga", "inicio":1989, "fim": 2024},
            {"Nome":"Bundesliga 2", "inicio":1989, "fim": 2024},
        ]
    },
]
from everyRounds import get_data_from_tournament
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSplitter,
    QTextEdit, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(335, 614)
        font = QFont()
        font.setFamilies([u"Leelawadee UI"])
        Main.setFont(font)
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
        self.splitter.addWidget(self.second_timeCB)

        self.gridLayout.addWidget(self.splitter, 11, 0, 1, 1)

        self.gerarButton = QPushButton(Main)
        self.gerarButton.setObjectName(u"gerarButton")
        self.gerarButton.setEnabled(False)
        self.gerarButton.setMinimumSize(QSize(200, 50))
        self.gerarButton.setMaximumSize(QSize(200, 50))
        self.gerarButton.setFont(font2)

        self.gridLayout.addWidget(self.gerarButton, 12, 0, 1, 1, Qt.AlignHCenter)

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

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.tituloLabel.setText(QCoreApplication.translate("Main", u"EXTRA\u00c7\u00c3O DE DADOS", None))
        self.logo.setText("")
        self.paisLabel.setText(QCoreApplication.translate("Main", u"Pa\u00eds", None))
        self.paisCB.setItemText(0, QCoreApplication.translate("Main", u"Selecione um Pa\u00eds", None))
        for i in range(0, len(paises_campeonatos)):
            self.paisCB.setItemText(i+1, QCoreApplication.translate("Main", paises_campeonatos[i]["País"], None))

        self.campeonatoLabel.setText(QCoreApplication.translate("Main", u"Campeonato", None))

        self.temporadaLabel.setText(QCoreApplication.translate("Main", u"Temporada", None))
        self.tempCB.setItemText(0, QCoreApplication.translate("Main", u"2023-2024", None))

        self.nomeDSLabel.setText(QCoreApplication.translate("Main", u"Nome do dataset", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Main", u"Digite o nome para o dataset", None))
        self.temposLabel.setText(QCoreApplication.translate("Main", u"Tempo(s) ", None))
        self.full_timeCB.setText(QCoreApplication.translate("Main", u"Tempo regulamentar (1\u00b0 e 2\u00b0 tempo)", None))
        self.first_timeCB.setText(QCoreApplication.translate("Main", u"1\u00b0 Tempo", None))
        self.second_timeCB.setText(QCoreApplication.translate("Main", u"2\u00b0 Tempo", None))
        self.gerarButton.setText(QCoreApplication.translate("Main", u"Gerar", None))

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mywidget = MyWidget()
    mywidget.show()
    sys.exit(app.exec())

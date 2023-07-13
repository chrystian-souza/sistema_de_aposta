# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'click_certo.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(682, 763)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 10, 615, 753))
        self.gridLayout_6 = QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_15 = QLabel(self.widget_2)
        self.label_15.setObjectName(u"label_15")
        font = QFont()
        font.setPointSize(25)
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_15)


        self.gridLayout_6.addWidget(self.widget_2, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_3 = QWidget(self.widget_4)
        self.widget_3.setObjectName(u"widget_3")
        self.formLayout = QFormLayout(self.widget_3)
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setScaledContents(False)

        self.horizontalLayout.addWidget(self.label)

        self.nome_apostador = QLineEdit(self.widget_3)
        self.nome_apostador.setObjectName(u"nome_apostador")

        self.horizontalLayout.addWidget(self.nome_apostador)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.time_casa = QLineEdit(self.widget_3)
        self.time_casa.setObjectName(u"time_casa")

        self.horizontalLayout_2.addWidget(self.time_casa)


        self.formLayout.setLayout(1, QFormLayout.LabelRole, self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.time_visitante = QLineEdit(self.widget_3)
        self.time_visitante.setObjectName(u"time_visitante")

        self.horizontalLayout_3.addWidget(self.time_visitante)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.valor_aposta = QLineEdit(self.widget_3)
        self.valor_aposta.setObjectName(u"valor_aposta")

        self.horizontalLayout_4.addWidget(self.valor_aposta)


        self.formLayout.setLayout(2, QFormLayout.LabelRole, self.horizontalLayout_4)


        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout = QGridLayout(self.widget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.placar_casa = QSpinBox(self.widget_6)
        self.placar_casa.setObjectName(u"placar_casa")

        self.horizontalLayout_5.addWidget(self.placar_casa)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)

        self.label_8 = QLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.widget_6)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.placar_visitante = QSpinBox(self.widget_6)
        self.placar_visitante.setObjectName(u"placar_visitante")

        self.horizontalLayout_6.addWidget(self.placar_visitante)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)


        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(192, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget_6, 1, 0, 1, 1)

        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.adicionar_aposta = QPushButton(self.widget_7)
        self.adicionar_aposta.setObjectName(u"adicionar_aposta")

        self.horizontalLayout_8.addWidget(self.adicionar_aposta)

        self.horizontalSpacer_4 = QSpacerItem(227, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.gridLayout_2.addWidget(self.widget_7, 2, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_4, 1, 0, 1, 1)

        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_5 = QGridLayout(self.widget_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gerar_resultado = QPushButton(self.widget_8)
        self.gerar_resultado.setObjectName(u"gerar_resultado")

        self.gridLayout_5.addWidget(self.gerar_resultado, 2, 1, 1, 1)

        self.label_12 = QLabel(self.widget_8)
        self.label_12.setObjectName(u"label_12")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_12, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(222, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(222, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setLayoutDirection(Qt.LeftToRight)
        self.widget1 = QWidget(self.widget_9)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(210, 10, 192, 24))
        self.horizontalLayout_11 = QHBoxLayout(self.widget1)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.widget1)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_9.setFont(font2)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.resultado_casa = QLineEdit(self.widget1)
        self.resultado_casa.setObjectName(u"resultado_casa")
        self.resultado_casa.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_9.addWidget(self.resultado_casa)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_9)

        self.label_10 = QLabel(self.widget1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.resultado_visitante = QLineEdit(self.widget1)
        self.resultado_visitante.setObjectName(u"resultado_visitante")
        self.resultado_visitante.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_10.addWidget(self.resultado_visitante)

        self.label_11 = QLabel(self.widget1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_11)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)


        self.gridLayout_5.addWidget(self.widget_9, 1, 0, 1, 3)


        self.gridLayout_6.addWidget(self.widget_8, 2, 0, 1, 1)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_4 = QGridLayout(self.widget_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_11 = QWidget(self.widget_5)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_3 = QGridLayout(self.widget_11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_7 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.label_14 = QLabel(self.widget_11)
        self.label_14.setObjectName(u"label_14")
        font3 = QFont()
        font3.setPointSize(14)
        self.label_14.setFont(font3)

        self.gridLayout_3.addWidget(self.label_14, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_8, 0, 2, 1, 1)

        self.tableWidget = QTableWidget(self.widget_11)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_3.addWidget(self.tableWidget, 1, 0, 1, 3)


        self.gridLayout_4.addWidget(self.widget_11, 1, 0, 1, 1)

        self.widget_10 = QWidget(self.widget_5)
        self.widget_10.setObjectName(u"widget_10")
        self.label_13 = QLabel(self.widget_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 10, 184, 19))
        self.label_13.setFont(font2)
        self.qtd_apostador = QLineEdit(self.widget_10)
        self.qtd_apostador.setObjectName(u"qtd_apostador")
        self.qtd_apostador.setGeometry(QRect(200, 10, 30, 20))
        self.qtd_apostador.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_4.addWidget(self.widget_10, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_5, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"ClickCerto007", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome do apostador:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Time da casa:", None))
#if QT_CONFIG(tooltip)
        self.time_casa.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.time_casa.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Time visitante:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Valor da aposta:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PLACAR", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Casa:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Visitante:", None))
        self.adicionar_aposta.setText(QCoreApplication.translate("MainWindow", u"Adicionar aposta", None))
        self.gerar_resultado.setText(QCoreApplication.translate("MainWindow", u"Gerar Resultado", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Resultado", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Casa", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Visitante", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Ganhadores", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Aposta", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Valor Ganho", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Quantidade de apostador:", None))
    # retranslateUi


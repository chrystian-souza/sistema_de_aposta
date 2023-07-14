import random
from click_certo_007.view import click_certo
import os
import shutil

from PySide6.QtWidgets import QMainWindow, QTableWidget, QMessageBox, QLineEdit, QTextEdit, QComboBox, \
    QTableWidgetItem, QHeaderView, QFileDialog
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIntValidator, QPixmap, QImage
from click_certo_007.view.click_certo import Ui_MainWindow
from click_certo_007.infra.entities.aposta import Aposta
from click_certo_007.infra.repository.aposta_repository import Aposta_repository


class MainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.gerar_resultado.clicked.connect(self.gerar_placar)
        self.adicionar_aposta.clicked.connect(self.salvar_aposta)

    def gerar_placar():
        gols_casa = random.randint(0, 5)
        gols_vistante = random.randint(0, 5)

        placar = [
            {"time": "Time da casa", "gols": gols_casa},
            {"time": "Time Visitante", "gols": gols_vistante}
        ]

        return placar


    def exibir_placar(placar):
        print("Placar final:")
        for resultado in placar:
            print(f"{resultado['time']}: {resultado['gols']}")


    def validar_vencedor(placar):
        if placar[0]['gols'] > placar[1]['gols']:
            return placar[0]['time']
        elif placar[1]['gols'] > placar[0]['gols']:
            return placar[1]['time']
        else:
            return "Empate"


    placar = gerar_placar()
    exibir_placar(placar)

    ganhador = validar_vencedor(placar)
    print(f"Vencedor: {ganhador} ganhou")


    def popula_tabela_aposta(self):
        self.tbl_aposta.setRowCount(0)
        conn = Aposta_repository
        self.tbl_aposta.setRowCount()

    def salvar_aposta(self):

        db = Aposta_repository()

        aposta = Aposta(
            nome_do_apostador=self.nome_apostador.text(),
            gols_casa=self.placar_casa.text(),
            gols_visitante=self.placar_visitante.text(),
            valor_da_aposta=self.valor_aposta.text()
        )

        if self.adicionar_aposta.text() == 'Adicionar aposta':
            retorno = db.insert(aposta)

            if retorno == 'OK':
                msg = QMessageBox()
                msg.setWindowTitle('Aposta confirmada')
                msg.setText('Aposta salva com sucesso.')
                msg.exec()
                # self.limpar_campos()








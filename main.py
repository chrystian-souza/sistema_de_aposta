import sys

from PySide6.QtWidgets import QApplication
from click_certo_007.view.tela_principal import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
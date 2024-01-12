#GPT
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        # Create "Open" action
        openAction = QAction('Open', self)
        openAction.triggered.connect(self.openFile)

        # Create "Save" action
        saveAction = QAction('Save', self)
        saveAction.triggered.connect(self.saveFile)

        # Create "Exit" action
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)

        # Create Menu Bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Notepad')
        self.show()

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)

        if fileName:
            with open(fileName, 'r') as file:
                text = file.read()
                self.textEdit.setPlainText(text)

    def saveFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)

        if fileName:
            with open(fileName, 'w') as file:
                text = self.textEdit.toPlainText()
                file.write(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec())

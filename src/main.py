import sys

from PyQt6.QtWidgets import QApplication

from window import UsdLinkWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = UsdLinkWindow()
    sys.exit(app.exec())

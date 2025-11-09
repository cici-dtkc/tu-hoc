from PyQt6.QtWidgets import QApplication
import sys

from ui.login_window import LoginWindow
from ui.main_window import ParkingManagementApp


if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = LoginWindow()
    login.exec = app.exec  # tránh lỗi
    login.accept_login = False

    login.show()
    app.processEvents()

    # Đợi user đóng login
    while login.isVisible():
        app.processEvents()

    if login.accept_login:
        window = ParkingManagementApp()
        window.show()
        sys.exit(app.exec())
    else:
        sys.exit()

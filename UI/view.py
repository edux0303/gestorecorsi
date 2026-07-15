import flet as ft

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.title = "Gestore corsi"
        self.page.horizontal_alignment = "center"
        self.title = None
        self.drop_didattico = None
        self.drop_corso = None
        self.btnPrintCorsiPD = None
        self.btnPrintIscrittiCorsiPD = None
        self.btnPrintIscrittiCodins = None
        self.btnPrintCDSCodins = None
        self._controller = None
        self.txt_result = None

    def load_interface(self):
        self.title = ft.Text("PROGRAMMA GESTIONE CORSI")
        self.page.add(self.title)

        self.drop_didattico = ft.Dropdown(label="Periodo Didattico",
                                          options=[ft.dropdown.Option("I"), ft.dropdown.Option("II")],
                                          width=200)

        self.btnPrintCorsiPD = ft.ElevatedButton(text="Stampa Corsi",
                                                 on_click=self._controller.handlePrintCorsiPD,
                                                 width=200)

        self.btnPrintIscrittiCorsiPD = ft.ElevatedButton(text="Stampa Iscritti",
                                                         on_click=self._controller.handlePrintIscrittiCorsiPD)

        self.page.add(ft.Row(
            controls=[self.drop_didattico, self.btnPrintCorsiPD, self.btnPrintIscrittiCorsiPD]
        ))
        self.drop_corso = ft.Dropdown(label="Corso", width=200)
        self._controller.fillddCodins()
        self.btnPrintIscrittiCodins = ft.ElevatedButton(text="Stampa iscritti al corso",
                                                        on_click=self._controller.handlePrintIscrittiCodins,
                                                        width=300)
        self.btnPrintCDSCodins = ft.ElevatedButton(text="Stampa CDS afferenti",
                                                   on_click=self._controller.handlePrintCDSCodins,
                                                   width=300)
        self.page.add(ft.Row(
            controls=[self.drop_corso, self.btnPrintIscrittiCodins, self.btnPrintCDSCodins]
        ))
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self.page.add(self.txt_result)
        self.page.update()
    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        pass

    def update_page(self):
        self.page.update()

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()
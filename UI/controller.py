import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view):
        self._view = view
        self._model = Model()
        self._ddCodinsValue = None

    def handlePrintCorsiPD(self, e):
        self._view.txt_result.controls.clear()
        pd = self._view.drop_didattico.value
        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico.")
            self._view.update_page()
            return
        if pd=="I":
            pdInt = 1
        else:
            pdInt = 2
        corsiPD = self._model.getCorsiPD(pdInt)
        for c in corsiPD:
            self._view.txt_result.controls.append(ft.Text(c))

        self._view.update_page()

    def handlePrintIscrittiCorsiPD(self, e):
        self._view.txt_result.controls.clear()
        pd = self._view.drop_didattico.value

        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico.")
            self._view.update_page()
            return

        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2

        corsi = self._model.getCorsiPDwIscritti(pdInt)  # ← differenza 1

        for c in corsi:
            self._view.txt_result.controls.append(
                ft.Text(f"{c[0]} -- N Iscritti: {c[1]}")  # ← differenza 2
            )

        self._view.update_page()
    def handlePrintIscrittiCodins(self, e):
            pass


    def handlePrintCDSCodins(self, e):
            pass
    def fillddCodins(self):
            for c in self._model.getAllCorsi():
                self._view.drop_corso.options.append(ft.dropdown.Option(
                    key=c.codins,
                    data=c,
                    on_click=self._choiceDDCodins
                ))

    def _choiceDDCodins(self, e):
            self._ddCodinsValue = e.control.data

    def handlePrintIscrittiCodins(self, e):
        self._view.txt_result.controls.clear()

        if self._ddCodinsValue is None:
            self._view.create_alert("Per favore selezionare un insegnamento.")
            self._view.update_page()
            return

        studenti = self._model.getStudentiCorso(self._ddCodinsValue.codins)

        for s in studenti:
            self._view.txt_result.controls.append(ft.Text(s))

        self._view.update_page()

    def handlePrintCDSCodins(self, e):
        self._view.txt_result.controls.clear()

        if self._ddCodinsValue is None:
            self._view.create_alert("Per favore selezionare un insegnamento.")
            self._view.update_page()
            return

        cds = self._model.getCDSofCorso(self._ddCodinsValue.codins)

        for c in cds:
            self._view.txt_result.controls.append(
                ft.Text(f"{c[0]} - N Iscritti: {c[1]}")
            )

        self._view.update_page()
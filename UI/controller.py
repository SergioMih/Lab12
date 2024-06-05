import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        for i in range(2015,2019):
            self._view.ddyear.options.append(ft.dropdown.Option(i))
        countries = DAO.getCountryList()
        for country in countries:
            self._view.ddcountry.options.append(ft.dropdown.Option(country))
    def readYear(self,e):
        self.year = self._view.ddyear.value
    def readCountry(self,e):
        self.country = self._view.ddcountry.value


    def handle_graph(self, e):
        self._model.buildGraph(self.country,self.year)
        lenNoedes = len(self._model.grafo.nodes)
        lenEdges = len(self._model.grafo.edges)
        self._view.txt_result.controls.append(ft.Text(f"il grafo ha {lenNoedes} nodi e {lenEdges} edges"))
        self._view._page.update()




    def handle_volume(self, e):
        tupla = self._model.volume()
        for t in tupla:
            self._view.txtOut2.controls.append(ft.Text(f"{t[0]} - {t[1]}"))
        self._view._page.update()


    def handle_path(self, e):
        pass

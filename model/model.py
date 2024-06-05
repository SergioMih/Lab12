import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.idMapR = {}

    def buildGraph(self, country, anno):
        self.retailers = DAO.getRetailers(country)
        self.grafo = nx.Graph()
        self.grafo.add_nodes_from(self.retailers)
        for r in self.retailers:
            self.idMapR[r.Retailer_code] = r
        for r in self.retailers:
            for r1 in self.retailers:
                if r != r1:
                    if not self.grafo.has_edge(r,r1):
                        connessione = DAO.getConnessione(r,r1,anno)
                        if connessione[0] > 0:
                            self.grafo.add_edge(r,r1,weight=connessione[0])

    def volume(self):
        tupla = []
        for r in self.retailers:
            vicini= self.grafo.neighbors(r)
            sum = 0
            for v in vicini:
                sum += self.grafo[r][v]["weight"]
            if sum>0:
                tupla.append((r,sum))
        tupla.sort(key=lambda x: x[1],reverse=True)
        print(tupla)
        return tupla







from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getCountryList():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT gr.Country 
FROM go_retailers gr 
order by gr.Country ASC """

        cursor.execute(query, ())

        for row in cursor:
            result.append(row["Country"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getRetailers(country):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * 
FROM go_retailers gr 
WHERE gr.Country = %s
order by gr.Retailer_name ASC  """

        cursor.execute(query, (country,))

        for row in cursor:
            result.append(Retailer(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConnessione(r,r1,anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT count(DISTINCT gds2.Product_number) as s
FROM go_daily_sales gds , go_daily_sales gds2 
where gds2.Retailer_code = %s
and gds.Retailer_code = %s
and gds2.Product_number = gds.Product_number
and Year(gds2.Date)=Year(gds.Date)
and Year(gds2.Date) = %s"""

        cursor.execute(query, (r.Retailer_code,r1.Retailer_code,anno,))

        for row in cursor:
            result.append(row["s"])

        cursor.close()
        conn.close()
        return result

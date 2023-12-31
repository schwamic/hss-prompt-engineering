# Run marked code lines with Shift+Enter to run as jupyter notebook.
# Therefore not the whole script is getting executed and variables are saved in a session.

import pandas
import json


class DataService:
    def __init__(self):
        self.name = "DataService"

    def get_context(self):
        return pandas.read_csv("../hss_documents/project_context.txt", delimiter="\t")

    def get_ideen(self):
        excel_ideen = pandas.read_excel(
            "../hss_documents/230116_Ideen.xlsx",
            sheet_name="230116_BLM_Ideen_SL3_Excelliste",
        )
        jsonstr_ideen = excel_ideen.to_json(orient="records")
        json_ideen = json.loads(jsonstr_ideen)
        # for idee in json_ideen:
        #     del idee["Fragencode"]
        #     del idee["Ideencode"]
        #     idee["Titel"] = idee.pop("Titel der Idee")
        #     idee["Beschreibung"] = idee.pop("Beschreibung der Idee")
        return json_ideen

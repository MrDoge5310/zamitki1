import json
from window_layout import *


def WriteToFile(data):
    with open("BIBI.json", 'w') as file:
        json.dump(data, file)


with open("BIBI.json", 'r') as file:
    notes = json.load(file)

notes_list.addItems(notes)

window.show()
app.exec_()

import json
from window_layout import *


def WriteToFile(data):
    with open("BIBI.json", 'w') as file:
        json.dump(data, file)


def showNote():
    key = notes_list.selectedItems()[0].text()
    text_field.setText(notes[key]["текст"])
    tag_list.clear()
    tag_list.addItems(notes[key]["теги"])


def createNote():
    name, ok = QInputDialog.getText(window, "Додати нотатку", "Назва нотатки:")
    if ok:
        if name != "":
            notes[name] = {"текст": "", "теги": []}
            notes_list.addItem(name)
        else:
            QMessageBox.warning(window, "Помилка", "Невірно вказана назва")


notes_list.itemClicked.connect(showNote)
create_note.clicked.connect(createNote)


with open("BIBI.json", 'r') as file:
    notes = json.load(file)

notes_list.addItems(notes)

window.show()
app.exec_()

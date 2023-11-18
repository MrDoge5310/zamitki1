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


def deleteNote():
    key = notes_list.selectedItems()[0].text()
    del notes[key]
    notes_list.clear()
    tag_list.clear()
    text_field.clear()
    notes_list.addItems(notes)
    WriteToFile(notes)


def saveNote():
    if notes_list.selectedItems():
        key = notes_list.selectedItems()[0].text()
        text = text_field.toPlainText()
        notes[key]["текст"] = text
        WriteToFile(notes)
        QMessageBox.information(notes_win, "Успішно", "Замітку збережено")
    else:
        QMessageBox.warning(notes_win, "Помилка", "Оберіть замітку")


notes_list.itemClicked.connect(showNote)
create_note.clicked.connect(createNote)
delete_note.clicked.connect(deleteNote)
save_note.clicked.connect(saveNote)


with open("BIBI.json", 'r') as file:
    notes = json.load(file)

notes_list.addItems(notes)

window.show()
app.exec_()

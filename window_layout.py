from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


app = QApplication([])

window = QWidget()
window.resize(800, 600)
window.setWindowTitle("Розумні нотатки")

text_field = QLineEdit("Текст нотатки")

notes_list = QListWidget()
notes_list.setWindowTitle('Список нотаток')

create_note = QPushButton("Створити нотатку")
delete_note = QPushButton("Видалити нотатку")
save_note = QPushButton("Зберегти нотатку")

tag_list = QListWidget()

search_line = QLineEdit("Введіть тег")

add_tag = QPushButton("Додати до нотатки")
delete_tag = QPushButton("Видалити тег")
search_tag = QPushButton("Пошук за тегом")

coloumn1 = QVBoxLayout()
coloumn2 = QVBoxLayout()
horizontal1 = QHBoxLayout()
horizontal2 = QHBoxLayout()
main_layout = QHBoxLayout()

coloumn1.addWidget(text_field)

coloumn2.addWidget(notes_list)
horizontal1.addWidget(create_note)
horizontal1.addWidget(delete_note)
coloumn2.addLayout(horizontal1)
coloumn2.addWidget(save_note)

coloumn2.addWidget(tag_list)
coloumn2.addWidget(search_line)
horizontal2.addWidget(add_tag)
horizontal2.addWidget(delete_tag)
coloumn2.addLayout(horizontal2)
coloumn2.addWidget(search_tag)

main_layout.addLayout(coloumn1, stretch=2)
main_layout.addLayout(coloumn2, stretch=1)
window.setLayout(main_layout)

window.show()
app.exec_()

from datetime import datetime,timezone


class Note:
    def __init__(self,topic,text):
        self.topic=topic 
        self.text=text
    
    def print_info(self):
        print(f"Заметка: {self.topic} \n текст: {self.text}")
    def __str__(self):
        return '{}(Заголовок: {!r}, текст: {!r})'.format(self.__class__.__name__, self.topic, self.text)
    def __repr__(self):
        return self.__str__()


def create_note():
    file = open('Notes_list.csv', 'a+',encoding='utf-8')
    note_topic = input(str("Введите заголовок заметки: "))
    note_text = input(str("Введите текст заметки: "))
    n = Note(note_topic,note_text)
    x=(n.__repr__())

    current_time=(datetime.now())
    notes = list()
    date=list()

    notes.append(x)
    date.append(str(current_time))
    data = list(*zip(notes,date))
    for line in data:
        file.write((line) + '; ')

    file.write('\n')

    print("Заметка успешно сохранена")

    file.close()



def note_remove():
    find = str(input('Выберите заметку: '))
    file = open('Notes_list.csv', encoding = 'utf-8')
    list_1 = list()
    for line in file:
        if find not in line:
            list_1.append(line)
    file.close()
    file = open('Notes_list.csv', 'w',encoding='utf-8')
    for line in list_1:
        file.write(line)
    file.close()

def print_notes():
    file = open('Notes_list.csv', 'r', encoding='utf-8')
    for line in file:
        print(line)
    file.close()


def edit_note():
    note_remove()
    create_note()


def Selection_menu(choice) ->int:
  if choice == 1:
    print_notes()
  elif choice == 2:
    create_note()
  elif choice == 3:
    note_remove()
  elif choice == 4:
    edit_note()


while True:
  print('\nВыберите необходимое действие:\n'
          "1. Отобразить все заметки\n"
          "2. Добавить заметку\n"
          "3. Удалить заметку\n"
          "4. Редактирование заметки\n"
          "5. Закончить работу")
  choice=int(input())
  if 1<=choice<=4:
    Selection_menu(choice)
  elif choice==5:
    break
  else: print('Ошибка')


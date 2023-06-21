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

    current_time=str(datetime.fromtimestamp(1687374769)) 
    notes = list()
    date=list()
    # id=list()
    # id.append(str(i))

    notes.append(x)
    date.append(current_time)
    data = list(*zip(notes,date))
    for line in data:
        file.write((line) + '; ')

    file.write('\n')

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


    
    

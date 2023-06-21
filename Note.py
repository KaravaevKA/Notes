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
    notes = list()
    date=list()
    current_time=str(datetime.fromtimestamp(1687374769))
    date.append(current_time)
    n = Note(note_topic,note_text)
    x=(n.__repr__())
    notes.append(x)
    data = list(*zip(notes,date))
    for line in data:
        file.write((line) + ' ')

    file.write('\n')

    file.close()

create_note()

    
    

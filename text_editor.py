#Text Editor на основе классов.
#https://py.checkio.org/ru/mission/text-editor/
#https://ru.wikipedia.org/wiki/Хранитель_(шаблон_проектирования)
#https://ru.wikipedia.org/wiki/Design_Patterns
class Text:
    def __init__(self):
        self.main_text = ''
        self.font = None

    def write(self, text):
        '''добавляет указанный текст к текущему.'''
        self.main_text +=text

    def set_font(self,font_name):
        '''устанавливает шрифт текста. Шрифт распространяется на весь текст, даже добавленный после установки шрифта и отображается в квадратных скобках перед началом текста и после конца: "[Arial]...example...[Arial]". Шрифт может быть задан сколько угодно раз, но отображается только последний из них.'''
        self.font = font_name

    def show(self):
        '''отображает текущий текст и шрифт (если задан).'''
        if self.font:
            return '[{}]{}[{}]'.format(self.font, self.main_text,self.font)
        else:
            return '{}'.format(self.main_text)


    def restore(self, text_version):
        '''возвращает текст к указанной версии.'''
        self.main_text = text_version[0]
        self.font = text_version[1]


class SavedText:
    def __init__(self):
        self.versions = []

    def save_text(self, text):
        '''сохраняет текущее состояние текста и текущий шрифт. Первая сохраненная версия имеет номер 0, вторая - 1 и так далее.'''
        if len(self.versions) >= 9:
            self.versions.pop(0)
            self.versions.append((text.main_text, text.font))
        else:
            self.versions.append((text.main_text, text.font))

    def get_version(self,number):
        '''метод используется вместе с методом restore класса Text и служит для выбора нужной версии текста.'''
        return self.versions[number]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")
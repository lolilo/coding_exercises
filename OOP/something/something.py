
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def print_name(self):
        print 'Helloka'


if __name__ == '__main__':
    p = Person('Liana', 23)
    Person.print_name()


class CommandExecuter(object):

    @staticmethod
    def run_command(command_text):
        print 'Hello, I ran {something}'.format(something=command_text)
        clt.execute(command_text)

CommandExecuter.run_command()


from garfield.config.write_output import print_debug

class ModuleInfo(object):
    def __init__(self, name, category, options={}, suboptions=[]):
        self.name = name
        self.category = category
        self.options = {
            'command': '-{name}'.format(name=self.name),
            'action': 'store_true',
            'dest': self.name,
            'help': '{name} passwords'.format(name=self.name)
        }
        self.suboptions = suboptions

    def error(self, message):
        print_debug('ERROR', message)

    def info(self, message):
        print_debug('INFO', message)

    def debug(self, message):
        print_debug('DEBUG', message)

    def warning(self, message):
        print_debug('WARNING', message)
from flet import *
import os, importlib.util


global _moduledList
_moduleList = {}

for _, dirs, __ in os.walk(r'./'):
    for dir in dirs:
        if dir == 'pages':
            for filename in os.listdir(dir):
                _file = os.path.join(dir, filename)
                if os.path.isfile(_file):
                    filename = filename[:-3]

                    _moduleList[
                            "/" + filename
                    ] = importlib.util.spec_from_file_location(filename, _file)


def main(page:Page):
    page.title = 'Idea-Day CB India'

    page.views.append(
        _moduleList['/login'].loader.load_module()._view_()
    )

    page.go("/home")
    page.update()
    pass


if __name__ == '__main__':
    app(target=main)
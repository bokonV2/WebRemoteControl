from models import Groups, Buttons


def createGroup(name):
    Groups.create(name=name)

def createButton(name, group_id, type, **kwargs):
    group = Groups.get(Groups.id == group_id)
    Buttons.create(
        name=name,
        group=group,
        type=type,
        **kwargs
    )

def getAll():
    rtn = {}
    for group in Groups.select():
        rtn[group.id] = (group.name, Buttons.select().where(Buttons.group == group.id))
    return rtn

def removeGroup(id):
    group = Groups.get(Groups.id == id)
    buttons = Buttons.select().where(Buttons.group == id)
    group.delete_instance()
    for button in buttons:
        button.delete_instance()

def removeButton(id):
    button = Buttons.get(Buttons.id == id)
    button.delete_instance()

def getButton(id):
    button = Buttons.get(Buttons.id == id)
    return button
    # print(button.id, button.name, button.type, button.x, button.y, button.duration, button.text)

from models import Groups, Buttons


def createGroup(name):
    Groups.create(name=name)

def createButton(name, group_id, type, x=None, y=None, duration=None, text=None):
    # print("add in DB")
    # print(name, group_id, type, x, y, duration, text)
    group = Groups.get(Groups.id == group_id)
    Buttons.create(
        name=name,
        group=group,
        type=type,
        x=x,
        y=y,
        duration=duration,
        text=text
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

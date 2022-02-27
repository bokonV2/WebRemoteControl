from peewee import *
import os, sys

if getattr(sys, 'frozen', False):
    db = SqliteDatabase(os.path.join(sys._MEIPASS, 'static/py/base.db'))
else:
    db = SqliteDatabase('static/py/base.db')


class BaseModel(Model):
    class Meta:
        database = db


class Groups(BaseModel):
    name = TextField()


class Buttons(BaseModel):
    name = TextField()
    group = ForeignKeyField(Groups)
    type = IntegerField(null=True)
    x = IntegerField(null=True)
    y = IntegerField(null=True)
    duration = FloatField(null=True)
    text = TextField(null=True)
    mode = IntegerField(null=True)
    presses = IntegerField(null=True)
    interval = IntegerField(null=True)
    button = TextField(null=True)
    clicks = IntegerField(null=True)
    move = IntegerField(null=True)
    scroll = FloatField(null=True)


if __name__ == '__main__':
    pass
    db.create_tables([Buttons, Groups])
    #
    # Groups.create(name="1")
    # Groups.create(name="2")
    # gr = Groups.get(Groups.name == "2")
    # Buttons.create(name="btn1", x=3, y=6, duration=0, type=0, group=gr)
    # Buttons.create(name="btn2", x=7, y=3, duration=5, type=3, group=gr)
    # Buttons.create(name="btn3", x=9, y=4, duration=0, type=4, group=gr)
    # Buttons.create(name="btn4", text="123", type=5, group=gr)
    # Buttons.create(name="btn5", text="start", type=8, group=gr)
    # Buttons.create(name="btn6", text="cmd", type=9, group=gr)
    #
    # gr = Groups.get(Groups.name == "1")
    # Buttons.create(name="btn1", x=9, y=4, duration=0, type=4, group=gr)
    # Buttons.create(name="btn2", text="cmd", type=9, group=gr)
    # Buttons.create(name="btn3", type=22, group=gr)
    # Buttons.create(name="btn4", type=9, group=gr)

    # for i in Groups.select():
    #     print(i.name, i.id)
    #     names = Buttons.select().where(Buttons.group == i.name)
    #     for name in names:
    #         print(name.name, name.type, name.id)
    #     print()

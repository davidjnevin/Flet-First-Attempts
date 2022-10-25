import flet
from time import sleep

from flet import Page, Text, Checkbox, ElevatedButton, Row, TextField, Column


def main(page: Page):
    # t = Text(value="Hello, world!", color="green")
    # page.controls.append(t)
    # page.update()

    # for i in range(10):
    # t.value = f"Step {i}"
    # page.update()
    # sleep(1)

    # for i in range(10):
    # page.controls.append(Text(f"Line {i}"))
    # if i > 4:
    # page.controls.pop(0)
    # page.update()
    # sleep(0.3)

    # def button_clicked(e):
    # page.add(Text("Clicked!"))

    # page.add(ElevatedButton(text="Click me", on_click=button_clicked))

    # def add_clicked(e):
    # page.add(Checkbox(label=new_task.value))

    # new_task = TextField(hint_text="Whats needs to be done?", width=300)
    # page.add(Row([new_task, ElevatedButton("Add", on_click=add_clicked)]))

    first_name = TextField(label="First name", autofocus=True)
    last_name = TextField(label="Last name")
    greetings = Column()

    def btn_click(e):
        greetings.controls.append(Text(f"Hello, {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ElevatedButton("Say hello!", on_click=btn_click),
        greetings,
    )


flet.app(target=main)

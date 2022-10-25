import flet

from flet import Page, Text


def main(page: Page):
    t = Text(
        value="This is a Text control sample",
        size=30,
        color="white",
        bgcolor="black",
        weight="bold",
        italic=True,
    )

    page.add(t)


flet.app(target=main)

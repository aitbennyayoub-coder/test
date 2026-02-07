from flet import *
def main(page:Page):
    page.window.width = 300
    page.window.height = 400
    page.bgcolor = Colors.WHITE

    page.add(
        ElevatedButton("enter")
    )
    page.update()
run(main)

import ui

def answer_for_area_perimator(sender):
    view["area"].text = ("the area is =" + str(5*3))
    view["perimator"].text = ("the perimator is =" + str(5*4))


view = ui.load_view()
view.present('sheet')

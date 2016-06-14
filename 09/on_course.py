#!/home/gedrex/pyladies/venv/bin/python
import pyglet
window = pyglet.window.Window()
window.clear()

def zpracuj_text():


window.push_handlers(on_text=zpracuj_text)

pyglet.app.run()

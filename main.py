basic.show_string("Hello")

def on_forever():
    basic.show_string("world!")
    basic.show_string("Bob!")
basic.forever(on_forever)

points = 0

def on_forever():
    def on_button_pressed_a():
        global points
        points -= 1
        basic.show_string("-", 100)
        pause(100)
        basic.clear_screen()
    input.on_button_pressed(Button.A, on_button_pressed_a)

    def on_button_pressed_b():
        global points
        points += 1
        basic.show_string("+", 100)
        pause(100)
        basic.clear_screen()
    input.on_button_pressed(Button.B, on_button_pressed_b)

    def on_button_pressed_ab():
        basic.show_number(points,100)
        pause(100)
        basic.clear_screen()
    input.on_button_pressed(Button.AB, on_button_pressed_ab)
basic.forever(on_forever)
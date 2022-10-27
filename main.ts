let points = 0
basic.forever(function on_forever() {
    input.onButtonPressed(Button.A, () => {
        points -= 1
        basic.showString("-", 100)
        pause(100)
        basic.clearScreen()
    })

    input.onButtonPressed(Button.B, () => {
        points += 1
        basic.showString("+", 100)
        pause(100)
        basic.clearScreen()
    })

    input.onButtonPressed(Button.AB, () => {
        basic.showNumber(points, 100)
        pause(100)
        basic.clearScreen()
    })
})

from lamp_082 import Lamp

def main():
    lamp1 = Lamp()

    assert(not(lamp1.on))
    lamp1.turn_off()
    assert(not(lamp1.on))
    lamp1.turn_on()
    assert(lamp1.on)
    lamp1.turn_on()
    assert(lamp1.on)
    lamp1.turn_off()
    assert(not(lamp1.on))
    lamp1.toggle()
    assert(lamp1.on)
    lamp1.turn_off()
    lamp1.turn_off()
    assert(not(lamp1.on))

    lamp2 = Lamp(True)

    assert(lamp2.on)
    lamp2.toggle()
    assert(not(lamp2.on))

if __name__ == '__main__':
    main()

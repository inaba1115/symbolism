import symbolism


def main():
    buffer = symbolism.Buffer()
    scale = symbolism.Scale(0, symbolism.scales["major"])
    dt = 1

    t = 0
    for x in [0, 1, 2, 2, 0, 4, 5, 6]:
        buffer.add(t, symbolism.Note(scale.map(x) + 60, 100, dt))
        t += dt

    buffer.write("foo.mid")


if __name__ == "__main__":
    main()

import symbolism


def main():
    buffer = symbolism.Buffer()
    scale = symbolism.Scale(0, symbolism.scales["major"])

    score = [
        ([0, 2, 4, 6], 1),
        ([], 0.5),
        ([2], 0.3),
        ([3], 0.3),
        ([4], 0.3),
        ([7], 0.3),
        ([-1], 0.3),
        ([0], 0.3),
        ([0, 2, 4, 6], 1),
    ]

    t = 0
    for notes, dt in score:
        for note in notes:
            buffer.add_note(scale.map(note) + 60, 100, t, dt)
        t += dt

    # buffer.write("foo.mid")
    buffer.play(symbolism.get_output_names()[0])


if __name__ == "__main__":
    main()

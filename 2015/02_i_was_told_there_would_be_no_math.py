with open('test1.txt') as f:
    wrapping_paper = 0
    feet_of_ribbon = 0
    for dimensions in f:
        dimensions = dimensions.strip('\n')
        l, w, h = map(int, dimensions.split("x"))

        sides = (l * w, w * h, h * l)
        slack = min(sides)
        wrapping_paper += sum(sides) * 2 + slack

        feet_of_ribbon += (l * w * h +
                           2 * (l + h + w) - 2 * (max(l, w, h)))

    print(f"First part result: {wrapping_paper}")
    print(f"Second part result: {feet_of_ribbon}")

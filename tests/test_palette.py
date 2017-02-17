from cursebox import palette


def test_distance():
    c0 = (0, 0, 0)
    c1 = (127, 0, 0)
    c2 = (255, 0, 0)

    assert palette.distance(c0, c1) < palette.distance(c0, c2)


def test_memoization():
    assert len(palette.closest_color.__defaults__[0]) == 0
    color = palette.closest_color((0, 127, 255))
    assert len(palette.closest_color.__defaults__[0]) == 1
    assert palette.closest_color((0, 127, 255)) == color

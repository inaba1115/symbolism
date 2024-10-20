__scales = [
    ("major", [0, 2, 4, 5, 7, 9, 11]),
    ("minor", [0, 2, 3, 5, 7, 8, 10]),
    ("dorian", [0, 2, 3, 5, 7, 9, 10]),
    ("mixolydian", [0, 2, 4, 5, 7, 9, 10]),
    ("lydian", [0, 2, 4, 6, 7, 9, 11]),
    ("phrygian", [0, 1, 3, 5, 7, 8, 10]),
    ("locrian", [0, 1, 3, 5, 6, 8, 10]),
    ("whole_tone", [0, 2, 4, 6, 8, 10]),
    ("half_whole_dim", [0, 1, 3, 4, 6, 7, 9, 10]),
    ("whole_half_dim", [0, 2, 3, 5, 6, 8, 9, 11]),
    ("minor_blues", [0, 3, 5, 6, 7, 10]),
    ("minor_pentatonic", [0, 3, 5, 7, 10]),
    ("major_pentatonic", [0, 2, 4, 7, 9]),
    ("harmonic_minor", [0, 2, 3, 5, 7, 8, 11]),
    ("harmonic_major", [0, 2, 4, 5, 7, 8, 11]),
    ("dorian_#4", [0, 2, 3, 6, 7, 9, 10]),
    ("phrygian_dominant", [0, 1, 4, 5, 7, 8, 10]),
    ("melodic_minor", [0, 2, 3, 5, 7, 9, 11]),
    ("lydian_augmented", [0, 2, 4, 6, 8, 9, 11]),
    ("lydian_dominant", [0, 2, 4, 6, 7, 9, 10]),
    ("super_locrian", [0, 1, 3, 4, 6, 8, 10]),
    ("8_tone_spanish", [0, 1, 3, 4, 5, 6, 8, 10]),
    ("bhairav", [0, 1, 4, 5, 7, 8, 11]),
    ("hungarian_minor", [0, 2, 3, 6, 7, 8, 11]),
    ("hirajoshi", [0, 2, 3, 7, 8]),
    ("in_sen", [0, 1, 5, 7, 10]),
    ("iwato", [0, 1, 5, 6, 10]),
    ("kumoi", [0, 2, 3, 7, 9]),
    ("pelog_selisir", [0, 1, 3, 7, 8]),
    ("pelog_tembung", [0, 1, 5, 7, 8]),
    ("messiaen3", [0, 2, 3, 4, 6, 7, 8, 10, 11]),
    ("messiaen4", [0, 1, 2, 5, 6, 7, 8, 11]),
    ("messiaen5", [0, 1, 5, 6, 7, 11]),
    ("messiaen6", [0, 2, 4, 5, 6, 8, 10, 11]),
    ("messiaen7", [0, 1, 2, 3, 5, 6, 7, 8, 9, 11]),
    ("chromatic", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
]

scales = dict(__scales)


def get_scale_names() -> list[str]:
    return [x for x, _ in __scales]

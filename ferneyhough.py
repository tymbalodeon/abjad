#!/usr/bin/env python3

import abjad
from abjad.demos.ferneyhough import FerneyhoughDemo

ferneyhough = FerneyhoughDemo()

proportions = [(1, n) for n in range(1, 11 + 1)]

tuplet = ferneyhough.make_nested_tuplet(abjad.Duration(1, 4), (1, 1), 5)
staff = abjad.Staff([tuplet], lilypond_type="RhythmicStaff")

tuplet = ferneyhough.make_nested_tuplet(abjad.Duration(1, 4), (2, 1), 5)
staff = abjad.Staff([tuplet], lilypond_type="RhythmicStaff")

tuplet = ferneyhough.make_nested_tuplet(abjad.Duration(1, 4), (3, 1), 5)
staff = abjad.Staff([tuplet], lilypond_type="RhythmicStaff")

normal_tuplet = abjad.Tuplet.from_duration_and_ratio(abjad.Duration(1, 4), (3, 5))
staff = abjad.Staff([normal_tuplet], lilypond_type="RhythmicStaff")

subdivided_tuplet = ferneyhough.make_nested_tuplet(abjad.Duration(1, 4), (3, 5), 3)
staff = abjad.Staff([subdivided_tuplet], lilypond_type="RhythmicStaff")

duration = abjad.Duration(1, 4)

tuplets = ferneyhough.make_row_of_nested_tuplets(duration, (2, 1), 6)
staff = abjad.Staff(tuplets, lilypond_type="RhythmicStaff")

# abjad.show(staff)

score = abjad.Score()
for tuplet_row in ferneyhough.make_rows_of_nested_tuplets(duration, 4, 6):
    staff = abjad.Staff(tuplet_row, lilypond_type="RhythmicStaff")
    score.append(staff)

# abjad.show(score)

score = ferneyhough.make_score(abjad.Duration(1, 4), 4, 6)
ferneyhough.configure_score(score)
# abjad.show(score)

lilypond_file = ferneyhough.make_lilypond_file(abjad.Duration(1, 4), 11, 6)
abjad.show(lilypond_file)

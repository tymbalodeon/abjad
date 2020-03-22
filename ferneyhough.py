#!/usr/bin/env python3

import abjad
from abjad.demos.ferneyhough import FerneyhoughDemo

ferneyhough = FerneyhoughDemo()

proportions = [(1, n) for n in range(1, 11 + 1)]

tuplet = ferneyhough.make_nested_tuplet(abjad.Duration(1, 4), (1, 1), 5)
staff = abjad.Staff([tuplet], lilypond_type="RhythmicStaff")
abjad.show(staff)

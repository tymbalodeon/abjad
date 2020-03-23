#!/usr/bin/env python3

import abjad
from abjad.demos import ligeti

pitches = [1, 2, 3]
maker = abjad.NoteMaker()
notes = maker(pitches, [(1, 8)])
abjad.beam(notes)
abjad.slur(notes)
abjad.attach(abjad.Dynamic("f"), notes[0])
abjad.attach(abjad.Dynamic("p"), notes[1])

voice_lower = abjad.Voice(notes)
voice_lower.name = "rh_lower"
command = abjad.LilyPondLiteral()

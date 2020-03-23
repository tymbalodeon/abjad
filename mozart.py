#!/usr/bin/env python3

import abjad
from abjad.demos import mozart

staff = abjad.Staff(
    """
    c'4 ( d'4 <cs' e'>8 ) -. r8
    <g' b' d''>4 ^ \marcato ~ <g' b' d''>1
    """
)
# abjad.f(staff)
# abjad.show(staff)

fragment = {"t": "g''8 ( e''8 c''8 )", "b": "<c e>4 r8"}

my_measure_dict = {"b": r"c4 ^\trill r8", "t": "e''8 ( c''8 g'8 )"}
treble, bass = mozart.make_mozart_measure(my_measure_dict)

# print(format(treble))
# print(format(bass))

my_measure_dict = mozart.make_mozart_measure_corpus()[-1][-1]
treble, bass = mozart.make_mozart_measure(my_measure_dict)

# print(format(treble))
# print(format(bass))

import random

list_ = [1, "b", 3]
result = [random.choice(list_) for i in range(20)]
result

# choices = mozart.choose_mozart_measures()
# for i, measure in enumerate(choices):
#     print(i, measure)

container = abjad.Container("c'4 d'4 e'4 f'4")
literal = abjad.LilyPondLiteral("before-the-container", "before")
abjad.attach(literal, container)
literal = abjad.LilyPondLiteral("after-the-container", "after")
abjad.attach(literal, container)
literal = abjad.LilyPondLiteral("opening-of-the-container", "opening")
abjad.attach(literal, container)
literal = abjad.LilyPondLiteral("closing-of-the-container", "closing")
abjad.attach(literal, container)
# abjad.f(container)

score = mozart.make_mozart_score()
# abjad.show(score)

lilypond_file = mozart.make_mozart_lilypond_file()
# print(lilypond_file)
# print(format(lilypond_file.header_block))
# print(format(lilypond_file.layout_block))
# print(format(lilypond_file.paper_block))

abjad.show(lilypond_file)

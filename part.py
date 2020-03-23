#!/usr/bin/env python3

import abjad
import copy
from abjad.demos import part

reservoir = part.create_pitch_contour_reservoir()
# for i in range(10):
#     descent = reservoir["First Violin"][i]
#     print(" ".join(str(x) for x in descent))

pitch_contour_reservoir = part.create_pitch_contour_reservoir()
shadowed_contour_reservoir = part.shadow_pitch_contour_reservoir(
    pitch_contour_reservoir
)
durated_reservoir = part.durate_pitch_contour_reservoir(shadowed_contour_reservoir)

descents = durated_reservoir["First Violin"][:10]
for i, descent in enumerate(descents[1:], 1):
    markup = abjad.Markup(r"\rounded-box \bold {}".format(i), direction=abjad.Up)
    abjad.attach(markup, descent[0])

staff = abjad.Staff(abjad.sequence(descents).flatten())
time_signature = abjad.TimeSignature((6, 4))
leaf = abjad.inspect(staff).leaf(0)
abjad.attach(time_signature, leaf)
# abjad.show(staff)

descents = durated_reservoir["Second Violin"][:10]
for i, descent in enumerate(descents[1:], 1):
    markup = abjad.Markup(r"\rounded-box \bold {}".format(i), direction=abjad.Up)
    abjad.attach(markup, descent[0])

staff = abjad.Staff(abjad.sequence(descents).flatten())
time_signature = abjad.TimeSignature((6, 4))
leaf = abjad.inspect(staff).leaf(0)
abjad.attach(time_signature, leaf)
# abjad.show(staff)

descents = durated_reservoir["Viola"][:10]
for i, descent in enumerate(descents[1:], 1):
    markup = abjad.Markup(r"\rounded-box \bold {}".format(i), direction=abjad.Up)
    abjad.attach(markup, descent[0])

staff = abjad.Staff(abjad.sequence(descents).flatten())
shards = abjad.mutate(staff[:]).split([(3, 2)], cyclic=True)
time_signature = abjad.TimeSignature((6, 4))
leaf = abjad.inspect(staff).leaf(0)
abjad.attach(time_signature, leaf)
# abjad.show(staff)

spacing_vector = abjad.SpacingVector(0, 0, 8, 0)
# print(format(spacing_vector))

lilypond_file = part.make_part_lilypond_file()
abjad.show(lilypond_file)

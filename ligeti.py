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
command = abjad.LilyPondLiteral(r"\voiceTwo")
leaf = abjad.inspect(voice_lower).leaf(0)
abjad.attach(command, leaf)
# abjad.show(voice_lower)

import math

n = int(math.ceil(len(pitches) / 2.0))
chord = abjad.Chord([pitches[0], pitches[0] + 12], (n, 8))
articulation = abjad.Articulation(">")
abjad.attach(articulation, chord)

voice_higher = abjad.Voice([chord])
voice_higher.name = "rh_higher"
command = abjad.LilyPondLiteral(r"\voiceOne")
abjad.attach(command, voice_higher)
# abjad.show(voice_higher)

voices = [voice_lower, voice_higher]
container = abjad.Container(voices, simultaneous=True)
staff = abjad.Staff([container])
# abjad.show(staff)


def make_desordre_cell(pitches):
    """
    Makes a Désordre cell.
    """

    notes = [abjad.Note(pitch, (1, 8)) for pitch in pitches]
    notes = abjad.Selection(notes)
    abjad.beam(notes)
    abjad.slur(notes)
    abjad.attach(abjad.Dynamic("f"), notes[0])
    abjad.attach(abjad.Dynamic("p"), notes[1])

    # make the lower voice
    lower_voice = abjad.Voice(notes)
    lower_voice.name = "RH_Lower_Voice"
    command = abjad.LilyPondLiteral(r"\voiceTwo")
    abjad.attach(command, lower_voice)
    n = int(math.ceil(len(pitches) / 2.0))
    chord = abjad.Chord([pitches[0], pitches[0] + 12], (n, 8))
    abjad.attach(abjad.Articulation(">"), chord)

    # make the upper voice
    upper_voice = abjad.Voice([chord])
    upper_voice.name = "RH_Upper_Voice"
    command = abjad.LilyPondLiteral(r"\voiceOne")
    abjad.attach(command, upper_voice)

    # combine them together
    voices = [lower_voice, upper_voice]
    container = abjad.Container(voices, simultaneous=True)

    # make all 1/8 beats breakable
    leaves = abjad.select(lower_voice).leaves()
    for leaf in leaves[:-1]:
        bar_line = abjad.BarLine("")
        abjad.attach(bar_line, leaf)

    return container


pitches = [[0, 4, 7], [0, 4, 7, 9], [4, 7, 9, 11]]
measure = ligeti.make_desordre_measure(pitches)
staff = abjad.Staff([measure])
# abjad.show(staff)


def make_desordre_measure(pitches) -> abjad.Container:
    """
    Makes a measure composed of Désordre cells.

    ``pitches`` is a nested list of integers, like [[1, 2, 3], [2, 3, 4]].
    """
    for sequence in pitches:
        container = make_desordre_cell(sequence)
        duration = abjad.inspect(container).duration()
        duration = abjad.NonreducedFraction(duration)
        time_signature = abjad.TimeSignature(duration)
        leaf = abjad.inspect(container).leaf(0)
        abjad.attach(time_signature, leaf)
    return container


pitches = [[[-1, 4, 5], [-1, 4, 5, 7, 9]], [[0, 7, 9], [-1, 4, 5, 7, 9]]]
staff = ligeti.make_desordre_staff(pitches)
# abjad.show(staff)


def make_desordre_score(pitches):
    """
    Makes Désordre score.
    """

    assert len(pitches) == 2
    staff_group = abjad.StaffGroup(lilypond_type="PianoStaff")

    # build the music
    for hand in pitches:
        staff = make_desordre_staff(hand)
        staff_group.append(staff)

    # set clef and key signature to left hand staff
    leaf = abjad.inspect(staff_group[1]).leaf(0)
    abjad.attach(abjad.Clef("bass"), leaf)
    key_signature = abjad.KeySignature("b", "major")
    abjad.attach(key_signature, leaf)

    # wrap the piano staff in a score
    score = abjad.Score([staff_group])

    return score


upper = [
    [[-1, 4, 5], [-1, 4, 5, 7, 9]],
    [[0, 7, 9], [-1, 4, 5, 7, 9]],
    [[2, 4, 5, 7, 9], [0, 5, 7]],
    [[-3, -1, 0, 2, 4, 5, 7]],
    [[-3, 2, 4], [-3, 2, 4, 5, 7]],
    [[2, 5, 7], [-3, 9, 11, 12, 14]],
    [[4, 5, 7, 9, 11], [2, 4, 5]],
    [[-5, 4, 5, 7, 9, 11, 12]],
    [[2, 9, 11], [2, 9, 11, 12, 14]],
]

lower = [
    [[-9, -4, -2], [-9, -4, -2, 1, 3]],
    [[-6, -2, 1], [-9, -4, -2, 1, 3]],
    [[-4, -2, 1, 3, 6], [-4, -2, 1]],
    [[-9, -6, -4, -2, 1, 3, 6, 1]],
    [[-6, -2, 1], [-6, -2, 1, 3, -2]],
    [[-4, 1, 3], [-6, 3, 6, -6, -4]],
    [[-14, -11, -9, -6, -4], [-14, -11, -9]],
    [[-11, -2, 1, -6, -4, -2, 1, 3]],
    [[-6, 1, 3], [-6, -4, -2, 1, 3]],
]

score = ligeti.make_desordre_score([upper, lower])
lilypond_file = ligeti.make_desordre_lilypond_file(score)
abjad.show(lilypond_file)

import abjad

score = abjad.Score()
piano_staff = abjad.StaffGroup(lilypond_type="PianoStaff")
upper_staff = abjad.Staff(name="Upper_Staff")
upper_staff_voice = abjad.Voice(name="Upper_Staff_Voice")
upper_staff.append(upper_staff_voice)
lower_staff = abjad.Staff(name="Lower_Staff")
lower_staff_voice_2 = abjad.Voice(name="Lower_Staff_Voice_II")
lower_staff.append(lower_staff_voice_2)
piano_staff.append(upper_staff)
piano_staff.append(lower_staff)
score.append(piano_staff)

upper_staff_voice.append(r"{ \time 2/4 a'8 g'8 f'8 e'8 }")
upper_staff_voice.append(r"{ \time 3/4 d'4 g'8 f'8 e'8 d'8 }")
upper_staff_voice.append(r"{ \time 2/4 c'8 d'16 e'16 f'8 e'8 }")
upper_staff_voice.append("{ d'2 }")
upper_staff_voice.append("{ d'2 }")

lower_staff_voice_2.append("{ b4 d'8 c'8 }")
lower_staff_voice_2.append("{ b8 a8 af4 c'8 bf8 }")
lower_staff_voice_2.append("{ a8 g8 fs8 g16 a16 }")

container = abjad.Container(
    [
        abjad.Voice(name="Lower_Staff_Voice_I"),
        abjad.Voice(name="Lower_Staff_Voice_II"),
    ],
    simultaneous=True,
)
literal = abjad.LilyPondLiteral(r"\voiceOne")
abjad.attach(literal, container["Lower_Staff_Voice_I"])
container["Lower_Staff_Voice_I"].append("b2")
literal = abjad.LilyPondLiteral(r"\voiceTwo")
abjad.attach(literal, container["Lower_Staff_Voice_II"])
container["Lower_Staff_Voice_II"].extend("b4 a4")
lower_staff.append(container)

container = abjad.Container(
    [
        abjad.Voice(name="Lower_Staff_Voice_I"),
        abjad.Voice(name="Lower_Staff_Voice_II"),
    ],
    simultaneous=True,
)
literal = abjad.LilyPondLiteral(r"\voiceOne")
abjad.attach(literal, container["Lower_Staff_Voice_I"])
container["Lower_Staff_Voice_I"].append("b2")
literal = abjad.LilyPondLiteral(r"\voiceTwo")
abjad.attach(literal, container["Lower_Staff_Voice_II"])
container["Lower_Staff_Voice_II"].append("g2")
lower_staff.append(container)
abjad.show(score)

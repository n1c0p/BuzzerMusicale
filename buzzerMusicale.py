import RPi.GPIO as GPIO
import time

buzzer_pin = 13
ledPinsBCM = [17, 18, 27, 22, 23, 24, 25, 2, 3, 8]  # BCM

noteLed = {
    "A": 2,  # A = la
    "B": 3,  # B = si
    "C": 27,  # C = do
    "D": 22,  # D = re
    "E": 23,  # E = mi
    "F": 24,  # F = fa
    "G": 25  # G = sol
}

note = {
    'B0': 31,  # B = si
    'C1': 33, 'Cs1': 35,  # C = do
    'D1': 37, 'Ds1': 39,  # D = re
    'Eb1': 39,  # E = mi
    'E1': 41,  # F = fa
    'F1': 44, 'Fs1': 46,  # G = sol
    'G1': 49, 'Gs1': 52,  # A = la
    'A1': 55, 'As1': 58,  # b = bemolle
    'Bb1': 58,  # s = diesis
    'B1': 62,  # 0 1 2 3 4 5 6 7 8 = ottave
    'C2': 65, 'Cs2': 69,
    'D2': 73, 'Ds2': 78,
    'Eb2': 78,
    'E2': 82,
    'F2': 87, 'Fs2': 93,
    'G2': 98, 'Gs2': 104,
    'A2': 110, 'As2': 117,
    'Bb2': 123,
    'B2': 123,
    'C3': 131, 'Cs3': 139,
    'D3': 147, 'Ds3': 156,
    'Eb3': 156,
    'E3': 165,
    'F3': 175, 'Fs3': 185,
    'G3': 196, 'Gs3': 208,
    'A3': 220, 'As3': 233,
    'Bb3': 233,
    'B3': 247,
    'C4': 262, 'Cs4': 277,
    'D4': 294, 'Ds4': 311,
    'Eb4': 311,
    'E4': 330,
    'F4': 349, 'Fs4': 370,
    'G4': 392, 'Gs4': 415,
    'A4': 440, 'As4': 466,
    'Bb4': 466,
    'B4': 494,
    'C5': 523, 'Cs5': 554,
    'D5': 587, 'Ds5': 622,
    'Eb5': 622,
    'E5': 659,
    'F5': 698, 'Fs5': 740,
    'G5': 784, 'Gs5': 831,
    'A5': 880, 'As5': 932,
    'Bb5': 932,
    'B5': 988,
    'C6': 1047, 'Cs6': 1109,
    'D6': 1175, 'Ds6': 1245,
    'Eb6': 1245,
    'E6': 1319,
    'F6': 1397, 'Fs6': 1480,
    'G6': 1568, 'Gs6': 1661,
    'A6': 1760, 'As6': 1865,
    'Bb6': 1865,
    'B6': 1976,
    'C7': 2093, 'Cs7': 2217,
    'D7': 2349, 'Ds7': 2489,
    'Eb7': 2489,
    'E7': 2637,
    'F7': 2794, 'Fs7': 2960,
    'G7': 3136, 'Gs7': 3322,
    'A7': 3520, 'As7': 3729,
    'Bb7': 3729,
    'B7': 3951,
    'C8': 4186, 'Cs8': 4435,
    'D8': 4699, 'Ds8': 4978
}

super_mario_theme = [
    note['E5'], note['E5'], 0, note['E5'],
    0, note['C5'], note['E5'], 0,
    note['G5'], 0, 0, 0,
    note['G4'], 0, 0, 0,

    note['C5'], 0, 0, note['G4'],
    0, 0, note['E4'], 0,
    0, note['A4'], 0, note['B4'],
    0, note['As4'], note['A4'], 0,

    note['G4'], note['E5'], note['G5'],
    note['A5'], 0, note['F5'], note['G5'],
    0, note['E5'], 0, note['C5'],
    note['D5'], note['B4'], 0, 0,

    note['C5'], 0, 0, note['G4'],
    0, 0, note['E4'], 0,
    0, note['A4'], 0, note['B4'],
    0, note['As4'], note['A4'], 0,

    note['G4'], note['E5'], note['G5'],
    note['A5'], 0, note['F5'], note['G5'],
    0, note['E5'], 0, note['C5'],
    note['D5'], note['B4'], 0, 0
]
super_mario_tempo = [
    12, 12, 12, 12,
    12, 12, 12, 12,
    12, 12, 12, 12,
    12, 12, 12, 12,

    12, 12, 12, 12,
    12, 12, 12, 12,
    12, 12, 12, 12,
    12, 12, 12, 12,

    9, 9, 9,
    12, 12, 12, 12,
    12, 12, 12, 12,
    12, 12, 12, 12,

    12, 12, 12, 12,
    12, 12, 12, 12,
    12, 12, 12, 12,
    12, 12, 12, 12,

    9, 9, 9,
    12, 12, 12, 12,
    12, 12, 12, 12,
    12, 12, 12, 12,
]

underworld_super_mario_theme = [
    note['C4'], note['C5'], note['A3'], note['A4'],
    note['As3'], note['As4'], 0,
    0,
    note['C4'], note['C5'], note['A3'], note['A4'],
    note['As3'], note['As4'], 0,
    0,
    note['F3'], note['F4'], note['D3'], note['D4'],
    note['Ds3'], note['Ds4'], 0,
    0,
    note['F3'], note['F4'], note['D3'], note['D4'],
    note['Ds3'], note['Ds4'], 0,
    0, note['Ds4'], note['Cs4'], note['D4'],
    note['Cs4'], note['Ds4'],
    note['Ds4'], note['Gs3'],
    note['G3'], note['Cs4'],
    note['C4'], note['Fs4'], note['F4'], note['E3'], note['As4'], note['A4'],
    note['Gs4'], note['Ds4'], note['B3'],
    note['As3'], note['A3'], note['Gs3'],
    0, 0, 0
]

underworld_tempo = [
    12, 12, 12, 12,
    12, 12, 6,
    3,
    12, 12, 12, 12,
    12, 12, 6,
    3,
    12, 12, 12, 12,
    12, 12, 6,
    3,
    12, 12, 12, 12,
    12, 12, 6,
    6, 18, 18, 18,
    6, 6,
    6, 6,
    6, 6,
    18, 18, 18, 18, 18, 18,
    10, 10, 10,
    10, 10, 10,
    3, 3, 3
]


def setup():  # setta il GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer_pin, GPIO.OUT)
    # LED Bar
    GPIO.setup(ledPinsBCM, GPIO.OUT)  # set all ledPins to OUTPUT mode
    GPIO.output(ledPinsBCM, GPIO.HIGH)  # make all ledPins output HIGH level, turn off all led


def destroy():
    GPIO.cleanup()


def play(traccia_audio, tempo, intervallo, note, ritmo=0.800):
    for i in range(0, len(traccia_audio)):  # inizio riproduzione

        for x in note:
            if note[x] == traccia_audio[i]:
                # print(f"Nota: {x} Frequenza: {note[x]}")
                for lettera in x:
                    # print(f"Prima lettera {lettera} pin {noteLed[lettera]}")
                    """ Accendo il LED Bar """
                    GPIO.output(noteLed[lettera], GPIO.LOW)
                    pin = noteLed[lettera]
                    break
                break

        durata_note = ritmo / tempo[i]
        generatore_onda(traccia_audio[i],
                        durata_note)  # lancia la funzione generatore_onda che crea un segnale ondulatorio in base alla frequenza della nota data

        intervallo_note = durata_note * intervallo
        time.sleep(intervallo_note)
        """ Spengo il LED Bar """
        GPIO.output(pin, GPIO.HIGH)


def generatore_onda(frequenza, durata_note):  # crea la funzione generatore_onda
    if frequenza == 0:  # se la frequenza e' 0 non crea nessuna onda
        time.sleep(durata_note)
        return
    periodo = 1.0 / frequenza  # calcolo del periodo come 1/frequenza
    semiperiodo = periodo / 2  # calcolo di meta periodo
    numero_onde = int(durata_note * frequenza)  # numero di onde che verranno generate

    for i in range(numero_onde):  # inizia a generare le onde

        GPIO.output(buzzer_pin, True)  # setta il pin HIGH per meta del periodo
        time.sleep(semiperiodo)  # il pin e' in HIGH
        GPIO.output(buzzer_pin, False)  # setta il pin in LOW per l'altra meta del periodo
        time.sleep(semiperiodo)  # il pin e' in LOW


if __name__ == '__main__':  # il programma parte da qui
    try:
        setup()
        """
        loop()
        """
        print("Super Mario Theme")
        play(super_mario_theme, super_mario_tempo, 1.3, note, 0.800)
        time.sleep(2)

        print("Super Mario Underworld Theme")
        play(underworld_super_mario_theme, underworld_tempo, 1.3, note, 0.800)
        time.sleep(2)
        destroy()

    except KeyboardInterrupt:  # il programma si arresta se viene premuto 'CTRL+C'
        destroy()

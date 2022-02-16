def Trichord(row):
    Trichords = [row[3*i:3*i+3] for i in range(4)]
    primeforms = [PrimeForm(pitches) for pitches in Trichords]
    return primeforms
def Tetrachord(row):
    Tetrachords = [row[4*i:4*i+4] for i in range(3)]
    primeforms = [PrimeForm(pitches) for pitches in Tetrachords]
    return primeforms   
def PrimeForm(pitches):
    pitches.sort()
    outerintervals = [12 - (pitches[i] - pitches[i-1])%12 for i in range(len(pitches))]
    correctrotation = outerintervals.index(min(outerintervals))
    rotatedpitches = [pitches[(i+correctrotation) % len(pitches)] for i in range(len(pitches))]
    normalorder = [(pitch - rotatedpitches[0]) % 12 for pitch in rotatedpitches]
    for i in range(len(normalorder)//2):
        if normalorder[i+1] - normalorder[i] > normalorder[-i-1] - normalorder[-i-2]:
            primeform = [-(normalorder[-i-1] - normalorder[-1]) for i in range(len(normalorder))]
            break
        else:
            primeform = normalorder[:]
    return primeform
print (Trichord([9, 0, 4, 1, 5, 8, 3, 6, 10, 7, 11, 2]))

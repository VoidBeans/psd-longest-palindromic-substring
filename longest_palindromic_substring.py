# Loosely based on Manacher's algorithm...
def findLongestPalindromicSubstring(string):
    if len(string) < 2:
        return string

    string = getUpdatedString(string)
    
    radii = [0 for _ in range(len(string))]
    center = 0
    radius = 0

    for i in range(len(string)):
        mirror = 2 * center - i
        if radius > i:
            radii[i] = min(radius - i, radii[mirror])
        else:
            radii[i] = 0

        # The try-clause here is used to deflect index out of bounds exceptions.
        # The condition is made simpler in this way without having to check bounds.
        try:
            while string[i + 1 + radii[i]] == string[i - 1 - radii[i]]:
                radii[i] += 1
        except:
            pass

        if i + radii[i] > radius:
            center = i
            radius = i + radii[i]

    maxRadius = max(radii)
    maxCenter = radii.index(maxRadius)

    return string[maxCenter - maxRadius : maxCenter + maxRadius].replace('|', '')
    
def getUpdatedString(string):
    updatedString = ['|']
    for c in string:
        updatedString += [c, '|']
                
    return ''.join(updatedString)
    
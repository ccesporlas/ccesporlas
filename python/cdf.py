from time import time
from numpy import array, unique

#===============================================================================
# Fast CDF algorithm without the need for binning
# Input: filepath of the file containing raw data, the number of decimal places
# to consider in making the bins, CDF arrange method (xg, xl, pdf)
# "pdf" - returns the PDF of the data
# "xl" - returns the CDF using sum(xi) < x
# "xg" - returns the CDF using sum(xi) > x
#===============================================================================

def CDF(filename, num_dec, arrange="xg"):
    f = open(filename)
    f2 = open(filename + "-hist", 'w')
    freq = {}
    print("Frequency Count")
    for line in f:
        try:
            entry = round(float(line), num_dec)
            freq[entry] = freq.get(entry, 0) + 1
        except ValueError:
            pass
    f.close()
    print('Writing to file')
    keys = freq.keys()
    sum = 0
    if arrange == "pdf":
        for key in keys:
            sum += freq[key]
            f2.write(str(key) + "\t" + str(freq[key]) + "\n")
    elif arrange == "xg":
        keys.sort(reverse=True)
        for key in keys:
            sum += freq[key]
            f2.write(str(key) + "\t" + str(sum) + "\n")
    elif arrange == "xl":
        keys.sort()
        for key in keys:
            sum += freq[key]
            f2.write(str(key) + "\t" + str(sum) + "\n")
    f2.close()

if __name__ == "__main__":
    CDF("soi", 2, "pdf")

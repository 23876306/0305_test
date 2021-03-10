import sys
import MyModudle as mm

if sys.argv[1] == "-f":
    val = int(sys.argv[2])
    print(mm.getFibonacci(val))

elif sys.argv[1] == "-n":
    val = int(sys.argv[2])
    print(mm.getDigits_Number(val))

elif sys.argv[1] == "-r":
    val = int(sys.argv[2])
    print(mm.getRandom_Number(val))

elif sys.argv[1] == "-c":
    val = int(sys.argv[2])
    print(mm.getC_value(val))

elif sys.argv[1] == "-F":
    val = int(sys.argv[2])
    print(mm.Floor_math(val))
import sys
from tools import *

def main():
    orig_filePath = sys.argv[1]
    imit_filePath = sys.argv[2]
    result_filePath = sys.argv[3]

    orig = SimHash( readFile(orig_filePath) )
    imit = SimHash( readFile(imit_filePath) )

    hanmingDistance = orig.hanmingDistance( imit )

    writeFile( result_filePath, hanmingDistance )

Test()

main()
    

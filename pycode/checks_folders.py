import sys
import common_code as cc

for i in range(1,len(sys.argv)):
    cc.check_and_make(sys.argv[i])
    print('checked ',sys.argv[i])
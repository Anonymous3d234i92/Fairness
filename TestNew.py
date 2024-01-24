import os

#os.system("python3 ./MutantGen-Test.py")
os.system("cp NewThres/TestGenerator-NMTMLT/*.txt NewThres/TestGenerator-NMTMLT/*.index ./NMT_zh_en0-8Mu/pad")
os.system("cd ./NMT_zh_en0-8Mu/pad && sh desp.sh")
os.system("cd ./NMT_zh_en0-8Mu/pad && sh test.sh")

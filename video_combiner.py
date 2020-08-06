from glob import glob
from itertools import groupby
import os

def getLectureRoot(x):
    return x.split('/')[-1].split('P')[0]

baseDir = "/Users/neuropunk/Documents/_grad_school/mathy/stat656/lectures_beta"
mp4Files = glob("%s/STAT656L*.mp4" % baseDir)

for k, v in groupby(sorted(mp4Files), lambda x: getLectureRoot(x)):
    subMp4Files = list(v)
    aggedMp4File = "%s/AGGED_%s.mp4" % (baseDir, k)

    fileCompsStr = " ".join(["-i %s" % x for x in subMp4Files])
    filterStr = " ".join(["[%d:v] [%d:a]" % (idx, idx) for idx, x in enumerate(subMp4Files)])
    cmd = """ffmpeg %s -filter_complex "%s concat=n=%d:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" %s""" \
          % (fileCompsStr, filterStr, len(subMp4Files), aggedMp4File)

    print("Running Command: %s" % cmd)
    os.system(cmd)

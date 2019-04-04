import os
import re

files = ["train", "dev", "test"]
for f in files:
    bio_format = []
    units = []
    labels = {}
    for line in open(os.path.join("data/resume", f+".txt"), "r", encoding="utf-8"):
        line = line.strip()
        if not line:
            bio_format.append(units)
            units = []
        else:
            seg = line.split()
            token = seg[0][0]
            # units.append(seg[0])
            bioes_tag = seg[1]
            if bioes_tag.startswith("M") or bioes_tag.startswith("E"):
                idx_ = bioes_tag.index("-")
                bio_tag = "I" + bioes_tag[idx_:]
            elif bioes_tag.startswith("S"):
                idx_ = bioes_tag.index("-")
                bio_tag = "B" + bioes_tag[idx_:] ###
            else:
                bio_tag = bioes_tag
            units.append((token, bio_tag))

    with open(os.path.join("data/resume", f+"_bio.txt"), "w", encoding="utf-8") as fw:
        for bio_sent in bio_format:
            for bio_units in bio_sent:
                label = bio_units[1]
                if label not in labels.keys():
                    labels[label] = len(labels.keys())
                fw.write("\t".join(bio_units))
                fw.write("\n")
            fw.write("\n")
        fw.close()

    print(labels)
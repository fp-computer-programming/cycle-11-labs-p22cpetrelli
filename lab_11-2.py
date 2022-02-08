#author CJP 2/8/2022

alma = open("alma_mater.txt")

lines = alma.readlines()

lines.reverse()

new_txt = "".join(lines)

print(new_txt)

alma.close()
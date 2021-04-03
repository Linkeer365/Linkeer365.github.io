import os

if not os.path.exists("all_links.txt"):
    open("all_links.txt","w").close()

abbrlinks=[]
# project_name=os.getcwd().split(os.sep)[-3]

cnt=0
for each in os.listdir("."):
    if each.endswith(".md"):
        cnt+=1
        with open("./{}".format(each),"r",encoding="utf-8") as f:
            lines=f.readlines()
        for line in lines:
            if line.startswith("abbrlink: "):
                abbr_num=line.split(" ")[1].strip("\n")
                abbrlink=f"https://linkeer365.github.io/{abbr_num}/"
                abbrlink.replace("'","")
                abbrlinks.append(abbrlink)
                break

pagecnt=cnt//10+1 if cnt%10!=0 else cnt//10

pagelinks=[]

for pagenum in range(1,pagecnt+1):
    if pagenum!=1:
        pagelink1=f"https://linkeer365.github.io/page/{pagenum}/"
        pagelink2=f"https://linkeer365.github.io/archives/page/{pagenum}/"
        pagelinks.append(pagelink1)
        pagelinks.append(pagelink2)

guide_links=[   f"https://linkeer365.github.io/",
                f"https://linkeer365.github.io/archives/",
            ]

links=[]

links.extend(guide_links)
links.extend(pagelinks)
links.extend(abbrlinks)

# print(project_name)
# print(abbrlinks)

links_s="\n".join(links)+"\n"

with open("all_links.txt","w",encoding="utf-8") as f:
    f.write(links_s)
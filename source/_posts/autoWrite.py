import os

from datetime import datetime

def main(file_dir=r"D:\OneDrive - CUHK-Shenzhen\Linkeer365Blog\Linkeer365.github.io\source\_posts"):
	empty_names=[]
	for each in os.listdir(file_dir):
		if (not os.path.isdir(each)) and each.endswith(".md"):
			with open(each,encoding="utf-8") as f:
				if len(f.readlines())<=5:
					empty_name=each[:-3]
					empty_names.append(empty_name)
					print("Empty Name:\t",empty_name)

	for each in empty_names:
		abs_md_file_path=file_dir+os.sep+each+'.md'
		abs_dir_path=file_dir+os.sep+each+"\\"
		print(abs_md_file_path)
		if os.path.isdir(abs_dir_path):
			os.chdir(abs_dir_path)
			whole_lines=[]
			if len(os.listdir(abs_dir_path))!=0:
				print("LEN:\t",len(os.listdir(abs_dir_path)))
				cnt=0
				for each_pic in os.listdir("."):
					if each_pic.endswith("jpg") or each_pic.endswith("png"):
						if cnt==0:
							first_pic=each_pic
						whole_line="{"+"% asset_img {} %".format(each_pic)+"}"
						whole_lines.append(whole_line)
						cnt+=1
					print(whole_lines)
				if first_pic[0]=='S':
					pre_len=len("Screenshot_")
				else:
					pre_len=0
				raw_time_str_ymd,raw_time_str_hms=(first_pic[pre_len:pre_len+15]).split("_")
				yy,mm,dd=raw_time_str_ymd[0:4],raw_time_str_ymd[4:6],raw_time_str_ymd[6:]
				hh,minmin,ss=raw_time_str_hms[0:2],raw_time_str_hms[2:4],raw_time_str_hms[4:]
				time_str="{}-{}-{} {}:{}:{}".format(yy,mm,dd,hh,minmin,ss)
				with open(abs_md_file_path,"r",encoding="utf-8") as f:
					lines=[each for each in f]
				lines[2]="date: {}\n".format(time_str)
				s="".join(lines)
				with open(abs_md_file_path,"w",encoding="utf-8") as f:
					f.write(s)
				with open(abs_md_file_path,"a",encoding="utf-8") as f:	
					for each2 in whole_lines:
						f.write(each2+"\n")
						# print("good.")
						os.chdir(file_dir)
			else:
				print("{} is empty.".format(each))
				os.chdir(file_dir)
				continue
	print("done.")

main()
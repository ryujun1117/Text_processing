PATH = "./data/作業ファイル"

# PATHを入力して、指定したディレクトリのファイルとフォルダの情報を引いてくる関数

# フォルダの数を出力
def folder_num(PATH):
  import os
  output = print(sum(os.path.isdir(os.path.join(PATH, name)) for name in os.listdir(PATH)))
  return output


# ファイルの数を出力
def file_num(PATH):
  import os
  output = print(sum(os.path.isfile(os.path.join(PATH, name)) for name in os.listdir(PATH)))
  return output


# フォルダ名のリストの取得
def folder_name_list(PATH):
  import os
  files = os.listdir(PATH)
  return files


# ファイル名のリストを取得
def file_name_list(PATH):
  import glob
  file_list = sorted(glob.glob(PATH + "*.txt"))
  return file_list


# txtファイルを開いて、csvファイルに書き込む
def typeC_write(OUTPUTFILE, output_C):
  import csv
  global NO_C
  with open(OUTPUTFILE, 'a', newline='', encoding = "shift-jis", errors = "ignore") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                          quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["C_" + str(NO_C), output_C[0],"-", "-", "-", "-", "-", "-", "-", output_C[1], output_C[2]])
  NO_C += 1
  return
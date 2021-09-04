PATH = "./data/作業ファイル"

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
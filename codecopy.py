import shutil
import os

basepath=r"H:\JAVA培训\05-项目二\08-十次方\01-前端\前端开发资源"
createpath="D:\代码"

def copy_code(basepath):
    dir_lst=os.listdir(basepath)
    if "代码" in dir_lst:
        cwd_path=os.path.join(basepath,"代码")
        sub_path=os.path.basename(os.path.dirname(cwd_path))
        parent_name=os.path.basename(os.path.dirname(basepath))
        new_dir=os.path.join(createpath,parent_name,sub_path)
        # if not os.path.exists(new_dir):
        #     os.makedirs(new_dir)
        shutil.copytree(cwd_path,new_dir)
    elif "code" in dir_lst:
        cwd_path = os.path.join(basepath, "code")
        sub_path = os.path.basename(os.path.dirname(cwd_path))
        parent_name = os.path.basename(os.path.dirname(basepath))
        new_dir = os.path.join(createpath, parent_name, sub_path)
        # if not os.path.exists(new_dir):
        #     os.makedirs(new_dir)
        shutil.copytree(cwd_path, new_dir)
    else:
        for dirname in dir_lst:
            basepath1=os.path.join(basepath,dirname)
            copy_code(basepath1)

copy_code(basepath)
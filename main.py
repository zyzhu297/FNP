import os
import re
import requests
import shutil
import time



filePath = r'D:\Pixiv\pixiv'
tmpPath = r'D:\Pixiv\tmp'


def remove_duplication(change=False):
    d = dict()
    pattern = r'\d+(_p\d+)?'
    for name in os.listdir(filePath):
        full_path = os.path.join(filePath, name)
        match = re.match(pattern, name)
        if match:
            # print(name)
            pren = match.group()
        else:
            print('格式错误', name)
            continue
        if pren in d:
            if len(full_path) >= len(d[pren]):
                print('保留的', full_path)
                print('要删的', d[pren])
                if change:
                    os.remove(d[pren])
            else:
                print('保留的', d[pren])
                print('要删的', full_path)
                if change:
                    os.remove(full_path)
        else:
            d[pren] = full_path


def make_id_pid():
    pattern = re.compile(r'\(pid-(\d+)\)(.*)')

    for file_name in os.listdir(filePath):
        match = pattern.match(file_name)
        full_path = os.path.join(filePath, file_name)
        if match:
            pid = match.group(1)
            content = match.group(2)
            new_file_name = f"{pid}_{content}"
            new_full_path = os.path.join(filePath, new_file_name)
            # 重命名文件
            os.rename(full_path, new_full_path)
            print(f"File renamed: {full_path} -> {new_full_path}")
        else:
            # print(f"No match found for {file_name}")
            pass


def make_id_other():
    pattern = re.compile(r'(.*)-(\d+.*)(\..*)')

    for file_name in os.listdir(filePath):
        match = pattern.match(file_name)
        full_path = os.path.join(filePath, file_name)
        # print(file_name)
        if match:
            yyyy = match.group(1)
            xxxx = match.group(2)
            t = match.group(3)
            new_file_name = f"{xxxx}_{yyyy}"

            # 构建新的完整路径
            new_full_path = os.path.join(filePath, new_file_name + t)

            # 重命名文件
            try:
                os.rename(full_path, new_full_path)
            except:
                os.remove(full_path)
            print(f"File renamed: {full_path} -> {new_full_path}")
        else:
            # print(f"No match found for {file_name}")
            pass


def delete_0user(change=False):
    pattern = r"(.*0+users.*)|(.*0+收藏.*)"
    pattern1 = '(\(.*\))'
    for name in os.listdir(filePath):
        full_path = os.path.join(filePath, name)
        match = re.match(pattern, name)
        if match:
            match1 = re.search(pattern1, name)
            if match1:
                tags = match1.group(0)[1:-1].split(',')
                # print(tags)
                for tag in tags[:]:
                    # print(tag)
                    match2 = re.match(pattern, tag)
                    if match2:
                        tags.remove(tag)
                new_tags = '(' + ','.join(tags) + ')'
                new_name = re.sub(pattern1, new_tags, name)
                new_full_path = os.path.join(filePath, new_name)
                print(full_path)
                print(new_full_path)
                try:
                    os.rename(full_path, new_full_path)
                except:
                    print(name)
            else:
                print(name)
                ind = name.index('.jpg') if '.jpg' in name else name.index('.png')
                file_name = name[:ind] + ')' + name[ind:]
                new_full_path = os.path.join(filePath, file_name)
                # try:
                #     os.rename(full_path, new_full_path)
                # except:
                #     print(name)
        else:
            # print('格式错误', name)
            continue

def extend_name(rm = False):
    import webbrowser
    s = set()
    op = set()
    url = 'https://www.pixiv.net/artworks/'
    i = 0
    j = 0
    for name in os.listdir(tmpPath + 'l'):
        l_ind = name.find('_')
        pid = name[:l_ind]
        op.add(pid)
    # print(op)
    for name in os.listdir(tmpPath):
        # if len(name) < 18:
        l_ind = name.find('_')
        pid = name[:l_ind]
        full_path = os.path.join(tmpPath, name)
        # print(full_path)
        # os.remove(full_path)
        if pid in op:
            continue
            # j += 1
            # print(full_path)
            # os.remove(full_path)
            # continue
        i += 1
        # tmp_path = os.path.join(r'D:\Pixiv\新建文件夹', name)
        # print(full_path)
        # time.sleep(0.1)
        # shutil.move(full_path, tmp_path)
        if i < 0:
            continue
        webbrowser.open(url + pid)
        time.sleep(0.1)
        if i > 49:
            break
    print(j)
    
def find_tag():
    pattern = r'\)\.'
    i = 0
    for name in os.listdir(filePath):
        if not re.search(pattern, name):
            if len(name) > 100:
                full_path = os.path.join(filePath, name)
                newn_path = os.path.join(filePath, name[:81] + ')' + name[-4:])
                os.rename(full_path, newn_path)
                print(full_path)
                print(newn_path)
            i += 1
            full_path = os.path.join(filePath, name)
            tmp_path = os.path.join(tmpPath, name)
            print(full_path)
            time.sleep(0.1)
            shutil.move(full_path, tmp_path)
    print(i)
    return

def move_short():
    i = 0
    for name in os.listdir(filePath):
        if len(name) < 32:
            full_path = os.path.join(filePath, name)
            tmp_path = os.path.join(tmpPath, name)
            print(full_path)
            # os.remove(full_path)
            i += 1
            time.sleep(0.1)
            shutil.move(full_path, tmp_path)
        # if i > 20:
        #     break

# make_id_other()
# remove_duplication(change=False)
# delete_0user(change=True)
extend_name()
# move_short()
# find_tag()

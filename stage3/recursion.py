import os
# print the directory's content
print(os.listdir('E:/down'))
# judge if the thing is directory
os.path.isdir('E:/down')
# judge if the path exists
os.path.exists('E:/down')
def get_files(path):
    # return all files
    file_list=[]
    if os.path.exists(path):
        for f in os.listdir(path):
            newpath=path+'/'+f
            if os.path.isdir(newpath):
                ele=get_files(newpath)
                file_list.append(ele)
            else:
               file_list.append(newpath)
    else:
        return []
    return file_list
if __name__ == '__main__':
    list1=get_files(r'E:\down\test')
    print(list1)
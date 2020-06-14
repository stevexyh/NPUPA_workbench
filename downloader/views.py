import os
from django.shortcuts import render
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
file_list = []
FILE_DIR = './downloader/contents/'
file_ignore = FILE_DIR + '.fileIgnore'


def home(request):
    return render(request, 'downloader/home.html')


def base(request):
    return render(request, 'downloader/base.html')


def upload(request):
    content = {}
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['file']
            store = FileSystemStorage()
            file_name = store.save(uploaded_file.name, uploaded_file)
            content['file_name'] = file_name
        except:
            content['file_name'] = 'NULL'
    return render(request, 'downloader/upload.html', content)


def downloads(request):
    list_files()
    content = {'files': file_list}
    return render(request, 'downloader/downloads.html', content)


def download_file(request):
    if request.method == 'POST':
        filename = request.POST.get('file_name')
        f = open(FILE_DIR + filename, 'rb')
        response = FileResponse(f)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename=' + filename
        return response


def list_files():
    '''获取目录下所有文件信息'''
    global file_list
    file_list.clear()
    try:
        file_dir = os.listdir(FILE_DIR)
    except FileNotFoundError:
        os.mkdir(FILE_DIR)
        file_dir = os.listdir(FILE_DIR)
    file_dir.sort()

    def is_ignored(filename):
        '''排除.fileIgnore列表中的文件'''
        with open(file_ignore, 'r') as f:
            ignored_files = f.read().splitlines()
            return True if filename in ignored_files else False

    def get_FileSize(filePath):
        '''获取文件的大小,结果保留两位小数'''
        fsize = os.path.getsize(filePath)
        level = 1000

        if fsize < level:
            return '{:.2f}'.format(fsize) + 'B'
        elif fsize < level**2:
            return '{:.2f}'.format(fsize/level) + 'KB'
        elif fsize < level**3:
            return '{:.2f}'.format(fsize/(level**2)) + 'MB'
        elif fsize < level**4:
            return '{:.2f}'.format(fsize/(level**3)) + 'GB'

    for f in file_dir:
        if not is_ignored(f):
            file_list.append({
                'file_name': f,
                'file_size': get_FileSize(FILE_DIR + f),
            })

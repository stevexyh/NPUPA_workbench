import os
from django.shortcuts import render
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage

FILE_LIST = []
FILE_DIR = './downloader/contents/'
FILE_IGNORE = FILE_DIR + '.fileIgnore'


def base(request):
    '''Render base template'''

    return render(request, 'downloader/base.html')


def home(request):
    '''Render home page'''

    return render(request, 'downloader/home.html')


def upload(request):
    '''Render upload page & upload files'''

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
    '''Render downloads page'''

    list_files()
    content = {'files': FILE_LIST}
    return render(request, 'downloader/downloads.html', content)


def download_file(request):
    '''Download files'''

    if request.method == 'POST':
        filename = request.POST.get('file_name')
        target_file = open(FILE_DIR + filename, 'rb')
        response = FileResponse(target_file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename=' + filename
        return response


def list_files():
    '''获取目录下所有文件信息'''
    global FILE_LIST
    FILE_LIST.clear()
    try:
        file_dir = os.listdir(FILE_DIR)
    except FileNotFoundError:
        os.mkdir(FILE_DIR)
        file_dir = os.listdir(FILE_DIR)
    file_dir.sort()

    def is_ignored(filename):
        '''排除.fileIgnore列表中的文件'''
        with open(FILE_IGNORE, 'r') as file_ignore:
            ignored_files = file_ignore.read().splitlines()
            return True if filename in ignored_files else False

    def get_filesize(file_path):
        '''获取文件的大小,结果保留两位小数'''
        fsize = os.path.getsize(file_path)
        level = 1000

        if fsize < level:
            return '{:.2f}'.format(fsize) + 'B'
        elif fsize < level**2:
            return '{:.2f}'.format(fsize/level) + 'KB'
        elif fsize < level**3:
            return '{:.2f}'.format(fsize/(level**2)) + 'MB'
        elif fsize < level**4:
            return '{:.2f}'.format(fsize/(level**3)) + 'GB'

    for each_file in file_dir:
        if not is_ignored(each_file):
            FILE_LIST.append({
                'file_name': each_file,
                'file_size': get_filesize(FILE_DIR + each_file),
            })

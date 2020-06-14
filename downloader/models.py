from django.db import models

# Create your models here.


class FileSource(models.Model):
    '''文件资源'''
    file_name = models.CharField(max_length=50, primary_key=True)
    size = models.CharField(max_length=50)
    upload_date = models.DateTimeField(auto_now_add=True)
    uploader = models.CharField(max_length=50, default='admin')
    description = models.TextField(default='')
    download_cnt = models.IntegerField(default=0)
    file_body = models.FileField(
        upload_to='', default='null')

    def __str__(self):
        dic = {
            'file_name': self.file_name,
            'size': self.size,
            'upload_date': self.upload_date,
            'uploader': self.uploader,
            'description': self.description,
            'download_cnt': self.download_cnt,
        }
        return str(dic)

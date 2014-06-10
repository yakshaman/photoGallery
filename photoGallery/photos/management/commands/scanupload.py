from django.core.management.base import BaseCommand, CommandError
from photos.models import Album, Photo
from django.conf import settings
from pprint import pformat
import os
from datetime import datetime
import imghdr
from utils.randString import genString
import shutil
from utils.thumbnails import genThumbs

class Command (BaseCommand) :
    args = 'Nope'
    help = 'Checks the upload dir for new pics and albums'

    def addPicToAlbum(self, fname, fpath, album) :
        self.stdout.write("Adding pic %s to album %d" % (fname, album))
        if imghdr.what(fpath) :
            try :
                p = Photo.objects.get(album=album, orig_filename__exact=fname)
                self.stdout.write("%s already in album %d" % (fname, album))
            except :
                filename, extension = os.path.splitext(fname)
                rname = genString() + extension
                Photo(album=album, title=fname, date=datetime.now(), orig_filename=fname, gen_filename=rname).save()
                os.rename(fpath, os.path.join(settings.STORAGE_DIR, rname))
                genThumbs(self, rname)

        else :
            self.stdout.write("File %s is not an image file" % fname)
            os.remove(fpath)

    def manageAlbum(self, fname, fpath) :
        self.stdout.write("Checking if the is already an album with this name")
        try :
            a = Album.objects.get(title__exact=fname)
            self.stdout.write("Album %s already present, adding pics to it" % fname)
        except :
            self.stdout.write("Album %s does not exists, creating it" % fname)
            a = Album(title=fname, date=datetime.now(), path=fpath)
            a.save()

        self.stdout.write(pformat(a))

        ls = os.listdir(fpath)
        for f in ls :
            ppath = os.path.join(fpath, f)
            if (os.path.isfile(ppath)) :
                self.addPicToAlbum(f, os.path.join(fpath, f), a.id)
        os.rmdir(fpath)

    def handle(self, *args, **options) :
        ls = os.listdir(settings.UPLOAD_DIR)
        self.stdout.write(settings.UPLOAD_DIR)
        self.stdout.write(pformat(ls))
        for f in ls :
            fpath = os.path.join(settings.UPLOAD_DIR, f)
            if os.path.isfile(fpath) :
                self.addPicToAlbum(f, fpath, 1)
            if os.path.isdir(fpath) :
                self.manageAlbum(f, fpath)

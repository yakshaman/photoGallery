from PIL import Image
from django.conf import settings
import os

def genThumbs(self ,file) :
    self.stdout.write("Doing thumbs for %s" % file)
    doThumb(self, settings.S_THUMB_SIZE, file, 'S')
    doThumb(self, settings.M_THUMB_SIZE, file, 'M')
    doThumb(self, settings.L_THUMB_SIZE, file, 'L')

def doThumb(self, size, fname, d) :
    self.stdout.write("Doing %s size thumb for %s" % (d, fname))
    im = Image.open(os.path.join(settings.STORAGE_DIR, fname))
    im.thumbnail(size)
    im.save(os.path.join(settings.STORAGE_DIR, d + '_' + fname))

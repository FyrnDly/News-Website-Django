from django.db import models
from django.utils.text import slugify

# Create your models here.
class CategoryChoice(models.TextChoices):
    ekonomi = 'ekonomi'
    sosial_Budaya = 'sosial-dan-budaya'
    pemerintah = 'pemerintahan'
    lainnya = 'lainnya'

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255, default='admin')
    category = models.CharField(max_length=255, choices=CategoryChoice.choices, default=CategoryChoice.lainnya)
    image = models.ImageField(upload_to='static/dunia/')
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return f"{self.id} | {self.title}"

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def getUrl(self):
        return f"/dunia/{self.category}/{self.slug}"
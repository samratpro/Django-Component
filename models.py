
# For JSON Field only
import jsonfield


# Create your models here.
class KeywordData(models.Model):
    List_Name = models.CharField(max_length=15, null=True)
    keywords = jsonfield.JSONField(null=True)


    def __str__(self):
        return self.List_Name

    def save(self, *args, **kwargs):
        return super.save(*args, **kwargs)    

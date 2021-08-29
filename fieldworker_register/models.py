from django.db import models

# Create your models here.

class Fieldworker(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    function=models.CharField(max_length=20)
    created_at=models.DateField(auto_now_add=True)
    
	
    class Meta:
        db_table = 'fieldworker' # table name
        managed = False
		
    def __str__(self):
        return self.first_name

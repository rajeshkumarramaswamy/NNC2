from django.db import models


class noc(models.Model):
        name = models.CharField(max_length=30)

	class Meta:
        	db_table = u'noc'


        def __str__(self):
                return self.name

class partner(models.Model):
        name = models.CharField(max_length=30)

	noc_id = models.IntegerField()
        def __str__(self):
                return self.name
	class Meta:
                db_table = u'partner'	


class client(models.Model):
	name = models.CharField(max_length=30)
	noc_id = models.IntegerField()
	partner_id = models.IntegerField()
	
	class Meta:
                db_table = u'client'


	def __str__(self):
		return self.name

	

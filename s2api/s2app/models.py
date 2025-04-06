from django.db import models


# Create geographic model for the project
class mdlGeo(models.Model):
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.country


# Create project category model for the project
class mdlPCategory(models.Model):
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)

    def __str__(self):
        return self.subcategory


# Create the model for the project 
class  mdlProject(models.Model):
    project = models.CharField(max_length=200)
    subcategory = models.ForeignKey(mdlPCategory, on_delete=models.CASCADE)
    country = models.ForeignKey(mdlGeo, on_delete=models.CASCADE)
    year = models.CharField(max_length=4) 
    budget= models.DecimalField(max_digits=10, decimal_places=2)
    OUTCOME_TYPES = [('S','Success'),('F','Failure'),('O','Ongoing')]
    outcome= models.CharField(max_length=100, choices=OUTCOME_TYPES)

    def __str__(self):
        return self.project

# Create project charter model for the project
class mdlPCharter(models.Model):
    project_phase = models.CharField(max_length=200)
    project_owner = models.CharField(max_length=200)
    project = models.ForeignKey(mdlProject, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    start_date= models.DateField()
    end_date= models.DateField()
    budget=models.DecimalField(max_digits=10, decimal_places=2)
    human_resources=models.IntegerField()
    STAGE_TYPES=[('A','Approved'),('O','Ongoing'), ('T','Terminated')] 
    stage=models.CharField(max_length=100, choices=STAGE_TYPES)

    def __str__(self):
        return self.project_phase
    

# Create project deliverable model for the project
class mdlPDeliverable(models.Model):
    deliverable_name = models.CharField(max_length=500)
    project_phase=models.ForeignKey(mdlPCharter, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    published_date = models.DateField()
    description = models.CharField(max_length=500)
    url = models.URLField()

    def __str__(self):
        return self.deliverable_name
from django.db import models

class School(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  
    name = models.CharField(max_length=100,null=True,blank=True)

class Class(models.Model):
    id = models.CharField(max_length=50, primary_key=True)    
    name = models.CharField(max_length=100,null=True,blank=True)

class AssessmentArea(models.Model):
    id = models.CharField(max_length=50, primary_key=True)    
    name = models.CharField(max_length=100,null=True,blank=True)

class Student(models.Model):
    id = models.CharField(max_length=50, primary_key=True)    
    fullname = models.CharField(max_length=100,null=True,blank=True)

class Answer(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  
    answer = models.CharField(max_length=500,null=True,blank=True)

class Award(models.Model):
    id = models.CharField(max_length=50, primary_key=True)    
    name = models.CharField(max_length=100,null=True,blank=True)

class Subject(models.Model):
    id = models.CharField(max_length=50, primary_key=True)    
    name = models.CharField(max_length=100,null=True,blank=True)
    score = models.CharField(max_length=100,null=True,blank=True)

class Summary(models.Model):
    school_id = models.CharField(max_length=100,null=True,blank=True)
    class_id = models.CharField(max_length=100,null=True,blank=True)
    assessment_area_id = models.CharField(max_length=100,null=True,blank=True)
    student_id = models.CharField(max_length=100,null=True,blank=True)
    subject_id = models.CharField(max_length=100,null=True,blank=True)
    award_id = models.CharField(max_length=100,null=True,blank=True)
    year_level_name = models.CharField(max_length=100,null=True,blank=True)
    sydney_participant = models.CharField(max_length=100,null=True,blank=True)
    sydney_percentile = models.CharField(max_length=100,null=True,blank=True)
    sydney_average_score = models.CharField(max_length=100,null=True,blank=True)
    student_score =models.CharField(max_length=100,null=True,blank=True)
    student_total_assessed = models.CharField(max_length=100,null=True,blank=True)
    student_area_assessed_score =models.CharField(max_length=100,null=True,blank=True)
    total_area_assessed_score = models.CharField(max_length=100,null=True,blank=True)
    participant = models.CharField(max_length=100,null=True,blank=True)
    correct_answer_percentage_per_class = models.CharField(max_length=100,null=True,blank=True)
    average_score = models.CharField(max_length=100,null=True,blank=True)
    school_percentile = models.CharField(max_length=100,null=True,blank=True)
    correct_answer = models.CharField(max_length=100,null=True,blank=True)
    category_id =models.CharField(max_length=100,null=True,blank=True)
    correct_answer_id =models.CharField(max_length=100,null=True,blank=True)

from django.db import models


class About(models.Model):
    about=models.TextField()
    cv_link=models.CharField(max_length=200)
    facebook_link=models.CharField(max_length=200)
    linkdin_link=models.CharField(max_length=200)
    github_link=models.CharField(max_length=200)

class Contact(models.Model):
    phone=models.CharField(max_length=11,primary_key=True)
    email=models.EmailField()
    address=models.TextField()


class Profile(models.Model):
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=35)
    about=models.OneToOneField(About, on_delete=models.CASCADE)
    contact=models.OneToOneField(Contact, on_delete=models.CASCADE)


    
class Skills(models.Model):
    skill=models.CharField(max_length=70)
    images=models.ImageField()
    about=models.ForeignKey(About,on_delete=models.CASCADE)

class Experiernces(models.Model):
    start_date=models.DateField()
    posision=models.CharField(max_length=200)
    company_name=models.CharField(max_length=70)
    company_logo=models.ImageField()
    address=models.TextField()
    description=models.TextField()
    about=models.ForeignKey(About,on_delete=models.CASCADE)

class Educations(models.Model):
    start_date=models.DateField()
    end_date=models.DateField()
    institution_name=models.CharField(max_length=70)
    institution_logo=models.ImageField()
    education=models.CharField(max_length=20)
    CGPA=models.FloatField()
    Out_of=models.FloatField()
    about=models.ForeignKey(About,on_delete=models.CASCADE)


class Testimonials(models.Model):
    Client_name=models.CharField(max_length=35)
    company=models.CharField(max_length=50,primary_key=True)
    speech=models.CharField(max_length=250)
    image=models.ImageField()
    video=models.FileField(upload_to='videos/',null=True)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)



class Services(models.Model):
    service_name=models.CharField(max_length=60,primary_key=True)
    description=models.TextField()
    icon=models.ImageField()
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

class Message(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField(primary_key=True)
    subject=models.CharField(max_length=22)
    message=models.TextField()
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

class Professions(models.Model):
    profession=models.CharField(max_length=60)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)


class Category(models.Model):
    name=models.CharField(max_length=50)



class Portfolio_projects(models.Model):
    title=models.CharField(max_length=60)
    thumbnail=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)

class Image(models.Model):
    image=models.ImageField()
    portfolio_projects=models.ForeignKey(Portfolio_projects,on_delete=models.CASCADE)




from django.contrib import admin
from .models import About,Educations,Skills,Experiernces,Profile,Testimonials,Services,Message,Professions,Category,Image,Portfolio_projects,Contact

class SkillsInline(admin.TabularInline):
    model = Skills

class ExperierncesInline(admin.TabularInline):
    model = Experiernces
   
class EducationsInline(admin.TabularInline):
    model = Educations


class TestimonialsInline(admin.TabularInline):
    model = Testimonials


class ServiceInline(admin.TabularInline):
    model = Services

class MessageInline(admin.TabularInline):
    model = Message

class ProfessionsInline(admin.TabularInline):
    model = Professions

class CategoryInline(admin.TabularInline):
    model = Category


class ImageInline(admin.TabularInline):
    model = Image

class ContactInline(admin.TabularInline):
    model = Contact


class Portfolio_projectsAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    class Meta:
        model=Portfolio_projects



class ProfileAdmin(admin.ModelAdmin):
    inlines = [TestimonialsInline,ServiceInline,MessageInline,ProfessionsInline]
    class Meta:
        model=Profile

class AboutAdmin(admin.ModelAdmin):
    inlines = [SkillsInline,ExperierncesInline,EducationsInline,]
    class Meta:
        model=About


admin.site.register(Profile,ProfileAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Skills)
admin.site.register(Contact)
admin.site.register(Experiernces)
admin.site.register(Educations)
admin.site.register(Testimonials)
admin.site.register(Services)
admin.site.register(Message)
admin.site.register(Professions)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Portfolio_projects,Portfolio_projectsAdmin)

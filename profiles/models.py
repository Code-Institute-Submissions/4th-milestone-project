from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from PIL import Image
import datetime
from multiselectfield import MultiSelectField
from plans.models import Plans
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

LANGUAGE_CHOICES = (
    ('English', 'English'),
    ('Mandarin Chinese',
        'Mandarin Chinese'),
    ('Hindi', 'Hindi'),
    ('Spanish', 'Spanish'),
    ('French', 'French'),
    ('Arabic', 'Arabic'),
    ('Bengali', 'Bengali'),
    ('Russian', 'Russian'),
    ('Portuguese', 'Portuguese'),
    ('Indonesian', 'Indonesian'),
    ('Other', 'Other'),
)

CODING_LANGUAGE_CHOICES = (
    ('JavaScript', 'JavaScript'),
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('PHP', 'PHP'),
    ('C#', 'C#'),
    ('C++', 'C++'),
    ('TypeScript', 'TypeScript'),
    ('Shell', 'Shell'),
    ('C', 'C'),
    ('Ruby', 'Ruby'),
    ('Other', 'Other'),
)

CODING_LANGUAGE_CHOICES = (
    ('JavaScript', 'JavaScript'),
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('PHP', 'PHP'),
    ('C#', 'C#'),
    ('C++', 'C++'),
    ('TypeScript', 'TypeScript'),
    ('Shell', 'Shell'),
    ('C', 'C'),
    ('Ruby', 'Ruby'),
    ('Other', 'Other'),
)

FRAMEWORK_CHOICES = (
    ('Ruby on Rails', 'Ruby on Rails'),
    ('Symfony', 'Symfony'),
    ('Angular JS', 'Angular JS'),
    ('React.js', 'React.js'),
    ('Cake PHP', 'Cake PHP'),
    ('Asp.net', 'Asp.net'),
    ('Node.js', 'Node.js'),
    ('Yii Framework', 'Yii Framework'),
    ('Meteor', 'Meteor'),
    ('Laravel', 'Laravel'),
    ('Ember', 'Ember'),
    ('Django', 'Django'),
    ('Express.js', 'Express.js'),
    ('Spring', 'Spring'),
    ('Flask', 'Flask'),
    ('Active Server Pages', 'Active Server Pages'),
    ('jQuery', 'jQuery'),
    ('CodeIgniter', 'CodeIgniter'),
    ('Drupal', 'Drupal'),
    ('Bootstrap', 'Bootstrap'),
)


class User(AbstractUser):
    phone_number = models.CharField(max_length=15)
    about_me = models.TextField(max_length=500)
    profile_image = models.ImageField(default='default.png',
                                      upload_to='profile-images/', blank=True, null=True)
    stripe_customer_id = models.CharField(max_length=50)
    # In case the object plan type is deleted, the user shouldn't be deleted
    plan_type = models.ForeignKey(
        'plans.Plans', on_delete=models.SET_NULL, null=True)
    is_job_seeker = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_job = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50)
    languages = MultiSelectField(
        choices=LANGUAGE_CHOICES, blank=True)
    coding_languages = MultiSelectField(
        choices=CODING_LANGUAGE_CHOICES, blank=True)
    frameworks = MultiSelectField(
        choices=FRAMEWORK_CHOICES, blank=True)


class WorkExperience(models.Model):
    experience_item = models.ForeignKey(
        JobSeekerProfile, on_delete=models.CASCADE, null=True, blank=True)
    job_title = models.CharField(max_length=50)
    location = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.job_title

    class Meta:
        ordering = ['-end_date']


class Education(models.Model):
    education_item = models.ForeignKey(
        JobSeekerProfile, on_delete=models.CASCADE, null=True, blank=True)
    study = models.CharField(max_length=50)
    location = models.CharField(max_length=50, null=True, blank=True)
    education_institute = models.CharField(
        max_length=50, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.study

    class Meta:
        ordering = ['-end_date']


class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    company_address1 = models.CharField(max_length=50)
    company_address2 = models.CharField(max_length=50, blank=True)
    company_city = models.CharField(max_length=50)
    company_ZIP = models.CharField(max_length=50, blank=True)
    company_state = models.CharField(max_length=50)
    company_country = models.CharField(max_length=50)


@ receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.is_job_seeker:
        JobSeekerProfile.objects.get_or_create(user=instance)
    else:
        RecruiterProfile.objects.get_or_create(user=instance)

    if instance.stripe_customer_id is None or instance.stripe_customer_id == '':
        new_customer_id = stripe.Customer.create(email=instance.email)
        job_seeker_plan = Plans.objects.create(plan_type='Jobseeker plan')
        instance.stripe_customer_id = new_customer_id['id']
        instance.plan_type = job_seeker_plan
        instance.save()


@ receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_job_seeker:
        instance.jobseekerprofile.save()

    else:
        instance.recruiterprofile.save()

    img = Image.open(instance.profile_image)

    if img.width > 300 or img.height > 300:
        img_dimensions = (300, 300)
        img.thumbnail(img_dimensions)
        img.save(instance.profile_image.path)

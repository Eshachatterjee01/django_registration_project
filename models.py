from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
'''class Client(models.Model):
        male=models.CharField(max_length=255, blank=True, null=True)
        female=models.CharField(max_length=255, blank=True, null=True)

        def __str__(self):
                return self.male,self.female'''
class Candidate(models.Model): 
                        ''''event = models.ForeignKey( "Eventdetails", models.DO_NOTHING, db_column="event", blank=True,  null=True 
                                                        ) 
                        job_position = models.ForeignKey( 
                                                "Jobrequisition", 
                                                models.DO_NOTHING, 
                                                db_column="job_position", 
                                                blank=True, 
                                                null=True, 
                                                ) '''
                        '''experience_level = models.ForeignKey( 
                                        "Experiencelevel", 
                                        models.DO_NOTHING, 
                                        db_column="experience_level", 
                                        blank=True, 
                                        null=True, 
                                        ) 
                        education_level = models.ForeignKey( 
                                        "Educationlevel", 
                                        models.DO_NOTHING, 
                                        db_column="education_level", 
                                        blank=True, 
                                        null=True, 
                                        ) 
                        education_qualification = models.ForeignKey( 
                                        "Educationqualification",
                                        models.DO_NOTHING, 
                                        db_column="education_qualification", 
                                        blank=True, 
                                        null=True, 
                                        ) 
                        education_specialization = models.ForeignKey( 
                                        "Educationspecialization", 
                                        models.DO_NOTHING, 
                                        db_column="education_specialization", 
                                        blank=True, 
                                        null=True, 
                                        ) '''
                        # This field type is a guess. 
                        '''source = models.ForeignKey( 
                                "Source", 
                                models.DO_NOTHING, 
                                db_column="source", 
                                blank=True, 
                                null=True, 
                                related_name="source_for_candidate_details", 
                                ) 
                        source_type = models.ForeignKey( 
                                "Sourcetype", models.DO_NOTHING, db_column="source_type", blank=True,  null=True 
                                ) '''
                        '''reason_for_change = models.ForeignKey( 
                                        "Reasonforchange", 
                                        models.DO_NOTHING, 
                                        db_column="reason_for_change",
                                        blank=True, 
                                        null=True, 
                                                )   '''  
                        # This field type is a guess. 
                        '''education_institution = models.ForeignKey( 
                                        "Source", 
                                        models.DO_NOTHING, 
                                        db_column="education_institution", 
                                        blank=True, 
                                        null=True, 
                                        ) '''
                        '''persona = models.ForeignKey( 
                                                        "Persona", 
                                                        models.DO_NOTHING, 
                                                        db_column="persona", 
                                                        blank=True, 
                                                        null=True, 
                                                        default=1, 
                                                        )'''
                        '''screening_mode = models.ForeignKey( 
                                                "Screeningmode", 
                                                models.DO_NOTHING, 
                                                db_column="screening_mode", 
                                                blank=True, 
                                                null=True, 
                                                ) '''
                        #gender = models.ForeignKey(Client, on_delete=models.CASCADE )
                        ''' marital_status = models.ForeignKey( 
                                                "Maritalstatus", 
                                                models.DO_NOTHING, 
                                                db_column="marital_status", 
                                                blank=True, 
                                                null=True, 
                                                ) '''
                        '''referred_by = models.ForeignKey( 
                                                "Employeedirectory", 
                                                models.DO_NOTHING, 
                                                db_column="referred_by", 
                                                blank=True, 
                                                null=True, 
                                                ) '''
                        #recruiter_alert = models.CharField(max_length=50, blank=True, null=True)  
                        first_name = models.CharField(max_length=255, blank=True, null=True)  
                        last_name = models.CharField(max_length=255, blank=True, null=True)  
                        email = models.CharField(max_length=50, blank=True, null=True) 
                        
                        role = models.CharField(max_length=15, blank=True, null=True) 
                        
                        #dob = models.DateField(blank=True,null=True) 
                        
                        #contact_no_primary = models.PhoneNumberField(_(""))(max_digits=10, decimal_places=0, blank=True, null=True  ) 
        
                        #contact_no_alternate = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True  ) 
        
                        
                        referred_by_other = models.CharField(max_length=250, blank=True, null=True)  
                        address_line = models.CharField(max_length=255, blank=True, null=True)  
                        #city = models.ForeignKey("City", models.DO_NOTHING, db_column="city", blank=True, null=True  ) 
                                        
                        pincode = models.IntegerField(max_length=100, blank=True,  null=True) 
                        
                        education_specialization_other = models.TextField( 
                                        blank=True, null=True 
                                        ) 
                        
                        education_institution_other = models.TextField( 
                                        blank=True, null=True 
                                        )                  
                        
                        years_of_experience = models.IntegerField( 
                                        max_length=100, blank=True, null=True  ) 
                        current_employer = models.CharField(max_length=100, blank=True, null=True)  
                        current_designation = models.TextField( 
                                        blank=True, null=True 
                                )
                        # This field type is a guess. 
                        current_monthly_salary = models.IntegerField( 
                                blank=True, null=True 
                                ) 
                        expected_monthly_salary = models.IntegerField( 
                                blank=True, null=True 
                                ) 
                        notice_period = models.CharField(max_length=50, blank=True, null=True)  
                                
                        photo_path = models.TextField(blank=True, null=True) # This field type is a  guess. 
                        resume_path = models.TextField(blank=True, null=True) # This field type is a  guess. 
                        login_time = models.DateTimeField(auto_now_add=True) 
                        logout_time = models.DateTimeField(auto_now_add=True) 
                        ip_address = models.CharField(max_length=15, blank=True, null=True)  
                        geo_location = models.CharField(max_length=50, blank=True, null=True)  
                        created_date = models.DateTimeField(auto_now_add=True)  
                        created_by = models.CharField(max_length=15, blank=True, null=True) 
                        modified_date = models.DateTimeField(auto_now=True)  
                        modified_by = models.CharField(max_length=15, blank=True, null=True) 
        
                        status = models.IntegerField(default=1) 
                        def  __str__(self):
                                return "%s %s"%(self.first_name,self.last_name)

class Meta: 
                managed = False 
                db_table = "CandidateDirectory" 
                db_table = "CandidateDirectory" 
                constraints = [ 
                                models.UniqueConstraint(
                                        fields=['first_name', 'last_name'],  name='full_name') 
                                        ]
'''class Contact(models.Model):
    phone = PhoneNumberField()
    #phoneNumber = PhoneNumberField(unique=True, null=False, blank=False)
                        #secondPhoneNumber = PhoneNumberField(null=True, blank=True)'''

'''class User(AbstractUser):
        phone_number=PhoneNumberField()'''

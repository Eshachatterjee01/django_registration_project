from django.shortcuts import render,HttpResponse
from .models import Candidate
from datetime import datetime


# Create your views here.
def index(request):
    return render(request,"index.html")

def add_emp(request):
    if request.method == 'POST':
        print("yes")
        
        firstname=request.POST["emp_first_name"]
        lastname=request.POST["emp_last_name"]
        email=request.POST["emp_email"]
        role=request.POST["emp_role"]
        #dobb=request.POST["emp_dob"]
        reffered_name=request.POST["emp_reffered_name"]
        address=request.POST["emp_address"]
        pincode=request.POST["emp_pincode"]
        education_spez=request.POST["emp_education_specialization"]
        edu_ins=request.POST["emp_education_institution"]
        yoe=request.POST["emp_yoe"]
        current_sal=request.POST["emp_current_sal"]
        expected_sal=request.POST["expectade_sal"]
        notice_period=request.POST["emp_notice_period"]
        photo_path=request.POST["emp_photo_path"]
        resume_path=request.POST["emp_resume_path"]
        ip_address=request.POST["emp_ip_address"]
        geo_loc=request.POST["emp_geo_location"]
        created_by=request.POST["emp_created_by"]
        modified_by=request.POST["emp_modified_by"]
        status=request.POST["emp_status"]
        #gender=int(request.POST["emp_gender"])

        new_emp=Candidate(first_name=firstname,last_name=lastname, email=email, role=role, referred_by_other=reffered_name, address_line=address,pincode=pincode,education_specialization_other=education_spez,education_institution_other=edu_ins,
                         years_of_experience= yoe, current_monthly_salary=current_sal,expected_monthly_salary=expected_sal,notice_period=notice_period,photo_path=photo_path,
                         resume_path=resume_path,ip_address=ip_address,
                        geo_location=geo_loc,created_by= created_by,modified_by=modified_by,status=status)
        new_emp.save()

        
        return HttpResponse("Employee added successfully")


    elif request.method=="GET":
        return render(request,"add_emp.html")
    else:
        return HttpResponse("an exception occured")
    


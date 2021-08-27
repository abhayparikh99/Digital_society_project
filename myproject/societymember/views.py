from django.shortcuts import render
from chairman.models import * 
from . utils import *
from random import *
# Create your views here.


def m_index(request):
    if "m_email" in request.session:
        uid = User.objects.get(email = request.session['m_email'])
        mid = Member.objects.get(user_id = uid)
        eid = Event.objects.all()
        complaintData = Complaint.objects.all()
        mem_id = Member.objects.all()
        nid = Notice.objects.all()
        imageData = Image.objects.all()
        suggestData = Suggestions.objects.all()
        notice_count = len(nid)
        mem_count = len(mem_id)
        event_count = len(eid)
        com_count = len(complaintData)
        context = {
                    'uid':uid,
                    'mid':mid,
                    'eid':eid,
                    'complaintData':complaintData,
                    'mem_id':mem_id,
                    'mem_count':mem_count,
                    'event_count':event_count,
                    'notice_count':notice_count,
                    'nid':nid,
                    'com_count':com_count,
                    'imageData':imageData,
                    'suggestData':suggestData,
                }
        return render(request,"societymember/m_index.html",{'context':context})
    else:
        return render(request,"chairman/c_login.html")

def loginpage(request):
    return render(request,"chairman/c_login.html")

def m_logout(request):
    if "m_email" in request.session:
        del request.session['m_email']
        return render(request,"chairman/c_login.html")
    else:
        return render(request,"chairman/c_login.html")

def sm_profile(request):
    uid = User.objects.get(email = request.session['m_email'])
    mid = Member.objects.get(user_id = uid)
    context = {
                    'uid':uid,
                    'mid':mid,
                }
    return render(request,"societymember/sm_profile.html",{'context':context})

def m_profile_update(request):
    uid = User.objects.get(email = request.session['m_email'])
    mid = Member.objects.get(user_id = uid)
    if request.method == 'POST':
        if not request.POST['newpassword']:
            password = request.POST['password']
            uid.password = password
            uid.save()
        else:
            newpassword = request.POST['newpassword']
            uid.password = newpassword
            uid.save()
        fname = request.POST['fname']
        lname = request.POST['lname']
        jobprofession = request.POST['jobprofession']
        houseno = request.POST['houseno']
        contact_no = request.POST['contact_no']
        job_address = request.POST['job_address']
        address = request.POST['address']
        vehicle_type = request.POST['vehicle_type']
        vehicle_no = request.POST['vehicle_no']
        blood_group = request.POST['blood_group']
        mid.fname = fname
        mid.lname = lname
        if "profilepic" in request.FILES:
            profilepic = request.FILES['profilepic']
            mid.profile_pic = profilepic
            mid.save()
    mdid = MemberDetails.objects.get(homeno = houseno)
    mdid.job_profession = jobprofession
    mdid.contact_no = contact_no
    mdid.job_address = job_address
    mdid.address = address
    mdid.vehicle_type = vehicle_type
    mdid.vehicle_no = vehicle_no
    mdid.blood_group = blood_group
    
    uid.save()
    mid.save()
    mdid.save()
    context = {
                    'uid':uid,
                    'mid':mid,
                    'mdid':mdid,
                }
    return render(request,"societymember/sm_profile.html",{'context':context})

def m_view_notice(request):
    uid = User.objects.get(email = request.session['m_email'])
    mid = Member.objects.get(user_id = uid)
    noticedata = Notice.objects.all()
    context = {
                    'uid':uid,
                    'mid':mid,
                    'noticedata':noticedata,
                }
    return render(request,"societymember/m-notice-list.html",{'context':context})

def m_view_event(request):
    uid = User.objects.get(email = request.session['m_email'])
    mid = Member.objects.get(user_id = uid)
    eventData = Event.objects.all()
    context = {
                    'uid':uid,
                    'mid':mid,
                    'eventData':eventData,
                }
    return render(request,"societymember/m-event-list.html",{'context':context})

def m_view_member(request):
    uid = User.objects.get(email = request.session['m_email'])
    mid = Member.objects.get(user_id = uid)
    mdid = Member.objects.exclude(user_id = uid)
    context = {
                    'uid':uid,
                    'mdid':mdid,
                    'mid':mid,
                }
    return render(request,"societymember/m_view_members.html",{'context':context})

def m_add_complaint_page(request):
    if "m_email" in request.session:
        uid = User.objects.get(email = request.session['m_email'])
        mid = Member.objects.get(user_id = uid)
        context = {
                    'uid':uid,
                    'mid':mid,
                }
        return render(request,"societymember/m-add-complaint.html",{'context':context})

def m_add_complaint(request):
    try:
        fname = request.POST['fname']
        lname = request.POST['lname']
        complaint_subject = request.POST['complaint_subject']
        complaint_desc = request.POST['complaint_desc']
        uid = User.objects.get(email = request.session['m_email'])
        mid = Member.objects.get(user_id = uid)
        m_id = Member.objects.get(fname = fname)
        coid = Complaint.objects.create(user_id = uid,m_id = m_id, complaint_subject = complaint_subject, complaint_desc= complaint_desc)
        uid = User.objects.get(email = request.session['m_email'])
        mid = Member.objects.get(user_id = uid)
        complaintData = Complaint.objects.all()
        context = {
                        'uid':uid,
                        'mid':mid,
                        'complaintData':complaintData,
                    }
        return render(request,"societymember/m_complaint_list.html",{'context':context})
    except:
        e_msg = "Something went wrong"
        context = {
                    'uid':uid,
                    'mid':mid,
                }
        return render(request,"societymember/m-add-complaint.html",{'context':context})

def m_view_complaint(request):
    uid = User.objects.get(email = request.session['m_email'])
    mid = Member.objects.get(user_id = uid)
    complaintData = Complaint.objects.all()
    context = {
                    'uid':uid,
                    'mid':mid,
                    'complaintData':complaintData,
                }
    return render(request,"societymember/m_complaint_list.html",{'context':context})

def m_del_complaint(request,pk):
    if "m_email" in request.session:
        uid = User.objects.get(email = request.session['m_email'])
        mid = Member.objects.get(user_id = uid)
        complaint_id = Complaint.objects.get(id=pk)
        complaint_id.delete()
        complaintData = Complaint.objects.all()
        context = {
                        'uid':uid,
                        'mid':mid,
                        'complaintData':complaintData,
                    }
        return render(request,"societymember/m_complaint_list.html",{'context':context})

def add_suggestion_page(request):
    if "m_email" in request.session:
        uid = User.objects.get(email = request.session['m_email'])
        mid = Member.objects.get(user_id = uid)
        context = {
                    'uid':uid,
                    'mid':mid,
                }
        return render(request,"societymember/m-add-suggestion.html",{'context':context})

def add_suggestion(request):
    uid = User.objects.get(email = request.session['m_email'])
    mid = Member.objects.get(user_id = uid)
    suggested_by = request.POST['suggested_by']
    suggestion_title = request.POST['suggestion_title']
    suggestion_desc = request.POST['suggestion_desc']
    sid = Suggestions.objects.create(suggested_by = suggested_by, suggestion_title = suggestion_title, suggestion_desc = suggestion_desc)
    suggestData = Suggestions.objects.all()
    context = {
                    'uid':uid,
                    'mid':mid,
                    'suggestData':suggestData,
                }
    return render(request,"societymember/suggestion-list.html",{'context':context})

def view_suggestions(request):
    uid = User.objects.get(email = request.session['m_email'])
    mid = Member.objects.get(user_id = uid)
    suggestData = Suggestions.objects.all()
    context = {
                    'uid':uid,
                    'mid':mid,
                    'suggestData':suggestData,
                }
    return render(request,"societymember/suggestion-list.html",{'context':context})

def del_suggestion(request,pk):
    if "m_email" in request.session:
        uid = User.objects.get(email = request.session['m_email'])
        mid = Member.objects.get(user_id = uid)
        sid = Suggestions.objects.get(id=pk)
        sid.delete()
        suggestData = Suggestions.objects.all()
        context = {
                        'uid':uid,
                        'mid':mid,
                        'suggestData':suggestData,
                    }
        return render(request,"societymember/suggestion-list.html",{'context':context})

def m_member_profile(request,pk):
    uid = User.objects.get(email = request.session['m_email'])
    mid = Member.objects.get(user_id = uid)
    mdid = Member.objects.get(id = pk)
    context = {
                    'uid':uid,
                    'mdid':mdid,
                    'mid':mid,
                }
    return render(request,"societymember/smm_profile.html",{'context':context})

def m_view_images(request):
    uid = User.objects.get(email = request.session['m_email'])
    mid = Member.objects.get(user_id = uid)
    imageData = Image.objects.all()
    context = {
                    'uid':uid,
                    'mid':mid,
                    'imageData':imageData
                }
    return render(request,"societymember/m_images.html",{'context':context})

def m_view_videos(request):
    uid = User.objects.get(email = request.session['m_email'])
    mid = Member.objects.get(user_id = uid)
    videoData = Video.objects.all()
    context = {
                    'uid':uid,
                    'mid':mid,
                    'videoData':videoData
                }
    return render(request,"societymember/m_videos.html",{'context':context})

def m_view_maintenance(request):
    uid = User.objects.get(email = request.session['m_email'])
    mid = Member.objects.get(user_id = uid)
    maintenanceData = Maintenance.objects.all()
    context = {
        'uid':uid,
        'mid':mid,
        'maintenanceData':maintenanceData,
    }
    return render(request,"societymember/m_maintenance_list.html",{'context':context})

def m_pay_maintenance(request):
    uid = User.objects.get(email = request.session['m_email'])
    member_id= Member.objects.get(user_id = uid)
    mid = Maintenance.objects.filter(member_id = member_id, status = "Pending")
    mid_paid = Maintenance.objects.filter(member_id = member_id, status = "Paid")
    context = {
        'uid':uid,
        'member_id':member_id,
        'mid':mid,
        'mid_paid':mid_paid,
    }
    return render(request,"societymember/m_pay_maintenance.html",{'context':context})

def m_view_visitors(request):
    if "m_email" in request.session:
        uid = User.objects.get(email = request.session['m_email'])
        mid = Member.objects.get(user_id = uid)
        visitorsData = Visitor.objects.all()
        context = {
            'uid':uid,
            'mid':mid,
            'visitorsData':visitorsData,
        }
        return render(request,"societymember/m_visitors_list.html",{'context':context})

def m_watchman_list(request):
    if "m_email" in request.session:
        uid = User.objects.get(email = request.session['m_email'])
        mid = Member.objects.get(user_id = uid)
        wid = Watchman.objects.filter(status = "Approved")
        wid_pending = Watchman.objects.filter(status = "Pending")
        context = {
                    'uid':uid,
                    'mid':mid,
                    'wid':wid,
                    'wid_pending':wid_pending,
                }
        return render(request,"societymember/m_watchman_list.html",{'context':context})
        

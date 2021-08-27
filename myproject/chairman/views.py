from django.shortcuts import render,HttpResponseRedirect,reverse
from . models import *
from . utils import *
from random import *
from django.views.decorators.csrf import csrf_exempt
from .paytm import generate_checksum, verify_checksum
from django.conf import settings
# Create your views here.
def index(request):
    if "c_email" in request.session:
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
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
                    'cid':cid,
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
        return render(request,"chairman/index.html",{'context':context})
    elif "m_email" in request.session:
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
    

def login_page(request):
    return render(request,"chairman/c_login.html")

def login_evalute(request):
    try:
        email = request.POST['email']     
        password = request.POST['password']
        role = request.POST['role']
        if role=="chairman":
            uid = User.objects.get(email = email)
            print("---------->uid",uid)
            print("---------->uid.password",uid.password)
            if uid.password == password:
                print("Welcome")
                cid = Chairman.objects.get(user_id = uid)
                request.session['c_email'] = uid.email
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
                            'cid':cid,
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
                return render(request,"chairman/index.html",{'context':context})
            else:
                e_msg = "INVALID PASSWORD!!!!"
                return render(request,"chairman/c_login.html",{'e_msg':e_msg})
        elif role == "member":
            uid = User.objects.get(email = email)
            if uid.password == password:
                print("Welcome")
                mid = Member.objects.get(user_id = uid)
                request.session['m_email'] = uid.email
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
                e_msg = "INVALID PASSWORD!!!!"
                return render(request,"chairman/c_login.html",{'e_msg':e_msg})
        elif role == "watchman":
            wid = Watchman.objects.get(email = email)
            if wid.password == password:
                request.session['w_email'] = wid.email
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
                        'wid':wid,
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
                return render(request,"watchman/w_index.html",{'context':context})
            else:
                e_msg = "INVALID PASSWORD!!!!"
                return render(request,"chairman/c_login.html",{'e_msg':e_msg})
        else:
            e_msg = "PLEASE SELECT VALID ROLE!!!!"
            return render(request,"chairman/c_login.html",{'e_msg':e_msg})
    except:
        e_msg = "EMAIL DOES NOT EXIST!!!!"
        return render(request,"chairman/c_login.html",{'e_msg':e_msg})

def logout(request):
    if "c_email" in request.session:
        del request.session['c_email']
        return render(request,"chairman/c_login.html")
    else:
        return render(request,"chairman/c_login.html")

def forgot_password_page(request):
    return render(request,"chairman/forgot_password.html")

def send_otp(request):
    try:
        email = request.POST['email']
        generate_otp = randint(1111,9999)
        uid = User.objects.get(email = email)
        if uid:
            uid.otp = generate_otp
            uid.save()              # update otp
            if uid.role == "chairman":
                cid = Chairman.objects.get(user_id = uid)
                sendmail("Forgot Password","main_template",email,{'otp':generate_otp,'cid':cid})
                return render(request,"chairman/reset_password.html",{'email':email})
            elif uid.role == "member":
                mid = Member.objects.get(user_id = uid)
                sendmail("Forgot Password","main_template",email,{'otp':generate_otp,'mid':mid})
                return render(request,"chairman/reset_password.html",{'email':email})
        else:
            e_msg = "EMAIL DOES NOT EXIST!!!!"
            return render(request,"chairman/c_login.html",{'e_msg':e_msg})
    except:
        e_msg = "EMAIL DOES NOT EXIST!!!!"
        return render(request,"chairman/c_login.html",{'e_msg':e_msg})

def reset_password(request):
    if request.POST:
        email = request.POST['email']
        otp = request.POST['otp']
        newpassword = request.POST['newpassword']
        repassword = request.POST['repassword']
        uid = User.objects.get(email = email)
        if uid:
            if str(uid.otp) == otp and newpassword == repassword:
                uid.password = newpassword
                uid.save()
                s_msg = "SUCCESSFULLY RESET PASSWORD!!!!"
                return render(request,"chairman/c_login.html",{'s_msg':s_msg})
            else:
                e_msg = "INVALID OTP OR PASSWORD"
                return render(request,"chairman/forgot_password.html",{'e_msg':e_msg})
        else:
            e_msg = "EMAIL DOES NOT EXIST!!!!"
            return render(request,"chairman/forgot_password.html",{'e_msg':e_msg})
    elif request.POST:
        email = request.POST['email']
        otp = request.POST['otp']
        newpassword = request.POST['newpassword']
        repassword = request.POST['repassword']
        mid = Member.objects.get(email = email)
        if mid:
            if str(mid.otp) == otp and newpassword == repassword:
                mid.password = newpassword
                mid.save()
                s_msg = "SUCCESSFULLY RESET PASSWORD!!!!"
                return render(request,"chairman/c_login.html",{'s_msg':s_msg})
            else:
                e_msg = "INVALID OTP OR PASSWORD"
                return render(request,"chairman/forgot_password.html",{'e_msg':e_msg})
        else:
            e_msg = "EMAIL DOES NOT EXIST!!!!"
            return render(request,"chairman/forgot_password.html",{'e_msg':e_msg})
    else:
        e_msg = "EMAIL DOES NOT EXIST!!!!"
        return render(request,"chairman/forgot_password.html",{'e_msg':e_msg})

def add_notice_page(request):
    if "c_email" in request.session:
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
        context = {
                    'uid':uid,
                    'cid':cid,
                }
        return render(request,"chairman/add-notice.html",{'context':context})

def add_notice(request):
    try:
        title = request.POST['title']
        desc = request.POST['desc']
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
        nid = Notice.objects.create(user_id = uid,title=title,description=desc)
        noticedata = Notice.objects.all()
        context = {
                        'uid':uid,
                        'cid':cid,
                        'noticedata':noticedata,
                    }
        return render(request,"chairman/notice-list.html",{'context':context})
    except:
        e_msg = "Something went wrong"
        context = {
                    'uid':uid,
                    'cid':cid,
                    'e_msg':e_msg,
                }
        return render(request,"chairman/add-notice.html",{'context':context})


def view_notice(request):
    uid = User.objects.get(email = request.session['c_email'])
    cid = Chairman.objects.get(user_id = uid)
    noticedata = Notice.objects.all()
    context = {
                    'uid':uid,
                    'cid':cid,
                    'noticedata':noticedata,
                }
    return render(request,"chairman/notice-list.html",{'context':context})

def del_notice(request,pk):
    if "c_email" in request.session:
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
        nid = Notice.objects.get(id=pk)
        nid.delete()
        noticedata = Notice.objects.all()
        context = {
                        'uid':uid,
                        'cid':cid,
                        'noticedata':noticedata,
                    }
        return render(request,"chairman/notice-list.html",{'context':context})

def profile(request):
    uid = User.objects.get(email = request.session['c_email'])
    cid = Chairman.objects.get(user_id = uid)
    context = {
                    'uid':uid,
                    'cid':cid,
                }
    return render(request,"chairman/profile.html",{'context':context})

def profile_update(request):
    uid = User.objects.get(email = request.session['c_email'])
    cid = Chairman.objects.get(user_id = uid)
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
        if "profilepic" in request.FILES:
            profilepic = request.FILES['profilepic']
            cid.profile_pic = profilepic
        cid.fname = fname
        cid.lname = lname
    mid = MemberDetails.objects.get(homeno = houseno)
    mid.job_profession = jobprofession
    mid.contact_no = contact_no
    mid.job_address = job_address
    mid.address = address
    mid.vehicle_type = vehicle_type
    mid.vehicle_no = vehicle_no
    mid.blood_group = blood_group
    uid.save()
    cid.save()
    mid.save()
    context = {
                    'uid':uid,
                    'cid':cid,
                    'mid':mid,
                }
    return render(request,"chairman/profile.html",{'context':context})

def view_member(request):
    uid = User.objects.get(email = request.session['c_email'])
    cid = Chairman.objects.get(user_id = uid)
    mid = Member.objects.all()
    context = {
                    'uid':uid,
                    'cid':cid,
                    'mid':mid,
                }
    return render(request,"chairman/view_members.html",{'context':context})

def member_profile(request,pk):
    uid = User.objects.get(email = request.session['c_email'])
    mid = Member.objects.get(id = pk)
    cid = Chairman.objects.get(user_id = uid)
    context = {
                    'uid':uid,
                    'cid':cid,
                    'mid':mid,
                }
    return render(request,"chairman/m_profile.html",{'context':context})

def add_event_page(request):
    if "c_email" in request.session:
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
        context = {
                    'uid':uid,
                    'cid':cid,
                }
    return render(request,"chairman/add-event.html",{'context':context})

def add_event(request):
    if "c_email" in request.session:
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
        event_title = request.POST['event_title']
        event_desc = request.POST['event_desc']
        event_date = request.POST['event_date']
        event_time = request.POST['event_time']
        eid = Event.objects.create(
            event_title = event_title,
            event_desc = event_desc,
            event_date = event_date,
            event_time = event_time,
        )
        if "event_pic" in request.FILES:
            event_pic = request.FILES['event_pic']
            eid.event_pic = event_pic
            eid.save()
        eid.save()
        eventData = Event.objects.all
        context = {
                    'uid':uid,
                    'cid':cid,
                    'eventData':eventData,
                }
        return render(request,"chairman/event-list.html",{'context':context})
    else:
        return render(request,"chairman/add-event.html")

def view_event(request):
    uid = User.objects.get(email = request.session['c_email'])
    cid = Chairman.objects.get(user_id = uid)
    eventData = Event.objects.all()
    context = {
                    'uid':uid,
                    'cid':cid,
                    'eventData':eventData,
                }
    return render(request,"chairman/event-list.html",{'context':context})

def del_event(request,pk):
    if "c_email" in request.session:
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
        eid = Event.objects.get(id=pk)
        eid.delete()
        eventData = Event.objects.all()
        context = {
                        'uid':uid,
                        'cid':cid,
                        'eventData':eventData,
                    }
        return render(request,"chairman/event-list.html",{'context':context})

def add_member_page(request):
    uid = User.objects.get(email = request.session['c_email'])
    cid = Chairman.objects.get(user_id = uid)
    context = {
                    'uid':uid,
                    'cid':cid,
                }
    return render(request,"chairman/add_member.html",{'context':context})

def add_member(request):
    if "c_email" in request.session:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        houseno = request.POST['houseno']
        address = request.POST['address']
        contact_no = request.POST['contact_no']
        family_member_details = request.POST['family_member_details']
        role = request.POST['role']
        password = str(randint(11,99))+fname[:2]+str(randint(11,99))
        userdate = User.objects.create(
            email = email,password = password,role = role
        )
        uid = User.objects.get(email = email)
        if "profilepic" in request.FILES:
            profilepic = request.FILES['profilepic']
            uid.profile_pic = profilepic
            uid.save()
        uid.save()
        memberDetails = MemberDetails.objects.create(
            homeno = houseno ,address = address,family_member_details = family_member_details,contact_no = contact_no
        )
        mdid = MemberDetails.objects.get(homeno = houseno)

        member = Member.objects.create(
            user_id = uid, fname = fname, lname = lname,profile_pic = profilepic, m_id = mdid
        )
        sendmail("Member Registration","member-confirmation",email,{'password':password,'member':member})
        return HttpResponseRedirect(reverse("view-member"))


def view_complaint(request):
    uid = User.objects.get(email = request.session['c_email'])
    cid = Chairman.objects.get(user_id = uid)
    complaintData = Complaint.objects.all()
    context = {
                    'uid':uid,
                    'cid':cid,
                    'complaintData':complaintData,
                }
    return render(request,"chairman/complaint_list.html",{'context':context})

def del_complaint(request,pk):
    if "c_email" in request.session:
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
        complaint_id = Complaint.objects.get(id=pk)
        complaint_id.delete()
        complaintData = Complaint.objects.all()
        context = {
                        'uid':uid,
                        'cid':cid,
                        'complaintData':complaintData,
                    }
        return render(request,"chairman/complaint_list.html",{'context':context})

def c_view_suggestions(request):
    uid = User.objects.get(email = request.session['c_email'])
    cid = Chairman.objects.get(user_id = uid)
    suggestData = Suggestions.objects.all()
    context = {
                    'uid':uid,
                    'cid':cid,
                    'suggestData':suggestData,
                }
    return render(request,"chairman/c-suggestion-list.html",{'context':context})

def upload_page(request):
    if "c_email" in request.session:
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
        context = {
                    'uid':uid,
                    'cid':cid,
                }
        return render(request,"chairman/uploadpage.html",{'context':context})

def add_image(request):
    if "c_email" in request.session:
        if request.POST:
            name = request.POST['name']
            imagefile = request.FILES['imagefile']
            aid = Image.objects.create(name = name, imagefile = imagefile)
            imageData = Image.objects.all()
            uid = User.objects.get(email = request.session['c_email'])
            cid = Chairman.objects.get(user_id = uid)
            context = {
                    'uid':uid,
                    'cid':cid,
                    'imageData':imageData
                }
            return render(request,"chairman/images.html",{'context':context})
        else:
            return HttpResponseRedirect(reverse("upload_page"))

def add_video(request):
    if "c_email" in request.session:
        if request.POST:
            name = request.POST['name']
            videofile = request.FILES['videofile']
            aid = Video.objects.create(name = name, videofile = videofile)
            videoData = Video.objects.all()
            uid = User.objects.get(email = request.session['c_email'])
            cid = Chairman.objects.get(user_id = uid)
            context = {
                    'uid':uid,
                    'cid':cid,
                    'videoData':videoData
                }
            return render(request,"chairman/videos.html",{'context':context})
        else:
            return HttpResponseRedirect(reverse("upload_page"))

def view_images(request):
    uid = User.objects.get(email = request.session['c_email'])
    cid = Chairman.objects.get(user_id = uid)
    imageData = Image.objects.all()
    context = {
                    'uid':uid,
                    'cid':cid,
                    'imageData':imageData
                }
    return render(request,"chairman/images.html",{'context':context})

def view_videos(request):
    uid = User.objects.get(email = request.session['c_email'])
    cid = Chairman.objects.get(user_id = uid)
    videoData = Video.objects.all()
    context = {
                    'uid':uid,
                    'cid':cid,
                    'videoData':videoData
                }
    return render(request,"chairman/videos.html",{'context':context})

def del_image(request,pk):
    if "c_email" in request.session:
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
        image_id = Image.objects.get(id = pk)
        image_id.delete()
        imageData = Image.objects.all()
        context = {
                        'uid':uid,
                        'cid':cid,
                        'imageData':imageData,
                    }
        return render(request,"chairman/images.html",{'context':context})

def del_video(request,pk):
    if "c_email" in request.session:
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
        video_id = Video.objects.get(id = pk)
        video_id.delete()
        videoData = Video.objects.all()
        context = {
                        'uid':uid,
                        'cid':cid,
                        'videoData':videoData
                    }
        return render(request,"chairman/videos.html",{'context':context})

def add_maintenance_page(request):
    if "c_email" in request.session:
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
        context = {
                    'uid':uid,
                    'cid':cid,
                }
        return render(request,"chairman/add_maintenance.html",{'context':context})



def w_registration_page(request):
    return render(request,"watchman/watchman_registration.html")    

def send_approval(request):
    if request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        address = request.POST['address']
        age = request.POST['age']
        contact_no = request.POST['contact_no']
        family_contact_no = request.POST['family_contact_no']
        profile_picture = request.FILES['profile_picture']
        watchman_id = Watchman.objects.create(
            fname=fname, lname=lname, email=email, address=address, age=age, contact_no=contact_no, family_contact_no=family_contact_no, profile_picture=profile_picture,
        )
        wid = Watchman.objects.all()
        sendmail("Watchman Request","watchman_request",email,{'watchman_id':watchman_id})
        s_msg = "REQUEST SENT TO CHAIRMAN FOR APPROVAL"        
        return render(request,"chairman/c_login.html",{'wid':wid,'s_msg':s_msg})

def watchman_list(request):
    if "c_email" in request.session:
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
        wid = Watchman.objects.filter(status = "Approved")
        wid_pending = Watchman.objects.filter(status = "Pending")
        context = {
                    'uid':uid,
                    'cid':cid,
                    'wid':wid,
                    'wid_pending':wid_pending,
                }
        return render(request,"chairman/watchman_list.html",{'context':context})

def watchman_status(request,pk,status):
    if "c_email" in request.session:
        uid = User.objects.get(email = request.session['c_email'])
        wid = Watchman.objects.get(id=pk)
        cid = Chairman.objects.get(user_id=uid)

        wid.status = status
        wid.save()
        if wid.status == "Approved":
            wid.role = "watchman"
            password = randint(111111,999999)                          #another way of random password: str(randint(11,99))+wid.fname[:2]+str(randint(11,99))
            wid.password = password
            wid.save()
            sendmail("Confirmation Mail","watchman_approval",wid.email,{"wid":wid,"status":status,'password':password})
        else:
            wid.status == "Rejected"
            wid.save()
        wid = Watchman.objects.filter(status = "Approved")
        wid_pending = Watchman.objects.filter(status = "Pending")
        context = {
                    'uid':uid,
                    'cid':cid,
                    'wid':wid,
                    'wid_pending':wid_pending,
                }
        return render(request,"chairman/watchman_list.html",{'context':context})
    else:
        return render(request,"chairman/c_login.html")
    
def c_view_visitors(request):
    if "c_email" in request.session:
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
        visitorsData = Visitor.objects.all()
        context={
            "uid":uid,
            "cid":cid,
            'visitorsData':visitorsData,
        }
        return render(request,"chairman/c_visitors_list.html",{"context":context})
    else:
        e_msg = "EMAIL DOES NOT EXIST!!!!"
        return render(request,"chairman/c_login.html",{'e_msg':e_msg})
        

def add_maintenance(request):
    if request.POST:
        title = request.POST['title']
        amount = request.POST['amount']
        due_date = request.POST['due_date']
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
        # add maintenance of chairman
        Maintenance.objects.create(
            user_id=uid, cid=cid, title=title, amount=amount, due_date=due_date
        )
        allmembers = Member.objects.all()
        # add maintenance to members
        for i in allmembers:
            mid = Member.objects.get(id = i.id)
            Maintenance.objects.create(
                user_id=uid, member_id=mid, title=title, amount=amount, due_date=due_date
            )
        maintenanceData = Maintenance.objects.all()
        context = {
            'uid':uid,
            'cid':cid,
            'maintenanceData':maintenanceData,
        }
        return render(request,"chairman/maintenance_list.html",{'context':context})
    else:
        uid = User.objects.get(email = request.session['c_email'])
        cid = Chairman.objects.get(user_id = uid)
        context = {
        'uid':uid,
        'cid':cid,
    }
    return render(request,"chairman/add_maintenance.html",{'context':context})

def view_maintenance(request):
    uid = User.objects.get(email = request.session['c_email'])
    cid = Chairman.objects.get(user_id = uid)
    maintenanceData = Maintenance.objects.all()
    context = {
        'uid':uid,
        'cid':cid,
        'maintenanceData':maintenanceData,
    }
    return render(request,"chairman/maintenance_list.html",{'context':context})

def pay_maintenance(request):
    uid = User.objects.get(email = request.session['c_email'])
    c_obj= Chairman.objects.get(user_id = uid)
    mid = Maintenance.objects.filter(cid = c_obj, status = "Pending")
    mid_paid = Maintenance.objects.filter(cid = c_obj, status = "Paid")
    context = {
        'uid':uid,
        'cid':c_obj,
        'mid':mid,
        'mid_paid':mid_paid,
    }
    return render(request,"chairman/pay_maintenance.html",{'context':context})

def initiate_payment(request,pk):        
    try:
        global paymentid
        mid = Maintenance.objects.get(id = pk)
        amount = mid.amount
        paymentid = pk

        if "c_email" in request.session:
            uid = User.objects.get(email = request.session['c_email'])
            transaction = Transaction.objects.create(made_by = uid, amount = amount, main_id = mid)
            print("----------> uid", uid)
            print("----------> amount", amount)
            print("----------> mid", mid)
            transaction.save()
        
        elif "m_email" in request.session:
            uid = User.objects.get(email = request.session['m_email'])
            member_id = Member.objects.get(user_id = uid)
            transaction = Transaction.objects.create(made_by = uid, amount = amount, main_id = mid, member_id = member_id)
            print("----------> uid", uid)
            print("----------> amount", amount)
            print("----------> mid", mid)
            print("----------> member_id", member_id)
            transaction.save()

    except Exception as e:
        print("------->>>> Exception",e)
        return render(request, 'chairman/pay.html', context={'error': 'Wrong Accound Details or amount'})

    print("---------------> made_by",uid)
    print("---------------> main_id",mid)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(transaction.made_by.email)),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', request.user.email),
        # ('MOBILE_N0', '9911223388'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/chairman/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    transaction.checksum = checksum
    transaction.save()

    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    return render(request, 'chairman/redirect.html', context=paytm_params)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        print('----------------------------------------------status',received_data['STATUS'])   
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
            if received_data['STATUS'] == ['TXN_SUCCESS']:
                maintenance = Maintenance.objects.get(id = paymentid)
                maintenance.status='Paid'
                maintenance.save()
                tid = Transaction.objects.get(main_id = maintenance)
                print("---------------> tid",tid)
                print("---------------> tid",tid.made_by)
                tid.status = 'Paid'
                tid.save()
                context = {'received_data':received_data}
                print("---------------> received_data", received_data)
        else:
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'chairman/callback.html', context=received_data)

        return render(request, 'chairman/callback.html', context=received_data)

# if ['TXN_SUCCESS'] in received_data.values():
        #     orderid = received_data['ORDERID']
        #     print("---->>> type if orderid ", type(orderid))
        #     s = str(orderid)
        #     n = s[2:]
        #     final = n[:-2]
        #     tid = Transaction.objects.get(order_id = final)

        #     try:
        #         memberid = tid.member_id.id
        #         if memberid:
        #             member_id = Member.objects.get(id = memberid)
        #             mid = Maintenance.objects.get(id = tid.main_id.id)
        #             mid.status = "Paid"
        #             mid.save()
        #             tid.status = "Paid"
        #             tid.save()
        #     except:
        #         orderid = received_data['ORDERID']
        #         s = str(orderid)
        #         n = s[2:]
        #         final = n[:-2]
        #         tid = Transaction.objects.get(order_id = final)
        #         chairman_id = tid.main_id.cid
        #         mid = Maintenance.objects.get(id = tid.main_id.id)
        #         mid.status = "Paid"
        #         mid.save()
        #         tid.status = "Paid"
        #         tid.save()
        # else:
        #     orderid = received_data['ORDERID']
        #     s = str(orderid)
        #     n = s[2:]
        #     final = n[:-2]
        #     tid = Transaction.objects.get(order_id = final)
        #     mid = Maintenance.objects.get(id = tid.main_id.id)
        #     mid.status = "Pending"
        #     mid.save()
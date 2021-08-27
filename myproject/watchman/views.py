from django.shortcuts import render,HttpResponseRedirect,reverse
from chairman.models import *
from . utils import *
from random import *
# Create your views here.

def w_index(request):
    if "w_email" in request.session:
        wid = Watchman.objects.get(email = request.session['w_email'])
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
        return render(request,"chairman/c_login.html")

def w_logout(request):
    if "w_email" in request.session:
        del request.session['w_email']
        return render(request,"chairman/c_login.html")
    else:
        return render(request,"chairman/c_login.html")

def w_login_page(request):
    return render(request,"chairman/c_login.html")

def w_view_member(request):
    wid = Watchman.objects.get(email = request.session['w_email'])
    mid = Member.objects.all()
    context = {
                    'wid':wid,
                    'mid':mid,
                }
    return render(request,"watchman/w_view_members.html",{'context':context})

def w_view_notice(request):
    wid = Watchman.objects.get(email = request.session['w_email'])
    noticedata = Notice.objects.all()
    context = {
                    'wid':wid,
                    'noticedata':noticedata,
                }
    return render(request,"watchman/w-notice-list.html",{'context':context})

def w_view_event(request):
    wid = Watchman.objects.get(email = request.session['w_email'])
    eventData = Event.objects.all()
    context = {
                    'wid':wid,
                    'eventData':eventData,
                }
    return render(request,"watchman/w-event-list.html",{'context':context})

def w_view_complaint(request):
    wid = Watchman.objects.get(email = request.session['w_email'])
    complaintData = Complaint.objects.all()
    context = {
                    'wid':wid,
                    'complaintData':complaintData,
                }
    return render(request,"watchman/w_complaint_list.html",{'context':context})

def w_view_suggestions(request):
    wid = Watchman.objects.get(email = request.session['w_email'])
    suggestData = Suggestions.objects.all()
    context = {
                    'wid':wid,
                    'suggestData':suggestData,
                }
    return render(request,"watchman/w-suggestion-list.html",{'context':context})

def w_profile(request):
    wid = Watchman.objects.get(email = request.session['w_email'])
    context = {
                    'wid':wid,
                }
    return render(request,"watchman/w_profile.html",{'context':context})

def w_profile_update(request):
    wid = Watchman.objects.get(email = request.session['w_email'])
    if request.method == 'POST':
        if not request.POST['newpassword']:
            password = request.POST['password']
            wid.password = password
            wid.save()
        else:
            newpassword = request.POST['newpassword']
            wid.password = newpassword
            wid.save()
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        contact_no = request.POST['contact_no']
        family_contact_no = request.POST['family_contact_no']
        wid.fname = fname
        wid.lname = lname
        wid.address = address
        wid.contact_no = contact_no
        wid.family_contact_no = family_contact_no
        if "profile_picture" in request.FILES:
            profile_picture = request.FILES['profile_picture']
            wid.profile_picture = profile_picture
            wid.save()
    wid.save()
    context = {
                    'wid':wid,
                }
    return render(request,"watchman/w_profile.html",{'context':context})

def add_visitor_page(request):
    if "w_email" in request.session:
        wid = Watchman.objects.get(email = request.session['w_email'])
        mdid = MemberDetails.objects.all()
        context = {
                    'wid':wid,
                    'mdid':mdid,
                }
        return render(request,"watchman/add_visitor.html",{'context':context})

def add_visitor(request):
    if request.POST:
        wid = Watchman.objects.get(email = request.session['w_email'])
        v_homeno = request.POST['v_homeno']
        v_name = request.POST['v_name']
        v_mobile_no = request.POST['v_mobile_no']
        v_date = request.POST['v_date']
        v_time = request.POST['v_time']
        reason = request.POST['reason']
        vid = Visitor.objects.create(
            v_homeno=v_homeno, v_name=v_name, v_mobile_no=v_mobile_no, v_date=v_date, v_time=v_time, reason=reason
        )
        visitorsData = Visitor.objects.all()
        context = {
                    'wid':wid,
                    'visitorsData':visitorsData,
                }
        return render(request,"watchman/visitors_list.html",{'context':context}) 

def view_visitor(request):
    if "w_email" in request.session:
        wid = Watchman.objects.get(email = request.session['w_email'])
        visitorsData = Visitor.objects.all()
        context = {
                    'wid':wid,
                    'visitorsData':visitorsData,
                }
        return render(request,"watchman/visitors_list.html",{'context':context})
    else:
        e_msg = "YOU ARE NOT AUTHORISED TO VIEW THIS PAGE"
        return render(request,"chairman/c_login.html",{'e_msg':e_msg})
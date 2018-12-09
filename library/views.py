# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,JsonResponse

from django.template import loader
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
import requests,json
import ast
import operator


from datetime import date, timedelta, datetime

'''def index(request):
    #data= Book_detail.objects.all()
    #template = loader.get_template('library/index.html')
    return render(request,'library/index.html',{"data":data})'''

def login(request):
    if(request.session.get('id', False) != False):
        del request.session['id']
    return render(request,'library/login.html')



def index(request,token):
     url="https://serene-wildwood-35121.herokuapp.com/oauth/getDetails"
     payload = {'token':token,'secret':"6268d306d1ff54e199bafa466b5d612eb132eb98456fe598846f66616b5a485fa13ed86b817b9f9534d1558ee7ce596574fa17c60eae07547bba3d7648214b9c"}
     k = requests.post(url,payload)
     details = json.loads(str(k.content).decode('utf8'))
     id = details["student"][0]["Student_ID"]
     username = details["student"][0]["Student_Last_name"]
     mail = details["student"][0]["Student_Email"]
     pwd = "iamstudent"
     if User.objects.filter(User_id = id).exists()==False:
         a = User()
         a = User.objects.create(User_id=id,User_name=username,User_mail=mail,User_pwd=pwd)
         a.save()
         # print(a.id)
         return redirect('home',str(id))
     else:
        print(id)
        return redirect('home',str(id))
     #return redirect('home')

def home(request,id):
    news = NewsFeed.objects.all()
    context ={ "id" : id, "news" : news}
    request.session['id'] = id
    return render(request,'library/home.html',context)

def search(request):
    if (request.session.get('id', False) !=False):
         if request.method == 'POST':
             sear = request.POST.get("search")
             context = {"id": sear}
             return render(request, 'library/search.html', context)
    else:
        return redirect('library/login')

def search1(request):
    if request.method == 'POST':
        if (request.POST.get('Name',False) != False):
            libr = User.objects.get(User_id=request.POST['UserID'])
            a = Book_detail()
            a.Book_name = request.POST['Name']

            book_name = Book_detail.objects.filter(Book_name=request.POST['Name'])
            # book_name = Book_detail.objects.filter(Book_name=request.POST['Name'],Edition__range=('2015','2017')).order_by('-Edition')
            #book_name = Issue_master.objects.filter(Issue_date__range=('2015-11-20','2019-11-20')).order_by('-Issue_date')
            #book_name = Book_detail.objects.raw('select * from items.Book_detail;')
            #bookdetails = Book_detail.objects.filter(Book_name = book_name)
            print (book_name)

            context = {"bookname": book_name,"id":libr}
                # a.User_id = User.objects.get(User_id=request.POST['UserID'])
                # fine = Issue_master.objects.filter(User_id=a.User_id)
                # message = "Your fine is :-"
                # context = {"id": libr, "message": message, "fine": fine}
            return render(request, 'library/search.html',context)
    return render(request, 'library/search.html')

def orderbook(request):
    if request.method== 'POST':
        ord = request.POST.get("order")
        if(Admin.objects.filter(Admin_id = ord)):
            order = Orderbook.objects.filter()
            context = {"id": ord , "order":order}
            return render(request, 'library/order1.html', context)
        else:
            context = {"id": ord}
            return render(request, 'library/order.html', context)


def order1(request):
    if request.method== 'POST':
        print ("desi")

        if (request.POST.get('UserID', False) != False and request.POST.get('BookName',False) != False and request.POST.get('AuthorName', False) != False):
            #print("hello")
            libr = request.POST['UserID']
            a = Orderbook()

            a.User_id  = request.POST['UserID']
            a.Book_name = request.POST['BookName']
            a.Author = request.POST['AuthorName']
            a.save()
            message = "order Successful!!"
            print("OUT3")
            context = {"id": libr, "message": message}
            return render(request, 'library/order.html', context)
        else:
             return render(request, 'library/order.html')


def add(request):
    if request.method== 'POST':
        add1 = request.POST.get("add")
        if (Admin.objects.filter(Admin_id=add1)):
            context = {"id": add1}
            return render(request, 'library/add.html', context)
        else:
            context = {"id": add1}
            return render(request, 'library/all.html', context)

def add1(request):
    if request.method== 'POST':
            libr = User.objects.get(User_id=request.POST['UserID'])
            print("ding")
            a = Book_detail()
            a.Book_name = request.POST['bookname']
            a.Author = request.POST['authorname']
            a.Edition = request.POST['edition']
            a.Price = request.POST['price']
            a.Bool = "0"
            a.save()
            print(a)
            message = "Added Successfully!!"
            print("OUT3")
            context = {"id": libr, "message": message}
            return render(request, 'library/add.html', context)
    return render(request, 'library/add.html')

def issuebook(request):
    if (request.session.get('id', False) != False):
        if request.method == 'POST':
            issu = request.POST.get("issue")
            if (Admin.objects.filter(Admin_id=issu)):
                context = {"id": issu}
                return render(request, 'library/issue.html', context)
            else:
                context = {"id": issu}
                return render(request, 'library/all.html', context)
    else:
        return redirect('../login')

def issue1(request):
    print ("hello1")
    if request.method == 'POST':
        issu = User.objects.get(User_id=request.POST['admin'])
        context = {"id":issu}
        if(Book_detail.objects.filter(Book_id=request.POST['BookID']).count() == 1):
            bookname = Book_detail.objects.get(Book_id=request.POST['BookID']).Book_name
            print(bookname)
        else:
            return render(request, 'library/issue.html', context)
        if(User.objects.filter(User_id = request.POST['UserID'])):
            if(Issue_master.objects.filter(User_id = request.POST['UserID'], Return_date = None).count() >= 2):
                message = "Issue Failed!!! Sorry, the student already has two books to return."
                print("OUT5")
                context = {"id": issu}
                return render(request, 'library/issue.html',context)
            elif(Book_detail.objects.filter(Book_name=bookname,Bool="0").count() <=2):
                message = "Issue Failed!!! Insufficient Books."
                print("OUT4")
                context = {"id": issu}
                return render(request, 'library/issue.html',context)
            # if Book_detail.objects.filter(User_id = request.POST['UserID'],bool="1"):
            #     if(Issue_master.objects.filter(User_id = request.POST['UserID'], Return_date = None)):
            #         return render(request, 'library/issue.html', context)
            else:
                if (Book_detail.objects.filter(Book_id=request.POST['BookID'], Bool="0")):
                    b = Issue_master()
                    b.User_id = User.objects.get(User_id=request.POST['UserID'])
                    b.Book_id = Book_detail.objects.get(Book_id=request.POST['BookID'])
                    b.Issue_date = request.POST['IssueDate']
                    b.Actual_return_date = (date.today()+timedelta(days=15)).isoformat()
                    # print (request.POST['admin'])
                    b.Admin_id = Admin.objects.get(Admin_id="20160010054")
                    b.save()

                    a = Book_detail()
                    if(Book_detail.objects.get(Book_id = request.POST['BookID'])):
                        Book_detail.objects.filter(Book_id=request.POST['BookID']).update(Bool = "1")
                        a.save()

                    message = "Issue Successful!!"
                    print("OUT3")
                    context = {"id": issu}
                    return render(request, 'library/issue.html',context)
                else:
                    return render(request, 'library/issue.html',context)
        else:
            return render(request, 'library/issue.html', context)
    return render(request, 'library/issue.html')

def donatebook(request):
    if request.method == 'POST':
        dono =  request.POST.get("donate")
        if (Admin.objects.filter(Admin_id=dono)):
            context = {"id": dono}
            return render(request, 'library/donate.html', context)
        else:
            context = {"id": dono}
            return render(request, 'library/all.html', context)

def donate1(request):
    if request.method == 'POST':
        libr = User.objects.get(User_id=request.POST['admin'])
        print(libr)
        b = DonateBook()
        b.User_id = User.objects.get(User_id=request.POST['DonatorID'])
        b.Name = request.POST['DonorName']
        b.Book_name = request.POST['BookName']
        b.Admin_id = Admin.objects.get(Admin_id="20160010054")
        b.save()
        context = {"id": libr}
        return render(request, 'library/donate.html',context)

def returnbook(request):
    if request.method == 'POST':
        retur = request.POST.get("return")
        if (Admin.objects.filter(Admin_id=retur)):
            context = {"id": retur}
            return render(request, 'library/return.html', context)
        else:
            context = {"id": retur}
            return render(request, 'library/all.html', context)

def return1(request):
    if request.method== 'POST':
        print("hello")
        libr = User.objects.get(User_id=request.POST['admin'])
        context = {"id":libr}
        if (User.objects.filter(User_id=request.POST['UserID'])):
            if (Book_detail.objects.filter(Book_id=request.POST['BookID'], Bool="1")):
                #print(Issue_master.objects.get(Book_id=request.POST['BookID'], Return_date=None).Actual_return_date)
                Issue_master.objects.filter(Book_id=request.POST['BookID'],Payment_status="0").update(Return_date=request.POST['ReturnDate'])

                date1 = Issue_master.objects.get(Book_id=request.POST['BookID'],Payment_status="0").Actual_return_date
                date2 = Issue_master.objects.get(Book_id=request.POST['BookID'],Payment_status="0").Return_date
                d1 = datetime.strptime(str(date1), "%Y-%m-%d")
                d2 = datetime.strptime(str(date2), "%Y-%m-%d")
                delta = (d2 - d1).days
                if(delta>0):
                    Issue_master.objects.filter(Book_id=request.POST['BookID'],Payment_status="0").update(Fine=(delta) * 2)

                Issue_master.objects.filter(Book_id=request.POST['BookID']).update(Payment_status="1")
                Book_detail.objects.filter(Book_id=request.POST['BookID']).update(Bool="0")
                message = "Your book is returned successfully!"
                context ={"id":libr , "message" : message}
                return render(request, 'library/return.html',context)
            else:
                context = {"id": libr}
                return render(request, 'library/return.html', context)
        else:
            context = {"id": libr}
            return render(request, 'library/message.html', context)
    return render(request, 'library/return.html')

def feedback(request):
    if request.method== 'POST':
        feedback = request.POST.get("feedback")

        if (Admin.objects.filter(Admin_id=feedback)):
            feed = Feedback.objects.filter()
            context = {"id": feedback ,"feed":feed}
            return render(request, 'library/feedback1.html', context)
        else:
            context = {"id": feedback}
            return render(request, 'library/feedback.html', context)

def feed1(request):
    if request.method== 'POST':
        #if (request.POST.get('UserID', False) != False and request.POST.get('BookName',False) != False and request.POST.get('AuthorName', False) != False):
            #print("hello")
            libr = User.objects.get(User_id=request.POST['UserID'])
            a = Feedback()
            #a.Issue_no  = request.POST['Issue_no']
            a.User_id = User.objects.get(User_id=request.POST['UserID'])
            a.Complaint = request.POST['Complaint']
            a.Date=request.POST['Date']
            a.save()
            message = "Your feedback is registered successfully!"
            context = {"id": libr, "message": message}
            return render(request, 'library/feedback.html', context)
    return render(request, 'library/feedback.html')

def fine(request):
    if request.method== 'POST':
        fine = request.POST.get("fine")
        if (Admin.objects.filter(Admin_id=fine)):
            context = {"id": fine}
            return render(request, 'library/fine.html', context)
        else:
            context = {"id": fine}
            return render(request, 'library/fine1.html', context)
    return render(request, 'library/fine.html')

def fine1(request):
    if request.method== 'POST':
        libr = User.objects.get(User_id=request.POST['user'])
        a = Issue_master()
        a.User_id = User.objects.get(User_id=request.POST['UserID'])
        fine = Issue_master.objects.filter(User_id=a.User_id)
        total = Issue_master.objects.filter(User_id=a.User_id).aggregate(Sum('Fine'))
        context = {"id": libr,"fine":fine,"total":total}
        if (Admin.objects.filter(Admin_id=libr)):
            return render(request, 'library/fine.html', context)
        else:
            return render(request, 'library/fine1.html', context)
    return render(request, 'library/fine.html')

def fine2(request):
    if request.method== 'POST':
        libr = User.objects.get(User_id=request.POST['user'])
        if (Admin.objects.filter(Admin_id=libr)):
            a= Issue_master()
            a.User_id = User.objects.get(User_id=request.POST['UserID'])
            Issue_master.objects.filter(User_id=a.User_id).update(Fine = 0)
            fine = Issue_master.objects.filter(User_id=a.User_id)
            total = Issue_master.objects.filter(User_id=a.User_id).aggregate(Sum('Fine'))
            context = {"id": libr, "fine": fine, "total": total}
            return render(request, 'library/fine.html', context)
        else:
            context = {"id": libr}
            return render(request, 'library/fine.html', context)

def news(request):
    if request.method == 'POST':
        new = request.POST.get("new")
        if (Admin.objects.filter(Admin_id=new)):
            context = {"id": new}
            return render(request, 'library/news.html', context)
        else:
            context = {"id": new}
            return render(request, 'library/all.html', context)
    else:
        return render(request, 'library/news.html')

def news1(request):
    if request.method== 'POST':
        new = request.POST.get("new")
        a= NewsFeed()
        a.Current_date = request.POST['Current_date']
        a.Designate_date = request.POST['ReturnDate']
        a.Description = request.POST['comment']
        a.save()
        context = {"id": new}
        return render(request, 'library/news.html', context)


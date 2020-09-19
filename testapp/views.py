from django.shortcuts import render
from django.http import HttpResponse
import random
from django.contrib import messages
import numpy as np
# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def numbers(request):
    ls=[]
    go = 0
    if request.method == "POST":
        try:
            testcases=request.POST.get('testcase',0)
            minval = request.POST.get('minval',0)
            maxval = request.POST.get('maxval',0)
            flag = request.POST.get('flag',True)
            print("Testcase = ",testcases," Minval =  ",minval," maxval = ",maxval," ",flag)
            if int(testcases)<=0:
                messages.error(request,"Test Case can't be less than or equal to 0")
            elif int(minval)>int(maxval):
                messages.error(request,"Minimum value can't be larger than maximum value")
            else:
                go = 1
        except ValueError:
            print("cant be 0")
        if go==1:
            for i in range(int(testcases)):
                n = random.randint(int(minval),int(maxval))
                ls.append(n)
            return render(request,'numbers.html',{'ls':ls,'flag':flag,'testcases':testcases})
    return render(request,'numbers.html')

def arrays(request):
    ls,ls1 = [],[]
    go = 0
    if request.method == "POST":
        try:
            testcases=request.POST.get('testcase',0)
            arrsize = request.POST.get('arrsize',0)
            minval = request.POST.get('minval',0)
            maxval = request.POST.get('maxval',0)
            distinct = request.POST.get('distinct',True)
            flag = request.POST.get('flag',True)
            print("Testcase = ",testcases,"array size = ",arrsize," Minval =  ",minval," maxval = ",maxval," ",flag)
            if distinct == 'True' and (int(maxval)-int(minval))<int(arrsize):
                messages.error(request,"Now sufficient values to make distinctive")
            elif int(testcases)<=0:
                messages.error(request,"Test Case can't be less than or equal to 0")
            elif int(minval)>int(maxval):
                messages.error(request,"Minimum value can't be larger than maximum value")
            elif int(arrsize)<=0:
                messages.error(request,"Array size can't be less or equal to 0")
            else:
                go = 1
        except ValueError:
            print("caught")
        if go==1:
            for i in range(int(testcases)):
                ls1=[]
                if distinct == False:
                    for j in range(int(arrsize)):
                        n = random.randint(int(minval),int(maxval))
                        ls1.append(n)
                    ls.append(ls1)
                else:
                    dis = random.sample(range(int(minval),int(maxval)),int(arrsize))
                ls.append(dis)
        # else:
        #     ls="Sorry"
            return render(request,'arrays.html',{'ls':ls,'flag':flag,'testcases':int(testcases)})
    return render(request,'arrays.html')

def matrix(request):
    result=[]
    z=0
    if request.method == "POST":
        try:
            testcases=request.POST.get('testcase',0)
            rows = request.POST.get('rows',0)
            columns = request.POST.get('columns',0)
            minval = request.POST.get('minval',0)
            maxval = request.POST.get('maxval',0)
            distinct = request.POST.get('distinct',True)
            flag = request.POST.get('flag',True)
            if distinct == 'True' and (int(maxval)-int(minval))<int(rows)*int(columns):
                messages.error(request,"Now sufficient values to make distinctive")
            elif int(testcases)<=0 or int(minval)>int(maxval) or int(rows)<0 or int(columns)<0:
                messages.error(request,"Invalid Input")
            else:
                z=1
        except ValueError:
            print("")
        if z==1 :
            for i in range(int(testcases)):
                ls2=[]
                if distinct == False:
                    for i in range(int(rows)):
                        ls1=[]
                        for j in range(int(columns)):
                            n = random.randint(int(minval),int(maxval))
                            ls1.append(n)
                        ls2.append(ls1)
                    result.append(ls2)
                else:
                    for i in range(int(rows)):
                        dis = random.sample(range(int(minval),int(maxval)),int(columns))
                        ls2.append(dis)
                result.append(ls2)
            return render(request,'matrix.html',{'ls':result,'flag':flag,'testcases':testcases,'rows':int(rows),'columns':int(columns)})
    return render(request,'matrix.html')





def strings(request):
    ls,ls1=[],[]
    z=0
    if request.method == "POST":
        try:
            testcases=request.POST.get('testcase',0)
            stringsize = request.POST.get('stringsize',0)
            chars = request.POST.get('chars',0)
            distinct = request.POST.get('distinct',True)
            flag = request.POST.get('flag',True)
            if int(testcases)<=0 or int(stringsize)<=0 or len(chars)<=0:
                messages.error(request,"Invalid Input")
            elif distinct == 'True' and len(chars)<int(stringsize):
                messages.error(request,"Now sufficient values to make distinctive")
            else:
                z=1
        except ValueError:
            print("")
        if z==1:
            letters = [str(a) for a in chars]
            if distinct == 'False':
                for i in range(int(testcases)):
                    ls1 = ''.join(random.choice(letters) for i in range(int(stringsize)))
                    ls.append(ls1)
            else:
                for i in range(int(testcases)):
                    ls1 = ''.join(random.sample(letters,int(stringsize)))
                    ls.append(ls1)
            return render(request,'strings.html',{'ls':ls,'flag':flag,'testcases':testcases})
    return render(request,'strings.html')


def string_matrix(request):
    ls,ls1=[],[]
    result=[]
    z=0
    if request.method == "POST":
        try:
            testcases=request.POST.get('testcase',0)
            rows = request.POST.get('rows',0)
            columns = request.POST.get('columns',0)
            chars = request.POST.get('chars',0)
            rowcol = request.POST.get('rowcol',True)
            flag = request.POST.get('flag',True)
            if int(testcases)<=0 or int(rows)<0 or int(columns)<0 or len(chars)<=0:
                messages.error(request,"Invalid Input")
            else:
                z=1
        except ValueError:
            print("")
        if z==1:
            letters = [str(a) for a in chars]
            for i in range(int(testcases)):
                ls=[]
                for j in range(int(rows)):
                    ls1 = ' '.join(random.choice(letters) for x in range(int(columns)))
                    ls.append(ls1)
                result.append(ls)
            return render(request,'string_matrix.html',{'ls':result,'flag':flag,'testcases':testcases,'rowcol':rowcol,'rows':rows,'columns':columns})
    return render(request,'string_matrix.html')

def variable_length_strings(request):
    ls,ls1=[],[]
    z=0
    if request.method == "POST":
        try:
            testcases=request.POST.get('testcase',0)
            min_length = request.POST.get('min_length',0)
            max_length = request.POST.get('max_length',0)
            chars = request.POST.get('chars',0)
            distinct = request.POST.get('distinct',True)
            flag = request.POST.get('flag',True)
            if int(testcases)<=0 or int(min_length)<0 or int(max_length)<0 or int(max_length)<int(min_length) or len(chars)<=0:
                messages.error(request,"Invalid Input")
            elif distinct == 'True' and int(max_length)>len(chars):
                print("len(chars) = ",len(chars))
                print("int(max_length)-int(min_length)) = ",int(max_length)-int(min_length))
                print("distinct = ",distinct)
                messages.error(request,"Not sufficient values to make distinctive Strings")
            else:
                z=1
        except ValueError:
            print("")
        if z==1:
            letters = [str(a) for a in chars]
            if distinct == 'False':
                for i in range(int(testcases)):
                    x = random.randint(int(min_length),int(max_length))
                    ls1 = ''.join(random.choice(letters) for i in range(x))
                    ls.append(ls1)
            else:
                for i in range(int(testcases)):
                    x = random.randint(int(min_length),int(max_length))
                    ls1 = ''.join(random.sample(letters,x))
                    ls.append(ls1)
            return render(request,'variable_strings.html',{'ls':ls,'flag':flag,'testcases':testcases})
    return render(request,'variable_strings.html')

def unweighted_tree(request):
    ls,ls1,ls2=[],[],[]
    z=0
    if request.method == "POST":
        try:
            testcases=request.POST.get('testcase',0)
            num_nodes = request.POST.get('num_nodes',0)
            index = request.POST.get('index',0)
            num_flag = request.POST.get('num_flag',True)
            flag = request.POST.get('flag',True)
            print("Testcase = ",testcases)
            if int(testcases)<=0 or int(num_nodes)<0 or int(index)<0:
                messages.error(request,"Invalid Input")
            else:
                z = 1
        except ValueError:
            print("")

        if z==1 :
            x = int(index)+int(num_nodes)
            for i in range(int(testcases)):
                ls1=[]
                for k in range(int(num_nodes)):
                    ls=[]
                    for j in range(2):
                        n = random.randint(int(index),x)
                        ls.append(n)
                    ls1.append(ls)
                ls2.append(ls1)
            return render(request,'unweighted_tree.html',{'ls':ls2,'flag':flag,'testcases':testcases,'num_flag':num_flag,'num_nodes':num_nodes})
    return render(request,'unweighted_tree.html')

def weighted_tree(request):
    ls,ls1,ls2=[],[],[]
    z=0
    if request.method == "POST":
        try:
            testcases=request.POST.get('testcase',0)
            num_nodes = request.POST.get('num_nodes',0)
            index = request.POST.get('index',0)
            min_weight = request.POST.get('min_weight',0)
            max_weight = request.POST.get('max_weight',0)
            num_flag = request.POST.get('num_flag',True)
            flag = request.POST.get('flag',True)
            print("Testcase = ",testcases)
            if int(testcases)<=0 or int(num_nodes)<0 or int(min_weight)>int(max_weight) or int(index)<0 :
                messages.error(request,"Invalid Input")
            else:
                z = 1
        except ValueError:
            print("")
        if z==1 :
            x = int(index)+int(num_nodes)
            for i in range(int(testcases)):
                ls1=[]
                for k in range(int(num_nodes)):
                    ls=[]
                    for j in range(2):
                        n = random.randint(int(index),x)
                        ls.append(n)
                    ls.append(random.randint(int(min_weight),int(max_weight)))
                    ls1.append(ls)
                ls2.append(ls1)
            return render(request,'weighted_tree.html',{'ls':ls2,'flag':flag,'testcases':testcases,'num_flag':num_flag,'num_nodes':num_nodes})
    return render(request,'weighted_tree.html')


def unweighted_graph(request):
    ls,ls1,ls2=[],[],[]
    error = False
    z=0
    if request.method == "POST":
        try:
            testcases=request.POST.get('testcase',0)
            num_nodes = request.POST.get('num_nodes',0)
            num_edges = request.POST.get('num_edges',0)
            index = request.POST.get('index',0)
            num_flag = request.POST.get('num_flag',True)
            flag = request.POST.get('flag',True)
            print("Testcase = ",testcases)
            if int(testcases)<=0 or int(num_nodes)<0 or int(num_edges)<0 :
                messages.error(request,"Invalid Input")
            else:
                z = 1
        except ValueError:
            print("")
        if z==1 :
            x = (int(num_nodes)*(int(num_nodes)-1))/2
            if int(num_edges)>x:
                error = True
                messages.error(request,"Please check that the number of edges are more than that could be created using that nodes. Edges could be <= ((nodes)*(nodes-1))/2")
                ls2.append("Edges Limit exceeded")
            else:
                y = int(index)+int(num_nodes)
                for i in range(int(testcases)):
                    ls1=[]
                    for k in range(int(num_edges)):
                        ls=[]
                        for j in range(2):
                            n = random.randint(int(index),y)
                            ls.append(n)
                        ls1.append(ls)
                    ls2.append(ls1)
            return render(request,'unweighted_graph.html',{'ls':ls2,'flag':flag,'testcases':testcases,'num_flag':num_flag,'num_nodes':num_nodes,'num_edges':num_edges,'error':error})
    return render(request,'unweighted_graph.html')


def weighted_graph(request):
    ls,ls1,ls2=[],[],[]
    error = False
    z=0
    if request.method == "POST":
        try:
            testcases=request.POST.get('testcase',0)
            num_nodes = request.POST.get('num_nodes',0)
            num_edges = request.POST.get('num_edges',0)
            index = request.POST.get('index',0)
            min_weight = request.POST.get('min_weight',0)
            max_weight = request.POST.get('max_weight',0)
            num_flag = request.POST.get('num_flag',True)
            flag = request.POST.get('flag',True)
            if int(testcases)<=0 or int(num_nodes)<0 or int(min_weight)>int(max_weight) or int(index)<0 or int(num_edges)<0:
                messages.error(request,"Invalid Input")
            else:
                z = 1
        except ValueError:
            print("")
        if z==1 :
            x = (int(num_nodes)*(int(num_nodes)-1))/2
            if int(num_edges)>x:
                error = True
                messages.error(request,"Please check that the number of edges are more than that could be created using that nodes. Edges could be <= ((nodes)*(nodes-1))/2")
                ls2.append("Edges Limit exceeded")
            else:
                y = int(index)+int(num_nodes)
                for i in range(int(testcases)):
                    ls1=[]
                    for k in range(int(num_nodes)):
                        ls=[]
                        for j in range(2):
                            n = random.randint(int(index),y)
                            ls.append(n)
                        ls.append(random.randint(int(min_weight),int(max_weight)))
                        ls1.append(ls)
                    ls2.append(ls1)
            return render(request,'weighted_graph.html',{'ls':ls2,'flag':flag,'testcases':testcases,'num_flag':num_flag,'num_nodes':num_nodes,'num_edges':num_edges,'error':error})
    return render(request,'weighted_graph.html')
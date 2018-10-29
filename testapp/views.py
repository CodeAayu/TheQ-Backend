from django.shortcuts import render
import datetime , json
from testapp.models import EventData, EventQueue, Queue
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , JsonResponse
from django.conf import settings

@csrf_exempt
def savetheevent(request):
    print (request.body)
    data = json.loads(request.body)
    #image = request.FILES["image"]
    event_name = data["event_name"]
    event_date_start = datetime.datetime.strptime(str(data["date_start"]),"%d%m%Y").date()
    event_date_end = datetime.datetime.strptime(str(data["date_end"]),"%d%m%Y").date()
    event_description = data["description"]
    event_city = data["city"]
    genre = data["genre"]
    ans = EventData.objects.create(event_name=event_name, date_start=event_date_start, date_end=event_date_end, description=event_description, city=event_city, genre=genre)
    EventQueue.objects.create(event_id=ans.event_id,start_point=0,end_point=0)
    return HttpResponse("Event successfully saved!")

@csrf_exempt
def showeventdetails(request):
    if request.method == 'GET':
        data = EventData.objects.all().values()
        listing = list(data)
        for i in range(len(listing)):
            if listing[i]["event_cover_image"]:
                listing[i]["event_cover_image"] = settings.BASE_URL + settings.STATIC_URL + listing[i]["event_cover_image"].split('/')[1]
            ## print (listing[i])
        return JsonResponse(listing, safe=False)
    return HttpResponse("Wrong request!")

@csrf_exempt
def deleteevent(request, id):
    if request.method == 'DELETE':
        EventData.objects.get(event_id=id).delete()
        EventQueue.objects.get(event_id=id).delete()
        return HttpResponse("Event successfully removed!")
    else:
        return HttpResponse("Wrong Request!")


@csrf_exempt
def queueenter(request):
    data = request.POST
    username = data["username"]
    event_id = data["event_id"]
    ans = EventQueue.objects.get(event_id=event_id)
    ans.end_point = ans.end_point + 1
    token_number = ans.end_point
    ans.save()
    Queue.objects.create(event_id=event_id, username=username, token_number=token_number)
    return JsonResponse([token_number], safe= False)


@csrf_exempt
def queueleave(request):
    data = request.POST
    event_id = data["event_id"]
    token_number = data["token_number"]
    ans = EventQueue.objects.get(event_id=event_id)
    ans.start_point = ans.start_point + 1
    ans.save()
    Queue.objects.get(event_id=event_id,token_number=token_number).delete()
    return HttpResponse("Removed from queue successfully!")


@csrf_exempt
def queuelength(request):
    data = json.loads(request.body)
    #print (data)
    event_id = int(data["event_id"])
    ans = EventQueue.objects.get(event_id=event_id)
    length = ans.end_point - ans.start_point
    return JsonResponse([length,ans.end_point,ans.start_point], safe=False)

@csrf_exempt
def tokenupdate(request):
    data = request.POST
    event_id = int(data["event_id"])
    ans = EventQueue.objects.get(event_id=event_id)
    start_point = ans.start_point
    return JsonResponse([start_point], safe=False)


@csrf_exempt
def userqueues(request):
    data = json.loads(request.body)
    name = data["username"]
    ans = Queue.objects.filter(username=name)
    listing = []
    for a in ans:
        listing.append({"event_id":a.event_id,"token_number":a.token_number})
    return JsonResponse(listing, safe=False)

@csrf_exempt
def registertheuser(request):
    data = request.body
    #print (type(data))
    # print (request)
    # data = json.loads(request.body)
    # user_name = data["user_name"]
    # user_profile_image = data["user_profile_image"]
    # user_cover_image = data["user_cover_image"]
    # EventData.objects.create(user_name=user_name, user_profile_image=user_profile_image, user_cover_image=user_cover_image)
    return HttpResponse("User successfully registered!")


# @csrf_exempt
# def test(request):
#     data = request.POST
#     print (data["name"])
#     image = request.FILES["image"]
#     print (type(image))
#     Test.objects.create(name=data["name"],image=image)
#     return HttpResponse("Done")
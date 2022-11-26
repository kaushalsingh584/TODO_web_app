from django.shortcuts import render,HttpResponse,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from .models import Task,User
from .forms import Task_form
# Create your views here.
def home(request):
    return render(request,"home.html")

# api views 
class task(APIView):
    permission_classes = [IsAuthenticated]
    # --------------------adding a task-------------------------------------------------------
    def post(self,request):
        name = request.data.get("name")
        status = request.data.get("status")
        priority = request.data.get("priority")
        try:
            task_obj = Task(
                user = request.user,
                name = name,
                status = status,
                priority = priority
            )
            task_obj.save()      
        except Exception as e:
            print(e)
            return Response({'error':str(e)},status=HTTP_400_BAD_REQUEST)
        return Response({'message' : "Task created"},status=HTTP_200_OK)

    # ----------------------gives the list of tasks for a particular user--------------------------
    def get(self,request):        
        task_done = Task.objects.filter(user = request.user)
        # creating an array of object for all tasks
        task_list = [{
            "id" : obj.uuid,
            "name" : obj.name,
            "status" : obj.status,
            "priority": obj.priority,
        } for obj in task_done]

        return Response(task_list,status=HTTP_200_OK)

    #--------------------- modifies the fields (name,status and priority) of a particular task,--------
    # ------------------------but mainly deals with marking task as completed--------------------------
    def patch(self,request):
        uuid = request.data.get("id")
        name = request.data.get("name")
        status = request.data.get("status")
        priority = request.data.get("priority")

        try:
            task_obj = Task.objects.get(pk = uuid)
            if status is not None :
                task_obj.status = status
            if name is not None and name is not "":
                task_obj.name = name
            if priority is not None and isinstance(priority,int) and priority > 1 and priority < 5 :
                task_obj.priority = priority
            task_obj.save()

        except Exception as e:
            print(e)
            return Response(status=HTTP_400_BAD_REQUEST)
        return Response({'id': task_obj.uuid,'message': "Modified"},status=HTTP_200_OK)
        
    # ----------------------------Deleting a task--------------------------------------------------------
    def delete(self,request):
        uuid = request.data.get("id")
        try:
            task_obj = Task.objects.get(pk=uuid)
            task_obj.delete()
        except Exception as e:
            print(e)
            return Response({'error' : "Not valid task_id"},status=HTTP_400_BAD_REQUEST)
        return Response({'message' : "Deleted"},status=HTTP_200_OK)


class completed_task(APIView):

    permission_classes = [IsAuthenticated]
    # ---------------------------------gives completed_task-----------------------------------------------
    def get(self,request):
        task_done = Task.objects.filter(
                        user = request.user,
                        status = True
                        )
        # creating an array of object for all tasks
        task_list = [{
            "id" : obj.uuid,
            "name" : obj.name,
            "status" : obj.status,
            "priority": obj.priority,
        } for obj in task_done]

        return Response(task_list,status=HTTP_200_OK)

class pending_task(APIView):
    permission_classes = [IsAuthenticated]
    # ------------------------------------git --gives pending_task---------------------------------------------
    def get(self,request):
        task_done = Task.objects.filter(
                        user = request.user,
                        status = False
                        )
        # creating an array of object for all tasks
        task_list = [{
            "id" : obj.uuid,
            "name" : obj.name,
            "status" : obj.status,
            "priority": obj.priority,
        } for obj in task_done]

        return Response(task_list,status=HTTP_200_OK)
    







from django.shortcuts import render
from django.utils.timezone import make_aware
from django.utils.dateparse import parse_datetime
from todo.models import Task

# Create your views here.
def index(request):
    if request.method == "POST":
        due = make_aware(parse_datetime(request.POST["due_at"])) if request.POST["due_at"] else None
        task = Task(
            title=request.POST["title"],
            due_at=due
        )
        task.save()

    if request.GET.get("order") == "due":
        tasks = Task.objects.order_by("due_at")
    else:
        tasks = Task.objects.order_by("-posted_at")

    context = {
        "tasks": tasks
    }
    return render(request, "todo/index.html", context)

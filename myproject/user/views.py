from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

def user_not_logged_in(user):
    return not user.is_authenticated

@user_passes_test(
    user_not_logged_in, login_url="blog:homepage", redirect_field_name=None
)
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog:homepage")
    form = NewUserForm()
    return render(
        request=request, template_name="user/register.html", context={"form": form}
    )

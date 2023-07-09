from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login,get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import views as auth_views
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.urls import reverse_lazy

def user_not_logged_in(user):
    return not user.is_authenticated

@user_passes_test(
    user_not_logged_in, login_url="blog:homepage", redirect_field_name=None
)
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_model = get_user_model()
            user.first_name = form.cleaned_data.get('name')
            user.save()
            login(request, user)
            return redirect("blog:homepage")
    else:
        form = NewUserForm()
    return render(
        request=request, template_name="user/register.html", context={"form": form}
    )

class CustomLoginView(FormView):
    template_name = 'user/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('blog:homepage')

    def form_valid(self, form):
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        # Perform custom authentication logic using email and password
        # Authenticate the user and generate JWT token
        # Example code:
        user = authenticate(request=self.request, email=email, password=password)
        if user is not None:
            login(self.request, user)
            # Redirect to success URL or return JSON response with token
            return super().form_valid(form)
        else:
            # Handle invalid credentials case
            # Redirect back to login page with error message or return JSON response
            return self.form_invalid(form)

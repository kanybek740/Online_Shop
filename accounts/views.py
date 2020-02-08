from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import CustomUser

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

@login_required
def edit_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            return redirect('shop:product_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form':form})

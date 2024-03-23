from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

# Read operation
def profile_view(request):
    # user_profile = get_object_or_404(Profile)
    # context = {'user_profile': user_profile}
    return render(request, 'profiles/profile_view.html')

# Update operation
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:profile_view', id_user=request.user.id)  # Rediriger vers la vue de profil avec l'ID de l'utilisateur
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/edit_profile.html', {'form': form})

# Delete operation
@login_required
def delete_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        profile.delete()
        # Rediriger vers une vue appropriée, comme la page d'accueil
        return redirect('home')  
    # Vous pouvez également ajouter une confirmation de suppression ici si nécessaire
    return render(request, 'profiles/delete_profile.html', {'profile': profile})

# Create operation
@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profiles:profile_view', id_user=request.user.id)  # Rediriger vers la vue de profil avec l'ID de l'utilisateur
    else:
        form = ProfileForm()
    return render(request, 'profiles/create_profile.html', {'form': form})

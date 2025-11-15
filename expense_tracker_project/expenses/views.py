from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import SignUpForm, ExpenseForm, CategoryForm
from .models import Expense, Category

def home(request):
    return render(request, 'expenses/home.html')

def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created. Welcome!")
            return redirect('expenses:dashboard')
    else:
        form = SignUpForm()
    return render(request, 'expenses/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'expenses/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('expenses:home')

@login_required
def logout_confirm(request):
    return render(request, 'expenses/logout.html')


@login_required
def dashboard(request):
    # quick stats
    total = Expense.objects.filter(user=request.user).aggregate(total=Sum('amount'))['total'] or 0
    recent = Expense.objects.filter(user=request.user)[:6]
    return render(request, 'expenses/dashboard.html', {'total': total, 'recent': recent})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.user = request.user
            exp.save()
            messages.success(request, "Expense added.")
            return redirect('expenses:expense_list')
    else:
        form = ExpenseForm()
        form.fields['category'].queryset = Category.objects.filter(user=request.user)
    return render(request, 'expenses/add_expense.html', {'form': form})

@login_required
def expense_list(request):
    qs = Expense.objects.filter(user=request.user)
    return render(request, 'expenses/expense_list.html', {'expenses': qs})

@login_required
def expense_detail(request, pk):
    exp = get_object_or_404(Expense, pk=pk, user=request.user)
    return render(request, 'expenses/expense_detail.html', {'expense': exp})

@login_required
def edit_expense(request, pk):
    exp = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            messages.success(request, "Expense updated.")
            return redirect('expenses:expense_list')
    else:
        form = ExpenseForm(instance=exp)
        form.fields['category'].queryset = Category.objects.filter(user=request.user)
    return render(request, 'expenses/add_expense.html', {'form': form, 'edit_mode': True})

@login_required
def delete_expense(request, pk):
    exp = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        exp.delete()
        messages.success(request, "Expense deleted.")
        return redirect('expenses:expense_list')
    return render(request, 'expenses/expense_detail.html', {'expense': exp})

@login_required
def delete_category(request, pk):
    """Deletes a category owned by the user via a POST request."""
    cat = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        # Deleting the category will set its Foreign Key on any related
        # expenses to NULL, as defined in the Expense model.
        cat.delete()
        messages.success(request, f"Category '{cat.name}' deleted.")
        return redirect('expenses:category_list')
    # Prevent deletion via GET request
    return redirect('expenses:category_list')

@login_required
def category_list(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.user = request.user
            try:
                cat.save()
                messages.success(request, "Category added.")
            except Exception:
                messages.error(request, "That category already exists.")
            return redirect('expenses:category_list')
    else:
        form = CategoryForm()
    cats = Category.objects.filter(user=request.user)
    return render(request, 'expenses/category_list.html', {'categories': cats, 'form': form})

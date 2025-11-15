from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ExpenseForm, CategoryForm
from .models import Expense, Category
from django.db.models import Sum

def home(request):
    return render(request, 'expenses/home.html')

def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('expenses:dashboard')
    else:
        form = SignUpForm()
    return render(request, 'expenses/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'expenses/login.html'

class CustomLogoutView(LogoutView):
    pass

@login_required
def dashboard(request):
    recent = Expense.objects.filter(user=request.user)[:5]
    total = Expense.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'expenses/dashboard.html', {'recent': recent, 'total': total})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            e = form.save(commit=False)
            e.user = request.user
            e.save()
            return redirect('expenses:expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

@login_required
def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    return render(request, 'expenses/expense_detail.html', {'expense': expense})

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    form = CategoryForm()
    return render(request, 'expenses/category_list.html', {'categories': categories, 'form': form})

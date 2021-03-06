from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from restapi.models import Expense
from django.forms.models import model_to_dict


# Create your views here.
class ExpenseListCreate(APIView):
    def get(self, request):
        expenses = Expense.objects.all()

        all_expenses = [model_to_dict(expense) for expense in expenses]
        return Response(all_expenses, status=200)

    def post(self, request):
        amount = request.data["amount"]
        merchant = request.data["merchant"]
        description = request.data["description"]
        category = request.data["category"]

        expense = Expense.objects.create(
            amount=amount, merchant=merchant, description=description, category=category
        )
        return Response(model_to_dict(expense), status=201)

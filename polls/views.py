from django.shortcuts import render
from .models import Category, Questions


def main_page(request):

    category_list = Category.objects.all()

    context = {
        'category_li': category_list,
    }

    return render(request, 'category.html', context)
    pass


def poll_page(request, id):
    current_category = Category.objects.get(id=id)
    argument_list = Questions.objects.filter(category=current_category)

    context = {
        'ids': current_category.id,
        'pollsname': current_category.category_text,
        'argument_list': argument_list,
    }

    return render(request, 'polls.html', context)
    pass


def result_page(request, id):
    current_category = Category.objects.get(id=id)
    parameter_list = Questions.objects.filter(category=current_category)
    ids = request.POST.get('text')

    selected_choice = Questions.objects.get(id=ids)
    selected_choice.votes += 1
    selected_choice.save()

    context = {
        'pollsname': current_category.category_text,
        'cur_cate': current_category.id,
        'parameter_list': parameter_list,
        'votes': selected_choice.votes

    }

    return render(request, 'result.html', context)
    pass

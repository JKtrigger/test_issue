
# -*- coding:utf-8 -*-


def get_val(request, val):
    return request.GET.get(val, None)


def common_values(request):
    values = {
        'group_num': get_val(request, 'group_num'),
        'depart': get_val(request, 'depart'),
        'is_active': get_val(request, 'is_active'),
    }
    return values

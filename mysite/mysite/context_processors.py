def global_year_filter(request):
    return {
        'global_year': getattr(request, 'global_year', '2017'),
        'global_year_slug': getattr(request, 'global_year_slug', '2017'),
        'available_years': [
            {'value': '2017', 'name': '2017'},
            {'value': '2007', 'name': '2007'},
            {'value': '1997', 'name': '1997'},
        ]
    }
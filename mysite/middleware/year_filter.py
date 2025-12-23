class GlobalYearFilterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Годы, доступные для фильтрации
        AVAILABLE_YEARS = ['2017', '2007', '1997']

        # 1. Проверяем GET-параметр (при выборе из dropdown)
        if 'year' in request.GET:
            year = request.GET.get('year')
            if year in AVAILABLE_YEARS:
                request.session['global_year'] = year
                request.session['global_year_slug'] = year  # или создайте slug если отличается

        # 2. Устанавливаем глобальный год в объект request
        request.global_year = request.session.get('global_year', '2017')  # значение по умолчанию
        request.global_year_slug = request.session.get('global_year_slug', '2017')

        response = self.get_response(request)
        return response
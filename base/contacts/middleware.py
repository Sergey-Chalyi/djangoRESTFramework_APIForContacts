import requests
from django.http import JsonResponse
from base import settings


class RegionRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def get_client_ip(self, request):
        """
           This function retrieves the client's IP address.

           Args:
               request (HttpRequest): The HTTP request object.

           Returns:
               str: The client's IP address.

           If the request is in debug mode, it returns a predefined test IP address. Otherwise, it checks the HTTP headers for the X-Forwarded-For header and returns the first IP address found. If the X-Forwarded-For header is not present, it falls back to the REMOTE_ADDR header.
        """
        if settings.DEBUG:
            return settings.TEST_IP_ADDRESS

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip


    def __call__(self, request):
        """
        This middleware checks if the client's IP address belongs to an allowed country.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: If the client's IP address is not from an allowed country, it returns a 403 Forbidden response. Otherwise, it passes the request to the next middleware or view.

        Raises:
            Exception: If there's an error while retrieving the client's IP address or country information.
        """
        ip_address = self.get_client_ip(request)

        try:
            response = requests.get(settings.GEOLOCATION_URL.format(ip=ip_address))
            data = response.json()
            country = data.get('country')
        except Exception as e:
            print(f"Error: {e}")  # добавил для отладки
            return JsonResponse({'details': "Couldn't get the information about ip"}, status=500)

        if country not in settings.ALLOWED_COUNTRIES:
            return JsonResponse({'details': "Access denied for your ip!"}, status=403)

        return self.get_response(request)


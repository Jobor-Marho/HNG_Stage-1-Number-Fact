"""
Views path for accessing my analyzeNum api
"""

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from . import utils


@api_view(["GET"])
@permission_classes([AllowAny])
def analyzeNum(request):
    """Analyzes a number and returns it with details about the number"""
    number = request.query_params.get("number")

    # If 'number' is missing or invalid, return a 400 response
    if not number or not number.isdigit():

        return Response(
            {
                "number":number,
                "error": True
             },
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Convert 'number' to an integer
    number = int(number)

    # Return the analyzed data for the number
    data = {
        "number": number,
        "is_prime": utils.is_num_prime(number),
        "is_perfect": utils.is_num_perfect(number),
        "properties": utils.return_num_properties(number),
        "digit_sum": utils.sum_number_digit(number),
        "fun_fact": utils.get_funfact_for_number(number),
    }

    return Response(data=data, status=status.HTTP_200_OK)

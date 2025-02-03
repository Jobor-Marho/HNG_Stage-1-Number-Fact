"""
Views path for accessing my analyzeNum api
"""

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from . import utils
import re


@api_view(["GET"])
@permission_classes([AllowAny])
def analyzeNum(request):
    """Analyzes a number and returns it with details about the number"""
    number = request.query_params.get("number")

    # If 'number' is missing or invalid, return a 400 response
    if number is None:

        return Response(
            {
                "number":"Missing number",
                "error": True
             },
            status=status.HTTP_400_BAD_REQUEST,
        )
    # Validate number format (allow negative integers but not decimals)
    if not re.match(r"^-?\d+$", number):
        return Response(
            {"message": number, "error": True},
            status=status.HTTP_400_BAD_REQUEST,
        )



    # Convert 'number' to an integer
    number = int(number)

    # Return the analyzed data for the number
    data = {
        "number": number,
        "is_prime": utils.is_num_prime(abs(abs(number))),
        "is_perfect": utils.is_num_perfect(abs(number)),
        "properties": utils.return_num_properties(abs(number)),
        "digit_sum": utils.sum_number_digit(abs(number)),
        "fun_fact": utils.get_funfact_for_number(number),
    }

    return Response(data=data, status=status.HTTP_200_OK)

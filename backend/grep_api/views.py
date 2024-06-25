from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .grep_code.agrep import grep_func

@api_view(['GET'])
def run_grep(request):
    # request include a dictionary in its .data, which we specify in the action to hold 'string' and 'regex' key value pairs
    w, r = request.data['string'], request.data['regex']
    # grep function from python script
    accept, nfa, path = grep_func(w, r)
    
    # result of grep
    result = {
        'status': accept,
        'nfa': nfa,
        'path': path,
    }
    
    return Response(result, status=status.HTTP_200_OK)

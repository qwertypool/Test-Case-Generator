from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    #path('',views.home),
    path('',views.home),
    path('numbers/',views.numbers),
    path('arrays/',views.arrays),
    path('matrix/',views.matrix),
    path('strings/',views.strings),
    path('string_matrix/',views.string_matrix),
    path('variable_strings/',views.variable_length_strings),
    path('unweighted_tree/',views.unweighted_tree),
    path('weighted_tree/',views.weighted_tree),
    path('unweighted_graph/',views.unweighted_graph),
    path('weighted_graph/',views.weighted_graph),
]

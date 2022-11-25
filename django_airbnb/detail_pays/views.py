from django.shortcuts import render
import pandas as pd

# Create your views here.

def detail_pays_view(request):

    df_london = pd.read_csv('/home/apprenant/Documents/Air_BNB_project/django_airbnb/data_set/london.csv')
    df_london=df_london.groupby('neighbourhood_cleansed').agg({"host_id": 'count', 'number_of_reviews' : 'sum'})
    html_london = df_london.to_html()

    

    context={
        'df_london' : html_london
    }

    return render(request, 'detail_pays/detail_pays.html', context=context)

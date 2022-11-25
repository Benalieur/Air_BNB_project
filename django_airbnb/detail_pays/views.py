from django.shortcuts import render
import pandas as pd

# Create your views here.

def detail_pays_view(request):

    df_london = pd.read_csv('/home/apprenant/Programmation/Air_BNB_project/AIR_BNB_PROJECT/django_airbnb/responses_csv/df_q1.csv')
    html_london = df_london.to_html(justify="left", classes="table table-responsive table-striped table-sm",index=False)

    df_london_1 = pd.read_csv('/home/apprenant/Programmation/Air_BNB_project/AIR_BNB_PROJECT/django_airbnb/responses_csv/df_q2.csv')
    html_london_1 = df_london_1.to_html(justify="left", classes="table table-responsive table-striped table-sm",index=False)

    df_london_2 = pd.read_csv('/home/apprenant/Programmation/Air_BNB_project/AIR_BNB_PROJECT/django_airbnb/responses_csv/df_q3.csv')
    html_london_2 = df_london_2.to_html(justify="left", classes="table table-responsive table-striped table-sm",index=False)

    df_london_3 = pd.read_csv('/home/apprenant/Programmation/Air_BNB_project/AIR_BNB_PROJECT/django_airbnb/responses_csv/df_q4.csv')
    html_london_3 = df_london_3.to_html(justify="left", classes="table table-responsive table-striped table-sm",index=False)

    df_london_4 = pd.read_csv('/home/apprenant/Programmation/Air_BNB_project/AIR_BNB_PROJECT/django_airbnb/responses_csv/df_q5.csv')
    html_london_4 = df_london_4.to_html(justify="left", classes="table table-responsive table-striped table-sm",index=False)

    df_london_5 = pd.read_csv('/home/apprenant/Programmation/Air_BNB_project/AIR_BNB_PROJECT/django_airbnb/responses_csv/df_q6.csv')
    html_london_5 = df_london_5.to_html(justify="left", classes="table table-responsive table-striped table-sm",index=False)

    df_london_6 = pd.read_csv('/home/apprenant/Programmation/Air_BNB_project/AIR_BNB_PROJECT/django_airbnb/responses_csv/df_q7.csv')
    html_london_6 = df_london_6.to_html(justify="left", classes="table table-responsive table-striped table-sm",index=False)

    df_london_7 = pd.read_csv('/home/apprenant/Programmation/Air_BNB_project/AIR_BNB_PROJECT/django_airbnb/responses_csv/df_q8.csv')
    html_london_7 = df_london_7.to_html(justify="left", classes="table table-responsive table-striped table-sm",index=False)



    context={        
        'df_london' : html_london,
        'df_london_1' : html_london_1,
        'df_london_2' : html_london_2,
        'df_london_3' : html_london_3,
        'df_london_4' : html_london_4,
        'df_london_5' : html_london_5,
        'df_london_6' : html_london_6,
        'df_london_7' : html_london_7,
    }

    return render(request, 'detail_pays/detail_pays.html', context=context)

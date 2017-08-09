from django.shortcuts import render
from django.http import HttpResponse # arun added

# Create your views here.
def index(request):
    my_dict = {'insert_text': "Hello i am coming from first app views py"}
    import pandas as pd

    metrics = pd.read_csv('ex.csv')
    metrics.columns = [' ','Past 30 days', 'Past 90 days','Past year', 'Status']
    metrics['More details'] = "link"
    metricsH = metrics.to_html(classes="table table-hover",index=False)
    metricsH = metricsH.replace('border="1"', '')
    # dfH = dfH.replace('link', "<a href='http://example.com/'>Click</a>")
    metricsH = metricsH.replace('link', "<a href='#''>Click</a>")
    #return render_template('index.html', totalAccts=100, totalBal=100, metricsH=metricsH)





    #return HttpResponse(metricsH)
    return render(request,'first_app/index.html',context = my_dict)

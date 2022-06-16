# Pricing-Module
Distance and Time based trip cost Calculator
**Initial requirement*
Django==4.0.5
djangorestframework==3.13.1
requests==2.27.1
virtualenv==20.14.1
python==3.9.12   *


Installation guide:
Take git clone 
Activate virtual environment
Runserver


Configure Distance and Time Base price :
Since Distance and Time base price are made static here and is fixed in range of (1$-8$) for both DBP and TBP.
To Configure or change DBP and TBP value , URL:- localhost:8000/rates/
Update in DBP and TBP will not create new object , it will just update the existing value in database.


API to calculate the Trip Cost according to distance and time

Runserver and hit url:- localhost:8000/prices/
Put Data in Content field Json Format. for eg:- 
{
"distance":3,
"time":2
}

Click on Post , will get data as total cost :


Thanks 

Kindly contact if any query.
email id- ravikntme30@gmail.com

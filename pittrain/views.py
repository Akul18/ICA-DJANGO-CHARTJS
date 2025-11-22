from django.http import HttpResponse, JsonResponse
from .models import PITAirportTrainFact
from django.shortcuts import render, get_object_or_404
import random

def hello(request):
   return HttpResponse("Hello World from PIT Airport Train App!")

def facts_json(request):
   data = list(PITAirportTrainFact.objects.values())
   return JsonResponse(data, safe=False)

def random_fact_page(request):
   facts = PITAirportTrainFact.objects.all()
   if not facts.exists():
       return HttpResponse("No fun facts yet!", status=404)

   fact = random.choice(facts)
   return render(request, "random_fact_page.html", {"fact": fact})

def random_fact_json(request):
   facts = PITAirportTrainFact.objects.all()
   if not facts.exists():
       return JsonResponse({"error": "No fun facts found"}, status=404)
  
   fact = random.choice(facts)
   return JsonResponse({
       "id": fact.id,
       "fun_fact": fact.funFact,
       "date_added": fact.dateAdded,
   })


def chart_page(request):
   facts = PITAirportTrainFact.objects.all()

   counts_dict = {}
   for fact in facts:
       date_str = fact.dateAdded.strftime("%Y-%m-%d")
       
       if date_str not in counts_dict:
           counts_dict[date_str] = 1
       else:
           counts_dict[date_str] += 1

   sorted_dates = sorted(counts_dict.keys())

   dates = []
   counts = []

   for date in sorted_dates:
       dates.append(date)
       counts.append(counts_dict[date])

   return render(request, "chart_test.html", {
       "dates": dates, 
       "counts": counts
   })
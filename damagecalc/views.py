from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from randomdotorg import RandomDotOrg
import json


def aceableRoll(skillLevel):
    r = RandomDotOrg('DamageCalc')
    result = 0
    roll = skillLevel
    while roll == skillLevel:
        roll = r.randrange(1, skillLevel + 1, 1)
        result = result + roll
    return result


def role(skillLevel):
    r = RandomDotOrg('DamageCalc')
    result = 0
    roll = r.randrange(1, skillLevel + 1, 1)
    result = result + roll
    return result


def index(request):
    shootingSkill = int(request.GET.get('shootingSkill', 4))
    shootingRange = int(request.GET.get('range', 0))
    cover = int(request.GET.get('cover', 0))
    specialized = int(request.GET.get('specialized', 2))
    mods = int(request.GET.get('mods', 0))
    context = {
        'shootingSkill': shootingSkill,
        'shootingRange': shootingRange,
        'cover': cover,
        'specialized': specialized,
        'mods': mods,
    }
    return render(request, 'damagecalc/index.html', context)


def calc_hit(request):
    if request.method == 'POST':
        shootingSkill = int(request.POST.get('shootingSkill', 4))
        shootingRange = int(request.POST.get('range', 0))
        cover = int(request.POST.get('cover', 0))
        specialized = int(request.POST.get('specialized', 2))
        mods = int(request.POST.get('mods', 0))
        rollResult = aceableRoll(shootingSkill)
        print rollResult
        result = (rollResult -
                  shootingRange -
                  cover -
                  specialized +
                  mods)
        print result
        context = {
            'shootingSkill': shootingSkill,
            'shootingRange': shootingRange,
            'cover': cover,
            'specialized': specialized,
            'mods': mods,
            'rollResult': rollResult,
            'result': result,
            'rolled': True,
        }
        return HttpResponse(
            json.dumps(context),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"status": "failed"}),
            content_type="application/json"
        )

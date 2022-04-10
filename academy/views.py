from django.shortcuts import render
from .forms import TermForm, PreScoreForm, ScoreFormSet
from user_auth.models import Biodata
from django import forms
from django.forms import formset_factory
from .models import Score, Term, Level, StudentProgress, StudentTermlyProfile
from django.db.models import Max, Avg, Min, Sum

from .models import Score, Biodata, Subject, Level
from django.contrib.auth.models import User


def index(request,):
    return render(request, 'academy/score.html',{})

def create_term(request):
    form = TermForm()
    if request.POST:
        form = TermForm(request.POST)
        form.save()
    students = User.objects.filter(groups__name='Student', active=True)
    biodata=()
    for student in students:
        biodata.append(biodata.objects.get(user=student))

def pre_score(request,):
    form = PreScoreForm()
    return render(request,
                  'academy/score.html',
                  {'form':form,
                   'title':'Student Score'}
                  )

def set_score(request,):
    
    if request.POST:
        subject_ = request.POST.get('subject')
        level_ = request.POST.get('level')
        number=Level.objects.get(id=level_).level_id
        class_population = Biodata.objects.filter(_clas=number).count()
        student_choices = (
            (i.id, str(i.surname) +' '+ str(i.other_names)) for i in Biodata.objects.filter(user__is_active=True, _clas=number)
        )
        class ScoreForm(forms.ModelForm):
            student = forms.ChoiceField(choices=student_choices)
            subject = forms.IntegerField(widget=forms.HiddenInput(), initial=subject_)
            level = forms.IntegerField(widget=forms.HiddenInput(), initial=level_)
            
            class Meta:
                model = Score
                exclude = []
                
        ScoreFormSet = formset_factory(ScoreForm, extra=class_population)
        return render(request,
                  'academy/score.html',
                  {'formset':ScoreFormSet,
                   'title':'Student Score'}
                  )


def submit_score(request,):
    context={}
    context['title']='Student Score'
    if request.POST:
        formset = ScoreFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                form.save()
            context['response'] = 'successfully submitted'
        else:
            context['response'] = 'You submitted invalid records'
            context['errors'] = formset.error_messages
        return render(request,
                  'academy/score.html',
                  context
                  )
def result(request,):
    context={}
    latest_term = Term.objects.all().order_by('-id')[0]
    bioo = Biodata.objects.get(user=request.user)
    
    cls = bioo._clas
    my_lev_id = Level.objects.get(level_id=cls, term_id=latest_term.id)

    c_bios = Biodata.objects.filter(_clas = cls)
    c_avg_list = []
    for c_bio in c_bios:
        c_bio_sum = 0
        c_bio_records = Score.objects.filter(level_id=my_lev_id, student=c_bio)
        print('*'*50)
        print(cls)
        print('*'*50)
        for rec in c_bio_records:
            c_bio_sum = c_bio_sum + rec.total_score
        c_bio_avg = c_bio_sum / c_bio_records.count()
        c_avg_list.append(c_bio_avg)
    highest_class_avg = c_avg_list[0]
    lowest_class_avg = c_avg_list[0]

    for i in c_avg_list:
        if i < lowest_class_avg:
            lowest_class_avg = i
        if i > highest_class_avg:
            max = highest_class_avg
    overall_t=0
    k=Score.objects.filter(level_id=my_lev_id)
    for i in k:
        overall_t = overall_t + i.total_score
    overall_avg = overall_t/k.count()


    #AVERAGE FUNCTION
    def aggrr(subject):
        records = Score.objects.filter(level_id=my_lev_id, subject__subject=subject)
        min = records[0].total_score
        max = records[0].total_score
        sum = 0
        var_scores = []
        for record in records:
            sum = sum + record.total_score
            if record.total_score < min:
                min = record.total_score
            if record.total_score > max:
                max = record.total_score
            var_scores.append(record.total_score)

        var_scores.sort(reverse=True)
        scr = Score.objects.get(level_id=my_lev_id, student=bioo, subject__subject=subject).total_score
        if scr <= 39:
            grade = 'F9'
        elif scr <= 44:
            grade = 'E8'
        elif scr <= 49:
            grade = 'D7'
        elif scr <= 54:
            grade = 'C6'
        elif scr <= 59:
            grade = 'C5'
        elif scr <= 64:
            grade = 'C4'
        elif scr <= 69:
            grade = 'B3'
        elif scr <= 74:
            grade = 'B2'
        else:
            grade = 'A1'
        pos = str(var_scores.index(scr)+1)
        if pos[:-1] == '1':
            pos = pos+'st'
        elif pos[:-1] == '2':
            pos = pos+'nd'
        elif pos[:-1] == '3':
            pos = pos+'rd'
        else:
            pos = pos+'th'
        avg = sum / records.count()
        return sum, avg, min, max, pos, grade

    st_r = Score.objects.filter(level_id=my_lev_id, student=bioo)
    total_obtainable = st_r.count()*100
    i = 0
    for r in st_r:
        i = i+ r.total_score
    total_obtained = i
    l_overall_avg = i/st_r.count()

    # TOP AGGREGATES
    context['total_obtainable'] = total_obtainable
    context['total_obtained'] = total_obtained
    context['l_overall_avg'] = l_overall_avg
    context['highest_class_avg'] = highest_class_avg
    context['lowest_class_avg'] = lowest_class_avg
    context['overall_avg'] = overall_avg
    context['student_level'] = my_lev_id


    if cls <=3:
            #SCORE RECORDS
            try:
                context['math']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='Mathematics')
            except:
                pass
            try:
                context['eng']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='English Language')
            except:
                pass
            try:
                context['bus']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='Business Studies')
            except:
                pass
            try:
                context['cca']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='CCA')
            except:
                pass
            try:
                context['yor']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='Yoruba')
            except:
                pass
            try:
                context['his']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='History')
            except:
                pass
            try:
                context['crs']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='CRS / IRS')
            except:
                pass
            try:
                context['pvs']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='PVS')
            except:
                pass
            try:
                context['nve']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='NVE')
            except:
                pass
            try:
                context['bst']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='Basic Science and Technology')
            except:
                pass
            try:
                context['mus']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='Music')
            except:
                pass
            try:
                context['igbo']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='Igbo')
            except:
                pass
            try:
                context['cvc']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='Civic Education')
            except:
                pass

            #AGGREGATES
            try:
                context['math_sum'], context['math_avg'],context['math_min'], context['math_max'], context['math_pos'], context['math_grade'] = aggrr('Mathematics')
            except:
                pass
            try:context['eng_sum'], context['eng_avg'], context['eng_min'], context['eng_max'], context['eng_pos'], context['eng_grade'] = aggrr('English Language')
            except:
                pass
            try:
                context['bus_sum'], context['bus_avg'], context['bus_min'], context['bus_max'], context['bus_pos'], context['bus_grade'] = aggrr('Business Studies')
            except:
                pass
            try:
                context['cca_sum'], context['cca_avg'], context['cca_min'], context['cca_max'], context['cca_pos'], context['cca_grade'] = aggrr('CCA')
            except:
                pass
            try:
                context['yor_sum'], context['yor_avg'], context['yor_min'], context['yor_max'], context['yor_pos'], context['yor_grade'] = aggrr('Yoruba')
            except:
                pass
            try:
                context['his_sum'], context['his_avg'], context['his_min'], context['his_max'], context['his_pos'], context['his_grade'] = aggrr('History')
            except:
                pass
            try:
                context['crs_sum'], context['crs_avg'], context['crs_min'], context['crs_max'], context['crs_pos'], context['crs_grade'] = aggrr('CRS / IRS')
            except:
                pass
            try:
                context['pvs_sum'], context['pvs_avg'], context['pvs_min'], context['pvs_max'], context['pvs_pos'], context['pvs_grade'] = aggrr('PVS')
            except:
                pass
            try:
                context['nve_sum'], context['nve_avg'], context['nve_min'], context['nve_max'], context['nve_pos'], context['nve_grade'] = aggrr('NVE')
            except:
                pass
            try:
                context['bst_sum'], context['bst_avg'], context['bst_min'], context['bst_max'], context['bst_pos'], context['bst_grade'] = aggrr('Basic Science and Technology')
            except:
                pass
            try:
                context['mus_sum'], context['mus_avg'], context['mus_min'], context['mus_max'], context['mus_pos'], context['mus_grade'] = aggrr('Music')
            except:
                pass
            try:
                context['igbo_sum'], context['igbo_avg'], context['igbo_min'], context['igbo_max'], context['igbo_pos'], context['igbo_grade'] = aggrr('Igbo')
            except:
                pass
            try:
                context['cvc_sum'], context['cvc_avg'], context['cvc_min'], context['cvc_max'], context['cvc_pos'], context['cvc_grade'] = aggrr('Civic Education')
            except:
                pass

            try:
                context['profile'] = StudentTermlyProfile.objects.get(student_id=request.user.biodata.id)
            except:
                pass
            context['class'] = StudentProgress.objects.get(user_id=request.user.biodata.id).clas
            return render(request, 'academy/result.html', context)

    elif cls <= 6:
        # SCORE RECORDS
        try:
            context['math'] = Score.objects.get(level_id=my_lev_id, student=bioo, subject__subject='Mathematics')
        except:
            pass
        try:
            context['eng']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='English Language')
        except:
            pass
        try:
            context['cvc']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='Civic Education')
        except:
            pass
        try:
            context['mkt']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='Marketing')
        except:
            pass
        try:
            context['bio']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='Biology')
        except:
            pass
        try:
            context['eco']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='Economics')
        except:
            pass
        #ART
        try:
            context['lit']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='Literature')
        except:
            pass
        try:
            context['crs'] = Score.objects.get(level_id=my_lev_id, student=bioo, subject__subject='CRS / IRS')
        except:
            pass
        try:
            context['gov']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='Government')
        except:
            pass
        #SCIENCE
        try:
            context['phy']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='Physics')
        except:
            pass
        try:
            context['chm']=Score.objects.get(level_id = my_lev_id, student=bioo, subject__subject='Chemistry')
        except:
            pass

        # AGGREGATES
        try:
            context['math_sum'], context['math_avg'], context['math_min'], context['math_max'], context['math_pos'], context['math_grade'] = aggrr('Mathematics')
        except:
            pass
        try:
            context['eng_sum'], context['eng_avg'], context['eng_min'], context['eng_max'], context['eng_pos'], context['eng_grade'] = aggrr('English Language')
        except:
            pass
        try:
            context['cvc_sum'], context['cvc_avg'], context['cvc_min'], context['cvc_max'], context['cvc_pos'], context['cvc_grade'] = aggrr('Civic Education')
        except:
            pass
        try:
            context['mkt_sum'], context['mkt_avg'], context['mkt_min'], context['mkt_max'], context['mkt_pos'], context['mkt_grade'] = aggrr('Marketing')
        except:
            pass
        try:
            context['bio_sum'], context['bio_avg'], context['bio_min'], context['bio_max'], context['bio_pos'], context['bio_grade'] = aggrr('Biology')
        except:
            pass
        try:
            context['eco_sum'], context['eco_avg'], context['eco_min'], context['eco_max'], context['eco_pos'], context['eco_grade'] = aggrr('Economics')
        except:
            pass
        # ART
        try:
            context['lit_sum'], context['lit_avg'], context['lit_min'], context['lit_max'], context['lit_pos'], context['lit_grade'] = aggrr('Literature')
        except:
            pass
        try:
            context['crs_sum'], context['crs_avg'], context['crs_min'], context['crs_max'], context['crs_pos'], context['crs_grade'] = aggrr('CRS / IRS')
        except:
            pass
        try:
            context['gov_sum'], context['gov_avg'], context['gov_min'], context['gov_max'], context['gov_pos'], context['gov_grade'] = aggrr('Government')
        # SCIENCE
        except:
            pass
        try:
            context['phy_sum'], context['phy_avg'], context['phy_min'], context['phy_max'], context['phy_pos'], context['phy_grade'] = aggrr('Physics')
        except:
            pass
        try:
            context['chm_sum'], context['chm_avg'], context['chm_min'], context['chm_max'], context['chm_pos'], context['chm_grade'] = aggrr('Chemistry')
        except:
            pass

        context['profile']=StudentTermlyProfile.objects.get(student_id=request.user.biodata.id)
        context['class']=StudentProgress.objects.get(user_id=request.user.biodata.id).clas
        return render(request,'academy/result2.html', context)




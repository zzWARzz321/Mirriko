from django import forms

#class ModelForm(forms.Form):
 #   output_press = forms.DecimalField(label='Давление на входе', decimal_places=2, max_digits=8)
  #  tonn_hour = forms.DecimalField(label='Расход массовый', decimal_places=2, max_digits=8)
   # water_value = forms.DecimalField(label='Обводненность', decimal_places=2, max_digits=8)
    #input_press = forms.DecimalField(label='Давление на входе', decimal_places=2, max_digits=8)
    #density_input = forms.DecimalField(label='Плотность нефти', decimal_places=2, max_digits=8)
    #input_temp = forms.DecimalField(label='Внутренняя температура', decimal_places=2, max_digits=8)
    #type_ptp = forms.ChoiceField(label='Тип присадки', widget = forms.Select(),choices = ([('Порошок ПАО С6','Порошок ПАО С6'),
                                #('Порошок ПАО С10','Порошок ПАО С10'),
                                #('Порошок ПАО С12','Порошок ПАО С12'),]),
                                #initial='3', required = True)

class ModelForm(forms.Form):
    nasos_one = forms.DecimalField(label='"Яч.01 АД-2 ДНС-3" - максимальное потребление 800 квт/ч', decimal_places=2, max_digits=8)
    nasos_two = forms.DecimalField(label='"Яч.21 Н-3" - максимальное потребление 800 квт/ч', decimal_places=2, max_digits=8)
    nasos_three = forms.DecimalField(label='"Яч.7 Н-1" - максимальное потребление 800 квт/ч', decimal_places=2, max_digits=8)
    nasos_four = forms.DecimalField(label='"Яч.8 Н-2" - максимальное потребление 800 квт/ч', decimal_places=2, max_digits=8)
    dry_ptp = forms.DecimalField(label='Подача кг/час сухой', decimal_places=2, max_digits=8)
    liquid_ptp = forms.DecimalField(label='Подача кг/час жидкой', decimal_places=2, max_digits=8)

class ModelForm1(forms.Form):
    nasos_one = forms.DecimalField(label='"Яч.01 АД-2 ДНС-3" - максимальное потребление 800 квт/ч', decimal_places=2, max_digits=8)
    nasos_two = forms.DecimalField(label='"Яч.21 Н-3" - максимальное потребление 800 квт/ч', decimal_places=2, max_digits=8)
    nasos_three = forms.DecimalField(label='"Яч.7 Н-1" - максимальное потребление 800 квт/ч', decimal_places=2, max_digits=8)
    nasos_four = forms.DecimalField(label='"Яч.8 Н-2" - максимальное потребление 800 квт/ч', decimal_places=2, max_digits=8)
    tonn = forms.DecimalField(label='Перекачеваемый объем - Тонн в час', decimal_places=2, max_digits=8)
    press = forms.DecimalField(label='Давление на выходе', decimal_places=2, max_digits=8)
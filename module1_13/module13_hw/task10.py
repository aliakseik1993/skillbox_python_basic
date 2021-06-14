print('Задача 10. Аннуитетный платёж')

# Кредит в сумме S млн руб.,
# выданный на n лет под i% годовых,
# подлежит погашению равными ежегодными выплатами в конце каждого года,
# включающими процентные платежи и сумму в погашение основного долга.
# 
# Проценты начисляются в один раз в год.
# После выплаты третьего платежа
# достигнута договорённость между кредитором и заёмщиком
# о продлении срока погашения займа на n_2 лет
# и увеличении процентной ставки с момента конверсии до i_2%.
# 
# Напишите программу,
# которая выводит план погашения оставшейся части долга.
# 
# A = KS
# 
# K = i(1 + i) ** n / (1 + i) ** n - 1
# 
# Пример:
# 
# Введите сумму кредита: 40e6
# На сколько лет выдан? 5
# Сколько процентов годовых? 6
# 
# Период: 1
# 
# Остаток долга на начало периода: 40000000.0
# Выплачено процентов: 2400000.0
# Выплачено тела кредита: 7095856.02
# 
# 
# Период: 2
# 
# Остаток долга на начало периода: 32904143.98
# Выплачено процентов: 1974248.6387999998
# Выплачено тела кредита: 7521607.3812
# 
# Период: 3
# 
# Остаток долга на начало периода: 25382536.5988
# Выплачено процентов: 1522952.195928
# Выплачено тела кредита: 7972903.824072
# 
# Остаток долга: 17409632.774728
# 
# =================================================
# 
# На сколько лет продляется договор? 2
# Увеличение ставки до: 10
# 
# Период: 1
# 
# Остаток долга на начало периода: 17409632.774728
# Выплачено процентов: 1740963.2774728
# Выплачено тела кредита: 3751267.5625271997
# 
# Период: 2
# 
# Остаток долга на начало периода: 13658365.2122008
# Выплачено процентов: 1365836.52122008
# Выплачено тела кредита: 4126394.3187799198
# 
# Период: 3
# 
# Остаток долга на начало периода: 9531970.89342088
# Выплачено процентов: 953197.0893420881
# Выплачено тела кредита: 4539033.750657911
# 
# Период: 4
# 
# Остаток долга на начало периода: 4992937.142762969
# Выплачено процентов: 499293.71427629696
# Выплачено тела кредита: 4992937.125723703
# 
# Остаток долга: 0.017039266414940357

def annuity_func(summ_s, years, procent_in_year):
  sums_s_let = summ_s
  count = 0
  annuity_coefficient = procent_in_year * (1 + procent_in_year) ** years / ((1 + procent_in_year) ** years - 1)
  #print(annuity_coefficient)
  while count < 3:
    count += 1
    print ("Период", count)
    print("Остаток долга на начало периода: ", summ_s)
    print("Выплачено процентов:", summ_s * procent_in_year)
    telo_in_credit = (round(sums_s_let * annuity_coefficient, 2) - summ_s * procent_in_year)
    print("Выплачено тела кредита:", telo_in_credit)
    summ_s -= telo_in_credit
  print("Остаток долга:", summ_s)
  print()
  new_years = (float(input("На сколько лет продляется договор? "))) / 100
  procent_in_year = procent_in_year +  new_years * 2
  print("Увеличена ставка процентов до:", int(procent_in_year * 100))
  sums_s_let = summ_s
  years_left = years - count + int(new_years * 100)
  annuity_coefficient = procent_in_year * (1 + procent_in_year) ** years_left / ((1 + procent_in_year) ** years_left - 1)
  #print(years_left, "осталось периодов")
  print()
  for number in range(years_left):
    print ("Период", number + 1)
    print("Остаток долга на начало периода: ", summ_s)
    print("Выплачено процентов:", summ_s * procent_in_year)
    telo_in_credit = (round(sums_s_let * annuity_coefficient, 2) - summ_s * procent_in_year)
    print("Выплачено тела кредита:", telo_in_credit)
    summ_s -= telo_in_credit
  print("Остаток долга:", summ_s)


summ_s = float(input("Введите сумму кредита: "))
years = int(input("На сколько лет выдан? "))
procent_in_year = float(input("Сколько процентов годовых? ")) / 100
annuity_func(summ_s, years, procent_in_year)

#Вариант 2, более сокращенный
def annuity_formula(summ_s, years, procent_in_year):
  annuity_coefficient = procent_in_year * (1 + procent_in_year) ** years / ((1 + procent_in_year) ** years - 1)
  annuity_formula = round(summ_s * annuity_coefficient, 2)
  return annuity_formula, annuity_coefficient

def annuity_func(summ_s, years, procent_in_year):
  count = 0
  for_biety = 0
  years_count = years
  annuity, annuity_coef = annuity_formula(summ_s, years, procent_in_year)
  #print(annuity, annuity_coef)
  #print(annuity_coefficient)
  while count != years_count:
    count += 1
    print ("\nПериод", count - for_biety)
    print("Остаток долга на начало периода: ", summ_s)
    print("Выплачено процентов:", summ_s * procent_in_year)
    telo_in_credit = annuity - summ_s * procent_in_year
    print("Выплачено тела кредита:", telo_in_credit)
    summ_s -= telo_in_credit
    if count == 3:
      for_biety = count
      print("Остаток долга:", summ_s)
      print()
      new_years = (float(input("На сколько лет продляется договор? "))) / 100
      procent_in_year = procent_in_year +  new_years * 2
      print("Увеличена ставка процентов до:", int(procent_in_year * 100))
      years_count += int(new_years * 100)
      years += int(new_years * 100) - count
      annuity, annuity_coef = annuity_formula(summ_s, years, procent_in_year)
  print("Остаток долга:", summ_s)


summ_s = float(input("Введите сумму кредита: "))
years = int(input("На сколько лет выдан? "))
procent_in_year = float(input("Сколько процентов годовых? ")) / 100
annuity_func(summ_s, years, procent_in_year)
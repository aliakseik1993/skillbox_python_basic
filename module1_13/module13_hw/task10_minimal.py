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
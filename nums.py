def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
s = '''В разные эпохи и у разных народов число Пи имело разное значение.
Например, в Древнем Египте оно равнялось 3.1604 у индусов оно приобрело
значение 3.162 китайцы пользовались числом, равным 3.1459
Буквенное обозначение число Пи получило только в 1706 году – оно происходит
от начальных букв двух греческих слов, означающих окружность и периметр.
Буквой π число наделил математик Джонс, а прочно вошла в математику она
уже в 1737 году.'''
res=[]
for i in s.split():
    if is_number(i):
        res.append(float(i))
print(res,len(res),sum(res),max(res),sep='\n')
       

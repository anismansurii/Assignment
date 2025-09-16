li_city = ["Ahmedabad" , "Surat" , "Vapi" , "Lynn"]

def filter_city(str):
    for char in str:
        if char in 'aeiou':
            return str

li_ans = list(filter(filter_city , li_city))
print(li_ans)


company = { 
"sales": {"manager": "Kiran", "team": {"T1": "Raj", "T2": "Neha"}}, 
"tech": {"manager": "Asha", "team": {"T1": "Dev", "T2": "Sonia"}} 
} 


# print(company["tech"]["team"]["T2"])

print(company["sales"]["team"].keys())
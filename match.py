import json
from tinydb import TinyDB
from find_data import detect_field_type

db = TinyDB('templates_data.json', encoding='utf-8')
templates = db.table('_default')

test_cases = [
    {"username": "ivan@gmail.com", "mobile": "+7 912 345 67 89"},  
    {"client_name": "Мария", "delivery_date": "2024-07-20"},  
    {"support_phone": "+7 800 123 45 67"},  
    {"email": "contact@shop.ru", "phone": "+7 495 555 44 33"},  
    {"login": "sasha@yandex.ru", "work_phone": "+7 916 000 11 22"},  
    {"customer": "Дмитрий", "order_date": "2024-03-10"},  
]

def match_template(input_data):
    input_types = {k: detect_field_type(v) for k, v in input_data.items()}
    best_fit = None
    highest_score = 0
    
    for template in templates.all():
        template_fields = {k: v for k, v in template.items() if k != 'title'}
        score = sum(
            1 for field, field_type in template_fields.items()
            if field in input_types and input_types[field] == field_type
        )
        
        if score > highest_score:
            highest_score = score
            best_fit = template['title']
    
    return {"template": best_fit} if best_fit else {"field_types": input_types}

def execute_tests():
    for case in test_cases:
        print("Input data:", json.dumps(case, ensure_ascii=False))
        result = match_template(case)
        print("Output:", json.dumps(result, indent=2, ensure_ascii=False))
        print("=" * 60)

if __name__ == "__main__":
    execute_tests()

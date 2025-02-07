from models.categories_models import Category

def list_category():
    categories = Category.list_categories()
    if categories == []:
        print("Nenhuma categoria cadastrada!")
        return False
    
    for category in categories:
        print(f"ID: {category.id} Categoria: {category.name}")

    return 


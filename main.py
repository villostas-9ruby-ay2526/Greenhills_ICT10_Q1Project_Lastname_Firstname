from pyscript import display, document

# This is for py script for the outcome.
def normal(e):

    document.getElementById('result').innerHTML = " "

    hotdog_option = document.getElementById("normal_opt")
    quantity_stock = int(document.getElementById("w_stocks").value)
    sku_output = 'SKU-HOT-NOR-15-'

    display(f'You rock, customer!', target='thank_you_po')
    display(f'Thank you for ordering from the BEST hotdog stand ever', target='much_love_po')
    display(f'Product SKU: {sku_output}{quantity_stock}', target='you_rock_po')

def cheese(e):

    document.getElementById('result').innerHTML = " "

    hotdog_option = document.getElementById("cheese_opt")
    quantity_stock = int(document.getElementById("w_stocks").value)
    sku_output = 'SKU-HOT-CH-15-'

    display(f'You rock, customer!', target='thank_you_po')
    display(f'Thank you for ordering from the BEST hotdog stand ever', target='much_love_po')
    display(f'Product SKU: {sku_output}{quantity_stock}', target='you_rock_po')

def bacon(e):

    document.getElementById('result').innerHTML = " "
    
    hotdog_option = document.getElementById("bacon_opt")
    quantity_stock = int(document.getElementById("w_stocks").value)
    sku_output = 'SKU-HOT-BAC-15-'

    display(f'You rock, customer!', target='thank_you_po')
    display(f'Thank you for ordering from the BEST hotdog stand ever', target='much_love_po')
    display(f'Product SKU: {sku_output}{quantity_stock}', target='you_rock_po')

def chicken(e):

    document.getElementById('result').innerHTML = " "
    
    hotdog_option = document.getElementById("chicken_opt")
    quantity_stock = int(document.getElementById("w_stocks"))
    sku_output = 'SKU-HOT-CHI-15-'

    display(f'You rock, customer!', target='thank_you_po')
    display(f'Thank you for ordering from the BEST hotdog stand ever', target='much_love_po')
    display(f'Product SKU: {sku_output}{quantity_stock}', target='you_rock_po')
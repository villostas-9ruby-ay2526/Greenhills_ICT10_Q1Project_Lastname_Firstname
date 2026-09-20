from pyscript import display, document


#This will help calculate for the price
def get_reciept(e):
    prod_1 = document.getElementbyId("first_option")
    prod_2 = document.getElementbyId("second_option")
    prod_3 = document.getElementbyId("third_option")
    subtotal = prod_1 + prod_2 + prod_3
    tax_rate = subtotal * 0.12
    total = subtotal + tax_rate


    display(f'Subtotal: {subtotal}, Tax: {tax_rate},  Total: {total}, target='result')